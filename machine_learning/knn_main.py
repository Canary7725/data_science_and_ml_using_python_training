import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.preprocessing import StandardScaler

import joblib

df=pd.read_csv('data/student_performance_clean.csv')
df.head()

X=df[['study_hours','attendance']]
Y=df['pass_status']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

scaler=StandardScaler()

x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)

model=KNeighborsClassifier(n_neighbors=5)

model.fit(x_train_scaled,y_train)

joblib.dump(model,'student_result_classifier.pkl')

value=pd.DataFrame(
    {
        "study_hours":[6],
        "attendance":[88]
    }
    )

value_scaled=scaler.transform(value)

predicted=model.predict(value_scaled)

print(predicted)