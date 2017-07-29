from population_data_receiver import get_population_number, get_birth_rates
from PopulationEstimator.main import check_region, to_lower
from PopulationEstimator.checker import check_dependence
from PopulationEstimator.common import TabulatedData

class TestUM:
    def test_region(self):
        assert check_region("africa") == True
        assert check_region("default_string") == False
        assert check_region(to_lower("WORLD")) == True

    def test_population(self):
         assert get_population_number(2020, "africa") == 1340103338
         assert get_population_number(2070, "australia") == 37788119

    def test_denpendency(self):
        assert check_dependence(200, 100) == 4
        assert check_dependence(100, 200) == 0

    def get_births(self):
        assert get_birth_rates() == TabulatedData([2009,2012, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015], [1.15, 1.17,1.22 ,1.22,1.22,1.22, 1.18, 1.18, 1.18, 1.18, 1.18])
