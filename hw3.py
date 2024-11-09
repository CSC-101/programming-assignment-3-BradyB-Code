import data
import county_demographics


# Part 1
def population_total(demographics: list[data.CountyDemographics])->int:
    total = 0
    for pop in demographics:
        total += pop.population["2014 Population"]
    return total


# Part 2
def filter_by_state(demographics: list[data.CountyDemographics], state_abbrev: str)->list[data.CountyDemographics]:
    states = []
    for st in demographics:
        if state_abbrev == st.state:
            states.append(st)
    return states


# Part 3
def population_by_education(population: list[data.CountyDemographics], ed: str) -> float:
    total = 0.0
    for subpop in population:
        if ed in subpop.education:
            total += (subpop.education[ed]/100 * subpop.population['2014 Population'])
    return total

def population_by_ethnicity(population: list[data.CountyDemographics], ethnic:str) -> float:
    total = 0.0
    for subpop in population:
        if ethnic in subpop.ethnicities:
            total += (subpop.ethnicities[ethnic]/100 * subpop.population['2014 Population'])
    return total

def population_below_poverty_level(population: list[data.CountyDemographics]) -> float:
    total = 0.0
    for subpop in population:
        if 'Persons Below Poverty Level' in subpop.income:
            total += (subpop.income['Persons Below Poverty Level']/100 * subpop.population['2014 Population'])
    return total


# Part 4
def percent_by_education(population: list[data.CountyDemographics], edu: str) -> float:
    percent = 0.0
    subpop = population_by_education(population, edu)
    total_pop = population_total(population)
    percent = round(subpop/total_pop * 100, 3)

    for county in population:
        if edu not in county.education:
            return 0

    return percent

def percent_by_ethnicity(population: list[data.CountyDemographics], ethnic:str) -> float:
    percent = 0.0
    subpop = population_by_ethnicity(population, ethnic)
    total_pop = population_total(population)
    percent = round(subpop/total_pop * 100, 3)

    for county in population:
        if ethnic not in county.ethnicities:
            return 0

    return percent

def percent_below_poverty_level(population: list[data.CountyDemographics]) -> float:
    percent = 0.0
    subpop = population_below_poverty_level(population)
    total_pop = population_total(population)
    percent = round(subpop/total_pop * 100, 3)

    return percent


# Part 5
def education_greater_than(population: list[data.CountyDemographics], edu: str, percent_threshold: float) -> list[data.CountyDemographics]:
    return [county for county in population if county.education[edu] > percent_threshold]

def education_less_than(population: list[data.CountyDemographics], edu: str, percent_threshold: float) -> list[data.CountyDemographics]:
    return [county for county in population if county.education[edu] < percent_threshold]


def ethnicity_greater_than(population: list[data.CountyDemographics], ethnicity: str, percent_threshold:float) -> list[data.CountyDemographics]:
    return [county for county in population if county.ethnicities[ethnicity] > percent_threshold]

def ethnicity_less_than(population: list[data.CountyDemographics], ethnicity: str, percent_threshold: float) -> list[
    data.CountyDemographics]:
    return [county for county in population if county.ethnicities[ethnicity] < percent_threshold]


def below_poverty_level_greater_than(population: list[data.CountyDemographics], percent_threshold: float) -> list[data.CountyDemographics]:
    return [county for county in population if county.income['Persons Below Poverty Level'] > percent_threshold]

def below_poverty_level_less_than(population: list[data.CountyDemographics], percent_threshold: float) -> list[data.CountyDemographics]:
    return [county for county in population if county.income['Persons Below Poverty Level'] < percent_threshold]

