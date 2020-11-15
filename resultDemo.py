import matplotlib.pyplot as plt
import pandas as pd
import os

if __name__=='__main__':
    #读两个文件
    if os.path.exists('output'):
        if os.path.exists('output/clusteredInstances/part-m-00000'):
            with open('output/clusteredInstances/part-m-00000','r') as f:
                instances=f.readlines()
        else:
            print('无instances文件')
        i=0
        while os.path.exists('output/cluster-'+str(i)):
            i=i+1
        #迭代次数
        iterationNum=i-1
        with open('output/cluster-'+str(i-1)+'/part-r-00000') as f:
            centers=f.readlines()
    else:
        print('无output文件夹')
    #把数据转换为适合画图
    x=[]
    y=[]
    cluster=[]
    for instance in instances:
        instance=instance.replace('\n','')
        x.append(float(instance.split(',')[0]))
        y.append(float(instance.split(',')[1].split('\t')[0]))
        cluster.append(float(instance.split(',')[1].split('\t')[1]))
    df=pd.DataFrame(columns=['x','y','cluster'])
    df['x']=x
    df['y']=y
    df['cluster']=cluster
    centersX=[]
    centersY=[]
    #聚类簇数k
    k=len(centers)
    for center in centers:
        center=center.replace('\n','')
        centersX.append(float(center.split(',')[2]))
        centersY.append(float(center.split(',')[3]))

    #画图
    for i in range(len(centersX)):
        plt.plot([centersX[i]],[centersY[i]],'^',label='center'+str(i+1))
        plt.scatter(df[df['cluster']==i+1]['x'],df[df['cluster']==i+1]['y'],label='cluster'+str(i+1))
    plt.axis([-1,101,-1,101])
    plt.legend()
    plt.savefig('img/'+str(k)+'classes'+str(iterationNum)+'time.png')