from datetime import *

class single_note:


    def __init__(self, date_create: datetime, title: str, msg: str):
        self.index = 1
        self.date_create = date_create
        self.date_modify = date_create
        self.title = title
        self.msg = msg

        pass
    