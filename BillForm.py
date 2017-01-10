import pandas as pd
pd.set_option('max_colwidth', 0)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)


d = {'efhs':'Excavation of foundation in h/s',
     'ewhs':'Earth work in hard soil',
     'cc(1:4:8)':'C.C. (1:4:8) using 40mm h.g. metal',
     'cc(1:3:6)':'C.C. (1:3:6) using 40mm h.g. metal',
     'cc(1:2:4)':'C.C. (1:2:4) using 12mm h.g. chips',
     'rcc':'R.C.C. (1:1.5:3) using 12mm h.g. chips',
     
     'm20':'R.C.C. m-20 grade concrete ',
     '20cp':'20mm thick grading plaster c.m.(1:4)',
     '12cp':'12mm thick plaster with c.m. (1:6)',
     '16cp':'16mm thick plaster with c.m. (1:6)',
     '6cp':'6mm thick plaster with c.m. (1:4)',
     'vTile':'Vitrified tile floor white cement fill',
     'wTile':'Ceramic glazed wall tile fixing',
     'wpcp':'Finishing water proofing cement paint',
     'slab':'Rigid/smooth centering shuttering slab',
     'beam':'Rigid/smooth centering shuttering beam',
     'plinth':'Rigidsmooth centeringshuttering plint',
     'lintel':'Rigidsmooth centeringshuttering lintel',
     'wall':'Rigidsmooth centeringshuttering wall',
     'hysd':'HYSD bar Reinforcement works in R.C.C.',
     'w_tile':'Cost of ceramic glazed wall tiles',
     'cess':'Cess for welfare of labourers',
     'contingency':'Work contingency',
     'display':'Cost of Display Board and photograph',
     'fill_sand':'Filling sand, watering & ramming',
     'vibrator':'Hire & Running of [late vibrator',
     'bmfp':'F.A. Brick masonry in c.m.(1:6) in F&P',
     'bmss':'F.A. Brick masonry in c.m.(1:6) in S/S',
     'msdoor':'Supplying and fixing of M.S. doors and windows',
     'paint':'Painting 2 coats over a coat of priming'
     
     
               }
d1= {'us':'differential cost of u/s labour',
     'ss':'differential cost of s/s labour',
     's':'differential cost of mason II',
     'hs':'differential cost of mason I',
     'cement':'differential cost of cement',
     'sand':'differential cost of fine sand',
     'chips12':'differential cost of 12mm cbg chips',
     'metal40':'differential cost of 40mm hgb metal',
     'sandf':'differential cost of filling sand'}
class BillForm():
    def __init__(self,data,columns = ['Quantity','ITEM OF WORK OR SUPPLIES','Unit','Rate']):
        self.data = data
        self.columns = columns
    def body(self):
        table = pd.DataFrame(self.data,columns = self.columns, index = range(1,len(self.data)+1,1))
        A=round(table['Quantity']*table['Rate'])
        table.insert(4, 'Amount',A)
        tamount = table['Amount'].sum()
        table['Rate']=table['Rate'].map('\u20B9{:.2f}'.format)
        table['Amount']=table['Amount'].map('\u20B9{:.2f}'.format)
        print(table,'\n\t\t\t\t\t\t','Total amount = ','\u20B9{:.2f}'.format(tamount))
class deduction():
    def __init__ (self,data,columns=['description','realisation']):
        self.data = data
        self.columns = columns
    def deduct(self):
        table = pd.DataFrame(self.data,columns = self.columns,index = range(1,len(self.data)+1,1))
        t_deduction = table['realisation'].sum()
        table['realisation']=table['realisation'].map('\u20B9{:.2f}'.format)
        
        print(table,'\n\t\t\t\t\t','Total deduction = ','\u20B9{:.2f}'.format(t_deduction))







