from flask import Blueprint, request, jsonify, redirect
from app.storage import store
from app.utils import generate_code, is_valid_url

bp = Blueprint("api", __name__)

@bp.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    url = data.get("url")

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_code()
    while store.get(short_code):
        short_code = generate_code()

    store.save(short_code, url)
    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@bp.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    entry = store.get(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    store.increment_click(short_code)
    return redirect(entry["url"])

@bp.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    entry = store.get(short_code)
    if not entry:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": entry["url"],
        "clicks": entry["clicks"],
        "created_at": entry["created_at"].isoformat()
    })
from flask import Blueprint, request, jsonify, redirect
from .utils import generate_code, is_valid_url
from .storage import store

routes = Blueprint("routes", __name__)

@routes.route("/api/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    url = data.get("url")

    if not url or not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_code()
    while store.get(short_code):
        short_code = generate_code()

    store.save(short_code, url)

    return jsonify({
        "short_code": short_code,
        "short_url": f"http://localhost:5000/{short_code}"
    }), 201

@routes.route("/<short_code>", methods=["GET"])
def redirect_url(short_code):
    record = store.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    store.increment_clicks(short_code)
    return redirect(record["url"])

@routes.route("/api/stats/<short_code>", methods=["GET"])
def stats(short_code):
    record = store.get(short_code)
    if not record:
        return jsonify({"error": "Short code not found"}), 404

    return jsonify({
        "url": record["url"],
        "clicks": record["clicks"],
        "created_at": record["created_at"].isoformat()
    })
