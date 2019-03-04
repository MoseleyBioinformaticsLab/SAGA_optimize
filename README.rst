SAGA_optimize
=============


.. image:: https://img.shields.io/pypi/l/SAGA_optimize.svg
   :target: https://choosealicense.com/licenses/bsd-3-clause-clear/
   :alt: License information

.. image:: https://img.shields.io/pypi/v/SAGA_optimize.svg
   :target: https://pypi.org/project/SAGA_optimize
   :alt: Current library version

.. image:: https://img.shields.io/pypi/pyversions/SAGA_optimize.svg
   :target: https://pypi.org/project/SAGA_optimize
   :alt: Supported Python versions

.. image:: https://api.travis-ci.org/MoseleyBioinformaticsLab/SAGA_optimize.svg?branch=master
   :target: https://travis-ci.org/MoseleyBioinformaticsLab/SAGA_optimize
   :alt: Travis CI status



`SAGA_optimize` is a novel type of combined simulated annealing and genetic algorithm used to find the optimal solutions to a set of parameters based on a given energy function calculated using the set of parameters.

Citation
~~~~~~~~
Please cite the GitHub repository until our manuscript is accepted for publications: https://github.com/MoseleyBioinformaticsLab/SAGA_optimize.git

Installation
~~~~~~~~~~~~

`SAGA_optimize` runs under Python 3.6+ and is available through python3-pip. Install via pip or clone the git repo and install the following dependencies and you are ready to go!

Install on Linux
----------------

Pip installation
................

.. code:: bash

    pip3 install SAGA-optimize

GitHub Package installation
...........................

Make sure you have git_ installed:

.. code:: bash 
 
   cd ~/
   git clone https://github.com/MoseleyBioinformaticsLab/SAGA_optimize.git
    
Dependecies 
...........

`SAGA_optimize` requires the following Python libraries:
    
    * JSONPickle_ for saving Python objects in a JSON serializable form and outputting to a file.


Quickstart
~~~~~~~~~~

.. code:: python

   >>> import SAGA_optimize
   >>> saga = SAGA_optimize.SAGA(stepNumber=100000, temperatureStepSize=100, startTemperature=0.5, alpha=1, direction=-1, energyCalculateion=energyCalculation, crossoverRate=0.5, mutationRate=3, annealMutationRate=1, populationSize=20)                  # SAGA instance creation.
   >>> saga.addElementDescriptions(SAGA_optimize.ElementDescription(low=0, high=10), SAGA_optimize.ElementDescription(low=0, high=10), SAGA_optimize.ElemenDescription(low=0, high=10), SAGA_optimize.ElementDescription(low=0, high=10), SAGA_optimize.ElementDescription(low=0, high=10))        # Add optimized parameters.
   >>> optimized_population = saga.optimize()              # the population returned after the opitimization.

.. note:: Read the User Guide and the ``SAGA_optimize`` Tutorial on ReadTheDocs_ to learn more and to see code examples on using the ``SAGA_optimize`` as a library.

License
~~~~~~~

.. include:: ../LICENSE

Made available under the terms of The Clear BSD License. See full license in LICENSE_.

Authors
~~~~~~~

* **Huan Jin**
* **Hunter N.B. Moseley**

.. _ReadTheDocs: https://saga-optimize.readthedocs.io/en/latest/
.. _jsonpickle: https://jsonpickle.github.io/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
.. _LICENSE: 

