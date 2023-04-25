from Label import Label


class Produce(Label):

    def __init__(self, name, estm_time2ripe, estm_time2seedling, estm_time2shoot, supplier, growing_season,
                 harvesting_month, seeding_month, starter_type, water_consumption, stage, is_microgreen=False):
        """

        :param name: produce name
        :param estm_time2ripe: estimated time to collect - microgreens or other
        :param estm_time2seedling: estimated time to be able to transplant - other
        :param estm_time2shoot: estiamted time to shoot - for microgreens or other
        :param supplier: name of supplier company
        :param growing_season: 4 seasons
        :param starter_type: microgreen seed, seed, seedling
        :param water_consumption: dependent of stage
        :param stage: each Produce can have multiple stages - seed, seeling, developped seedling, ripping
        :param harvesting_month:
        :param seeding_month: when to seed - 4 seasons
        :param is_microgreen: is a microgreen
        """
        self.name = name
        self.__class__.__name__ = name

        self.estm_time2ripe = estm_time2ripe
        self.estm_time2seedling = estm_time2seedling
        self.estm_time2shoot = estm_time2shoot
        self.supplier = supplier
        self.type = starter_type
        self.growing_season = growing_season
        self.seeding_season = seeding_month
        self.harvesting_season = harvesting_month
        self.is_microgreen = is_microgreen
        self.water_consumption = water_consumption
        self.stage = stage

        Label.__init__(self)

        pass
