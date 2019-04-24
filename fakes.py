# -*- coding: utf-8 -*-
# Time    : 2019/4/24 23:38
# Author  : LiaoKong

from faker import Faker

from models import Admin, Category, Post
from extensions import db

fake = Faker()


def fake_admin():
    admin = Admin(
        username="admin",
        blog_title="Blog",
        blog_sub_title="I'm the real thing.",
        name="Liao Kong",
        about="I'm liao kong."
    )

    admin.set_password("123456")
    db.session.add(admin)
    db.session.commit()


def fake_categories(count=10):
    category = Category(name="Default")
    db.session.add(category)

    for i in range(count):
        category = Category(name=fake.word())
        db.session.add(category)

        try:
            db.session.commit()
        except InterruptedError:
            db.session.rollback()


def fake_posts(count=50):
    for i in range(count):
        pass
        # todo:this
        # post = Post(
        #     title=fake.sentence(),
        #
        # )
