import numpy as np 

movies = np.array([
    ["Interstellar", "Inception", "Avengers"],
    ["Conjuring", "Tangled", "IT"],
    ["Joker", "LaLaLand","Evil dead"]
    ])
    
arr=movies.flatten()   
rating=np.array([
    
    [9, 7, 9.3, 8.6, 9.3, 5.2, 9.1, 8.9, 7],
    [8.6, 9.1, 0, 4.5, 6.7, 2.3, 9.8, 1.2, 7.4],
    [8.9, 8, 6, 3.1, 5.6, 9.9, 4.2, 0.8, 2.7]
    ])
r=rating>0
r_sum=np.sum(r,axis=0)
m=np.mean(rating,axis=0)
high=np.argmax(m)
low=np.argmin(m)

user = rating[1]
unseen = np.where(user == 0)[0]
recommend = unseen[np.argmax(m[unseen])]

print("Recommended movie:", arr[recommend])
print("Highest rating movie:",arr[high])
print("Lowest rating movie:",arr[low])
