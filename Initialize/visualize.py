import igraph


def visualize_graph(graph):
    layout = graph.layout("circular")  # Other possible layouts: kk, drl, fr, tree

    # Visual style of the graph
    visual_style = dict(
        vertex_size=8,
        edge_color='#999',
        vertex_shape="circle",
        vertex_dist=20,
        vertex_label_size=16,
        vertex_label_color='#121212',
        vertex_label_dist=3,
        vertex_label_angle=0,
        vertex_color='#121212',
        margin=50,
        autocurve=True,
    )

    igraph.plot(graph, layout=layout, **visual_style)
