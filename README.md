# Decentralized Graph Coloring Exploration

This repository explores decentralized strategies for graph coloring, focusing on a 2D lattice structure. Two distinct approaches are investigated: a general method involving random color assignments and a specialized method utilizing clustered color assignments to potentially improve coloring efficiency.

## Description

The repository contains two Python programs designed to address the problem of graph coloring in a decentralized manner. The goal is to explore how different initial color assignment strategies affect the number of iterations required to resolve color conflicts on a 2D lattice graph.

### Programs Overview

1. **General Random Coloring Approach**: Assigns colors randomly to each node and then iteratively resolves conflicts.
   
2. **Clustered Coloring Approach**: Assigns colors in clusters to minimize initial conflicts, followed by conflict resolution.

Both approaches are analyzed for their effectiveness in reducing the number of iterations needed to achieve a conflict-free coloring.



### Dependencies

- Python 3.x
- NetworkX
- matplotlib
