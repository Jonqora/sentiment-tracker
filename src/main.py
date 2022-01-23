# coding=utf-8

# Boilerplate code from tutorial:
# https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

from .entities.entity import Session, engine, Base
from .entities.textpost import TextPost

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
posts = session.query(TextPost).all()

if len(posts) == 0:
    # create and persist mock post
    python_post = TextPost(
        "Data Test - Entity",
        "This is a test post. Hooray!",
        "script"
    )
    session.add(python_post)
    session.commit()
    session.close()

    # reload exams
    posts = session.query(TextPost).all()

# show existing exams
print('### Posts:')
for post in posts:
    print(f'({post.id}) {post.title} - {post.description}')
