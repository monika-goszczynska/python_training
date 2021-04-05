# -*- coding: utf-8 -*-
class Group:

    # tworzymy konstruktor
    # oprócz standardowej self przyjmuje również inne parametry: name, header, footer
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
