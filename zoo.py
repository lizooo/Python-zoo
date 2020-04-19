class Zoo:
    is_suitable_for_kids = True

    def __init__(self, number_of_visitors_per_year=0, name="none", number_of_animals=0, location_city="none",
                 price_of_ticket=0.0, rating_on_google=0.0):
        self.number_of_visitors_per_year = number_of_visitors_per_year
        self.name = name
        self.number_of_animals = number_of_animals
        self.location_city = location_city
        self.price_of_ticket = price_of_ticket
        self.rating_on_google = rating_on_google

    def __del__(self):
        pass

    def __str__(self):
        return ',\n'.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])+'\n'

    @staticmethod
    def get_is_suitable_for_kids():
        return Zoo.is_suitable_for_kids


