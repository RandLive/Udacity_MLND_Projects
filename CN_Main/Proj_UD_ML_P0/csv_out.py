import numpy as np
import pandas as pd

# RMS Titanic data visualization code 
# 数据可视化代码
from titanic_visualizations import survival_stats
from IPython.display import display

# Load the dataset 
# 加载数据集
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

#==============================================================================
# print(data)
#==============================================================================



def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    # 确保预测的数量与结果的数量一致
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        # 计算预测准确率（百分比）
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"
    
def predictions_3(data):
    """ Model with multiple features. Makes a prediction with an accuracy of at least 80%. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
         
        if passenger['Sex']=='female':
            if passenger['Pclass'] == 3:
                if passenger['Embarked'] == 'C' or passenger['Embarked'] == 'Q':
                    predictions.append(1)
                else:
                    predictions.append(0)
            else:
                predictions.append(1)

        else:
            if passenger['Age'] < 10:
                if passenger['Pclass'] <= 2:
                    predictions.append(1)
                else:
                    predictions.append(0)
            elif (passenger['Age'] > 10 and passenger['Age'] <= 15):
                if passenger['Pclass'] <= 2:
                    predictions.append(1)
                else:
                    predictions.append(0)

            elif passenger['Age'] > 15:
                if passenger['Pclass'] == 1 and passenger['Parch'] >= 5:
                    if passenger['Fare'] > 20:
                        predictions.append(1)
                    else:
                        predictions.append(0) 
                else:
                    predictions.append(0) 
            else:
                predictions.append(0) 

    
    # Return our predictions
    return pd.Series(predictions)

in_file = 'test.csv'
data = pd.read_csv(in_file)

predictions = predictions_3(data)

df = pd.DataFrame(predictions)

print(predictions)




predictions.to_csv('prj_1.csv', index=True)
#==============================================================================
# print accuracy_score(outcomes, predictions)
#==============================================================================


#==============================================================================
# import numpy as np
# import pandas as pd
# 
# # RMS Titanic data visualization code 
# # 数据可视化代码
# from titanic_visualizations import survival_stats
# from IPython.display import display
# 
# # Load the dataset 
# # 加载数据集
# in_file = 'titanic_data.csv'
# full_data = pd.read_csv(in_file)
# 
# outcomes = full_data['Survived']
# data = full_data.drop('Survived', axis = 1)
# 
# print(data)
#==============================================================================
