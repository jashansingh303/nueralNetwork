import sys
import numpy as np
import matplotlib
#Part 1
# inputs = [1, 2, 3, 2.5]

# weights1 = [0.2, 0.8, -0.5, 1.0]
# weights2 = [0.5, -0.91, 0.26, -0.5]
# weights3 = [-0.26, -0.27, 0.17, 0.87]

# bias1 = 2
# bias2 = 3
# bias3 = 0.5

# #Each input should be multiplied by each weight and the entire thing gets the bias added to it
# #This is because this is only one neuron. Each neuron gets one bias but since there are 4 inputs there have to be the same amount of weights 
# output = [inputs[0]*weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
#           inputs[0]*weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
#           inputs[0]*weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]
# print(output)

#Part 2
# inputs = [1,2,3,2.5]

# weights = [[0.2, 0.8, -0.5, 1.0],[0.5, -0.91, 0.26, -0.5],[-0.26, -0.27, 0.17, 0.87]]

# biases = [2,3,0.5]

# layer_outputs = [] #output of current layer
# for neuron_weights, neuron_bias in zip(weights, biases):
#     neuron_output = 0 #output of given neuron
#     for n_input, weight in zip(inputs, neuron_weights):
#         neuron_output += n_input*weight
#     neuron_output += neuron_bias
#     layer_outputs.append(neuron_output)
    
# print(layer_outputs)

#Part 3
# inputs = [1,2,3,2.5]

# weights = [[0.2, 0.8, -0.5, 1.0],[0.5, -0.91, 0.26, -0.5],[-0.26, -0.27, 0.17, 0.87]]

# biases = [2,3,0.5]

# #Weights need to go first because we need it indexed by the weights. Putting inputs first also causes a shape error
# output = np.dot(weights, inputs) + biases
# print(output)

#Part 4
