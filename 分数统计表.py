import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
df = pd.read_csv('scores.csv')
def draw(a,b,c,d,e):
    algorithm = ["under 60","60-69","70-79","80-89","90-100"]
    results = [e,d,c,b,a]
    plt.figure('label',figsize=(4,4), dpi = 160)
    plt.bar(algorithm, results, alpha=1, width=0.5)
    plt.xlabel('Section', fontdict={'family':'Times New Roman', 'size':12})
    plt.ylabel('Number of students', fontdict={'family':'Times New Roman', 'size':12})
    plt.ylim([0, 40])
    plt.title('Grade Distribution Map')
    for x,y in zip(algorithm, results): 
        plt.text(x, y, '%d' % y, ha='center', va='bottom', fontdict={'family':'Times New Roman', 'size':12})
    plt.show()
a=0
b=0
c=0
d=0
e=0
for index,row in df.iterrows():
    sum=row["homework"]*0.2+row["quiz"]*0.2+row["midterm"]*0.2+row["final"]*0.4
    if sum<60:
        e+=1
    elif sum>=60 and sum<70:
        d+=1
    elif sum>=70 and sum<80:
        c+=1
    elif sum>=80 and sum<90:
        b+=1
    else:
        a+=1
draw(a,b,c,d,e)


