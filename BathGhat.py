import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it








if __name__ == "__main__":
    print('Name of the work:-Improvement of KaraKhai at Kaudiamunda')
    print('Head of Account:-______________\tEstimated Cost:-\u20B92,00,000.00')
    print('-'*80)
    print(it.items['efhs'])
    foundation= cl.Quantity([['cut-off walls',2,17.00,0.68,0.45],
                             ['cut-off walls top & bottom',2,4.5-.38-.68,0.68,0.45]
                             ])
    foundation.rate=103.2
    foundation.volume()
    print(it.items['CC(1:3:6)'])
    concrete=cl.Quantity([['cut-off walls both side',2,17.00,0.38,0.45+0.45],
                          ['small steps',18,4.5,0.75,0.15],
                          ['bigger steps',1,4.5,3.2,0.15],
                          ['bigger step 2',1,4.5,2.75,0.15],
                          ['cut-off walls top and bottom',2,4.5-0.76,0.38,0.45],
                          ['kerbs',2,17.00,0.3,0.45],
                          ])
    concrete.rate=3700.47
    concrete.volume()
    chips_concrete= cl.Quantity([['smaller steps',18,4.5-0.75,0.6,0.1],
                                 ['larger step 1',1,4.5,2.6,0.1],
                                 ['larger step2',1,4.5-2*0.38,3.05,0.1]])
    chips_concrete.rate=4814.96
    chips_concrete.volume()
    sand_filling =cl.Quantity([['bottom of the steps',1,17.00-.76,4.5-0.76,0.45]])
    sand_filling.rate=313.52
    sand_filling.volume()
    print(it.items['rscs_walls'])
    centering=cl.Quantity([['walls both sides',2*2,17,0.45],
                           ['steps risers',20*2,4.5,0.15],
                           ['wearing coats',20,4.5,0.1],
                           ['kerbs',2*2,17.0,0.45]])
    centering.rate = 387.08
    centering.vArea()
    print(it.items['12cp(1:6)'])
    plaster=cl.Quantity([['risers of steps',20,4.5-.6,0.15],
                         ['kerb walls',4,17,0.45]])
    plaster.rate=85.22
    plaster.vArea()
    
    print('\t\t\tCess for welfare of labourers = \u20B92000.00')
    print('\t\t\tWork contiongency = \u20B92000.00')
    print('\t\t\tDisplay Board and photograph = \u20B92000.00')
    print('-'*80)
    fl.signature(200000, 'Two lakhs only',3 , 'Sankara G.P.')
    