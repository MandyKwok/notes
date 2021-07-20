# Dimensionality Reduction

<img style="float: left;" src="https://miro.medium.com/max/2000/1*WhKA9Jboj_1sHa0MbWQQ7w.png" width="700"/>



* **The Curse of Dimensionality**, all the problems that arise when working with data in the higher dimensions, that did not exist in the lower dimensions
  * <img style="float: left;" src="https://miro.medium.com/max/1020/1*vah8IolNqlxNHq9ysVzYkw.png" width="500"/>
  * \# features &#8593; :arrow_right: model complexity &#8593; :arrow_right: chances of ***overfitting*** &#8593;
  * Advantages of dimentionality reduction:
    * The fewer features our training data has, the lesser assumptions our model makes and the simpler it will be.
    * Less misleading data means model accuracy improves.
    * Less dimensions mean less computing. Less data means that algorithms train faster.
    * Less data means less storage space required.
    * Less dimensions allow usage of algorithms unfit for a large number of dimensions.
    * Removes redundant features and noise.



#### Feature Selection

* <mark>The process of identifying and selecting relevant features for your sample.</mark>

* Manually,

  * When: 1) the relevance/irrelevance of certain features are obvious; 2) common knowledge; 3) domain knowledge
  * Tools: 1) heatmap of correlation; 2) visualization of relationship between the features and the target variable

* Programmically, *scikit-learn*

  * **Variance Threshold**, *baseline approach*, drops all features where the variance along the column does not exceed a threshold value
    * Premise: a feature which doesn't vary much within itself, has very little predictive power.
    * O​nl​y ​se​e​s​ ​th​e ​inp​ut​ f​eat​ure​s ​(x) without considering any information from the dependent variable (y) :arrow_right: **Unsupervised learning**
  * **Univariate selection**, uses univariate statistical tests to select features
    * **Supervised learning**
    * e.g. Person Correlation, Maximal information coefficient, Distance correlation, ANOVA, Chi-square
      * Chi-square: between categorical variables
      * ANOVA: between categorical and numerical variables
      * F-test: captures only linear dependency
      * Mutual information: captures any kind of dependency

  * **Recursive Feature Elimination (RFE)**, based on `coef_` or `feature_importances_` attributes of a ML model, backward selection
  * **SelectFromModel (Scikit-Learn)**, based on `coef_` or `feature_importances_` attributes of a ML model, *by threshold* (default: mean)
  * **Sequential Feature Selection (SFS)**, *greedy*, *maximize cross-validation score*
    * SFS-Forward, SFS-Backward



#### Feature Engineering

* <mark>Manually generating new features from exisiting features, by applying some transformation or performing some operation on them.</mark>

* ***Linear*** Dimensionality Reduction Methods
  * **Factor Analysis**
    * The values of observed data are expressed as functions of a number of possible causes in order to find which are the most important.
    * Assumptions
      * observations = a *linear transformation of lower dimentional latent factors* + *Gaussian noise*
      * no multicollinearity
      * relevant variables included into analysis
      * true correlation between variables and factors
    * Most commonly used, **PCA (Principal Component Analysis)**, rotates and projects data along the direction of increasing variance
      * principal components: the features with the maximum variance
  * **LDA (Linear Discriminant Analysis)**: projects data in a way that the *class separability* is maximised.
    * <img style="float: left;" src="https://miro.medium.com/max/1400/1*4ibdHcy6xlV7-HU3KjonsQ.png" width="500"/>
    * ***PCA vs. LDA***: <mark>PCA orients data along the direction of the component with maximum variance whereas LDA projects the data to signify the class separability.</mark>>

* ***Non-linear*** Dimensionality Reduction Methods
  * Used when the data doesn't lie on a linear subspace
  * Based on the *manifold hypothesis*: in a high dimensional structure, most relevant information is concertrated in small number of low dimensional manifolds.
  * **Multi-dimensional scaling (MDS)**, projects data to a lower dimension such that data points that are close to each other (in terms if Euclidean distance) in the higher dimension are close in the lower dimension as well.
    * Used for analyzing *similarity* or *dissimilarity* of data as distances in a geometric spaces 
  * **Isometric Feature Mapping (Isomap)**, projects data to a lower dimension while preserving the geodesic distance (rather than Euclidean distance as in MDS)
  * **Locally Linear Embedding (LLE)**, recovers global non-linear structure from linear fits
  * **Hessian Eigenmapping (HLLE)**, projects data to a lower dimension while preserving the local neighbourhood like LLE but uses the Hessian operator to better achieve this result and hence the name
  * **Spectral Embedding (Laplacian Eigenmaps)**, uses spectral techniques to perform dimensionality reduction by mapping nearby inputs to nearby outputs
    * Preserves locality rather than local linearity
  * **t-distributed Stochastic Neighbor Embedding (t-SNE)**, computes the probability that pairs of data points in the high-dimensional space are related and then chooses a low-dimensional embedding which produce a similar distribution

* **Auto-encoders**, a type of artificial NN that aims to copy their inputs to their outputs
  * <mark><u>**Encoder** compresses the input into a *latent-space representation*, and then **decoder** reconstructs the output from this representation</u></mark> 
  * <img style="float: left;" src="https://miro.medium.com/max/1400/1*I5MVGIrROrAnD3U_2Jm1Ng.png" width="700"/>



__Reference__

[A beginner's guide to dimensionality reduction in ML](https://towardsdatascience.com/dimensionality-reduction-for-machine-learning-80a46c2ebb7e)

[11 Dimensionality reduction techniques you should know in 2021](https://towardsdatascience.com/11-dimensionality-reduction-techniques-you-should-know-in-2021-dcb9500d388b)

[5 Feature Selection Method from Scikit-Learn you should know](https://towardsdatascience.com/5-feature-selection-method-from-scikit-learn-you-should-know-ed4d116e4172)

[Statistics Solutions - Factor Analysis](https://www.statisticssolutions.com/free-resources/directory-of-statistical-analyses/factor-analysis/)
