import ClassLibrary as cl 
import FunctionLibrary as fl
import items as it
l=615






if __name__ == "__main__":
    print('Name of the Woprk:- Grade I metalling of the road from Bhikabahali to Sakma')
    print('Estimated Cost:-\u20B94,00,000.00\tHead of Account:- Biju K.B.K.(2014-15)')
    print('-'*80)
    print(it.items['subbase'])
    subbasemoorum = cl.Quantity([['sub-base of the road',1,l,3.65,0.1]])
    subbasemoorum.rate = 183.06
    subbasemoorum.volume()
    print(it.items['gradeI'])
    gradeImetalling = cl.Quantity([['GradeI metalling',1,l,3.65,0.1]])
    gradeImetalling.rate =347.26
    gradeImetalling.volume()
    print(it.items['moorumcollection'])
    subbasemoorum = cl.Quantity([['sub-base of the road',1,l,3.65,0.1],
                                 ['for filling of tnterstices in metalling',0.25,l,3.65,0.1]])
    subbasemoorum.rate = 233.9
    subbasemoorum.volume()
    print(it.items['metalcollection'])
    gradeImetalling = cl.Quantity([['GradeI metalling',1,l,3.65,0.1]])
    gradeImetalling.rate =936.3
    gradeImetalling.volume()
    
    print('Cess for welfare of labourers = \u20B94,000.00')
    #-------------------------------- print('Work contingency= \u20B9 4,000.00')
    print('Display Board and photograph = \u20B91,500.00')
    
    print('-'*80)
    fl.signature(400000, 'Four lakh only', 2, '')