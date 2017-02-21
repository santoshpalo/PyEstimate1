import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it










if __name__ == "__main__":
    print(it.items['rcc'])
    rcc=cl.Quantity([['slab',1,8.05,4.35,0.1],
                     ['beam',1,3.5,0.25,0.25],
                     ['roof bend',1,6.5*2+3.5*2,0.25,0.15]])
    rcc.rate=5068.16
    rcc.volume()
    print(it.items['20cp(1:4)'])
    grading=cl.Quantity([['slab top',1,8.05,4.35]])
    grading.rate=120.64
    grading.hArea()
    print(it.items['rscs_slab'])
    slab=cl.Quantity([['slab area',1,8.05,4.35],
                      ['deduct beam',-1,3.5,0.25],
                      ['deduct roof bend',1,20,0.05]])
    slab.rate=261.08
    slab.hArea()
    print(it.items['rscs_beam'])
    beam = cl.Quantity([['beam',1,3.5,0.75]])
    beam.rate=383.34
    beam.vArea()
    print(it.items['CC(1:4:8)'])
    pcc=cl.Quantity([['sub base of floor',1,6.00-.13,3.5-.13,0.1]])
    pcc.rate=2665.96
    pcc.volume()
    print(it.items['hysd'])
    reinforcement=cl.Quantity([['beam main bar',5,4.00-.08,0.89],
                               ['extra end top in beam',2,1.4,0.89],
                               ['stirrups in beams',25,1.07,.395],
                               ['roof bend long',2*4,6.5-.08,.62],
                               ['roof bend short',2*4,4-.08,.62],
                               ['roof bend stirrups',133,0.87,0.395],
                               ['panel 1 bottom 1',7,3.68,.395],
                               ['panel 1 bottom 2 ',7,4.23,.395],
                               ['panel 2 bottom 1',7,2.875+.5+.2+1.32,.395],
                               ['panel 2 bottom 2',7,2.875+.5+.75+.45,.395],
                               ['panel 1 and 2 top',22,4.2,.395],
                               ['extra top bars in verandah',7,1.32+.25+.75,.62],
                               ['peripherial distribution 1',4,8.05-.08,0.395],
                               ['peripheraial distribution 2',4,4.35-.08,0.395],
                               ['verandah distribution',14,4.28,.395],
                               ['panel1 and 2 long span distribution',30,4.38,.395],
                               ['panel1 and panel2 short span distribution',12,8.05-.08,0.395],
                               ['extra on walls',22,0.9,0.395],
                               ['extra on walls top 2',7,.8,0.395]])
    print(reinforcement.reinforcement()['y0'],'{:.2f}kg'.format(reinforcement.reinforcement()['y1']))
    
    
    
    
    
    
    
