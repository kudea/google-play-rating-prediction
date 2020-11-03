# Google play rating prediction
## Dataset
From Kaggle [googleplaystore.csv](https://www.kaggle.com/lava18/google-play-store-apps?fbclid=IwAR1ewDYe45_X6PghbcjYJgfO8guxUI9-EdRzpqR_Gt1c1decR_9RH6CklaQ "link")
## algorithm SVM vs SVR
Support vector machines (SVM) is a supervised machine learning classification algorithm, 
which can be used for classification problem in multi-dimension space.
It is widely used in mining researches, such as text mining and opinion mining, and it has a great result. 
Comparing to other classification algorithms, SVM algorithm usually has better result in higher dimension, 
where all number of features is quite large and the data is sparse.
SVM uses g(x)=w^T x+b  as the linear separation hyperplane, 
where w is the weight vector, b is the bias, x is a set of high dimensional non-linear transformation function, 
w and b is determined by training data that optimize the following formulas:

![image](https://github.com/kudea/google-play-rating-prediction/blob/master/pic/SVM.png)
 
whereε_iis the slack variables, C is the penalty coefficient, for all the training samples (x_i,y_i).

Support Vector Regression (SVR) is using the SVM algorithm on regression problem. 
The goal of SVM is to find the separation hyperplane; and the goal of SVR is to find the regression hyperplane. 

For the given training set:	 {(x_1,z_1), …, (x_i,z_i)}

where x_i∈Rn is a feature vector, and z_i∊ R1 is the target output. 
In order to find the hyperplane, two parameters C>0 and ε>0 must be given and the support vector regression can be defined:
 
 ![image](https://github.com/kudea/google-play-rating-prediction/blob/master/pic/SVR.png)
 
In our experiment, we use a free SVM toolkit, sklearn, C = 1to train the SVR model.
# Method
![image](https://github.com/kudea/google-play-rating-prediction/blob/master/pic/flow.PNG)
# Result
![image](https://github.com/kudea/google-play-rating-prediction/blob/master/pic/result.png)

# Conclusion
The comparison of the three proposed methods are shown in Table I. 
Among the three mothods, KNN with K = 15 has the best accuracy against the other two, 
and Decision Tree method had the worst performance. 
Hence, to do such rating prediction on Google Play apps, 
SVR and KNN algorithm is more acceptable. With the trained model, 
we can predict the rating when a app is given with the corresponding features, 
so that improve the user experience when surfing the Apps market 
and provide a early evaluation for developing the potential products.
