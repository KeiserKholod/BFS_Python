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
    return matrix, int(count)
    
matrix, size = get_matrix()
 