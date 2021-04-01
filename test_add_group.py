# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


class TestAddGroup(unittest.TestCase):

    """@... zamienia zwykłą funkcję na inicjalizator fikstury"""
    @pytest.fixture()
    def app(request):
        fixture=Application
        request.addfinalizer(fixture.destroy)
        return fixture

    def test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="gr_name", header="gr_header", footer="gr_footer"))
        app.logout()

    def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()
