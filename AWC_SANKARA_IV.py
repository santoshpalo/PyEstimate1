import FunctionLibrary as fl
import ClassLibrary as cl
import items as it














if __name__ == "__main__":
    tcl1 = cl.Quantity([['long wall 1',2,10.74],
             ['long wall 2',1,8.51],
             ['short wall 1',2,5.94],
             ['short wall 2',2,3.68],
             ['short wall 3',2,2.13]])
    tcl1.tcl()
    print(it.items['CC(1:4:8)'])
    metal_concrete = cl.Quantity([['class room',1,8.06,3.23,0.1],
                                  ['verandah,kitchen and store',3,2.49,1.68,0.1],
                                  ['toilets',1,3.23,1.8,0.1],
                                  ['steps entrance',1,1.5,1.0,0.1],
                                  ['kitchen exit',1,1.2,1.00,0.1],
                                  ['toilet steps',1,3,1.0,0.1]
                                  ])
    metal_concrete.rate=2835.52
    metal_concrete.volume()
    print(it.items['m20'])
    rcc = cl.Quantity([['R.C.C. slab 1',1,11.29,4.23,0.1],
                       ['R.C.C. slab 2',1,9.06,2.13,0.1],
                       ['R.C.C. beams',2,3.43,0.25,0.25],
                       ['R.C.C. roof bend',1,53.49-1,0.25,0.15],
                       ])
    rcc.rate=4142.32
    rcc.volume()
    print(it.items['bmss'])
    brick_super_structure = cl.Quantity([['walls above lintel',1,53.49-2,0.25,0.6],
                                         ['toilet half brick walls',2,1.8,0.13,0.6]])
    brick_super_structure.rate = 2823.95
    brick_super_structure.volume()
    brick_f_p = cl.Quantity([['entrance steps 1',1,1.5,1.00,0.25],
                             ['entrance steps 2',1,1.5,0.75,0.15],
                             ['entrance steps 3',1,1.5,0.50,0.15],
                             ['entrance steps 4',1,1.5,0.25,0.15],
                             ['kitchen steps 1',1,1.2,1.00,0.25],
                             ['kitchen steps 2',1,1.2,0.75,0.15],
                             ['kitchen steps 3',1,1.2,0.5,0.15],
                             ['kitchen steps 4',1,1.2,0.25,0.15],
                             ['toilet steps 1',1,3.00,1.00,0.25],
                             ['toilet steps 2',1,3.0,0.75,0.15],
                             ['toilet steps 3',1,3.0,0.5,0.15],
                             ['toilet steps 4',1,3.0,0.25,0.15]])
    brick_f_p.rate = 2790.95
    brick_f_p.volume()
    print(it.items['rscs_slab'])
    centering_slab=cl.Quantity([['slab 1',1,11.29,4.23],
                                ['slab 2',1,9.06,2.13],
                                ['deduct beam',-2,3.93,0.25],
                                ['add roof bend',1,53.49-1,.05]])
    centering_slab.rate = 305.67
    centering_slab.hArea()
    print(it.items['rscs_beam'])
    centering_beam = cl.Quantity([['beams',2,3.93-.5,0.75]])
    centering_beam.rate = 462.1
    centering_beam.vArea()
    print(it.items['hysd'])
    print('\nProvisional Cost = 7.50q @ Rs.4513.66/q = Rs. 33,852.00')
    print(it.items['12cp(1:6)'])
    plaster12 = cl.Quantity([['alaround walls',1,53.49+1-2,3.15],
                               ['in the plinth',1,33.36+4*0.38,0.75],
                               ['add half brick thick walls',4,1.8,3.15],
                               ['ver openings',-1,2.5,2.1],
                               ['windows',-4*0.5,0.9,1.33],
                               ['Door-1',-0.5,1.2,2.1],
                               ['Door-2',-2*.5,0.9,2.1],
                               ['Door-3',-3*0.5,0.75,2.1]])
    plaster12.rate = 81.21
    plaster12.vArea()
    #===========================================================================
    # print(it.items.keys())
    #===========================================================================
    #===========================================================================
    # print("The area of your rectangle is {}cm\u00b2".format(5))
    #===========================================================================
    print(it.items['16cp(1:6)'])
    plaster16 = cl.Quantity([['alaround walls',1,53.49-1-2,3.15],
                               ['in the plinth',1,33.36+4*0.38,0.75],
                               ['add half brick thick walls',4,1.8,3.15],
                               ['ver openings',-1,2.5,2.1],
                               ['windows',-4*0.5,0.9,1.33],
                               ['Door-2',-2*.5,0.9,2.1],
                               ['Door-3',-3*0.5,0.75,2.1]])
    plaster16.rate=112.27
    plaster16.vArea()
    print(it.items['20cp(1:6)'])
    plaster20= cl.Quantity([['external walls in plinth',1,38.44,0.75]])
    plaster20.rate=121.98
    plaster20.vArea()
    print(it.items['20cp(1:4)'])
    grading=cl.Quantity([['roof part1',1,11.29,4.23],
                         ['roof part2',1,9.06,2.13]])
    grading.rate=133.10
    grading.hArea()
    print(it.items['6cp(1:4)'])
    plaster6=cl.Quantity([['chajjas1',1,6.1,0.5],
                          ['chajja2',1,3.93,0.5],
                          ['chajja3',3,1.2,.5],
                          ['chajja4',1,1.05,0.5],
                          ['chajja5',1,2.01,0.5],
                          ['beams',2,3.43,0.75]])
    plaster6.rate=88.88
    plaster6.vArea()
    print('\nCost and conveyance of M.S. Doors and windows = 5.05q @\u20B96300.00/q = \u20B931815.00\n')
    print('\t\t\tCess for welfare of labourers = 2250.00')
    #===========================================================================
    # print(it.items['paint'])
    # paint=cl.Quantity([['windows',4*2.75,0.9,1.33],
    #                            ['Door-1',1*2.25,1.2,2.1],
    #                            ['Door-2',2*2.25,0.9,2.1],
    #                            ['Door-3',3*2.25,0.75,2.1]])
    # paint.rate=78.86
    # paint.vArea()
    #===========================================================================
    print('-'*80)
    fl.signature(225000, 'Two lakh twenty five thousands only', 1, '')
    
    
    
    
    
    