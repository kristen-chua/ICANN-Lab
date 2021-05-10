#quakerNetworkX.py
#https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python
import csv
from operator import itemgetter
import networkx as nx 
from networkx.algorithms import community 
#importing matplotlib was giving me an error, so I had to write
# pip install matplotlib in the console
import matplotlib.pyplot as plt #importing to do the visualization with pyplot https://www.kaggle.com/kingburrito666/pokemon-complete-analysis-networkx
#This part of networkx, for community detection, must be imported separately

with open('quakers_nodelist.csv','r') as nodecsv: #open the file
		nodereader = csv.reader(nodecsv) #read the csv
		#retrieve the data (using Python list comprehension and list slicing to remove the header row)
		nodes = [n for n in nodereader][1:]

node_names = [n[0] for n in nodes] #get list of only the node names

with open('quakers_edgelist.csv','r') as edgecsv: #open the file
	edgereader = csv.reader(edgecsv) #read the csv
	edges = [tuple(e) for e in edgereader][1:] #retrieve the data

#checks to make sure data is ok
print(len(node_names)) #should be 119 nodes
print(len(edges)) #should be 174 edges

G = nx.Graph()
#creates graph object G with nothing in it

G.add_nodes_from(node_names)
G.add_edges_from(edges)

print(nx.info(G)) #prints info about the graph

#create five empty dictionaries for your attributes
hist_sig_dict = {}
gender_dict = {}
birth_dict = {}
death_dict = {}
id_dict = {}

#loop through nodes list and add appropriate items to each dictionary
for node in nodes: #loop through the list, one row at a time 
	hist_sig_dict[node[0]]=node[1]
	gender_dict[node[0]]=node[2]
	birth_dict[node[0]]= node[3]
	death_dict[node[0]]=node[4]
	id_dict[node[0]]=node[5]

#the set_node_attributes function takes three  three variables: 
#the Graph to which you’re adding the attribute, the dictionary of id-attribute pairs, and the name of the new attribute
nx.set_node_attributes(G, hist_sig_dict, 'historical_significance')
nx.set_node_attributes(G, gender_dict, 'gender')
nx.set_node_attributes(G, birth_dict, 'birth_year')
nx.set_node_attributes(G, death_dict, 'death_year')
nx.set_node_attributes(G, id_dict, 'sdfb_id')

for n in G.nodes():#Loop through every node in our data "n" will be the name of the person
	print(n, G.nodes[n]['birth_year']) #access every node by its name, and then by the attribute "birth_year"

#Network density (simply the ratio of actual edges in the network to all possible edges in the network) gives you a quick sense of how closely knit your network is.
density = nx.density(G)
print("Network density:", density)
#density of our network is approximately 0.0248. On a scale of 0 to 1, not a very dense network,

#calculate shortest path
#pass input variables: the whole graph, your source node, and your target node.
#shortest path between Margaret Fell and George Whitehead?
fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")
print("Shortest path between Fell and Whitehead:",fell_whitehead_path)
#The output of shortest_path will be a list of the nodes that includes the “source” (Fell), the “target” (Whitehead), and the nodes between them
print("Length of that path:", len(fell_whitehead_path)-1)
#We take the length of the list minus one because we want the number of edges (or steps) between the nodes listed here, rather than the number of nodes.

#diameter, which is the longest of all shortest paths. 
#After calculating all shortest paths between every possible pair of nodes in the network, diameter is the length of the path between the two nodes that are furthest apart. 
#The measure is designed to give you a sense of the network’s overall size, the distance from one end of the network to another.
# !!! nx.diameter(G) #yields error "not connected". Because there are some nodes that have no path at all to others, it is impossible to find all of the shortest paths. 
# If your Graph has more than one component, this will return False:
print(nx.is_connected(G))
#use nx.connected_components to get list of components
#use max() to find the largest one
components = nx.connected_components(G)
largest_component = max(components, key=len)

#create a "subgraph" of the largest component
#calculate the diameter of the subgraph
subgraph = G.subgraph(largest_component)
diameter = nx.diameter(subgraph)
print("Network diameter of largest component:", diameter)

#Triadic closure supposes that if two people know the same person, they are likely to know each other. 
#One way of measuring triadic closure is called clustering coefficient because of this clustering tendency, but the structural network measure you will learn is known as transitivity.
#Transitivity is the ratio of all triangles over all possible triangles. 
triadic_closure = nx.transitivity(G)
print("Triadic closure:", triadic_closure)

