import ClassLibrary as cl 
import FunctionLibrary as fl 
import items as it
import math as mt





if __name__ == "__main__":
    print('Restoration of Nama Mandap at Phabsi, Baunsuni G.P.')
    print('Head of Account:- M.L.A.L.A.D.(2016-17)\t Estimated Cost:-\u20B9100000.00')
    print('-'*80)
    print(it.items['floor tile'])
    floor=cl.Quantity([['circular floor',mt.pi,4.22,4.22],
                       ['rectangular portion',-1,2.57,2.57],
                       ['mid portion',1,7.09,2.43],
                       ['out side step 1',1,1.5+2*.3,0.25],
                       ['out side step 2',1,1.0,0.25]
                       ])
    floor.rate=251.94
    floor.hArea()
    print('''Cost of 30cm x 30cm / 40cm x 40cm special plain / printedser\nies ceramic floor
tiles of premium grade having thickness 7mm to 8mm confirminq to IS 13755''')
    print('Cost = 67.35sqm @ \u20B9429.00 / sqm = \u20B928893.00')
    print(it.items['wall tile'])
    wall=cl.Quantity([['square mandap sides',4,2.53,0.4],
                      ['altar back 1',2,1.8,0.3],
                      ['altar back 2',2,1.2,0.3],
                      ['altar back 3',2,0.65,0.3],
                      ['altar back 4',2,0.5,0.25],
                      ['altar sides',2,.4,0.45],
                      ['altar inside offsets',2,0.3,0.15],
                      ['altar inside offsets',2,0.1,0.15],
                      ['altar inside offsets',2,.12,.15],
                      ['pillars of inside mandap',4*4,0.3,2.1],
                      ['beams of mandap',4,2.45,0.2]])
    wall.rate = 242.97
    wall.vArea()
    print('''\n30cm / 20cm x 20cm special plain /printed series ceramic wall tiles of
premium grade having thicknes 6 mm to 6.7 mm.confirminq to IS 13755\n''')
    print('Cost = 19.05sqm @ \u20B9387.00 / sqm = \u20B97372.00.00')
    print(it.items['vitrified'])
    vitrify=cl.Quantity([['raised mandap',1,2.57,2.57],
                         ['deduct for pillars',-4,0.3,0.3]])
    vitrify.rate=840.24
    vitrify.hArea()
    print('''\nDismantling and removing lime concrete flooring 7.5 cm to 10 cm thick including
stacking the useful materials for reuse and removing the debris within 50m lead''')
    dismantle=cl.Quantity([['concrete 1',1,4.57,0.6],
                           ['concrete 2',1,2.13,0.55]])
    dismantle.rate = 35.4
    dismantle.hArea()
    print(it.items['CC(1:4:8)'])
    concrete= cl.Quantity([['in the foundation 1',1,4.57,0.55,0.1],
                           ['in the foundation 2',1,2.13,0.55,0.1],
                           ['in the sub base of floor',1,7.09,2.43,0.1],
                           ])
    concrete.rate = 3102.92
    concrete.volume()
    print(it.items['bmfp'])
    brick=cl.Quantity([['wall 1',1,4.57,0.25,0.5],
                       ['wall 2',1,2.13,0.25,0.5],
                       ['step out side 1',1,1.5,0.5,0.15],
                       ['step out side 2',1,1.0,0.25,0.15],
                       ['step inside 1',1,1.0,0.43,0.15],
                       ['step inside 2',1,1.0,0.2,0.15],
                       ['altar 1',1,1.8,0.25,0.3],
                       ['altar 2',1,1.2,0.25,0.15],
                       ['altar 3',1,0.65,0.13,0.3],
                       ['altar 4',1,0.5,0.13,0.25],
                       ['altar 5',1,0.6,0.4,0.15],
                       ['altar 6',1,0.6,0.25,0.15],
                       ['altar 7',1,0.6,0.15,0.15]])
    brick.rate=2884.44
    brick.volume()
    print(it.items['sand_fill'])
    sand=cl.Quantity([['in the foundation 1',1,4.57,0.55,0.15],
                      ['in the foundation 2',1,2.13,0.55,0.15],
                      ['in the plinth',1,7.09-0.5,2.43,0.2]])
    sand.rate = 313.52
    sand.volume()
    plaster16=cl.Quantity([['in the plinth',1,28.05,0.45],
                           ['mid portion',4.57,0.3],
                           ['mid portion 2',2.13,0.3]])
    plaster16.rate = 119.57
    plaster16.vArea()
    plaster6=cl.Quantity([['R.C.C. circular pillars',12*mt.pi,0.3,2.5],
                          ['inside mandap beams',4,2.45,0.25+0.2+0.38],
                          ['circular beams bottom slab',2*mt.pi,4.02,0.25+0.15+0.25],
                          ['columns of inside top mandap',4*4,0.25,0.6],
                          ['edges of bottom circular slab',1,28.04,0.12],
                          ['edges of top slab',1,12.75,0.12]])
    plaster6.rate = 93.91
    plaster6.vArea()
    
    
    
    
    
    
    