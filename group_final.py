"""Script that analyses cycles of a particular length in k-regular graphs."""
import matplotlib.pyplot as plt
import networkx as nx

"""tests
k = 2
n = 14
degree_seq = [k for i in range(n)]
graph1 = nx.configuration_model(degree_seq)
cycles = list(nx.simple_cycles(graph1))
print(cycles)
nx.draw(graph1, with_labels=True)
plt.show()
"""


def generate_graphs(samples, nodes, degree):
    """Find distribution of cycles for fixed k."""
    degree_seq = [degree for i in range(nodes)]
    cycle_collection = {}
    for sample in range(samples):
        a_graph = nx.configuration_model(degree_seq)
        nx.draw(a_graph, with_labels=True)
        plt.show()
        cycles = list(nx.simple_cycles(a_graph))
        for cycle in cycles:
            length_cycle = len(cycle)
            if length_cycle not in cycle_collection:
                cycle_collection[length_cycle] = 1
            else:
                cycle_collection[length_cycle] += 1
    return cycle_collection


all_cycles = generate_graphs(1, 10, 2)
print(all_cycles)
x = []
y = []
for key in all_cycles:
    x.append(key)
    y.append(all_cycles[key])

plt.scatter(x, y)
plt.show()
