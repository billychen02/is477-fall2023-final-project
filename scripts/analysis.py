#Analysis

#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#reading dataset from downloaded folder path
df = pd.read_csv("data/wdbc.data")

#holistic summary statistics of the dataset
summary_stats = df.describe().drop(index = 'count', columns='ID')
summary_stats.to_csv('results/summary_stats.csv')


#Summary Statistics: Key comparison between Benign and Malignant

rmeanM1 = df[df['Diagnosis']=='M']['radius1'].mean()
rmeanM2 = df[df['Diagnosis']=='M']['radius2'].mean()
rmeanM3 = df[df['Diagnosis']=='M']['radius3'].mean()
rmeanB1 = df[df['Diagnosis']=='B']['radius1'].mean()
rmeanB2 = df[df['Diagnosis']=='B']['radius2'].mean()
rmeanB3 = df[df['Diagnosis']=='B']['radius3'].mean()

Bcell_mean_radius = (rmeanB1+rmeanB2+rmeanB3)/3
Mcell_mean_radius = (rmeanM1+rmeanM2+rmeanM3)/3
print('Average Radius of a Benign Tumor Cell: ',Bcell_mean_radius)
print('Average Radius of a Malignant Tumor Cell: ',Mcell_mean_radius, '\n')

cmeanM1 = df[df['Diagnosis']=='M']['compactness1'].mean()
cmeanM2 = df[df['Diagnosis']=='M']['compactness2'].mean()
cmeanM3 = df[df['Diagnosis']=='M']['compactness3'].mean()
cmeanB1 = df[df['Diagnosis']=='B']['compactness1'].mean()
cmeanB2 = df[df['Diagnosis']=='B']['compactness2'].mean()
cmeanB3 = df[df['Diagnosis']=='B']['compactness3'].mean()

Bcell_mean_compactness = (cmeanB1+cmeanB2+cmeanB3)/3
Mcell_mean_compactness = (cmeanM1+cmeanM2+cmeanM3)/3
print('Average Compactness of a Benign Tumor Cell: ',Bcell_mean_compactness)
print('Average Compactness of a Malignant Tumor Cell: ',Mcell_mean_compactness,'\n')

cvmeanM1 = df[df['Diagnosis']=='M']['concavity1'].mean()
cvmeanM2 = df[df['Diagnosis']=='M']['concavity2'].mean()
cvmeanM3 = df[df['Diagnosis']=='M']['concavity3'].mean()
cvmeanB1 = df[df['Diagnosis']=='B']['concavity1'].mean()
cvmeanB2 = df[df['Diagnosis']=='B']['concavity2'].mean()
cvmeanB3 = df[df['Diagnosis']=='B']['concavity3'].mean()

Bcell_mean_concavity = (cvmeanB1+cvmeanB2+cvmeanB3)/3
Mcell_mean_concavity = (cvmeanM1+cvmeanM2+cvmeanM3)/3
print('Average Concavity of a Benign Tumor Cell: ',Bcell_mean_concavity)
print('Average Concavity of a Malignant Tumor Cell: ',Mcell_mean_concavity,'\n')

#Classification report
X = df.drop(['ID','Diagnosis'], axis=1)
y = df['Diagnosis'].map({'M':1, 'B':0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
classification_report = classification_report(y_test,y_pred)
print(classification_report)

#Key Classification Features for Breast Cancer Diagnosis
f_importance = pd.Series(classifier.feature_importances_,index = X.columns)

#plots

f_importance.nlargest(10).plot(kind='barh')
plt.title('Main Predictor Features of Breast Cancer')
plt.xlabel('Relative Importance')
plt.tight_layout()
plt.savefig('results/feature_importance.png')
plt.close()

statistic_compare_plt = pd.DataFrame({
    "Benign":[8.603469094304389,0.09473180578898227,0.07943069309056956],
    "Malignant":[13.068908018867925, 0.18409768396226414, 0.2177347641509434]},
    index=["Radius", "Compactness", "Concavity"])

statistic_compare_plt.plot(kind="bar",figsize=(10, 5))
plt.title("Comparison between Tumor Type and Corresponding Features")
plt.xlabel("Tumor Cell Features")
plt.ylabel("Relative Units for each feature")
plt.tight_layout()
plt.savefig('results/BM_comparison.png')
plt.close()