if __name__ == "__main__":
    print('\t\t\t\t\t\tSee Rule 109')
    print('Comp. Voucher No.\tRUNNING ACCOUNT BILL\t Voucher No.')
    print('Date___________\t\t\t\t\t\tDate_______')
    print('\tTo be used for payment for work (Supplies actually measured)')
    print('-'*80)
    print('Case Record No/Year:-244(2016-17)')
    print('''Name of work:-Restoration and renovation of Bhagabatgudi, Kaudiamunda
''')
    print('Head of Account:-M.L.A.L.A.D.(2013-14)')
    print('Estimated Cost:-\u20B93,00,000.00')
    print('Serial number of this bill:-2nd F / A bill')
    print('Date of commencement of the work:-______________\tM.B. No. :-569')
    print('Date of completion of the work:-________________\tPage No. :-(104-111)')
    print('Name of the executant/V.L.L.:-Departmental\n')
    print('\t\tACCOUNT OF WORK DONE OR SUPPLY MADE')
    print('-'*80)
    bill = BillForm([[25.81,d['12cp'],'sqm',84.9],
                     [23.06,d['16cp'],'sqm',119.19],
                     [1.15,d['cc(1:4:8)'],'cum',3052.46],
                     [33.03,d['vTile'],'sqm',839.55],
                     
                     [8.69,d['w_tile'],'sqm',252.21],
                     
                     
                     [8.69,'cost and conv. of glazed wall tiles','sqm',387],
                     
                     
                    [1.5,d['msdoor'],'cum',6300],
                    [1,'conveyance of doors and windows','',500],
                    [24.5,d['paint'],'sqm',83.33],
                    [194.5,d['wpcp'],'kg',12.72],
                    [3.06,'Cost of paint','l',193],
                    [1.32,'Red oxide primer','kg',116],
                    [48.63,'w.p.c.p. compound','kg',35],
                    [1,'labour charges for fixing doors','',1000],
                    
                     [1,d['cess'],'',550],
                     [1,d['contingency'],'',550],
                       #========================================================
                       # [1,d['display'],'no',1500],
                       #========================================================
                       #========================================================
                       # [35.44,'diff cost of c.b.g & h.b.g metal','cum',238]
                       #========================================================
                     
                     ] )            
                    
                    
                    #===========================================================
                    # [33.21,d1['us'],'no',50],
                    # [12.42,d1['ss'],'no',50],
                    # [15.64,d1['s'],'no',50],
                    # [1.1,d1['hs'],'no',55],
                    # [22.74,d1['cement'],'qtl',622-658],
                    # [3.1,d1['sand'],'cum',33.4],
                    # [3.91,d1['chips12'],'cum',184.4],
                    # [2.28,d1['metal40'],'cum',120.4],
                    # [8.3,d1['sandf'],'cum',32.4],
                    #===========================================================
                    
                    
                    
                    #===========================================================
                    # [4.18,'cost of HYSD bar','qnt',4000],
                    #===========================================================
                    
                    #===========================================================
                    # [1,d['cess'],'',380],
                    #===========================================================
                    #===========================================================
                    # [1,d['contingency'],'',655],
                    #===========================================================
                    
                    
    bill.body()
    print('\t\t\t\tAdd amount of 1st R / A bill = \u20B945,002.00')
    print('\t\t\t\t\t\tTotal Amount = \u20B91,05,749.00')
    print('\t\t\t\tTotal Amount limited to = \u20B91,00,000.00')
    print('\t\t\tDeduct amount of 1st R / A bill = (-)\u20B945,002.00')
    print('\t\t\t\tAmount of 2nd R / A bill = \u20B954998.00')
    #===========================================================================
    # print('\t\t\t\tDeduct less amount @ .02 % = \u20B9223.00')
    # print('\t\t\t\tGross payable amount =\u20B911,17,160.00    ')
    #===========================================================================
    x = deduction([['E.G.B.',0],
                   ['VAT',0],
                   ['Royalty',0],
                   ['Cess',550],
                   ['W.C.',550],
                   ['Income Tax',0]])
    x.deduct()
    print('-'*80)
    print('''\tThe full name of the work as given in the estimate should
be entered here expent in the case of bill for stock materials. The purpose
of supply applicable to case should be filled in and the last scored out.
Not required in the case of work done or supplies made under a piece work
agreement. If the outlay on the work is recorded by subheads the total for
each sub heads should be shown in column 5 and against this total there
should be an entry in column 6 also in on other case should any entries
be made in column 6''')
    print('\t\t\tCERTIFICATE AND SIGNATURE')
    print('\t\t\t','-'*24)
    print('''The measurements were made by me on _______ and are recorded at pages(______) of
the measurement book no.___ . No advance payment has been made previously with
measurement the work has been done with due deligence in approved specification.''')
    print('\n\n\n\tExecutant\tAssistant Engineer\tJunior Engineer\n')
    print('\t\t\tMEMORANDUM OF PAYMENT')
    print('\t\t\t','-'*20)
    print('1. Total value of work done.........................')
    print('2. DEDUCTION')
    print('\t a. Advance.......................................')
    print('\t b. Amount paid in the R/A........................')
    print('3. Balance..........................................')
    print('4. REALISATION')
    x.deduct()
    print('\t\t\t\t\t\tNet Payable \u20B9')
    print('-'*80)
    print('''Passed for payment of \u20B9...........(Rupees...........................) only ''')
    print('''Realise a sum of \u20B9........... (Rupees..................................)only
as detailed above.''')
    print('Net Payable: \u20B9..........(Rupees....................................... )only')
    print('Countersigned\n\n')
    print('Chairman\t\t\t\tBlock Development Officer')
    print('''Received \u20B9........(Rupees...........\tPaid \u20B9 vide cheque no..........''')
    print('\t\t\t\t\tDated............A/C No............')
    print('\t\t\t\t\t& Realised\u20B9..............vide MR No.....')
    print('\t\t\t\t\tDated......... Total \u20B9..........')
    print('Recipient')
    print('\n\n\t\t\t\t\tBlock Development Officer')
    
    
    
    
    
    
    
    
    
    
    