# coding=utf-8

# Boilerplate code from tutorial:
# https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

from flask_cors import CORS

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.textpost import TextPost, TextPostSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/textposts')
def get_textposts():
    # fetching from the database
    session = Session()
    textpost_objects = session.query(TextPost).all()

    # transforming into JSON-serializable objects
    schema = TextPostSchema(many=True)
    posts = schema.dump(textpost_objects)

    # serializing as JSON
    session.close()
    return jsonify(posts)


@app.route('/textposts', methods=['POST'])
def add_textpost():
    # mount textpost object
    posted_textpost = TextPostSchema(only=('title', 'description'))\
        .load(request.get_json())
        
    print(posted_textpost)
    post = TextPost(**posted_textpost, created_by="HTTP post request")

    # persist textpost
    session = Session()
    session.add(post)
    session.commit()

    # return created textpost
    new_textpost = TextPostSchema().dump(post)
    session.close()
    return jsonify(new_textpost), 201


# TEST POST for database connection
#
# # start session
# session = Session()
#
# # check for existing data
# posts = session.query(TextPost).all()
#
# if len(posts) == 0:
#     # create and persist mock post
#     python_post = TextPost(
#         "Data Test - Entity",
#         "This is a test post. Hooray!",
#         "script"
#     )
#     session.add(python_post)
#     session.commit()
#     session.close()
#
#     # reload exams
#     posts = session.query(TextPost).all()
#
# # show existing exams
# print('### Posts:')
# for post in posts:
#     print(f'({post.id}) {post.title} - {post.description}')
