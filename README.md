I am using this repo just to save my code as I keep doing Gurobi exercises.


# Ressource allocation model 

Given a matrix Days/workers, make a model that decide on the amount of workers to allocated in each day while making sure that each day has at least the required number of workers. 

Using a set covering problem, this would be a suitable model for this problem: 

$min \sum\limits_{j \in  S}{c_jx_j} $ 

$\sum\limits_{j \in  S}{a_{ij}x_j } \forall i \in T $

