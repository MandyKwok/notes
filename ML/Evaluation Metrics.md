# Evaluation Metrics

* <mark>**First-order Suggestions**</mark>, *classification*
  * Predicting probabilities:
    - Need class labels:
      - Positive class more important: Use Precision-Recall AUC
      - Both classes important: Use ROC AUC
    - Need probabilities: Use Brier Score and Brier Skill Score
  * Predicting class labels:
    * Positive class more important:
      * False negatives and false positives equally important: Use F1-Measure
      * False negatives more important: Use F2-Measure
      * False positives more important: Use F0.5-Measure
    * Both classes important:
      * < 80% - 90% examples for the majority class: Use Accuracy
      * \> 80% - 90% examples for the majority class: Use G-Mean



---



* __Classification Accuracy__, the ratio of number of correct predictions to the total numbeer of input samples
  * <img style="float: left;" src="https://miro.medium.com/max/746/1*yRa2inzTnyASJOre93ep3g.gif" width="300"/>
  * It works well only if there are <u>equal number of samples belonging to each class</u>.
  * Given imbalance dataset: gives us the false sense of achieving high accuracy.
    * The real problem arises, when the <u>cost of misclassification</u> of the minor class samples are very high. If we deal with a rare but fatal disease, the cost of failing to diagnose the disease of a sick person is much higher than the cost of sending a healthy person to more tests.

* __Logarithmic/Log Loss__, penalizing the false classifications

  * <img style="float: left;" src="https://miro.medium.com/max/688/1*dtpzlB_dNrmxDq7fGnJ4cg.gif" width="300"/><br/>(N samples, M classes) <br/>

    * $y_{ij}$, indicates whether sample i belongs to class j or not

      $p_{ij}$, indicates the probability of sample i belonging to class j

  * It works well for <u>multi-class classification</u>. When working with Log Loss, the classifier must assign probability to each class for all the samples.

  * Log Loss has no upper bound and it exists on the range [0, ∞). 

    * Log Loss nearer to 0 indicates higher accuracy, whereas if the Log Loss is away from 0 then it indicates lower accuracy.

  * In general, minimising Log Loss gives greater accuracy for the classifier.

* __Confusion Matrix__, a matrix that describes the complete performance of the model
  * <img style="float: left;" src="https://miro.medium.com/max/746/1*xvJylefImAAukT7dx7lZ3g.png" width="300"/>
  * <img style="float: left;" src="https://2.bp.blogspot.com/-EvSXDotTOwc/XMfeOGZ-CVI/AAAAAAAAEiE/oePFfvhfOQM11dgRn9FkPxlegCXbgOF4QCLcBGAs/s1600/confusionMatrxiUpdated.jpg" width="500"/>
    * True Positive Rate = Sensitivity
    * True Negative Rate = Specificity

* __Area Under Curve (*AUC*)__, *AUC* of a classifier is equal to the probability that the classifier will rank a randomly chosen positive example higher than a randomly chosen negative example.
  * It is used for binary classification problem.
  * <mark>*AUC* is the area under the curve of plot *False Positive Rate vs. True Positive Rate* at different points in $[0, 1]$.</mark>
    * *AUC* has a range of [0, 1]. 
    * The greater the value, the better is the performance of our model.
    * <img style="float: left;" src="https://miro.medium.com/max/1280/1*zFW1Kj3e2X_mmluTW3rVeA.png" width="500"/>

* __F1 Score__, used to measure a test's accuracy

  * F1 Score is the *Harmonic Mean* between precision and recall.
    * The range for F1 Score is [0, 1]. 
    * <mark>It tells you how **precise** your classifier is (how many instances it classifies correctly), as well as how **robust** it is (it does not miss a significant number of instances).</mark>
    * <img style="float: left;" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/05/Screenshot-2019-05-14-at-12.12.47-PM.png" width="400"/>
      * Why harmonic mean, not arithmetic mean? **HM punishes extreme values more**.
    * High precision but lower recall, gives you an extremely accurate, but it then misses a large number of instances that are difficult to classify. 
    * The greater the F1 Score, the better is the performance of our model. 

  * F1 Score tries to find the balance between precision and recall.
  * Interpreting F1 Score: The importance of the F1 score is different based on the scenario. Lets assume the target variable is a binary label.
    - **Balanced class**: In this situation, the F1 score can effectively be ignored, the mis-classification rate is key.
    - **Unbalanced class, but both classes are important**: If the class distribution is highly skewed (such as 80:20 or 90:10), then a classifier can get a low mis-classification rate simply by choosing the majority class. In such a situation, I would choose the classifier that gets high F1 scores on both classes, as well as low mis-classification rate. A classifier that gets low F1-scores should be overlooked.
    - **Unbalanced class, but one class if more important that the other**. For e.g. in Fraud detection, it is more important to correctly label an instance as fraudulent, as opposed to labeling the non-fraudulent one. In this case, I would <mark>pick the classifier that has a good F1 score *only on the important class*</mark>. Recall that the F1-score is available per class.

