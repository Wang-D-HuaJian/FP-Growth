import time
start = time.clock()
import sys
sys.path.append("F:\Machine_Learning_Algorithm")
from FP_growth_algorithm.fpGrowth import *

#rootNode = treeNode('pyramid',9,None)
#rootNode.children['eye']=treeNode('eye',13,None)
#rootNode.children['phoenix']=treeN-ode('phoenix',3,None)

#rootNode.disp()

simpDat = loadSimpDat()
#print(simpDat)
initSet = createInitSet(simpDat)
#print(initSet)

#####创建FP树
myFPtree, myHwaderTab = createTree(initSet, 3)
#myFPtree.disp()

#####测试条件模式基的构建

#result1 = findPrefixPath('x',myHwaderTab['x'][1])
#print(result1)

#result2 = findPrefixPath('z',myHwaderTab['z'][1])
#print(result2)

#result3 = findPrefixPath('r',myHwaderTab['r'][1])
#print(result3)

#freqItems = []
#mineTree(myFPtree, myHwaderTab, 3, set([]), freqItems)
#print(freqItems)


end = time.clock()
print("The running time is %s Seconds!" % (end-start))

##############统计程序运行时间的代码
#import time
#start=time.clock()
#codes
#end=time.clock()
#run_time=end-start(秒)