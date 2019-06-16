# A ToDo Checklist

## Initial Setup

A setup script based on environment Linux vs Mac
Like have a Requirement.txt file
Install

* Python
* Pytorch

GPU vs Non GPU

## Preprocessing

lower-casing, standardizing new lines, removing junk

For document classification:

* Number of sentences per document
* Number of words: Truncate long sentences to these many words

## Embeddings

* Glove
* Word2vec
* FastText
* Elmo/Bert

## Training time

* Visualize Loss - TensorBoard, Visualize saved model
* GPU vs Non GPU
* Different Loss functions
  * BCE Loss
* Different Optimizers
  * Adam
  * AdaBound
  * AdaGrad

## Productionizing

* Batching at Predict time
* PyLint Score
* Iterative loading of train file
* Well Commented Code
* Set Random Seed
* Quantization or 16 bit precision at train time
* Everything in try catch block
* Unit Tests
* Dockerized version

## Approaches

### Deep Learning Based

* CNN
* RNN
* LSTM
* RCNN
* Attention
* Hierarchical Attention nw for Doc Classification

### Statistical Based

* BagofWords
* SVM
* NaiveBayes
* Decision Trees
* Random Forest
