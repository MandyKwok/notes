# Learning Rate

*Learning rate for gradient descent: scales the magnitude of the weight updates in order to minimize the network's loss function, the most important hyper-parameter to tune for training deep NN.*

<img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-24-at-11.47.09-AM.png" width="800"/>

* The ***loss landscape*** of a neural network is a function of the network's parameter values quantifying the "error" associated with using a specific configuration of parameter values when performing inference (prediction) on a given dataset. ([Paper: Visualizing the Loss Landscape of Neural Nets](https://arxiv.org/pdf/1712.09913.pdf))
  * <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-26-at-10.50.53-PM.png" width="600"/>
  * <u>The optimal learning rate will be dependent on the topology of your loss landscape</u>, which is in turn dependent on both your model architecture and your dataset. 

#### A systematic approach towards finding the optimal learning rate

<img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/lr_finder.png" width="600"/>

* The best learning rate is associated with the *steepest* drop in loss, so we're mainly interested in analyzing the slope of the plot.

  * You should set the range of your learning rate bounds for this experiment such that you observe **all three** phases, making the optimal range trivial to identify.

  * **Cyclical Learning Rates**, lets the learning rate cyclically vary between reasonable boundary values ([Paper: Cyclical Learning Rates for Training Neural Networks](https://arxiv.org/pdf/1506.01186.pdf))

    * Assumption: Increasing the learning rate might have a short term negative effect and yet achieve a longer term beneficial effect. 
      * By allowing for the learning rate to increase at times, we can "jump out" of sharp minima which would temporarily increase the loss but may ultimately lead to converagence on a more diserable minima.
        * Sharp minima: a saddle point where the minimum dimensions are very steep while the maximum dimensions are very wide.
        * <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/sharp_minima.png" width="300"/>
      * Increasing the learning rate can also allow for "more rapid traversal of saddle point plateaus. (the gradients can be very small at a saddle point)
        * **Saddle point**: a critical point in which some dimensions observe a local minimum while other dimensions observe a local maximum.
        * <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/Saddle_point.svg.png" width="300"/>
      * Indeed, his paper includes several examples of a loss function evolution which temporarily deviates to higher losses while ultimately converging to a lower loss when compared with a benchmark fixed learning rate.
      * On generalization, robustness, ...
    * <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-25-at-8.44.49-PM.png" width="500"/>

    

#### Setting a schedule to adjust your learning rate during training

* **Learning rate annealing**, starting with a relatively high learning rate and then gradually lowering the learning rate during training, <mark>*define a **learning rate schedule***</mark>
  * **step decay**, most popular
  * <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/stepdecay.png" width="400"/>
* Too high of a learning rate can cause the parameter update to "jump over" the ideal minima and subsequent updates will either result in a continued noisy convergence in teh general region of the minima, or in more extreme cases may result in divergence from the minima.



#### Stochastic Gradient Descent with Warm Restarts (SGDR)

* Similar to cyclic approach, an aggressive annealing schedule is combined with periodic "restarts" to the original starting learning rate.
* By drastically increasing the learning rate at each restart, we can essentially exit a local minima and continue exploring the loss landscape.
* <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/cosine_annealing.png" width="400"/>
* *Neat idea: By snapshotting the weights at the end of each cycle, researchers were able to <u>build an ensemble of models at the cost of training a single model</u>. This is because the network "settles" on various local optima from cycle to cycle.*  ([Paper: Snapshot Ensembles: Train 1, Get M for Free](https://arxiv.org/pdf/1704.00109.pdf), [Repo: Snapshot Ensembles in Keras](https://github.com/titu1994/Snapshot-Ensembles))
* <img style="float: left;" src="https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-26-at-9.12.57-PM.png" width="400"/>



__Reference__

[Setting the learning rate of your neural network](https://www.jeremyjordan.me/nn-learning-rate/)
