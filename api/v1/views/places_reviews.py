#!/usr/bin/python3
"""An end point for usr"""
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.review import Review


@app_views.route('/places/<place_id>reviews',
                 methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """Retrieve a list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = place.reviews
    review_list = [review.to_dict() for review in reviews]
    return jsonify(review_list)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """a function to retrieve user from the database"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('reviews/<review_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_review(review_id=None):
    """a function that delete the object db"""
    review = storage.get("Review", review_id)
    if review is not None:
        storage.delete(review)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def post_review():
    """a function to create review"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    new_review = Review(**data)
    new_review.save()
    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a Review object by ID"""
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
