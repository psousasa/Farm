from Label import *


class FarmInfraStructures(Label):
    def __init__(self, shape, cost, height, weight=None):
        Label.__init__(self)
        self.shape = shape
        self.height = height
        self.weight = weight
        self.cost = cost

        pass


class Greenhouse(FarmInfraStructures):
    def __init__(self, shape, height, weight, cost, is_nursery):
        FarmInfraStructures.__init__(self, shape, height, weight, cost)
        self.is_nursery = is_nursery
        pass


class Trellis(FarmInfraStructures):
    def __init__(self, shape, height, weight, cost):
        FarmInfraStructures.__init__(self, shape, height, weight, cost)
        pass


class Rack(FarmInfraStructures):
    def __init__(self, shape, height, weight, number_shelves, cost):
        FarmInfraStructures.__init__(self, shape, height, weight, cost)
        self.number_shelves = number_shelves
        pass


class Shelf(FarmInfraStructures):
    def __init__(self, shape, height, weight, cost):
        """

        :param shape:
        :param height: shelf height from shelf base, to top shelf bottom
        """
        FarmInfraStructures.__init__(self, shape, height, weight, cost)

        pass


class Tray(FarmInfraStructures):
    def __init__(self, shape, height, weight, has_drainage, is_flat, cost):
        FarmInfraStructures.__init__(self, shape, height, weight, cost)
        self.with_drainage = has_drainage
        self.is_flat = is_flat


class LightBulb(FarmInfraStructures):
    def __init__(self, shape, height, power, bulb_type, lumens, estm_lifetime, cost):
        """

        :param shape: line or point
        :param power: watts
        :param bulb_type: led, fluorescent
        :param lumens:
        :param estm_lifetime: year per daily work hours
        :param cost:
        """
        FarmInfraStructures.__init__(self, shape, cost, height=height)
        self.power = power
        self.bulb_type = bulb_type
        self.lumens = lumens
        self.estm_lifetime = estm_lifetime
        pass


class Sprinkler(FarmInfraStructures):
    def __init__(self, shape, height, cost, output, spacing, radius, is_drip):
        """

        :param output: water flow output
        :param spacing: for drip systems - in meters
        :param radius: for sprinklers
        :param is_drip: if is drip system
        """
        FarmInfraStructures.__init__(self, shape, cost, height)
        self.output = output
        self.radius = radius
        self.sprinkler_type = 'Drip' if is_drip else 'Sprinkler'
        self.spacing = spacing
        pass
