import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it
l = 87









if __name__ == "__main__":
    print('Name of the Work:- Constn. of C.C. road from Baunsuni NuaBasti High School Road')
    print('Head of Account:-G.G.Y.(2016-17)\tEstimated Cost:-\u20B93,20,000.00')
    print('-'*80)
    print('Calculation of total builtup area:-')
    tba = cl.Quantity([['patch 1',1,9.15,3.85],
                       ['patch 2',1,13.8,3.9],
                       ['patch 3',1,19.5,3.5],
                       ['patch 4',1,15.1,5.25],
                       ['patch 5',1,14.7,4.2],
                       ['steps 1st footing',2,3.05,0.7],
                       ['steps 2nd footings',2,3.05,0.35],
                       ['old road and new road junction',1,3.65,1.2]])
    
    print(tba.tba()['y0'],'{:.2f}sqm'.format(tba.tba()['y1']))
    print('\nClaculation of cut-off wall lengths:-')
    tcl=cl.Quantity([['patch 1',2,9.15],
                     ['patch 2',2,13.8],
                     ['patch 3',2,19.5],
                     ['patch 4',2,15.1],
                     ['patch 5',2,14.7],
                     ['old road and new road junction',2,4.88]])
    print(tcl.tcl()['y0'],'{:.2f}m'.format(tcl.tcl()['y1']))
    print('\nSurface Area of cut-off walls')
    cutoff=cl.Quantity([['cut-off walls',1,154.26,.2]])
    print(cutoff.tba()['y0'],'{:.2f}sqm'.format(cutoff.tba()['y1']))
    print(it.items['efhs'])
    foundation = cl.Quantity([['cut-off walls',1,154.26,0.2,0.2]])
    foundation.rate = 103.2
    foundation.volume()
    print(it.items['sand_fill'])
    sand_fill = cl.Quantity([['road subgrade',1,278.24,.05]])
    sand_fill.rate = 313.52
    sand_fill.aVolume()
    print(it.items['CC(1:3:6)'])
    metal_concrete = cl.Quantity([['cut-off walls',2,30.85,0.25],
                                  ['sub-base concrete',1,309.09,0.09]
                                  ])
    metal_concrete.rate = 3700.47
    metal_concrete.aVolume()
    print(it.items['CC(1:2:4)'])
    chips_concrete = cl.Quantity([['crust of the road',1,309.09,0.09]
                                  ])
    chips_concrete.rate =4814.96
    chips_concrete.aVolume()
    print(it.items['rscs_plinth'])
    cut_off = cl.Quantity([['outside cut-off',2,154.26,0.05+.2],
                           ['inside cut-off',2,154.26,0.05]])
    cut_off.rate = 82.08
    cut_off.vArea()
    print(it.items['hysd'])
    reinforcement=cl.Quantity([['short bars',24,1.12,0.395],
                               ['long bars',8,3.58,.395]])
    print(reinforcement.reinforcement()['y0'],reinforcement.reinforcement()['y1'])
    print('\nCost towards hire and running of plate vibrator')
    print('\n\t\t\t11.12 hour @ \u20B9 106.00/ hour = \u20B9 1180.00')
    print('\n\t\t\tCess for welfare of labourers = \u20B9 3200.00')
    print('\n\t\t\tDepartmental contingency \u20B9 3200.00')
    print('\n\t\t\tDisplay board and photograph = \u20B9 1500.00')
    print('-'*80)
    fl.signature(320000,'three lakh twenty thousand only', 2, 'Baunsuni G.P.')
    
    
    
    
    
    
    
     