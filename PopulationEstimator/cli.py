from PopulationEstimator.population_data_receiver import population_data_manager
import click
from PopulationEstimator.common import BadYearValue, BadRegion

def check_region(region):
    regions = ["africa", "asia", "australia", "europe", "world" ]

    if region not in regions:
        return False
    return True

def to_lower(string):
    return string.lower()


def execute(year, region):
    region = to_lower(region)
    try:
        if year > 2100 or year < 1950:
            raise BadYearValue('Year must be between 1950-2100')
        if check_region(region) is False:
            raise BadRegion("Can't check for this region")
    except Exception as e:
        print(e)
        exit(1)


    result = population_data_manager(year, region)
    print('Reliability for this parameters is about {} percent'.format((1086-result)*100/1086))

@click.command()
@click.option('--year', type = int, prompt='Type year to check estimation of future population')
@click.option('--region', prompt='Type any region (africa, asia, australia, europe, world)')
def main(year, region):

    execute(year, region)
    


if __name__ == "__main__":
    main()
