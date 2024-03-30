from setuptools import setup, find_packages

setup(
    name='URL-Shortner-Flask-Redis',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'redis',
        'pip-tools',
        # Add any other dependencies your project requires
    ],
    entry_points='''
        [console_scripts]
        url-shortner-flask-redis=src:main
    ''',
    author='Ashish Kumar Maurya',
    author_email='kashish979@gmail.com.com',
    description='URL Shortener is a simple application built with Flask and Redis that allows users to shorten long URLs into shorter, more manageable links.',
    url='https://github.com/akmanon/url-shortner-flask-redis/',
)
