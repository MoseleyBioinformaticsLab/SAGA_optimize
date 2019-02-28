User Guide
==========

Description
~~~~~~~~~~~

The :mod:`SAGA_optimize` package provides a simple Python interface for solving boundary-value inverse problem based on the simulated annealing and genetic algorithm. 

Installation
~~~~~~~~~~~~

`SAGA_optimize` runs under Python 3.6+ and is available through python3-pip. Install via pip or clone the git repo and install the following dependencies and you are ready to go!

Install on Linux
----------------

Pip installation (method 1)
...........................

.. code:: bash

    pip3 install SAGA-optimize

GitHub Package installation (method 2)
......................................

Make sure you have git_ installed:

.. code:: bash
   
   cd ~/
   git clone https://github.com/MoseleyBioinformaticsLab/SAGA_optimize.git
    
Dependecies 
...........

`SAGA_optimize` requires the following Python libraries:
    
    * JSONPickle_ for saving Python objects in a JSON serializable form and outputting to a file.
    
Basic usage
~~~~~~~~~~~
The :mod:`SAGA_optimize` package is used to find the optimal solutions to a set of parameters based on a given energy function calculated using the set of parameters.
   

.. note:: Read :doc:`tutorial` to learn more and see code examples on using the :mod:`SAGA_optimize` as a library.

.. _pip: https://pip.pypa.io/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/
.. _JSONPickle: https://github.com/jsonpickle/jsonpickle
