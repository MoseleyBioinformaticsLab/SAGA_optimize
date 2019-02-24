SAGA-optimize
=============

`SAGA-optimize` is a novel type of combined simulated annealing and genetic algorithm used to find the optimal solutions to a set of parameters based on a given energy function calculated using the set of parameters.

Citation
~~~~~~~~
Please cite the GitHub repository until our manuscript is accepted for publications:

Installation
~~~~~~~~~~~~

`SAGA-optimize` runs under Python 3.6+ and is available through python3-pip. Install via pip or clone the git repo and install the following dependencies and you are ready to go!

Install on Linux
----------------

Pip installation
................

.. code:: bash

    python3 -m pip install SAGA-optimize

GitHub Package installation
...........................

Make sure you have git_ installed:

.. code:: bash 
    
Dependecies 
...........

`SAGA-optimize` requires the following Python libraries:
    
    * JSONPickle_ for saving Python objects in a JSON serializable form and outputting to a file.


Quickstart
~~~~~~~~~~

.. code:: bash

   >>>from SAGA_optimize import SAGA
   >>>saga = SAGA.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5, alpha=1, direction=-1, energyCalculateion=energyCalculation, crossoverRate=0.5, mutationRate=3, annealMutationRate=1, populationSize=20)                  # SAGA instance creation.
   >>>saga.addElementDescriptions(SAGA.ElementDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10), SAGA.ElemenDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10), SAGA.ElementDescription(low=0, high=10))        # Add optimized parameters.
   >>>optimized_population = saga.optimize()              # the population returned after the opitimization.

.. note:: Read the User Guide and the ``SAGA-optimize`` Tutorial on ReadTheDocs_ to learn more and to see code examples on using the ``SAGA-optimize`` as a library.

License
~~~~~~~

.. include:: ../LICENSE

Made available under the terms of The Clear BSD License. See full license in LICENSE_.

Authors
~~~~~~~

* **Huan Jin**
* **Hunter N.B. Moseley**

.. _ReadTheDocs: 
.. _jsonpickle: https://jsonpickle.github.io/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
.. _LICENSE: 

