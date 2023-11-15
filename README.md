I am using this repo just to save my code as I keep doing Gurobi exercises. I am implementing models proposed by the logistic chair of my university, as most of the models that I could find were either too easy or too hard, I am still in my learning phase.


# Ressource allocation model 

Given a matrix Days/workers, make a model that decide on the amount of workers to allocated in each day while making sure that each day has at least the required number of workers. 

Using a set covering problem, this would be a suitable model for this problem: 

$min \sum\limits_{j \in  S}{c_jx_j} $ 

$\sum\limits_{j \in  S}{a_{ij}x_j } \forall i \in T $


# Faciliy location problem 

Given a set of clients and a set of potential locations, choose up to p locations that can cover all the clients while also minimizing the total covering distance.
