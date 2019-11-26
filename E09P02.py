import pandas as pd

boxes = pd.DataFrame(
        {'Box' : ['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension' : ['Length','Width','Height','Length','Width','Height'],
         'Value' : [6,4,2,5,3,4] })

tidy = boxes.pivot_table(index = 'Box', columns = 'Dimension', values = 'Value')
volume = [48, 60]

tidy['Volume'] = volume