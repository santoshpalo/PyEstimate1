import ClassLibrary as cl 
import FunctionLibrary as fl 
import items as it







if __name__ == "__main__":
    print('''Name of the work:-Addl. work for construction of 100 seated ST/SC Girls hostel
at Women college at Binka''')
    print('Estimated Cost:-\u20B912,50,000.00, Head of account:-ST/SC Welfare Department Fund')
    print('-'*80)
    print('''Returning filling of excavated materials into the foundation trench
including all T & P and labour charges etc. complete.''')
    print('\nReference page:-1-2 of M.B. No. 559')
    print('\nQuantity :- 296.33 cum @ \u20B968.80/cum = \u20B930,338.00')
    print(it.items['Earth_work_mechanical'])
    print('Excavation of the whole earth at the work site for workability cause.\n')
    excavation = cl.Quantity([['work site for the buildingf',1,55.5,20.00,1.43],
                              ['deduct area not to cut',-1,6.00,5,1.43]])
    excavation.rate=94.4
    excavation.volume()
    print('\nFilling of area around the building\n')
    filling = cl.Quantity([['at the front of the building',1,55.5,16.76,1],
                           ['between existing buildings',1,10.75,10,0.3],
                           ['at the back of the building',1,55,5,2.5],
                           ['at the left of the buyilding',1,6,5,1.25],
                           ['near the private building',1,25,6.55,1]])
    filling.rate=121.9
    filling.volume()
    print('\nOrdinary rolling of earth layer by layer not exceeding 30cm in height\n')
    print('1851.18cum @ \u20B9 383.05 % cum = \u20B97091.00 ')
    print(it.items['subbase'])
    moorum = cl.Quantity([['at the front of the building',1,55.5,16.76,.2],
                           ['between existing buildings',1,10.75,10,0.2],
                           ['at the back of the building',1,55,5,0.2],
                           ['at the left of the buyilding',1,6,5,0.2],
                           ['near the private building',1,25,6.55,.2]])
    moorum.rate=183
    moorum.volume()
    print(it.items['moorumcollection'])
    moorum = cl.Quantity([['at the front of the building',1,55.5,16.76,.2],
                           ['between existing buildings',1,10.75,10,0.2],
                           ['at the back of the building',1,55,5,0.2],
                           ['at the left of the buyilding',1,6,5,0.2],
                           ['near the private building',1,25,6.55,.2]])
    moorum.rate=233.9
    moorum.volume()
    print('''\nTreatment of sub base of flooring using chemical emulsion @ one litre
with chlropyrifos/ Lindane E.C. 20% with 1% concentration / one sqm\n''')
    print('\nArea of 400 sqm @ \u20B91830.62/sqm = 1830.62/ sqm = \u20B97,32,248.00')
    print('\nCess for welfare of labourers = \u20B912,500.00')
    print('Display Board and photograph = \u20B9 1,603.00')
    

