import pandas as pd

WBB_Math = pd.DataFrame (
        {'Student' : ['Ice Bear','Panda','Grizzly'],
         'Math' : [80,95,79] })

WBB_Electronics = pd.DataFrame (
        {'Student' : ['Ice Bear','Panda','Grizzly'],
         'Electronics' : [85,95,83] })

WBB_GEAS = pd.DataFrame (
        {'Student' : ['Ice Bear','Panda','Grizzly'],
         'GEAS' : [90,79,93] })

WBB_ESAT = pd.DataFrame (
        {'Student' : ['Ice Bear','Panda','Grizzly'],
         'ESAT' : [93,89,88] })

M1 = pd.merge(WBB_Math, WBB_Electronics, how = 'right', on = 'Student')
M2 = pd.merge(M1, WBB_GEAS, how = 'right', on = 'Student')
finalMerge = pd.merge(M2, WBB_ESAT, how = 'right', on = 'Student')

melted1 = pd.melt(finalMerge, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
finalMelt = melted1.rename(columns = {'variable' : 'Subject', 'value' : 'Grades'})



