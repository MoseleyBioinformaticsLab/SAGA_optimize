The SAGA_optimize Tutorial
==========================

The `SAGA_optimize` package is a novel type of combined simulated annealing and genetic algorithm used to find the optimal solutions to a set of parameters based on a given energy function calculated using the set of parameters.

ElementDescription creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The creation of ElementDescription instance (optimized parameter) may need the range of the parameter, and its name. Default value and mutation function can be provided. Please refer to the API documentation for detailed information.

   .. code:: Python
      
      >>>import SAGA
      >>>element1 = SAGA.ElementDescription(low=0, high=10, name='element1')    # ElementDescription instance creation.
      >>>element2 = SAGA.ElementDescription(low=0, high=10, name='element2') 
      >>>element3 = SAGA.ElementDescription(low=0, high=10, name='element3') 
      >>>element4 = SAGA.ElementDescription(low=0, high=10, name='element4')
      >>>elements = [element1, element2, element3, element4] 

Guess creation
~~~~~~~~~~~~~~

The Guess instance collects all the optimized parameters and their corresponding values for a given energy function.
 
   .. code:: Python

      >>>import SAGA
      >>>values = [element.value for element in elements]
      >>>guess = SAGA.Guess(elements, values)     # Guess instance creation.
      >>>clonedGuess = guess.clone()              # Create a new guess by cloning the ElementDescriptions and the corresponding values of an existing guess instance.

Population creation
~~~~~~~~~~~~~~~~~~~

The Population instance collects a group of Guess instanaces, aggregates information accross among these Guess instances, and selects the best Guess instance. Creatation of Population instance requires the size, elementDescriptions, energyCalculation parameters. Please refer to the API documentation for detailed information.

   .. code:: Python

      >>>import SAGA
      >>>def energyCalculation(elements):     # example of energy calculation function definition.
      >>>   energy = 0
      >>>   for indedx in range(len(elements)):
      >>>      energy += abs(index+1-elements[index])
      >>>   return energy
      >>>population = SAGA.Population(20, elements, energyCalculation)   # Population instance creation.
      >>>bestIndex = population.bestIndex     # Get the index of the best Guess among the Population.
      >>>bestGuess = population.bestGuess     # Get the best Guess instance of the Population instance.

SAGA creation
~~~~~~~~~~~~~

The SAGA class is responsible for the optimization process. Optimization parameters like stepNumber, startTemperature, temperatureStepSize, alpha, populationSize, energyCalculation should be provided for SAGA creation. Please refer to the API documentation for detailed information.

   .. code:: Python
   
      >>>import SAGA
      >>>saga = SAGA.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5, alpha=1, direction=-1, energyCalculateion=energyCalculation, crossoverRate=0.5, mutationRate=3, annealMutationRate=1, populationSize=20)                     # SAGA instance creation.
      >>>saga.addElementDescriptions(SAGA.ElementDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10), SAGA.ElemenDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10))           # Add optimized parameters.
      >>>optimized_population = saga.optimize()              # the population returned after the opitimization.
      
