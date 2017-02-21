import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it
l = 87









if __name__ == "__main__":
    print('Name of the Work:- Constn. of C.C. road from Fabsi Harijan Pada Byepass road to AWC Building')
    print('Head of Account:-G.G.Y.(2016-17)\tEstimated Cost:-\u20B92,00,000.00')
    print('-'*80)
    print('Calculation of total builtup area:-')
    tba = cl.Quantity([['patch 1',1,29,4.32],
                       ['patch 2',-1,2.0,1.5],
                       ['patch 3',0.5,2.1,1.68]
                       
                       ])
    
    print(tba.tba()['y0'],'{:.2f}sqm'.format(tba.tba()['y1']))
    print('\nClaculation of cut-off wall lengths:-')
    tcl=cl.Quantity([['patch 1',2,29],
                     
                       ])
    print(tcl.tcl()['y0'],'{:.2f}m'.format(tcl.tcl()['y1']))
    print('\nSurface Area of cut-off walls')
    cutoff=cl.Quantity([['cut-off walls',1,58.00,.2]])
    print(cutoff.tba()['y0'],'{:.2f}sqm'.format(cutoff.tba()['y1']))
    print(it.items['efhs'])
    foundation = cl.Quantity([['cut-off walls',1,58.00,0.2,0.2]])
    foundation.rate = 103.2
    foundation.volume()
    print(it.items['sand_fill'])
    sand_fill = cl.Quantity([['road subgrade',1,112.44,.05]])
    sand_fill.rate = 313.52
    sand_fill.aVolume()
    print(it.items['CC(1:3:6)'])
    metal_concrete = cl.Quantity([['cut-off walls',1,11.6,0.5],
                                  ['sub-base concrete',1,124.04,0.07]
                                  ])
    metal_concrete.rate = 3700.47
    metal_concrete.aVolume()
    print(it.items['CC(1:2:4)'])
    chips_concrete = cl.Quantity([['crust of the road',1,124.04,0.07]
                                  ])
    chips_concrete.rate =4814.96
    chips_concrete.aVolume()
    print(it.items['rscs_plinth'])
    cut_off = cl.Quantity([['outside cut-off',1,58,0.05+.14],
                           ['inside cut-off',1,58,0.05]])
    cut_off.rate = 82.08
    cut_off.vArea()
    #===========================================================================
    # print(it.items['Earth_work_mechanical'])
    #===========================================================================
    #===========================================================================
    # reinforcement=cl.Quantity([['short bars',24,1.12,0.395],
    #                            ['long bars',8,3.58,.395]])
    # print(reinforcement.reinforcement()['y0'],reinforcement.reinforcement()['y1'])
    #===========================================================================
    #===========================================================================
    # ew=cl.Quantity([['both side of road',1,53.58,1.5,0.6]])
    # ew.rate=129.8
    # ew.volume()
    #===========================================================================
    #===========================================================================
    # print('Supplying and fixing of NP-3 type 0.30m dia R.C.C. hume pipe ')
    # print('\n\t\tCost =2.50m @ Rs.387.00/m Rs. 968.00')
    # print('\n\t\tConveyance=                    Rs. 500.00')
    # print('\n\t\tLabour charges for laying = Rs. 300.00')
    #===========================================================================
    print('\nCost towards hire and running of plate vibrator')
    print('\n\t\t\t3.47 hour @ \u20B9 106.00/ hour = \u20B9 368.00')
    print('\n\t\t\tCess for welfare of labourers = \u20B9 1000.00')
    print('\n\t\t\tDepartmental contingency \u20B9 1000.00')
    print('\n\t\t\tDisplay board and photograph = \u20B9 1500.00')
    print('-'*80)
    fl.signature(100000,'two lakh only', 2, 'Baunsuni G.P.')
    
    
    
    
    
    
    
     