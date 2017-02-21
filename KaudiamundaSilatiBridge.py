#import pandas as pd
import numpy as np
import items as it
import ClassLibrary as cl 
import FunctionLibrary as fl
import math as mt
from statistics import  mean
l=25










if __name__ == "__main__":
    print('''Name of the work:-Construction of C.C. road with small Bridge from Kaudiamunda
Bagbahali Road to Silati Road''')
    print('Estimated Cost:-Rs. 3,20,000.00\t\tHead of Account:-G.G.Y.(2016-17)')
    print('-'*80)
    print('\t\t\t\tSection-A (Bridge)')
    print(it.items['efhs'])
    foundation=cl.Quantity([['abutments of the bridge',2,6.3,2.6,2.0]])
    foundation.rate=103.2
    foundation.volume()
    print(it.items['CC(1:4:8)'])
    concrete=cl.Quantity([['footing 1',2,6.10,2.5,0.2],
                          ['footing 2',2,6.1,2.1,0.2],
                          ['footing 2',2,6.1,2.0,0.2],
                          ['footing 3',2,6.1,1.9,0.2],
                          ['footing 4',2,6.1,mean([1.5,0.9]),1.2]])
    concrete.rate = 4132.62
    concrete.volume()
    print(it.items['rscs_plinth'])
    footing=cl.Quantity([['footing1,2,3,4',4*2*2,6.1,0.2],
                         ['side of footing 1',2,2.5,0.2],
                         ['side of footing 2',2,2.1,0.2],
                         ['side of footing 3',2,2.0,0.2],
                         ['side of footing 4',2,1.9,0.2]
                         ])
    footing.rate=82.08
    footing.vArea()
    print(it.items['rscs_walls'])
    wall=cl.Quantity([['outer side of wall',2,6.1,.93+1.2],
                      ['inside walls',2,6.1,1.2+.3],
                      ['both sides',2*2,mean([1.5,.9]),1.2]])
    wall.rate=387.08
    wall.vArea()
    print(it.items['m25'])
    rcc=cl.Quantity([['bearing plate',2,6.1,0.9,0.3],
                 ['Dart walls',2,6.1,0.63,0.3]])
    rcc.rate=4711.2
    rcc.volume()
    print(it.items['hysd'])
    reinforcement=cl.Quantity([['main bars in bearing plate',2*2*6,6.1-.08,0.89],
                               ['distribution in dart wall',2*8,6.1-.08,0.62],
                               ['stirrups in bearing plate',2*42,2.16,.89],
                               ['main bars in dart walls',42,2.22,0.62],
                               ['extra main bars in dart wall',42,1.1,0.89]])
    print(reinforcement.reinforcement()['y0'],reinforcement.reinforcement()['y1'])
    print('\t\t\t\t4.50q @ Rs.4324.45/ q = Rs.19460.00 ')
    print('\n\t\t\t\t SECTION-B (Concrete Road)')
    print(it.items['efhs'])
    foundation = cl.Quantity([['cut-off walls',2,l,0.2,0.2]])
    foundation.rate = 103.2
    foundation.volume()
    print(it.items['sand_fill'])
    sand_fill = cl.Quantity([['road subgrade',1,l,3.65-.4,.05]])
    sand_fill.rate = 313.52
    sand_fill.volume()
    print(it.items['CC(1:3:6)'])
    metal_concrete = cl.Quantity([['cut-off walls',2,l,0.2,0.25],
                                  ['sub-base concrete',1,l,3.65,0.1]
                                  ])
    metal_concrete.rate = 3700.47
    metal_concrete.volume()
    print(it.items['CC(1:2:4)'])
    chips_concrete = cl.Quantity([['crust of the road',1,l,3.65,0.1]])
    chips_concrete.rate =4814.96
    chips_concrete.volume()
    print(it.items['rscs_plinth'])
    cut_off = cl.Quantity([['outside cut-off',2,l,0.05+.2],
                           ['inside cut-off',2,l,0.05]])
    cut_off.rate = 82.08
    cut_off.vArea()
    print('\nCost towards hire and running of plate vibrator')
    print('\n\t\t\t3.65 hour @ \u20B9 106.00/ hour = \u20B9 387.00')
    print('\n\t\t\tCess for welfare of labourers = \u20B9 3200.00')
    print('\n\t\t\tDepartmental contingency \u20B9 3200.00')
    print('\n\t\t\tDisplay board and photograph = \u20B9 1500.00')
    print('-'*80)
    fl.signature(320000,'three lakh twenty thousand only', 2, 'Baunsuni G.P.')
    
    
    
    
    
    
    
    
    
