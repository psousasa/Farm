from HandleDB import *


class Label(QueryDb):
    """
    label each component on the farm
     - produce
     - bed
     - infrastructure
    """
    def __init__(self):
        self.type = self.__class__.__name__
        # todo: get from DB what initials and code will correspond to
        pass


