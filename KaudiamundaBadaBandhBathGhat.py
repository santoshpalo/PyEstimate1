import items as it
import ClassLibrary as cl 
import FunctionLibrary as fl
import statistics as st
a=[0.15,.2,.1,.13,.13,.13,.13,.15,.14,.15,.16,.16,.14,.15,.16,.15,.14]


b=[.3,0.5,0.55,0.75,.9,.9,.9,0.93,1.08,1.18,1.3,1.4,1.23,1.35,0.75,.4,.63]
b1 =[i+0.25 for i in b]
b2= [i-.25 for i in b]
c=[18.4166,18.33,18.4166,18.25,18.25,18.25,18.0833,18,18,18,18,18,18.166,18.0833,18.166,18.0833,18.0833]
c = [round(i*.3048,2)-0.9 for i in c]
d= [8,2,2.083,2,2,2,10,2,2,2,2,2,2,2,2.083,2.083,5]
d1=[round(i*.3048,2) for i in d]
d2 = [i+.15 for i in d1]






if __name__ == "__main__":
    print(it.items['efhs'])
    foundationtrench=cl.Quantity([['both side cut-off walls',2,15.81-.45+.6,0.75,0.45],
                                  ['top and bottom cut-off walls',2,4.88,0.75,0.45],
                                  ['middle cut-off walls',1,4.88,0.75,0.45]])
    foundationtrench.rate=103.2
    foundationtrench.volume()
    print(it.items['CC(1:3:6)'])
    pcc=cl.Quantity([['1st step',2,d1[0],0.45,b1[0]],
                      ['2nd step',2,d1[1],0.45,b1[1]],
                      ['3rd step',2,d1[2],0.45,b1[2]],
                      ['4th step',2,d1[3],0.45,b1[3]], 
                      ['5th step',2,d1[4],0.45,b1[4]],
                      ['6th step',2,d1[5],0.45,b1[5]],
                    ['7th step',2,d1[6],0.45,b1[6]],
                    ['8th step',2,d1[7],0.45,b1[7]],
                    ['9th step',2,d1[8],0.45,b1[8]],
                    ['10th step',2,d1[9],0.45,b1[9]],
                    ['11th step',2,d1[10],0.45,b1[10]],
                    ['12th step',2,d1[11],0.45,b1[12]],
                    ['13th step',2,d1[12],0.45,b1[12]],
                    ['14th step',2,d1[13],0.45,b1[13]],
                    ['15th step',2,d1[14],0.45,b1[14]],
                    ['16th step',2,d1[15],0.45,b1[15]],
                    ['17th step',2,d1[16],0.45,b1[16]],
                    ['1st step',1,c[0],d2[0],a[0]],
                      ['2nd step',1,c[1],d2[1],a[1]],
                      ['3rd step',1,c[2],d2[2],a[2]],
                      ['4th step',1,c[3],d2[3],a[3]], 
                      ['5th step',1,c[4],d2[4],a[4]],
                      ['6th step',1,c[5],d2[5],a[5]],
                    ['7th step',1,c[6],d2[6],a[6]],
                    ['8th step',1,c[7],d2[7],a[7]],
                    ['9th step',1,c[8],d2[8],a[8]],
                    ['10th step',1,c[9],d2[9],a[9]],
                    ['11th step',1,c[10],d2[10],a[10]],
                    ['12th step',1,c[11],d2[11],a[12]],
                    ['13th step',1,c[12],d2[12],a[12]],
                    ['14th step',1,c[13],d2[13],a[13]],
                    ['15th step',1,c[14],d2[14],a[14]],
                    ['16th step',1,c[15],d2[15],a[15]],
                    ['17th step',1,c[16],d2[16],a[16]],
                    ['bottom cut-off',1,4.88,0.45,0.45],
                    ['top cut-off',1,4.88,0.45,0.85],
                    ['middle cut-off',1,4.88,0.45,1.03+.45]])
    pcc.rate=3700
    pcc.volume()
    print(it.items['CC(1:2:4)'])
    pcchips=cl.Quantity([['1st step',1,c[0],d2[0],.1],
                      ['2nd step',1,c[1],d2[1],.1],
                      ['3rd step',1,c[2],d2[2],.1],
                      ['4th step',1,c[3],d2[3],.1], 
                      ['5th step',1,c[4],d2[4],.1],
                      ['6th step',1,c[5],d2[5],.1],
                    ['7th step',1,c[6],d2[6],.1],
                    ['8th step',1,c[7],d2[7],.1],
                    ['9th step',1,c[8],d2[8],.1],
                    ['10th step',1,c[9],d2[9],.1],
                    ['11th step',1,c[10],d2[10],.1],
                    ['12th step',1,c[11],d2[11],.1],
                    ['13th step',1,c[12],d2[12],.1],
                    ['14th step',1,c[13],d2[13],.1],
                    ['15th step',1,c[14],d2[14],.1],
                    ['16th step',1,c[15],d2[15],.1],
                    ['17th step',1,c[16],d2[16],.1]])
    pcchips.rate=4800
    pcchips.volume()
    print(it.items['sand_filling'])
    sandfill=cl.Quantity([['1st step',2,c[0],d1[0],b2[0]],
                      ['2nd step',2,c[1],d1[1],b2[1]],
                      ['3rd step',2,c[2],d1[2],b2[2]],
                      ['4th step',2,c[3],d1[3],b2[3]], 
                      ['5th step',2,c[4],d1[4],b2[4]],
                      ['6th step',2,c[5],d1[5],b2[5]],
                    ['7th step',2,c[6],d1[6],b2[6]],
                    ['8th step',2,c[7],d1[7],b2[7]],
                    ['9th step',2,c[8],d1[8],b2[8]],
                    ['10th step',2,c[9],d1[9],b2[9]],
                    ['11th step',2,c[10],d1[10],b2[10]],
                    ['12th step',2,c[11],d1[11],b2[12]],
                    ['13th step',2,c[12],d1[12],b2[12]],
                    ['14th step',2,c[13],d1[13],b2[13]],
                    ['15th step',2,c[14],d1[14],b2[14]],
                    ['16th step',2,c[15],d1[15],b2[15]],
                    ['17th step',2,c[16],d1[16],b2[16]]])
    sandfill.rate=313
    sandfill.volume()
    print(it.items['rscs_walls'])
    print(st.mean(a))
    print (len(a))