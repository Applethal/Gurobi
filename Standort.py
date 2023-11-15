import gurobipy as gp

Filialen = range(1, 11)
Standorte = range(1, 16)

zeit_data = {(i, j): value for (i, j), value in zip(
    [(i, j) for i in Filialen for j in Standorte],
    [23, 18, 35, 16, 45, 28, 27, 34, 19, 23, 17, 6, 29, 34, 23,
     21, 30, 43, 15, 36, 27, 32, 21, 19, 10, 26, 19, 10, 23, 15,
     13, 27, 12, 19, 27, 18, 7, 9, 11, 15, 14, 18, 8, 11, 23,
     26, 15, 23, 17, 19, 9, 19, 10, 25, 17, 19, 20, 17, 11, 15,
     14, 23, 20, 16, 9, 8, 15, 23, 25, 11, 17, 15, 27, 23, 13,
     12, 18, 19, 4, 10, 17, 26, 18, 20, 23, 12, 10, 17, 23, 9,
     9, 17, 25, 39, 27, 15, 12, 20, 27, 10, 24, 16, 17, 10, 27,
     19, 24, 18, 13, 8, 10, 17, 5, 12, 2, 7, 29, 10, 27, 20,
     17, 4, 19, 15, 16, 2, 11, 17, 15, 20, 26, 11, 10, 12, 20,
     7, 9, 10, 17, 4, 19, 15, 16, 2, 11, 12, 26, 13, 10, 13]
)}

p = 5

model = gp.Model()

x = model.addVars(Filialen, Standorte, vtype=gp.GRB.BINARY, name="x")
y = model.addVars(Standorte, vtype=gp.GRB.BINARY, name="y")

model.setObjective(gp.quicksum(zeit_data[i, j] * x[i, j] for i in Filialen for j in Standorte), gp.GRB.MINIMIZE)

for i in Filialen:
    model.addConstr(gp.quicksum(x[i, j] for j in Standorte) == 1, f"Zuordnung_{i}")

model.addConstr(gp.quicksum(y[j] for j in Standorte) == p, "Standortanzahl")

for i, j in zeit_data.keys():
    model.addConstr(x[i, j] <= y[j], f"Kopplung_{i}_{j}")

model.update()
model.optimize()

if model.status == gp.GRB.OPTIMAL:
    print("Optimal solution found:")
    for i in Filialen:
        for j in Standorte:
            print(f"x[{i},{j}] = {x[i, j].x}")
    print("Objective value:", model.objVal)
else:
    print("No optimal solution found.")
