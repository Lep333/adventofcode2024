import copy

def part_one(connections: list[tuple[str, str]]) -> int:
    network = {}
    inter_connected = []
    for pc1, pc2 in connections:
        if pc := network.get(pc1):
            pc.append(pc2)
        else:
            network[pc1] = [pc2]
        if pc := network.get(pc2):
            pc.append(pc1)
        else:
            network[pc2] = [pc1]
    
    total = 0
    for pc1, neighbours in network.items():
        for pc2 in neighbours:
            for pc3 in network[pc2]:
                if pc1 in network[pc3]:
                    if {pc1, pc2, pc3} not in inter_connected:
                        inter_connected.append({pc1, pc2, pc3})

    for net in inter_connected:
        for pc in net:
            if pc[0] == "t" and len(net) == 3:
                total += 1
                break
    return total

def part_two(connections: list[tuple[str, str]]):
    network = {}
    for pc1, pc2 in connections:
        if pc := network.get(pc1):
            pc.append(pc2)
        else:
            network[pc1] = [pc2]
        if pc := network.get(pc2):
            pc.append(pc1)
        else:
            network[pc2] = [pc1]
    
    cliques = []
    visited = []
    max_network = 0
    for pc1 in network.keys():
        biggest_network = find_common_pcs(network, pc1, visited, max_network)
        if len(biggest_network) > max_network:
            max_network = len(biggest_network)
        cliques.append(biggest_network)
        visited.append(pc1)
    
    cliques.sort(key=lambda el: len(el), reverse=True)
    clique_as_list = list(cliques[0])
    clique_as_list.sort()
    return ",".join(clique_as_list)

def pc_in_network(networks: list[list[str]], pc_to_find: str) -> list[str]|None:
    for network in networks:
        if pc_to_find in network:
            return network
    return None

def find_clique(network: dict[list], inter_connected):
    for node, neighbours in network.items():
        queue = [neighbours]
        visited = []
        while queue:
            node = queue.pop()
            if not visited:
                visited.append(node)
            else:
                continue

def find_common_pcs(network: dict[list], pc: str, visited: list, biggest_clique: int) -> list:
    nodes: list = network[pc]
    nodes = list(set(nodes).difference(set(visited)))
    if len(nodes) + 1 <= biggest_clique:
        return []
    cliques = [{pc}]
    new_cliques = []
    no_of_neighbours = len(network[pc])
    all_cliques = []
    for i in range(no_of_neighbours):
        while cliques:
            clique = cliques.pop(0)
            for node in nodes:
                if node in clique or node in visited:
                    continue
                common_neighbours = set(network[node]).intersection(clique)
                if common_neighbours == clique:
                    new_clique = clique.union({node})
                    if new_clique not in all_cliques:
                        new_cliques.append(new_clique)
                        all_cliques.append(new_clique)
        cliques = copy.deepcopy(new_cliques)
        if not clique:
            break
        new_cliques = []
    all_cliques.sort(key=lambda el: len(el), reverse=True)
    return all_cliques[0] if all_cliques else set()

if __name__ == "__main__":
    input_file_path = "input/day23input.txt"
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    input = input.split("\n")
    input = [el.split("-") for el in input]
    print("please wait for a bit!")
    print("part one: ", part_one(input))
    print("part two: ", part_two(input))