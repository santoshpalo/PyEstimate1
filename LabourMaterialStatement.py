# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:25:08 2016

@author: spalo
"""

# import AnalysisRates as ar
# import Estimate_1 as es1
import numpy as np
import LeadStatement1 as ls1
import math as mt
import pandas as pd
pd.set_option('max_colwidth',0)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)
pd.set_option('max_colwidth', 0)

pd.set_option('display.expand_frame_repr', False)
#===============================================================================
# pd.set_option('display.precision', 2)
#===============================================================================
pd.options.display.max_rows = 999

def material_labour(item,q):
    if item == 'bmfp':
        c = ['u/s','masonI','masonII','cement','sand','bricks']
        i = ['brick masonry in F & P']
        d = {'u/s':[2.96*q],'masonI':[0.35*q],'masonII':[1.05*q],'cement':[0.672*q],'sand':[0.28*q],'bricks':[mt.ceil(350*q)]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)

    elif item == 'rcc':
        c = ['u/s','masonII','cement','sand','chips12']
        i = ['R.C.C. (1:1.5:3)']
        d = {'u/s':[4.6*q],'masonII':[0.68*q],'cement':[4.29*q],'sand':[0.45*q],'chips12':[0.9*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)

    elif item == 'cc148':
        c = ['u/s','masonII','cement','sand','metal40']
        i = ['Cement Concrete (1:4:8)']
        d = {'u/s':[3.9*q],'masonII':[0.18*q],'cement':[1.72*q],'sand':[0.48*q],'metal40':[0.96*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)

    elif item == 'rscscolumn':
        c = ['s/s','masonII']
        i = ['Centering of column']
        d = {'s/s':[2.75/4.2*q],'masonII':[2.75/4.2*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)

    elif item == 'rscsplinth':
        c = ['s/s','masonII']
        i = ['Centering of footing']
        d = {'s/s':[0.05*q],'masonII':[0.05*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)

    elif item == 'efhs':
        c = ['u/s']
        i = ['Excavation Foundation']
        d = {'u/s':[0.43*1.2*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == 'hysd':
        c = ['u/s','s/s','masonI','b_wire']
        i = ['Reinforcement works']
        d = {'u/s':[0.8*q],'s/s':[.044*q],'masonI':[0.3*q],'b_wire':[0.8*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}qtl'.format)
    elif item == 'paint':
        c = ['u/s','masonI','paint','primer']
        i = ['Paint and priming']
        d = {'u/s':[1.6/9.3*q],'masonI':[1.75/9.3*q],'paint':[1.25/10*q],'primer':[0.54/10*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'wpcp':
        c = ['u/s','masonI','wpcp']
        i = ['water proofing cement paint']
        d = {'u/s':[.032*q],'masonI':[.022*q],'wpcp':[2.5/10*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == '12cp(1:6)':
        c = ['u/s','masonII','cement','sand']
        i = ['plaster (1:6) 12mm thick']
        d = {'u/s':[.12*q],'masonII':[.14*q],'cement':[.0358*q],'sand':[.015*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == '12cp(1:4)':
        c = ['u/s','masonII','cement','sand']
        i = ['plaster (1:4) 12mm thick']
        d = {'u/s':[.12*q],'masonII':[.14*q],'cement':[.0644*q],'sand':[.015*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'sandfill':
        c = ['u/s','sand(c)']
        i = ['Filling sand']
        d = {'u/s':[.1236*q],'sand(c)':[q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'asf(1:2:4)':
        c = ['u/s','masonI','cement','sand','chips12']
        i = ['A.S. Flooring (1:2:4)']
        d = {'u/s':[.33*q],'masonI':[0.13*q],'cement':[.0858*q],'sand':[0.012*q],'chips12':[0.023*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == '16cp(1:6)':
        c = ['u/s','masonII','cement','sand']
        i = ['plaster (1:6) 16mm thick']
        d = {'u/s':[.24*q],'masonII':[.16*q],'cement':[.043*q],'sand':[.018*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'rcc M-25':
        c = ['u/s','s/s','masonII','cement','sand','chips10','chips20','generator','CCmixer']
        i = ['R.C.C. M-25 grade']
        d = {'u/s':[20.0/15*q],'s/s':[0.86/15*q],'masonII':[.1*q],'cement':[6.05*10/15*q],'sand':[.45*q],'chips10':[5.4/15*q],'chips20':[8.1/15*q],'generator':[0.4*q],'CCmixer':[0.4*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == 'pcc M-20':
        c = ['u/s','s/s','masonII','cement','sand','chips10','chips20','metal40','generator','CCmixer']
        i = ['P.C.C. M-20 grade']
        d = {'u/s':[20.0/15*q],'s/s':[0.86/15*q],'masonII':[.1*q],'cement':[5.16*10/15*q],'sand':[.45*q],'chips10':[1.35/15*q],'chips20':[4.05/15*q],'metal40':[8.1/15*q],'generator':[0.4*q],'CCmixer':[0.4*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == 'rscsslab':
        c = ['s/s','masonII']
        i = ['Centering of slab']
        d = {'s/s':[2.75/9*q],'masonII':[2.75/9*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'rscswalls':
        c = ['s/s','masonII']
        i = ['Centering of walls']
        d = {'s/s':[13.5/23.9*q],'masonII':[13.5/23.9*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == '20cp(1:4)':
        c = ['u/s','masonII','cement','sand']
        i = ['plaster (1:4) 20mm thick']
        d = {'u/s':[.24*q],'masonII':[.16*q],'cement':[.0744*q],'sand':[.021*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'cc136':
        c = ['u/s','masonII','cement','sand','metal40']
        i = ['Cement Concrete (1:3:6)']
        d = {'u/s':[3.9*q],'masonII':[0.18*q],'cement':[2.29*q],'sand':[0.48*q],'metal40':[0.96*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == 'cc124':
        c = ['u/s','masonII','cement','sand','chips12']
        i = ['Cement Concrete (1:2:4)']
        d = {'u/s':[4.6*q],'masonII':[0.68*q],'cement':[3.23*q],'sand':[0.45*q],'chips12':[0.90*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}cum'.format)
    elif item == 'rscslintel':
        c = ['s/s','masonII']
        i = ['Centering of lintel']
        d = {'s/s':[1.25/7.8*q],'masonII':[1.25/7.8*q]}
        table = pd.DataFrame(d,index = i,columns = c)
        table.insert(0,'quantity',q)
        table['quantity']=table['quantity'].map('{:.2f}sqm'.format)
    elif item == '20cp(1:6)':
        c = ['u/s', 'masonII', 'cement', 'sand']
        i = ['plaster (1:6) 20mm thick']
        d = {'u/s': [.24 * q], 'masonII': [.16 * q], 'cement': [.057 * q], 'sand': [.021 * q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}sqm'.format)
    elif item == '6cp(1:4)':
        c = ['u/s', 'masonII', 'cement', 'sand']
        i = ['plaster (1:4) 6mm thick']
        d = {'u/s': [.17 * q], 'masonII': [.14 * q], 'cement': [.0372 * q], 'sand': [.0075 * q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'distemper':
        c = ['u/s', 'masonI', 'distemper']
        i = ['Distemper 2 coats']
        d = {'u/s': [0.062 * q], 'masonI': [0.052* q], 'distemper':[0.25*q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'vitrified':
        c = ['u/s', 'masonI', 'sand','cement','w_cement','v_tile']
        i = ['vitrified tile flooring']
        d = {'u/s': [0.216 * q], 'masonI': [0.216 * q], 'sand': [0.021 * q],'cement':[.1074*q],'w_cement':[.0075*q],'v_tile':[1*q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}sqm'.format)
    elif item == 'ewhs':
        c = ['u/s']
        i = ['Earth work in hard soil']
        d = {'u/s': [0.43* q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    elif item == 'rrhg':
        c = ['u/s', 'masonI', 'masonII', 'cement', 'sand', 'stone']
        i = ['RRHG stone masonry in F & P']
        d = {'u/s': [3.17 * q], 'masonI': [0.35 * q], 'masonII': [1.41 * q], 'cement': [0.8151 * q],
         'sand': [0.34 * q], 'stone': [mt.ceil(1 * q)]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    elif item == 'bmfps':
          c = ['u/s', 'masonI', 'masonII', 'cement', 'sand', 'F.A.bricks']
          i = ['F.A.brick masonry(1:6)']
          d = {'u/s': [2.96 * q], 'masonI': [0.35 * q], 'masonII': [1.05 * q], 'cement': [0.672 * q], 'sand': [0.28 * q],
             'F.A.bricks': [mt.ceil(350 * q)]}
          table = pd.DataFrame(d, index=i, columns=c)
          table.insert(0, 'quantity', q)
          table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    elif item == 'bmfps1':
        c = ['u/s', 'masonI', 'masonII', 'cement', 'sand', 'F.A.bricks']
        i = ['F.A.brick masonry(1:4)']
        d = {'u/s': [2.96 * q], 'masonI': [0.35 * q], 'masonII': [1.05 * q], 'cement': [1.00 * q], 'sand': [0.28 * q],
             'F.A.bricks': [mt.ceil(350 * q)]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    elif item == 'floor_tile':
        c = ['u/s', 'masonI', 'f_tile', 'cement', 'sand']
        i = ['Fixing tiles in floor']
        d = {'u/s': [0.216 * q], 'masonI': [0.216 * q], 'f_tile': [1.0 * q], 'cement': [.2297* q], 'sand': [0.013 * q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    elif item == 'wall_tile':
        c = ['u/s', 'masonI', 'w_tile', 'cement', 'sand']
        i = ['Fixing tiles on walls']
        d = {'u/s': [0.325 * q], 'masonI': [0.325 * q], 'w_tile': [1.0 * q], 'cement': [.1375 * q],
             'sand': [0.015 * q]}
        table = pd.DataFrame(d, index=i, columns=c)
        table.insert(0, 'quantity', q)
        table['quantity'] = table['quantity'].map('{:.2f}cum'.format)
    






















    else :
        pass
    return table
if __name__ == "__main__":
    rate = pd.Series([200,220,240,260,ls1.z['total cost'][4],ls1.z['total cost'][2]-38.4,ls1.z['total cost'][9]-138.3,ls1.z['total cost'][11]-138.3,ls1.z['total cost'][1],75,249,129,35,ls1.z['total cost'][3]-38.4,ls1.z['total cost'][8]-138.3,ls1.z['total cost'][10]-138.3,240,177,66,17.25,665,ls1.z['total cost'][7]-138.3,ls1.z['total cost'][13]-0,429.00,387.00],
                 index=['u/s','s/s','masonII','masonI','cement','sand','chips12','metal40','bricks','b_wire','paint','primer','wpcp','sand(c)','chips10','chips20','generator','CCmixer','distemper','w_cement','v_tile','stone','F.A.bricks','f_tile','w_tile'])

    a = material_labour('bmfp',0)
    b = material_labour('rcc',0)
    c = material_labour('cc148',0)
    d = material_labour('rscscolumn',0)
    e = material_labour('rscsplinth',34.88+37.42)
    f = material_labour('efhs',13.76+15.81)
    g = material_labour('hysd',0)
    h = material_labour('paint',0)
    i = material_labour('wpcp',0)
    j = material_labour('12cp(1:6)',13.67+14.9)
    k = material_labour('sandfill',48.76+42.03)
    l = material_labour('asf(1:2:4)',0)
    m = material_labour('16cp(1:6)',0)
    n = material_labour('rcc M-25',0)
    o = material_labour('rscsslab',0)
    p = material_labour('rscswalls',44.96+34.88)
    q = material_labour('20cp(1:4)',0)
    r = material_labour('cc136',33.67+21.76)
    s = material_labour('cc124',7.01+9.96)
    t = material_labour('rscslintel',0)
    u = material_labour('20cp(1:6)',0)
    v = material_labour('6cp(1:4)',0)
    w = material_labour('distemper',0)
    x = material_labour('vitrified',0)
    y = material_labour('ewhs',105+126)
    a1 = material_labour('rrhg',0)
    a2 = material_labour('bmfps',0)
    a3 = material_labour('bmfps1',0)
    a4 = material_labour('floor_tile',0)
    a5 =material_labour('wall_tile',0)
    a6 = material_labour('12cp(1:4)',0)
    a7=material_labour('pcc M-20', 0)
    z =a.append(b).append(c).append(d).append(e).append(f).append(g).append(h).append(i).append(j).append(k).append(l).\
        append(m).append(n).append(o).append(p).append(q).append(r).append(s).append(t).append(u).append(v).append(w).\
        append(x).append(y).append(a1).append(a2).append(a3).append(a4).append(a5).append(a6).append(a7)

    z = z[['quantity','u/s','s/s','masonII','masonI','cement','sand','chips12','metal40','bricks','b_wire',
           'paint','primer','wpcp','sand(c)','chips10','chips20','generator','CCmixer','distemper','w_cement',
           'v_tile','stone','F.A.bricks','f_tile','w_tile']]

    result = z.sum(axis=0,numeric_only = True)
    #z1= result.iloc[1:10]
    table1 = pd.DataFrame(dict(quantity = result, rate = rate))
    table1['total']=table1['quantity']*table1['rate']
    total_cost=table1['total'].sum().round()
    table1['rate']=table1['rate'].map('Rs.{:.2f}'.format)
    table1['total']=table1['total'].map('Rs.{:.2f}'.format)
    #===========================================================================
    # ram = z.drop(z['quantity'] != 0)
    #===========================================================================
    #===========================================================================
    # z = z.drop(['bricks','paint','primer','wpcp','chips12','distemper','w_cement','vitrified tile','f_tile','w_tile','stone'],axis=1)
    # table1=table1.drop(table1['quantity']== 0)
    #===========================================================================


    print (table1[table1['quantity']!=0],'\n',z[z['u/s']!=0].dropna(axis=1,how='all'),'\n','The total cost =','Rs.{:.2f}'.format(total_cost))
    
    
    
    
    