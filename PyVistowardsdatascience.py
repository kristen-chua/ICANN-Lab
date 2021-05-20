from pyvis.network import Network
# adding nodes to network
net = Network()
#adding node one by one
net.add_node(1, label="Node 1")
net.add_node(2)

#adding node as a list
nodes = ["a","b","c","d"]
net.add_nodes(nodes)
net.add_nodes("hello")

#add edge
net.add_edge(1,2,weight=.87)

#visualization
net.toggle_physics(True)
net.show('mygraph.html') # open in File explorer
net.show_buttons(filter_=['physics']) # adds bounciness
