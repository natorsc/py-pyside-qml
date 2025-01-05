# -*- coding: utf-8 -*-
"""."""

from PySide6.QtCore import QObject, Slot


class MainWindow(QObject):
    def __init__(self):
        super().__init__()

    @Slot(str, result=str)
    def to_upper(self, text):
        return f'\nPython: {text.upper()}!'
