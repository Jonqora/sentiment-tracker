# coding=utf-8

# Boilerplate code from tutorial:
# https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/

from sqlalchemy import Column, String

from .entity import Entity, Base


class TextPost(Entity, Base):
    __tablename__ = 'textpost'

    title = Column(String)
    description = Column(String)

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
