from validators import url as valid_url
from urllib.parse import urlparse
from flask import Flask, request, jsonify, redirect
from . import utils
from . import db

app = Flask(__name__)
redis_conn = db.ConnectRedis()


@app.route("/shorten")
def shortner():

    arg_count = len(request.args)
    url_user = request.args.get("url")

    if url_user is None or arg_count != 1:
        return jsonify({"error": "Only URL parameter is required"}), 400

    if not valid_url(url_user):
        return (
            jsonify(
                {"error": "Bad Request - Invalid URL provided. https://www.example.com"}
            ),
            400,
        )

    url_hash = utils.generate_hash(url_user)[4:9]
    root_url = urlparse(request.url).netloc
    shorten_url = root_url + "/" + url_hash

    resp = redis_conn.set_url(url_hash, url_user)

    if resp:
        return jsonify({"shorten_url": f"{shorten_url}"}), 200

    return (
        jsonify(
            {"error": "An unexpected error occurred while processing the request."}
        ),
        500,
    )


@app.route("/<path:url>")
def wildcard_route(url):
    status, data_url = redis_conn.get_url(url)
    if status:
        if data_url is not None:
            return redirect(data_url)
        return (
            jsonify({"error": "Not Found - The requested URL was not found."}),
            404,
        )
    return jsonify({"error": "Unexpected error while processing the request"}), 400


if __name__ == "__main__":
    app.run(debug=True)
