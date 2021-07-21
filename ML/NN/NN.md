# Neural Networks

#### Concepts

* __Activation function__
  * <mark>An activation function in a neural network defines how the weighted sum of the input is transformed into an output from a node or nodes in a layer of the network.</mark>
  * Relating to NN: All hidden layers typically use the same activation function. The output layer will typically use a different activation function from the hidden layers and is dependent upon the type of prediction required by the model.
  * Activation functions are also typically *differentiable*, meaning the first-order derivative can be calculated for a given input value. 
    * This is required given that neural networks are typically trained using the __backpropagation__ of error algorithm that requires the derivative of prediction error in order to update the weights of the model.
  * Activation for Hidden Layers
    * Rectified Linear Activation (__ReLU__), $max(0, x)$, [link](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/)
      * Pro: less susceptible to *vanishing gradients* that prevent deep models from being trained
      * Con: saturated or "dead" units
    * Logistic (__Sigmoid__), $1 / (1 + e^{-x})$
    * Hyperbolic Tangent (__Tanh__), $(e^{x} – e^{-x}) / (e^{x} + e^{-x})$
  * How to choose a hidden layer activation function?
    * A NN will almost always have the same activation function in all hidden layers.
    * Sigmoid/Tanh: vanishing gradients problem.
    * **Multilayer Perceptron (MLP)**: ReLU activation function.
    * **Convolutional Neural Network (CNN)**: ReLU activation function.
    * **Recurrent Neural Network**: Tanh and/or Sigmoid activation function.
  * Activation for Output Layers
    * **Linear**, identity
    * Logistic (**Sigmoid**), $1 / (1 + e^{-x})$
    * **Softmax**, $e^{x} / sum(e^{x})$
  * How to choose a output layer activation function?
    * **Regression**: One node, linear activation.
    * **Binary Classification**: One node, sigmoid activation.
    * **Multiclass Classification**: One node per class, softmax activation.
    * **Multilabel Classification**: One node per class, sigmoid activation.

* __Vanishing Gradients__: describes the situation where a deep multilayer feed-forward network or a recurrent neural network is <mark>unable to propagate useful gradient information from the output end of the model back to the layers near the input end of the model.</mark>
  * The problem: As more layers using certain activation functions are added to neural networks, the gradients of the loss function approaches zero, making the network hard to train.
  * Why: Certain activation functions, like the sigmoid function, squishes a large input space into a small input space between 0 and 1. Therefore, a large change in the input of the sigmoid function will cause a small change in the output. Hence, the derivative becomes small.
    * <img style="float: left;" src="https://miro.medium.com/max/2000/1*6A3A_rt4YmumHusvTvVTxw.png" width="500"/>
    * When *n* hidden layers use an activation like the sigmoid function, *n* small derivatives are multiplied together. Thus, the gradient decreases exponentially as we propagate down to the initial layers.
    * A small gradient means that the <u>weights and biases</u> of the initial layers will not be updated effectively with each training session. Since these initial layers are often crucial to recognizing the core elements of the input data, it can lead to overall inaccuracy of the whole network.
  * Solutions:
    * Use other activation functions, such as ReLU, which doesn't cause a small derivative.
    * Residual networks: provide residual connections straight to earlier layers. This residual connection doesn’t go through activation functions that “squashes” the derivatives, resulting in a higher overall derivative of the block.
      * <img style="float: left;" src="https://miro.medium.com/max/770/1*mxJ5gBvZnYPVo0ISZE5XkA.png" width="300"/>
    * Batch normalization layers: <u>sigmoid function with restricted inputs</u>
      * The problem arises when a large input space is mapped to a small one, causing the derivatives to disappear. Batch normalization reduces this problem by simply normalizing the input so |x| doesn't reach the outer edges of the sigmoid function.
      * <img style="float: left;" src="https://miro.medium.com/max/1400/1*XCtAytGsbhRQnu-x7Ynr0Q.png" width="500"/>

* __Backward-propagation__

  * Gradients of neural networks are found using backpropagation. 
  * Simply put, <mark>backpropagation finds the derivatives of the network by moving layer by layer from the final layer to the initial one. </mark>
  * By the *chain rule*, the derivatives of each layer are multiplied down the network (from the final layer to the initial) to compute the derivatives of the initial layers.

  

#### Model Structure

* 3 types of layers in a NN:
  * __input layers__: take raw input from the domain
  * **hidden layers**: take input from another layer and pass output to another layer
  * **output layers**: make a prediction




#### Toolkit

* __TensorBoard__ - TensorFlow's visualization toolkit for ML experimentation, [main page](https://www.tensorflow.org/tensorboard)
  * [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/get_started)



__Reference__

* Activation Function
  * [How to choose an Activation Function for DL](https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/)
  * [Activation Functions in NN](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6)
* Vanishing Gradients

  * [How to Fix the Vanishing Gradients Problem Using the ReLU](https://machinelearningmastery.com/how-to-fix-vanishing-gradients-using-the-rectified-linear-activation-function/)
  * [The Vanishing Gradient Problem](https://towardsdatascience.com/the-vanishing-gradient-problem-69bf08b15484)
* Batch Normalization
  * [A Gentle Introduction to Batch Normalization for Deep NN](https://machinelearningmastery.com/batch-normalization-for-training-of-deep-neural-networks/)
* Dropout
  * [A Gentle Introduction to Dropout for Regularizing Deep NN](https://machinelearningmastery.com/dropout-for-regularizing-deep-neural-networks/)





## Checklist

- [ ] weight initialisation
- [ ] Multi-layer Perceptron, [link](https://scikit-learn.org/stable/modules/neural_networks_supervised.html)
- [ ] SGD, Momentum, Adam, and other optimizers
- [ ] backward-propagation
- [ ] learning rate
- [ ] Convolutions 
- [ ] RNN
- [ ] batch normalization
- [ ] dropout
- [ ] data augmentation
- [ ] weight decay
- [ ] Image classification and regression
- [ ] Entity and word embeddings
- [ ] NLP specific: LSTM, transformer, ...
- [ ] Segmentation
- [ ] model interpretation
- [ ] transfer learning



## Articles to Read

* [Why Data should be Normalized before Training a NN](https://towardsdatascience.com/why-data-should-be-normalized-before-training-a-neural-network-c626b7f66c7d#:~:text=Among%20the%20best%20practices%20for,and%20leads%20to%20faster%20convergence.)

