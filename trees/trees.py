"""This code produces a tree-like plot."""

from math import sin, cos
import matplotlib.pyplot as plt

# scaling factor
scale = 1
# scaling reduction
scale_reduction = 0.6
# branch specifications
branch_specifications = [[0,1,0]]
# number of layers
n_layers = 5
# plot trunk of tree (vertical)
plt.plot([0,0],[0,1])

for _ in range(n_layers):
    new_branch_specifications = []

    for j in range(len(branch_specifications)): 
        # create new branches
        new_branch_1 = [branch_specifications[j][0]+scale*sin(branch_specifications[j][2]-0.1), branch_specifications[j][1]+scale*cos(branch_specifications[j][2]-0.1), branch_specifications[j][2]-0.1]
        new_branch_2 = [branch_specifications[j][0]+scale*sin(branch_specifications[j][2]+0.1), branch_specifications[j][1]+scale*cos(branch_specifications[j][2]+0.1), branch_specifications[j][2]+0.1]
        # append new branches
        new_branch_specifications.append(new_branch_1)
        new_branch_specifications.append(new_branch_2)
        # plot new branches
        plt.plot([branch_specifications[j][0], new_branch_specifications[-2][0]],[branch_specifications[j][1], new_branch_specifications[-2][1]])
        plt.plot([branch_specifications[j][0], new_branch_specifications[-1][0]],[branch_specifications[j][1], new_branch_specifications[-1][1]])
    
    # update branch specifications with new branches
    branch_specifications = new_branch_specifications
    # reduce scale
    scale *= scale_reduction

# save tree
plt.savefig('tree.png')
