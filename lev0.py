import json
import networkx as nx

f=open('Input data/level0.json')
data=json.load(f)

def generate_graph(distance_matrix):
    nodes=len(distance_matrix)
    G=nx.Graph()

    for i in range(nodes):
        for j in range(i+1,nodes):
            weight = distance_matrix[i][j]
            G.add_edge(i, j, weight=weight)
    return G

def solve_tsp(graph):
   
    tsp_path = nx.approximation.traveling_salesman_problem(graph, cycle=True)
    return tsp_path



distance_matrix=[]
val=[]

val.append(0)
for i in (data["restaurants"]["r0"]["neighbourhood_distance"]):
    val.append(i)
#print(val)
distance_matrix.append(val)
val=[]
#print(data["restaurants"]["r0"]["neighbourhood_distance"][2])
for i in range(data["n_neighbourhoods"]):
    pathh = str("n")+str(i)
    val.append(data["restaurants"]["r0"]["neighbourhood_distance"][i])
    for j in data["neighbourhoods"][str(pathh)]["distances"]:
        val.append(j)
    distance_matrix.append(val)
    val=[]
#print(distance_matrix)

weighted_graph = generate_graph(distance_matrix)
tsp_path = solve_tsp(weighted_graph)
print(tsp_path)
for i in range(len(tsp_path)) :
    if(i==0):
        tsp_path[i]=str("r")+str(tsp_path[i])
    elif(i==len(tsp_path)-1):
        tsp_path[i]=str("r")+str(tsp_path[i])
    else:
        tsp_path[i]=str("n")+str(tsp_path[i]-1)
    #print(i)
print(tsp_path)

output={
    "v0":
    {
        "path":tsp_path
    }
}

with open("lev0_out.json","w") as output_file:
    json.dump(output,output_file)











