from math import sin 
from gaft import GAEngine
from gaft.components import BinaryIndividual, Population
from gaft.operators import RouletteWheelSelection, UniformCrossover, FlipBitMutation
from gaft.analysis import ConsoleOutput

# Analysis plugin base class.
from gaft.plugin_interfaces.analysis import OnTheFlyAnalysis

indv_template = BinaryIndividual(ranges=[(0, 15)], eps=0.001)
population = Population(indv_template=indv_template, size=50)
population.init()  # Initialize population with individuals.

# Use built-in operators here.
selection = RouletteWheelSelection()
crossover = UniformCrossover(pc=0.8, pe=0.5)
mutation = FlipBitMutation(pm=0.1)

engine = GAEngine(population=population, selection=selection,
                  crossover=crossover, mutation=mutation, analysis=[ConsoleOutput])

@engine.fitness_register
def fitness(indv):
    x, = indv.solution
    return (-3)*(x-30)**2*sin(x)

if '__main__' == __name__:
    engine.run(ng=100)