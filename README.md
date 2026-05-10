# Kaggle earthquake challenge
The code was a part of a kaggle challenge, which had a dataset having around 20 features for earthquake magnitude. The goal was to perform data processing and produce a model which can perform good predictions. The training data is provided with target, on which one can train the model, and a Test file is also provided on which we had to perform our final predictions.


In this challenge I employed the use of five different models stacked together: Random Forest, XGBoost, LightGB, SVR and Deep Neural Network. 
With this combination I was able to reach final error score of **0.530** on full Test dataset.

I tried various permutations and combinations elimainating each model one by one, or by removing one model and trying with the rest (ablation test). My findings were that the combination of all models give the best score. Random Forest and DNN models were most inflential


<img src="https://github.com/computervisionpro/kaggle-earthquake-challenge/blob/main/md-img.png" alt="Gemma4" width="900" height="450">


The following are Ridge meta model's coefficient of each model:
- rf: 0.2593
- xgb: 0.0583
- dnn: 0.3082
- lightgb: 0.0662
- svr: 0.0384


Benefits of Ridge meta-model are:

✅ handles correlated base models well
✅ reduces overfitting
✅ fast & stable
