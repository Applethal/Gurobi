import gurobipy as gp
from gurobipy import GRB


Tage = range(1, 8)
Schichten = range(1, 6)
b = {1: 20, 2: 25, 3: 26, 4: 26, 5: 30, 6: 30, 7: 35}
c = {1: 252, 2: 170, 3: 250, 4: 200, 5: 125}
a = {(i, j): 0 for i in Tage for j in Schichten}
a[1, 1] = 1
a[1, 3] = 1
a[2, 1] = 1
a[2, 5] = 1
a[3, 3] = 1
a[3, 4] = 1
a[4, 2] = 1
a[4, 5] = 1
a[5, 2] = 1
a[5, 4] = 1
a[5, 5] = 1
a[6, 2] = 1
a[6, 4] = 1
a[7, 1] = 1
a[7, 3] = 1

model = gp.Model()
x = model.addVars(Schichten, vtype=gp.GRB.INTEGER, name="x")
model.setObjective(gp.quicksum(c[j] * x[j] for j in Schichten), gp.GRB.MINIMIZE)
for i in Tage:
    model.addConstr(gp.quicksum(a[i, j] * x[j] for j in Schichten) >= b[i], name=f"Bedarf_{i}")


if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found:")
    for j in Schichten:
        print(f"x[{j}] = {x[j].x}")
    print("Objective value:", model.objVal)
else:
    print("No optimal solution found.")
