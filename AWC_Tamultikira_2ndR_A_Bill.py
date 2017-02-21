import ClassLibrary as cl
import FunctionLibrary as fl
import items as it








if __name__ == "__main__":
    print('Total centre line length ')
    tcl = cl.Quantity([['long wall 1',2,9.9],
                       ['long wall 2',1,6.95],
                       ['short wall 1',3,6.0],
                       ['short wall 2',1,2.95],
                       ['short wall 3',1,1.9],
                       ])
    print(tcl.tcl()['y0'],
          tcl.tcl()['y1'])
    
    print(it.items['m20'])
    rcc=cl.Quantity([['effective centre line length',1,49.6-4*0.25,0.25,0.15],
                     ['extra thick at verandah lintel',1,3.23+.5-.03,0.25,0.1],
                     ['verandah lintel chajja',1,3.7,0.45,0.06],
                     ['toilet and kitchen chajja',1,6.0,0.45,0.06],
                     ['store room chajja',1,1.78,0.45,0.06],
                     ['window chajja',2,1.2,0.45,0.06],
                     ['columns 1',6,0.25,0.25,0.45],
                     ['columns 2',6,0.25,0.25,0.75],
                     ])
    rcc.rate=4500.1
    rcc.volume()
    print(it.items['bmss'])
    brick = cl.Quantity([['all walls',1,49.6-12*0.25-0.5,0.25,0.45],
                         ['extra height 1',6,3.23,0.25,0.3],
                         ['extra height 2',1,3.65,0.25,0.3],
                         ['extra height 3',2,1.65,0.25,0.3]])
    brick.rate = 2792.14
    brick.volume()
    print(it.items['rscs_lintel'])
    lintel= cl.Quantity([['effective centre line length',2,49.6-4*0.25,0.15],
                     ['extra thick at verandah lintel',2,3.7,0.1],
                     ['bottom of door 1',1,
                      1.08,0.25],
                     ['bottom of door 2',3,0.9,0.25],
                     ['bottom of door3',2,0.75,.25],
                     ['bottom of windows',3,0.9,0.25]])
    lintel.rate = 195.11
    lintel.vArea()
    print(it.items['rscs_slab'])
    chajja = cl.Quantity([['verandah chajja',1,3.7,0.45],
                        ['kitchen and toilet chajja',1,6.0,0.45],
                        ['store chajja',1,1.75,0.45],
                        ['window chajja',2,1.2,0.45]])
    chajja.rate=291.61
    chajja.hArea()
    print(it.items['rscs_beam'])
    column=cl.Quantity([['columns',4*6,0.25,0.45],
                        ['columns',4*6,0.25,0.75]])
    column.rate=462.1
    column.vArea()
    reinforcement=cl.Quantity([['long walls1',4,9.9+.17,0.62],
                               ['long walls 2',4,6.59,0.62],
                               ['long walls 3',4,6.95-.08,0.62],
                               ['short walls 4',3*4,3.45+2.69+.17,0.62],
                               ['kitchen and toilet',4,2.95+.17,0.62],
                               ['store',4,1.9+.25-.08,0.62],
                               ['verandah lintel',5,3.23+.5-.1,0.89],
                               ['extra on verandah top',2,1.2,0.89],
                               ['extra bottom at D-1',1,1.58,0.62],
                               ['extra bottom at D-2',3,1.4,0.62],
                               ['extra bottom at D-3',1,2.87,0.62],
                               ['extra bottom at W-3',3,1.4,0.62],
                               ['stirrups in lintel bend',285,0.67,.395],
                               ['beam stirrups',22,0.87,.395],
                               ['column stirrups',6*4+6*6,.87,0.395],
                               ['verandah chajja bars',25,0.7-.08,0.395],
                               ['toilet and kitchen chajja bars',40,0.7-.08,0.395],
                               ['window chajja bars',9,0.45+.25-.08,0.395],
                               ['store room chajja bars',13,0.45+.25-.08,0.395],
                               ['toilet and kitchen chajja distribution bars',3,6-.08,0.395],
                               ['window chajja distributions',3*2,1.13,0.395],
                               ['store chajja distributions',3,1.95,0.395],
                               ['verandah chajja distribution',3,3.65,.395]])
    reinforcement.rate = 286.86
    print(reinforcement.reinforcement()['y0'])
    print(reinforcement.reinforcement()['y1'])
    print(it.items['CC(1:4:8)'])
    concrete=cl.Quantity([['area of building',1,2.95+6.95+.25,3.9+1.9+0.25,0.1],
                         ['deduct wall area',-1,49.6-1,0.25,0.1]])
    concrete.rate = 2791.36
    concrete.volume()


