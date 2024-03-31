from validators import url as valid_url
from urllib.parse import urlparse
from flask import Flask, request, jsonify
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
                {
                    "error": "Invalid URL format: should be like this https://www.example.com"
                }
            ),
            400,
        )

    url_hash = utils.generate_hash(url_user)[4:9]
    root_url = urlparse(request.url).netloc
    shorten_url = root_url + "/" + url_hash

    resp = redis_conn.set_url(url_hash, url_user)

    if resp:
        return jsonify({"shorten_url": f"{shorten_url}"}), 200

    return "Unexpected Error While shortening the URl Please try later"


@app.route("/<path:url>")
def wildcard_route(url):
    return f"You entered: {url}"


if __name__ == "__main__":
    app.run(debug=True)