* **Fbeta Score**, a generalisation of F Score that adds a *configuration parameter* called beta.

  * <img style="float: left;" src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/05/Screenshot-2019-05-14-at-12.34.35-PM.png" width="300"/>
  * Attach β times as much importance to recall as precision.
    * A smaller beta value, such as 0.5, gives more weight to precision and less to recall.
    * A larger beta value, such as 2.0, gives less weight to precision and more weight to recall in the calculation of the score.
    * β = 0, equivalent to F Score

* __Mean Absolute Error (*MAE*)__, the average of the difference between the Original Values and the Predicted Values

  * It gives us the measure of how far the predictions were from the actual output. However, they don’t gives us any idea of the direction of the error i.e. whether we are under predicting the data or over predicting the data.
  * <img style="float: left;" src="https://miro.medium.com/max/606/1*qak4Dadzs7pO0hnz4q8O8Q.gif" width="300"/>

* __Mean Squared Error (***MSE***)__, similar to MAE, takes the average of the *square* of the difference between the original values and the predicted values
  * The advantage of MSE being that it is easier to compute the gradient, whereas MAE requires complicated linear programming tools to compute the gradient. As, we take square of the error, the effect of larger errors become more pronounced then smaller error, hence the model can now focus more on the larger errors.
  * <img style="float: left;" src="https://miro.medium.com/max/624/1*okvAVQNY6s5cMHxrqUzM5A.gif" width="300"/>

