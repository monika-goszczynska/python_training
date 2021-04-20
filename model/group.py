# -*- coding: utf-8 -*-
class Group:

    # tworzymy konstruktor
    # oprócz standardowej self przyjmuje również inne parametry: name, header, footer
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # ta funkcja okresla jak bedzie wygladac obiekt przy wyprowadzeniu na konsole - representation
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # biezacy obiekt self jest porownywany z innym obiektem, ktory jest przyjmowany jako parametr
    # nastepuje porownanie wg sensu, a nie fizycznego rozmieszczenia obiektow
    def __eq__(self, other):
        return self.id == other.id and self.name == other.name
