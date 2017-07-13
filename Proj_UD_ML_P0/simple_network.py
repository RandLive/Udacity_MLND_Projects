# -*- coding: utf-8 -*-
"""
Created on Fri May 12 22:36:00 2017

@author: dream_rab04is
"""

import numpy as np
 
 
class Perceptron:
    """
    This class models an artificial neuron with step activation function.
    """
 
    def __init__(self, weights = np.array([1]), threshold = 0):
        """
        Initialize weights and threshold based on input arguments.
        Note that no type-checking is being performed here for simplicity.
        """
        self.weights = weights
        self.threshold = threshold
 
 
    def activate(self, values):
        """
        Takes in @param values,
       a list of numbers equal to length of weights.
        @return the output of a threshold perceptron
        with given inputs based on
        perceptron weights and threshold.
        """
        # First calculate the strength
        # with which the perceptron fires
        strength = np.dot(values,self.weights)
        # Then return 0 or 1 depending
        # on strength compared to threshold
        return int(strength > self.threshold)
 
 
# Part 1: Set up the perceptron network
Network = [
    # input layer, declare input layer perceptrons here
    [1, 1], \
    # output node, declare output layer perceptron here
    [1, 1, -2]
]
 
# Part 2: Define a procedure to compute the output of the network
# given inputs
def EvalNetwork(inputValues, Network):
    """
    Takes in @param inputValues, a list of input values,
    and @param Network
    that specifies a perceptron network.
    @return the output of the Network for
    the given set of inputs.
    """
    _and_val = Perceptron(Network[0], 1).activate(inputValues)
    inputValues = np.append(inputValues, _and_val)
    # Be sure your output value is a single number
    OutputValue = Perceptron(Network[1]).activate(inputValues)
    return OutputValue
 
 
def test():
    """
    A few tests to make sure that
    the perceptron class performs as expected.
    """
    print "0 XOR 0 = 0?:", EvalNetwork(np.array([0,0]), Network)
    print "0 XOR 1 = 1?:", EvalNetwork(np.array([0,1]), Network)
    print "1 XOR 0 = 1?:", EvalNetwork(np.array([1,0]), Network)
    print "1 XOR 1 = 0?:", EvalNetwork(np.array([1,1]), Network)
 
if __name__ == "__main__":
    test()