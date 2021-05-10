
import networkx as nx
import numpy as np
import pandas as pd

G1 = nx.Graph()
G1.add_edges_from([(0,1), 
                   (0,2),
                   (0,3),
                   (0,5),
                   (1,3),
                   (1,6),
                   (3,4),
                   (4,5),
                   (4,7),
                   (5,8),
                   (8,9)])
nx.draw_networkx(G1)