#a node's degree is the sum of its edges
#calculates degree
degree_dict = dict(G.degree(G.nodes()))
#adding it as an attribute to our network
nx.set_node_attributes(G, degree_dict,'degree')
#since we added degree as an attribute, we can see William Penn's degree
print(G.nodes['William Penn'])
# find the top twenty nodes ranked by degree
sorted_degree = sorted(degree_dict.items(), key=itemgetter(1), reverse=True)
#degree_dict.items() = items you want to sort
#key=itemgetter(1) = what to sort by (the degrees)
#reverse=True . Tells sorted() to go in reverse so that the highest degree is first
print("Top 20 nodes by degree:")
for d in sorted_degree[:20]:
	print(d)

#eigenvector centrality is a kind of extension of degree—it looks at a combination of a node’s edges and the edges of that node’s neighbors. 
#Eigenvector centrality cares if you are a hub, but it also cares how many hubs you are connected to. 
#betweenness centrality looks at all the shortest paths that pass through a particular node 
betweenness_dict = nx.betweenness_centrality(G) #run betweenness centrality
eigenvector_dict = nx.eigenvector_centrality(G) #run eigenvector centrality

#Assign each to an attribute in your network
nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')

#sort betweenness by changing the variable names in the sorting code
sorted_betweenness = sorted(betweenness_dict.items(),key=itemgetter(1),reverse=True)
#key=itemgetter(1) means sort by betweenness centrality

print("Top 20 nodes by betweenness centrality:")
for b in sorted_betweenness[:20]:
	print(b)
#What if you want to know which of the high betweenness centrality nodes had low degree? 
#That is to say: which high-betweenness nodes are unexpected? 

#First get top 20 nodes by betweeneness as a list
top_betweenness = sorted_betweenness[:20]
#Then find and print their degree
for tb in top_betweenness: #Loop through top_betweenness
	degree = degree_dict[tb[0]] # use degree_dict to access a node's degree
	print("Name:", tb[0], "| Betweenness Centrality:", tb[1],"| Degree:", degree)

communities = community.greedy_modularity_communities(G)
##The method greedy_modularity_communities() tries to determine the number of communities appropriate for the graph,
# it creates a list of special “frozenset” objects (similar to lists).

# In order to add this information to your network in the now-familiar way, 
# you must first create a dictionary that labels each person with a number value for the group to which they belong:

modularity_dict = {} #create a blank dictionary
for i,c in enumerate(communities): #Loop through list of communities
	for name in c: #Loop through each person in a community
		modularity_dict[name]=i #create an entry in the dictonary forthe person, where the value is which group they belong

#Now you can add modularity information like we did the other metrics
nx.set_node_attributes(G, modularity_dict,'modularity')

#First get a list of just the nodes in that class
class0 = [n for n in G.nodes() if G.nodes[n]['modularity']==0]

#Then create a dictionary of the eigenvector centralities of those nodes
class0_eigenvector = {n:G.nodes[n]['eigenvector'] for n in class0}

#Then sort that dictionary and print the first 5 results
class0_sorted_by_eigenvector = sorted(class0_eigenvector.items(), key=itemgetter(1), reverse=True)

print("Modularity Class 0 Sorted by Eigenvector Centrality:")
for node in class0_sorted_by_eigenvector[:5]:
	print("Name:", node[0],"| Eigenvector Centrality:", node[1])


for i,c in enumerate(communities): #Loop through the list of communities
	if len(c) > 2: #Filter out modularity classes with 2 or fewer nodes
		print('Class '+str(i)+":",list(c))

#creates quaker_network.gexf. Open file in gephi program
#nx.write_gexf(G, 'quaker_network.gexf')
#Was able to graph with gephi, but scrolling did not work
#and no dev work for a few yearsvideos that helped me play around with gephi
#how to do labels  #https://www.youtube.com/watch?v=eu1mibcOrN0
#how to change node sizes #https://www.google.com/search?q=change+node+size+gephi&oq=change+node+size+gephi&aqs=chrome..69i57.4929j1j4&sourceid=chrome&ie=UTF-8#kpvalbx=_Y72RYJ_uAp7P0PEPpMClwAs18

#since gephi seemed outdated, I tried plotting the network with
#matplotlib, but it didn't do what I thought it would 
#seeing disconnected line segments as of 05/04/2021
#https://www.kaggle.com/kingburrito666/pokemon-complete-analysis-networkx
plt.figure(figsize=(20,20))
pos=nx.spring_layout(G,k=0.15)
nx.draw_networkx(G,pos,node_size=25, node_color='blue')
plt.show()
