file_path = './day8.in'


with open(file_path,'r')as file:
    lines=file.read().strip().split('\n')

    instructions,entries = lines[0],lines[2:]
    nodes = {}
    for line in entries:
        lhs,rhs = map(str.strip,line.split('='))
        nodes[lhs] = list(map(str.strip, rhs[1:-1].split(',')))

    count = 0
    node_value = 'AAA'
