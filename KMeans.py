from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

df = pd.read_csv("data.csv")

plt.scatter(df.reviews,df.stars)
plt.xlabel('reviews')
plt.ylabel('stars')


km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df[['reviews','stars']])

df['cluster']=y_predicted

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.reviews,df1.stars,color='green')
plt.scatter(df2.reviews,df2.stars,color='red')
plt.scatter(df3.reviews,df3.stars,color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('reviews')
plt.ylabel('stars')
plt.legend()

#plt.show()

#Preprocessing using min max scaler#############
scaler = MinMaxScaler()

scaler.fit(df[['stars']])
df['stars'] = scaler.transform(df[['stars']])

scaler.fit(df[['reviews']])
df['reviews'] = scaler.transform(df[['reviews']])

plt.scatter(df.reviews,df.stars)
plt.xlabel('reviews')
plt.ylabel('stars')

#plt.show()#####################################

#Elbow Plot#####################################
sse = []
k_rng = range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df[['reviews','stars']])
    sse.append(km.inertia_)

plt.xlabel('K')
plt.ylabel('Sum of squared error')
plt.plot(k_rng,sse)

plt.show()



