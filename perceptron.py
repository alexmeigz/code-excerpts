# Imports
import numpy as np
import numpy.linalg as npla
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

def train_perceptron(X: list, y: list):
    '''
    Train a perceptron model given a set of training data
    :param X: contains the training data points (vectors)
    :param y: contains the training labels (+1/-1)
    :return: learned weight vector
    '''

    model_size = X.shape[1]
    w = np.zeros(model_size) 
    iteration = 1

    while True:
        # compute results according to the hypothesis
        results = np.sign(np.multiply(np.matmul(X, w), y))

        # get incorrect predictions (you can get the indices)
        indices = np.arange(X.shape[0])
        misclassified_indices = indices[results != 1]

        # Check the convergence criteria (if there are no misclassified
        # points, the PLA is converged and we can stop.)
        if len(misclassified_indices) == 0:
            print("Total Iterations: {}".format(iteration))
            break

        # Pick one misclassified example.
        picked_misclassified = random.choice(misclassified_indices)
        x_star, y_star = X[picked_misclassified], y[picked_misclassified]

        # Update the weight vector with perceptron update rule
        w += y_star * x_star

        iteration += 1

    return w

def make_prediction(model: list, data: list):
    '''
    Print the predictions given the dataset and the learned model.
    :param model: model vector
    :param data:  data points
    :return: nothing
    '''
    return np.sign(np.matmul(data, model))

def calc_accuracy(predicted: list, actual: list):
  '''
  Calculate accuracy given predicted and actual labels.
  '''
  n = len(predicted)
  correct = sum([1 if predicted[i] == actual[i] else 0 for i in range(n)])
  return correct / n

def runPLA(X: list, y: list):
  '''
  runs PLA algorithm and reports results
  '''
  trained_model = train_perceptron(np.array(x_vector), np.array(classes))
  print("Model:", trained_model)
  print("Accuracy: {:.2f}".format(100 * calc_accuracy(make_prediction(trained_model, np.array(x_vector)), classes)))

  # Hypothesis function line
  slope = -1 * trained_model[1] / trained_model[2]
  print("Slope: {:.2f}".format(slope))

  intercept = -1 * trained_model[0] / trained_model[2]
  print("Intercept: {:.2f}".format(intercept))

# Test functionality
if __name__ == '__main__':
  # Generate Linearly Separable Data
  def generateCoordinate():
    '''
    returns a random number in (-50, 50)
    '''
    return 100 * random.random() - 50

  def generatePoint(dimensions: int):
    '''
    returns a data vector with <dimensions> with coordinates in (-50, 50)
    '''
    return [generateCoordinate() for i in range(dimensions)]

  def generateLinearData(sampleSize: int, dimensions: int):
    '''
    return a list of [sample, label] elements of length sampleSize where
    sample is of length dimensions
    '''
    newData = list()

    for i in range(sampleSize):
      newPoint = generatePoint(dimensions)

      # Choose target separation function at x = 0 axis
      newData.append((newPoint, 1 if newPoint[0] > 0 else -1))

    return newData

  print("Running PLA for n = {}".format(100))

  dataList = generateLinearData(100, 2)
  x_vector = list()
  classes = list()

  for x, y in dataList:
    x_vector.append([1] + x)
    classes.append(y)

  runPLA(x_vector, classes)