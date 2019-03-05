import SAGA_optimize
import math
import random

random.seed(9001)


def energyCalculation(elements):
    energy = 0
    for index in range(0, len(elements)):
        energy += abs(index + 1 - elements[index])
    return energy


def test_saga_optimize():

    saga = SAGA_optimize.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5,
                              alpha=1, direction=-1, energyCalculation=energyCalculation, crossoverRate=0.5,
                              mutationRate=3, annealMutationRate=1, populationSize=20)

    saga.addElementDescriptions(SAGA_optimize.ElementDescription(low=0, high=10),
                                SAGA_optimize.ElementDescription(low=0, high=10),
                                SAGA_optimize.ElementDescription(low=0, high=10),
                                SAGA_optimize.ElementDescription(low=0, high=10),
                                SAGA_optimize.ElementDescription(low=0, high=10))

    
    optimized_population = saga.optimize()
    bestGuess = optimized_population.bestGuess

    for i in range(len(bestGuess.elements)):
        assert abs(bestGuess.elements[i] - 1 - i) < math.pow(10, -6)



