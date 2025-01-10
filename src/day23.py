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

def part_two():
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




if __name__ == "__main__":
    input_file_path = "input/day23input.txt"
    input = ""
    with open(input_file_path, "r") as f:
        input = f.read()
    input = input.split("\n")
    input = [el.split("-") for el in input]
    print("part one: ", part_one(input))