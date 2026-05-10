# Kaggle earthquake challenge
The code was a part of a kaggle challenge, which had a dataset having around 20 features for earthquake magnitude. The goal was to perform data processing and produce a model which can perform good predictions. The training data is provided with target, on which one can train the model, and a Test file is also provided on which we had to perform our final predictions.


In this challenge I employed the use of five different models stacked together: Random Forest, XGBoost, LightGB, SVR and Deep Neural Network. 
With this combination I was able to reach error score of **0.530**

I tried various permutation 


<img src="https://github.com/computervisionpro/kaggle-earthquake-challenge/blob/main/md-img.png" alt="Gemma4" width="900" height="450">


The following are each model's contribution:
- rf: 0.2769
- xgb: 0.0561
- dnn: 0.2756
- lightgb: 0.0726
- svr: 0.0415
