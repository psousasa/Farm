from Label import *


class Bed(Label):

    def __init__(self, shape, code_name):
        Label.__init__(self)
        self.shape = shape
        self.code_name = code_name

        pass
