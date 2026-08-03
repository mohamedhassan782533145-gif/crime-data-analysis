import numpy as np 
import pandas as pd
df=pd.read_excel("Crime_Data_Project.xlsx")
print(df)
print("********************************************************************************************")

data=df.to_numpy()
print(data)
print("*********************************************************************************************")

numbers=data[:,1:]
data_max=np.max(numbers)
data_min=np.min(numbers)
data_sum=np.sum(numbers)
data_mean=np.sum(numbers)
data_median=np.median(numbers)
data_sd=np.std(numbers)
data_var=np.var(numbers)
data_argmax=np.argmax(numbers)
data_argmin=np.min(numbers)
print(numbers ,data_max ,data_min ,data_sum ,data_mean ,data_median ,data_sd ,data_var ,data_argmax ,data_argmin)
print("***********************************************************************************************")

schools=data[:,1]
schools_max=np.max(schools)
school_min=np.min(schools)
schools_sum=np.sum(schools)
schools_mean=np.mean(schools)
schools_median=np.median(schools)
schools_sd=np.std(schools)
schools_var=np.var(schools)
schools_argmax=np.max(schools)
schools_argmin=np.min(schools)
print(schools ,schools_max ,school_min ,schools_sum ,schools_mean ,schools_median ,schools_sd ,schools_var ,schools_argmax ,schools_argmin)
print("************************************************************************************************")

index_max = np.argmax(schools)
state_max = data[index_max, 0]
print(index_max ,state_max)