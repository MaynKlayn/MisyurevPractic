def get_neighbors(animal):
    neighbors = list(zoo_graph.neighbors(animal))
    return neighbors


import networkx as nx
import matplotlib.pyplot as plt

zoo_graph = nx.Graph()

zoo_graph.add_node("Лиса (умерла)")
zoo_graph.add_node("Горные козлы")
zoo_graph.add_node("Обезьяна")
zoo_graph.add_node("Крокодил")
zoo_graph.add_node("Горные козлы")
zoo_graph.add_node("Жирафы")
zoo_graph.add_node("Бабочки")
zoo_graph.add_node("Пеликаны")
zoo_graph.add_node("Бурый медведь")
zoo_graph.add_node("Лев")
zoo_graph.add_node("Бобры")
zoo_graph.add_node("Гималайский медведь")
zoo_graph.add_node("Муравьед")
zoo_graph.add_node("Лама")
zoo_graph.add_node("Фламинго")

zoo_graph.add_edges_from([
    ("Лиса (умерла)", "Обезьяна"),
    ("Лиса (умерла)", "Пеликаны"),
    ("Лиса (умерла)", "Горные козлы"),
    ("Лиса (умерла)", "Муравьед"),
    ("Пеликаны", "Горные козлы"),
    ("Пеликаны", "Бабочки"),
    ("Пеликаны", "Бобры"),
    ("Бабочки", "Бурый медведь"),
    ("Бурый медведь", "Азиатский лев"),
    ("Азиатский лев", "Лев"),
    ("Лев", "Амурский тигр"),
    ("Лев", "Гималайский медведь"),
    ("Амурский тигр", "Гималайский медведь"),
    ("Бурый медведь", "Жираф"),
    ("Азиатский лев", "Жираф"),
    ("Горные козлы", "Жираф"),
    ("Обезьяна", "Крокодил"),
    ("Муравьед", "Фламинго"),
    ("Муравьед", "Бобры"),
    ("Муравьед", "Фламинго"),
    ("Бобры", "Фламинго"),
    ("Муравьед", "Лама"),
])

pos = nx.spring_layout(zoo_graph)
plt.figure(figsize=(10, 8))
nx.draw(zoo_graph, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black',
        font_weight='bold', edge_color='gray')
plt.title("Структурный зоопарк")
plt.show()

input_animal = "Лама"

neighbors = get_neighbors(input_animal)
if neighbors:
    print(f"Соседи у {input_animal}: {neighbors}")
else:
    print(f"{input_animal} не найден в зоопарке.")
