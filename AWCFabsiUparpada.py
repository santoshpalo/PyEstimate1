import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it






if __name__ == "__main__":
    print('Total centre line length')
    
    tcl = cl.Quantity([['long walls',2,8.6],
                       ['short walls',3,6.00],
                       ['short wall1',1,6.55],
                       ['short wall2',1,8.6-6.55],
                       ['short wall 3',1,2.05]])
    print(tcl.tcl()['y0'])
    print('Total centre line length = ','{:.2f}m'.format(tcl.tcl()['y1']))
    print(it.items['efhs'])
    foundation=cl.Quantity([['foundation of columns',9,1.5,1.5,1.2],
                            ['open foundation',1,29.2-8*1.5,0.6,0.6]])
    foundation.rate = 122.97
    foundation.volume()
    print(it.items['m20'])
    rcc = cl.Quantity([['rcc column footings',9,1.2,1.2,0.3],
                       ['rcc pedestals',9,0.45,0.45,1.0],
                       ['rcc columns',9,0.25,0.25,2.10],
                       ['rcc plinth beams',1,45.85+2.05-5*.25,0.25,0.3],
                       ['rcc lintel band',1,45.85-1,0.25,0.15],
                       ['extra thickness lintel at verandah',1,4.54,0.25,0.1],
                       ['cantilever beams',2,1.5,0.25,0.1],
                       ['kitchen wash slabs',1,2.3,1.5,0.1],
                       ['kitchen platform',1,1.75,0.45+0.25+.05,0.06],
                       ['store and shoe rack',2,2.3,0.45+0.25+0.23,0.06],
                       ['verandah chajja',1,6.06,0.45,0.06],
                       ['toilet chajja',1,3.9,0.45,0.06],
                       ['chajja on window',3,1.2,0.45,0.06],
                       ['store loft',1,1.8,0.45,0.06]])
    rcc.rate =4435.46
    rcc.volume()
    brickFP = cl.Quantity([['walls in F and Plinth',1,29.2-8*0.45,0.38,1.2-.3-.2],
                           ['around plinth beams',2,45.85+2.05-5*0.25,0.065,0.3]])
    brickFP.rate =3193.2
    brickFP.volume()
    brickSS = cl.Quantity([['walls alround',1,45.85-9*0.25-3*0.25,0.25,2.1],
                           ['front door',-1,1.08,0.25,2.1],
                           ['windows',-3,0.9,0.25,1.2],
                           ['door1',-3,0.9,0.25,2.1],
                           ['toilet doors',-2,0.75,0.25,2.1],
                           ['verandah openings',-1,4.04,0.25,2.1],
                           ])
    brickSS.rate = 3226.2
    brickSS.volume()
    print(it.items['rscs_plinth'])
    plinth = cl.Quantity([['footings',4*9,1.2,0.3]
                          ])
    plinth.rate =82.08
    plinth.vArea()
    print(it.items['rscs_beam'])
    column = cl.Quantity([['pedestals',4*9,0.45,1.0],
                          ['columns',4*9,0.25,2.1]])
    column.rate = 462.1
    column.vArea()
    print(it.items['rscs_lintel'])
    lintel = cl.Quantity([['alround lintel',2,45.85-1,0.15],
                          ['extra thick lintel',2,4.53,0.1],
                          ['cantilever',2,1.5,0.1],
                          ['bottom of door1',1,1.08,0.25],
                          ['bottom of door2',1,0.9,0.25],
                          ['bottom of door3',2,0.9,0.25],
                          ['bottom of window',3,0.9,0.25],
                          ['shoe rack and store shelf',2,1.8,0.45+0.23],
                          ['kitchen platform',1,1.5,0.5],
                          ['bottom of verandah',1,4.04,0.25]])
    lintel.rate = 199.15
    lintel.vArea()
    print(it.items['rscs_slab'])
    chajja = cl.Quantity([['cantilever chajja',1,2.05,1.5],
                          ['verandah cjajja',1,4.54,0.45],
                          ['toilet chajja',1,3.9,0.45],
                          ['chajjas on windows',3,1.2,0.45],
                          ['store racks',1,1.8,0.45]])
    chajja.rate=305.67
    chajja.hArea()
    reinforcement=cl.Quantity([['footing bars',2*9*8,1.12,0.62],
                                    ['column bars',4*9,5.7,1.58],
                                    ['stirrups',22*9,0.87,0.395],
                                    ['pedestal bars',9*8,1.45,0.395],
                                    ['stirrups',9*8,1.56,.395],
                                    ['back side walls',2*5,8.76,0.89],
                                    ['middle wall',6,7.1,0.89],
                                    ['middle short walls',6,1.72,0.89],
                                    ['short walls',2*5,6.15,0.89],
                                    ['short wall at middle',6,6.15,0.89],
                                    ['short walls at verandah',2*5,1.97,0.89],
                                    ['extra top1',4,2.94,0.89],
                                    ['extra top2',8,1.6,0.89],
                                    ['extra top3',4,1.46,0.89],
                                    ['extra top4',4,2.08,0.89],
                                    ['extra top5',8,0.7,1.58],
                                    ['stirrups',300,0.97,0.395],
                                    ['shelf and shoe rack',2*15,0.45+0.25+0.23-.08,0.395],
                                    ['distributions',2*6,2.22,0.395],
                                    ['back side walls',4,8.76,0.62],
                                    ['front side wall',5,4.5,0.89],
                                    ['extra top',2,1.6,0.89],
                                    ['front side wall',4,4.5,0.62],
                                    ['middle wall',4,7.1,0.62],
                                    ['middle short walls',4,1.72,0.62],
                                    ['short walls',3*4,6.15,0.62],
                                    ['cantilever beam at wash bottom',2*2,1.5+.25-.08,0.62],
                                    ['cantilever beam at wash top',2*3,1.5+.25,0.89],
                                    ['short walls at verandah',4,1.97,0.62],
                                    ['extra bottom at door1',1,1.58,0.62],
                                    ['extra bar at door2,window',6,1.4,0.62],
                                    ['extra bar at toilet',1,2.8,0.62],
                                    ['stirrups',273,0.67,0.395],
                                    ['cantilever and verandah stirrups',2*10+27,0.87,0.395],
                                    ['verandah chajja bars',30,0.45+0.25-.08,0.395],
                                    ['toilet chajja bars',22,0.45+.25-.08,0.395],
                                    ['window chajja bars',3*8,0.45+0.25-.08,0.395],
                                    ['store room rack',12,.45+.25-.08,0.395],
                                    ['kitchen platform',12,0.45+0.25+.05-.08,0.395],
                                    ['kitchen platform distribution',6,1.75-.08,.395],
                                    ['verandah chajja distribution',3,4.54-.08,0.395],
                                    ['window chajja distribution',3,1.2-.08,0.395],
                                    ['toilet chajja',3,3.83,0.395],
                                    ['wash area main bar',10,2.3-.08,0.395],
                                    ['wash area distribution',14,1.75-.08,0.395],
                                    ['store loft distribution',3,1.8-.08,0.395]])
    print(reinforcement.reinforcement()['y2'],reinforcement.reinforcement()['y1'])
    print(it.items['CC(1:4:8)'])
    concrete = cl.Quantity([['column footings',9,1.5,1.5,0.1],
                            ['alround walls',1,45.85-9*0.45-2*.45,0.6,0.1],
                            ['class room',1,6.55-0.38,3.9-.38,0.1],
                            ['store',1,2.25-.38,2.05-.38,0.1],
                            ['verandah',1,6.55-2.25-0.38,2.05-.38,0.1],
                            ['kitchen',1,2.05-.38,2.7-.38,0.1],
                            ['toilet',1,3.3-.38,2.05-.38,0.1]])
    concrete.rate = 3219.39
    concrete.volume()
    print(it.items['sand_filling'])
    filling = cl.Quantity([['volume of building',1,8.97,6.38,0.6],
                          ['deduct r.c.c',-1,9.21,1,1],
                          ['deduct brick masonry',-1,8.63,1,1],
                          ['volume of excavation',0.5,30.49,1,1],
                          ['volume of C.C.',-1,8.48,1,1]])
    filling.rate= 277.34
    filling.volume()
    
    
    
    