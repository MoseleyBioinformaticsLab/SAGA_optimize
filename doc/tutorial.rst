The SAGA_optimize Tutorial
==========================

The `SAGA_optimize` package is a novel type of combined simulated annealing and genetic algorithm used to find the optimal solutions to a set of parameters based on a given energy function calculated using the set of parameters.

To perform `SAGA_optimize`, we need define an energy function first.

   .. code:: Python
      
      >>> def energyCalculation(elements):     # example of energy function.
      >>>    energy = 0
      >>>    for indedx in range(len(elements)):
      >>>       energy += abs(index+1-elements[index])
      >>>    return energy

Then we need to construct the parameters (ElementDescription instances) for optimization. ElementDescription instance initialization may require the range of the parameter, and its name. Default value and mutation function can also be provided. Please refer to the API documentation for detailed information.

We can construct ElementDescription instances first, and then pass them into SAGA.
      
   .. code:: Python

      >>> import SAGA_optimize
      >>> element1 = SAGA_optimize.ElementDescription(low=0, high=10, name='element1')    # ElementDescription instance creation.
      >>> element2 = SAGA_optimize.ElementDescription(low=0, high=10, name='element2') 
      >>> element3 = SAGA_optimize.ElementDescription(low=0, high=10, name='element3') 
      >>> element4 = SAGA_optimize.ElementDescription(low=0, high=10, name='element4')
      >>> element5 = SAGA_optimize.ElementDescription(low=0, high=10, name='element5')
      >>> elements = [element1, element2, element3, element4, element5] 
      >>> saga = SAGA_optimize.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5, elementDescriptions=elements,
                                    alpha=1, direction=-1, energyCalculation=energyCalculation, crossoverRate=0.5, mutationRate=3, 
                                    annealMutationRate=1, populationSize=20)
      
Or we can create SAGA instance first, and then add the ElementDescirption instances.
     
   .. code:: Python
  
      >>> import SAGA_optimize
      >>> saga = SAGA_optimize.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5, alpha=1, direction=-1, 
                                    energyCalculation=energyCalculation, crossoverRate=0.5, mutationRate=3, annealMutationRate=1, 
                                    populationSize=20)                     # SAGA instance creation.
      >>> saga.addElementDescriptions(SAGA_optimize.ElementDescription(low=0, high=10, name='element1'), SAGA_optimize.ElementDescription(low=0, high=10, name='element2'), 
                                      SAGA_optimize.ElemenTDescription(low=0, high=10, name='element3'), SAGA_optimize.ElementDescription(low=0, high=10, name='element4'), 
                                      SAGA_optimize.ElementDescription(low=0, high=10, name='element5'))           # Add optimized parameters.

Next, we can conduct optimization.

   .. code:: Python

      >>> optimized_population = saga.optimize()              # the population returned after the opitimization.
      >>> bestIndex = optimized_population.bestIndex          # To get the best index of the Population.
      >>> bestGuess = optimized_population.bestGuess          # To get the best Guess instance of the Population.
      >>> print(bestGuess)

   .. code:: bash

      Guess: Energy = 0.010800440413622603 Parameters: Element 1 = 0.9986605131302921 Element 2 = 2.0049781612156004 Element 3 = 3.0036003043186144 Element 4 = 3.999532176465393 Element 5 = 5.000414664475093
      