* __Cumulative Gains, Lift Curves__, mainly concerned to check the rank ordering of the probabilities

  * <img style="float: left;" src="https://miro.medium.com/max/1400/1*roOl8bjXIk4b1l3OLRG4LQ.png" width="600"/>

  * *<u>Business Goal: Why ROC and AUC are not enough? more intuitive and actionable</u>*

    * Predictive goal: examine a new set of records to detect which ones are most likely to belong to a particular class you’re interested in :arrow_right: assess how effectively a classification model can ***rank*** new records.
    * <mark>There are a lot of business problems that boil down to just figuring out how well a model helps us to select a relatively small number of records that hold a relatively large proportion of what’s important in the context of the problem. </mark>
      * From how accurately the next new observation under consideration is classified, to how well the model can create a hierarchy of ranked observations.
    * A good baseline for comparison: random assignment. 
      * Cumulative actual class: on average, increase by the the total count of the interesting class divided by the total number of observations in each row.
      * The plot of this baseline cumulative total will be a diagonal line that goes from point $(0,0)$ to point $(total\hspace{2mm}observations,{\#}\hspace{2mm}of\hspace{2mm}class\hspace{2mm}of\hspace{2mm}interest)$. 
    * Meaningful statements that give intuitive insight into why and how this model is useful are now available to share with business stakeholders.
    * <img style="float: left;" src="https://raw.githubusercontent.com/alexeygrigorev/wiki-figures/master/ufrt/kddm/lift-chart-ex.png" width="400"/>

    

  * The lift chart provides an easy way to visualize how many times better applying the model is than random selection for any percentage of the ranked records.



## Related

* __Types of Predictive Models__
  * regression model (continuous output)
  * classificaiton model (nominal or binary output)
    * class output: SVM, KNN, ...
      * *Today we have algorithms which can convert these class outputs to probability. But these algorithms are not well accepted by the statistics community.*
    * probability output: Logistic Regression, Random Forest, Gradient Boosting, Adaboost, ...
      * *Converting probability outputs to class output is just a matter of creating a threshold probability.*

* **Texonomy of Classifier Evaluation Metrics**
  * **Threshold Metrics**, *assume that the class distribution in the training set and the test set match*
    *  $Accuracy = \frac{Correct\ Predictions}{Total\ Predictions}$
    *  $Erorr = \frac{Incorrect\ Predictions}{Total\ Predictions}$
    *  $Sensitivity = \frac{True\ Positive}{True\ Positive \ + \ False\ Negative}$
    * $Specificity = \frac{True\ Negative}{True\ Negative \ + \ False\ Positive}$
    * $G-Mean\ (geometric \ mean) = \sqrt{Sensitivity * Specificity}$
    *  $Precision = \frac{True\ Positive}{True\ Positive \ + \ False\ Positive}$
    * $Recall = \frac{True\ Positive}{True\ Positive \ + \ False\ Negative}$
    * $F-Measure = \frac{2 \ * \ Precision \ * \ Recall}{Precision \ + \ Recall}$
    * $Fbeta-Measure = \frac{(1 \ + \ beta^2) \ * \ Precision \ * \ Recall}{beta^2 \ * \ Precision\ + \ Recall}$
    * Kappa, Macro-Average Accuracy, Mean-Class-Weighted Accuracy, Optimized Precision, Adjusted Geometric Mean, Balanced Accuracy, and more ...
  * **Ranking Metrics**, *don't make assumptions about class distributions*
    * Evaluate classifiers based on how effective they are at *separating classes*
    * Require that a classifier predicts a score or a probability of class membership
    * ROC (Receiver Operating Characterstic) Curve, analyzing binary classifiers based on their ability to *discriminate* classes, ROC AUC (Area Under Curve)
      * Optimistic metric under a severe class imbalance, especially when the number of examples in the minority class is small
      * $TruePositiveRate = \frac{TruePositive}{TruePositive + FalseNegative}$
      * $FalsePositiveRate = \frac{FalsePositive}{FalsePositive + TrueNegative}$
      * <img style="float: left;" src="https://machinelearningmastery.com/wp-content/uploads/2019/10/Depiction-of-a-ROC-Curve.jpg" width="400"/>
      * Alternative: precision-recall curve, focuses on the performance of the classifier on the minority class, PR AUC = Precision-Recall Area Under Curve
  * **Probability Metrics**, *quantify the uncertainty in a classifier's predictions*
    * These are useful for problems where we are less interested in incorrect vs. correct class predictions and more interested in the uncertainty the model has in predictions and penalizing those predictions that are wrong but highly confident.
    * Classifiers trained using a probabilistic framework, such as *maximum likelihood estimation*, meaning that their probabilities are already calibrated, e.g. logistic regression
    * Classifieres not trained using a probabilistic framework, require their probabilities to be calibrated against a dataset prior to being evaluated via a probabilistic metric, e.g. SVM, KNN
    * $log loss = -((1 – y) * log(1 – \hat{y}) + y * log(\hat{y}))$
      * log loss for binary classification (negative log likelihood), or cross-entropy
    * $Brier Score=1/N * sum_{i=1}^{N} (\hat{y}_{i} - y_{i})^2$, mean squared error between the expected probabilities for the positive class and the predicted probabilities
      * The differences in Brier score for different classifiers can be very small. In order to address this problem, the score can be scaled against a reference score, such as the score from a no skill classifier
      * $Brier Skill Score (BSS) = 1 - (Brier Score / Brier Score_{ref})$
        * no skill = 0; worse than no skill < 0; perfect skill = 1
* **Challenge of Evaluation Metrics**, **Imbalance Classification**
  * All metrics make assumptions about the problem or about what is important in the problem. Therefore <mark>an evaluation metric must be chosen that best captures what you or your project stakeholders believe is important about the model or predictions.</mark>
  * Imbalanced classification problems typically rate classification errors with the minority class as more important than those with the majority class.
* Selecting a model, and even the data preparation methods together are a search problem that is guided by the evaluation metric.



__Reference__

[Metrics to Evaluate your Machine Learning Algorithm](https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234)

[11 Important Model Evaluation Metrics for Machine Learning Everyone should know](https://www.analyticsvidhya.com/blog/2019/08/11-important-model-evaluation-error-metrics/)

[How to interpret F-measure values?](https://stats.stackexchange.com/questions/49226/how-to-interpret-f-measure-values)

[How to Evaluate Classification Model Performance with Cumulative Gains, Lift Curves and Python](https://towardsdatascience.com/evaluate-model-performance-with-cumulative-gains-and-lift-curves-1f3f8f79da01)

[ML Wiki - Cumulative Gain Chart](http://mlwiki.org/index.php/Cumulative_Gain_Chart)

[Tour of Evaluation Metrics for Imbalanced Classification](https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/)

