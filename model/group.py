# -*- coding: utf-8 -*-
class Group:

    # tworzymy konstruktor
    # oprócz standardowej self przyjmuje również inne parametry: name, header, footer
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id
