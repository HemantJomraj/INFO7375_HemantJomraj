class McPN:
    def __init__(self, weights, threshold):
        self.weights = weights
        self.threshold = threshold

    def activation(self, inputs):
        # constraint
        if len(inputs) != len(self.weights):
            raise ValueError("Number of inputs should be equal to the number of weights")

        # wighted sum of ip
        weighted_sum = sum(w * x for w, x in zip(self.weights, inputs))

        # activation function
        output = 1 if weighted_sum >= self.threshold else 0
        return output

# Weights and threshold for the neuron
neuron_weights = [1, 1]
neuron_threshold = 1

# Instance of the McPN
mcPNeuron = McPN(neuron_weights, neuron_threshold)

# Input values for the neuron
input_values = [1, 0]

# Output of the neuron
output = mcPNeuron.activation(input_values)

print("Output:", output)