import collections

def get_matrix(path_to_file="input.txt"):
    matrix_str = ""
    with open(path_to_file,"r") as file:
        count = file.readline()
        matrix_str = file.read()
    matrix = []
    
    lines = matrix_str.split("\n")
    for line in lines:
        elements = line.split(" ")
        matrix.append(elements)
    return matrix
    
def is_acyclic(matrix, root=0):
    nodes = range(0, len(matrix))
    # посещенные вершины
    visited = collections.deque()
    visited.append(root)
    # массив, где лежит предыдущая вершина для каждой вершины(из которой в нее пришли)
    previous_nodes = [None for i in range(0, len(matrix))]
    
    while len(visited) != 0:
        current_node = visited.popleft()
        # проверяем, есть ли смежная нашей и не посещенная вершина
        for next_node in nodes:
            # индекс следующей вершины должен быть больше предыдущей
            if current_node <= next_node:
                if previous_nodes[next_node] is None:
                    if matrix[current_node][next_node] == "1":
                        visited.append(next_node)
                        previous_nodes[next_node] = current_node
                        print(str(current_node+1)+" "+str(next_node+1))
                        print(previous_nodes)
                else:
                    if matrix[current_node][next_node] == "1":
                        print(str(current_node+1)+" "+str(next_node+1))
                        print(previous_nodes)
                        # если вершина была посещена и мы можем в нее пойти, то мы встретили цикл
                        cycle = get_cycle(matrix, previous_nodes, current_node, next_node, root)
                        return False, cycle
    return True, None
                    
def get_cycle(matrix, previous_nodes, current_node, next_node, root):
    cycle = []
    # возвращаемся по списку посещенных вершин и собираем все "предыдущие" вершины
    previous_nodes[next_node] = current_node
    node = next_node
    cycle.append(node)
    while node != root:
        node = previous_nodes[node]
        cycle.append(node)
    cycle.sort()  
    return cycle              
        
        
    
    
matrix = get_matrix()
graph_is_acyclic, cycle = is_acyclic(matrix)
if graph_is_acyclic:
    print("A")
else:
    print("N " + str(cycle))
