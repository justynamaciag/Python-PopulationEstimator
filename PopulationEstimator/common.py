class BadYearValue(Exception):
    def __init__(self,arg):
        self.args = arg

class BadRegion(Exception):
    def __init__(self,arg):
        self.args = arg

class TabulatedData:
    def __init__(self, dates, values):
        self.dates = dates
        self.values = values

