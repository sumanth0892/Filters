#Tracking movement of a pet using Bayesian filters.
#Bayesian filters named so due to their probabilistic nature
#Consider a pet moving in a hallway.
#Sensors are usually faulty and data isn't reliable

import numpy as np
import matplotlib.pyplot as plt
hallway = np.array([1,1,0,0,0,0,0,0,1,0])
#Normalization
#The sum of probabilities isn't 1 so we need to normalize it.
def normalize (p):
    s = sum(p)
    for i in range(len(p)):
        p[i] = p[i]/s
def update (pos,measure,p_hit,p_miss):
    q = np.array(pos,dtype=float)
    for i in range(len(hallway)):
        if (hallway[i]==measure):
            q[i]=pos[i]*p_hit
        else:
            q[i]=pos[i]*p_miss
    normalize(q)        
    return q
pos = np.array([0.2]*10)
reading = 1 # 1 is door and 0 is wall
prob_hitting=0.6 #Probability of being right
prob_miss = 0.2 #Probabilty of a miss
pos = update(pos,1,0.6,0.2) #0.6 and 0.2 are randomly chosen


#Incorporating movement data

print(pos)
print ('Sum = ',sum(pos))
N = len(pos)
x = range(N)
width = 1/1.5
plt.bar(x,pos,width,color='blue')
#plt.grid(True,color='black')
plt.show()

def perfect_predict(pos,move):
    #Move the position by move where positive is to the right
    n = len(pos)
    result = np.array(pos,dtype=float)
    for i in range(n):
        result[i]=pos[(i-move)%n]
    return result
pos = np.array([0.4,0.1,0.2,0.3])
print ("position before predict =",pos)

pos = perfect_predict(pos,1)
print("Position after predict=",pos)

N = len(pos)
x = range(N)
plt.bar(x,pos,width=1/1.5,color='blue')

plt.show()

#Adding noise
#Assume that when the sensor sends data, it is 70% likely to be right, 20% overshot
#and 10% undershot
#For example:
#If the sensor sends '4' (meaning 4 spaces to right), there is a 70% probailtity
#That the pet has moved 4 spaces right
#20% likely that it has moved 5 spaces right and
#10% likely that it has moved 3 spaces to the right
def predict (pos,move,p_correct,p_under,p_over):
    n = len(pos)
    result = np.array(pos,dtype=float)
    for i in range(n):
        result[i]= \
                   pos[(i-move)%n] * p_correct +\
                   pos[(i-move-1)%n] *p_over +\
                   pos[(i-move+1)%n] *p_under
    return result

p = np.array([0,0,0,1,0,0,0,0])
res = predict(p,3,0.7,0.1,0.2)
print(res)


        


            
            
