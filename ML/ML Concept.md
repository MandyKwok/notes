# ML Concept

* __Type I/II errors __, related to *hypothesis testing*.
  * References
    * [Scribbr: Type I and Type II errors](https://www.scribbr.com/statistics/type-i-and-type-ii-errors/#:~:text=What%20are%20Type%20I%20and,hypothesis%20when%20it's%20actually%20false.)
  * <mark>Type I error = false positive = reject the null hypothesis when it's actually true</mark>
    * The probability of making a Type I error is the significance level, or alpha (α).
    * α is a value you set to assess the statistical probability of obtaining your results (*p*-value).
    * <img style="float: left;" src="https://cdn.scribbr.com/wp-content/uploads/2021/01/type-i-error-rate.png" width="500"/>
  * <mark>Type II error = false negative = not reject the null hypothesis when it's actually false </mark>
    * The probability of making a Type II error is beta (β).
    * A Type II error means failing to conclude there was an effect when there actually was.
    * The risk of a Type II error is inversely related to the __satistical power__ of a study. The higher the statistical power, the lower the probability of making a Type II error.
      * Statistical power is determined by: 1) size of the effect; 2) measurement error; 3) sample size; 4) significance level.
      * To (indirectly) reduce the risk of a Type II error, you can increase the sample size or the significance level.
    * <img style="float: left;" src="https://cdn.scribbr.com/wp-content/uploads/2021/01/type-ii-error-rate.png" width="500"/>
  * Trade-off between Type I and Type II errors
    * The Type I and Type II error rates influence each other. That’s because the significance level (the Type I error rate) affects statistical power, which is inversely related to the Type II error rate.
      * Setting a lower significance level decreases a Type I error risk, but increases a Type II error risk.
      * Increasing the power of a test decreases a Type II error risk, but increases a Type I error risk.
    * <img style="float: left;" src="https://cdn.scribbr.com/wp-content/uploads/2021/01/type-i-and-ii-error-2.png" width="500"/>





## Prob & Stats

__Hypothesis Testing__

* __*p*-value__: describes how likelly you are to have found a particular observation if the null hypothesis were true. [link](https://www.scribbr.com/statistics/p-value/)
  * The smaller the *p*-value, the more likely you are to reject the null hypotheisis.
  * *Degrees of freedom*: number of observations minus number of independent variables.
    *  The number of independent variables you include in your test changes how large or small the test statistic needs to be to generate the same _p_-value.
  * Reporting *p*-values: 
    * for example, correlation coefficient in a linear regression, the average difference between treatment groups in a *t*-test.
    * narrative: statistical significance, p-value
* __Statistical test__
  * two-group comparison: *t*-test
  * multiple pairwise comparisons: ANOVA



- [ ] VC (Vapnik-Chervonenkis) dimension
- [ ] information entropy
- [ ] cross entropy
- [ ] KL (Kullback-Leibler) divergence
- [ ] cross validation
- [ ] boosting
- [ ] bagging
- [ ] L1/L2 regularization
- [ ] [Data Science Interview Questions](http://mlwiki.org/index.php/Data_Science_Interview_Questions)
