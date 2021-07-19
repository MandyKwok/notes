# Tree Algorithms

* <mark>**ID3, C4.5, C5.0, CART**</mark>
  * [Tree algorithms: ID3, C4.5, C5.0, CART](https://medium.datadriveninvestor.com/tree-algorithms-id3-c4-5-c5-0-and-cart-413387342164)
  * **ID3 (Iterative Dichotomiser 3)**, categorical feature, largest information gain
  * **C4.5**, successor to ID3, categorical/numerical features
    * <u>removed the restriction that features must be categorical</u> by dynamically defining a discrete attribute (based on numerical variables) that partitions the continuous attribute value into a discrete set of intervals.
  * **Classification and Regression Trees (CART)**, similar to C4.5, categorical/numerical target variables, does not compute rule sets
    * CART constructs binary trees using the feature and threshold that yields the largest information gain at each node.
    * [Generating a Rule Set from a Decision Tree](https://www.ibm.com/docs/en/spss-modeler/18.1.0?topic=builder-generating-rule-set-from-decision-tree)





#### Information Theory

* **Information Entropy**, <mark>*a measure of uncertainty/information*</mark>

  * In the context of training Decision Trees, Entropy can be roughly thought of as <mark>*how much variance the data has*</mark>.

  * Non-negative

  * <img style="float: left;" src="https://miro.medium.com/max/1122/0*DkWdyGidNSfdT1Nu.png" width="200"/> 

    

    * Basic property 1: *Uniform distributions* have maximum uncertainty.

      * Entropy, Bernoulli trials: 

      <img title="Entropy, Bernoulli trials" style="float: left;" src="https://miro.medium.com/max/600/0*8JwLMUrBgGWM7rWr.png" width="200"/>

      * Uniform distributions with more outcomes have more uncertainty.

    * Basic property 2: Uncertainty is *additive* for independent events.

      <img title="Undertainty is additive for independent events." style="float: left;" src="https://miro.medium.com/max/1252/0*9VDWro34ADgoajyb.png" width="200"/>

    * Basic property 3: Adding an outcome with zero probability has no effect.

      <img title="Adding a zero-probability outcome has no effect on entropy." style="float: left;" src="https://miro.medium.com/max/1400/0*SVvx3qTzKCBrAvfK.png" width="250"/>

    * Basic property 4: The measure of uncertainty is *continuous* in all its arguments.

* **Information Gain**, a metric used to train Decision Trees, measures *the quality of a split*

  * Gini Impurity

* Reference
  * [A Simple Explanation of Information Gain and Entropy](https://victorzhou.com/blog/information-gain/)
  * [Entropy is a measure of uncertainty](https://towardsdatascience.com/entropy-is-a-measure-of-uncertainty-e2c000301c2c)
  * [A Simple Explanation of Gini Impurity](https://victorzhou.com/blog/gini-impurity/)
  * [A Gentle Introduction to Cross-Entropy for Machine Learning](https://machinelearningmastery.com/cross-entropy-for-machine-learning/)



