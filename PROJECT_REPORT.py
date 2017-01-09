import FunctionLibrary as fl
EC = 'Rs.{:.2f}'.format(300000)
ECT = '(Three lakh only)'
NW ='''Construction opf C.C. road inside Baunsuni Weekly market, Baunsuni
'''
HA = 'out of G.G.Y.(2016-17) head of account'
text = '''\n\tThis road has to serve a pavement inside market area for allpurposes
and all seasons road. For cambering and filling up the pot holes the subgrade is
to be filled up  with sand well watered and rammed, The cut-off walls and sub-
base are to be constructed with C.C.(1:3:6) using 40mm c.b.g. metal. The crust
of the road is to be constructed with C.C.(1:2:4) using 12 mm c.b.g. chips'''
middle = '''\n\tThis estimate has been prepared based on Analysis of Rates 2006.
Schedule of Rates - 2014 has been taken into Account.Prevailing Labour rates
have been taken into account at framing of the estimate.'''
conclusion = '''\n\tAll works will be executed as per guidance of engineer-in-charge.'''











if __name__ == "__main__":
    

    print('\n\tThis estimate amounting to',EC,ECT)
    print('has been framed to meet the probable expenditure towards')
    print(NW,HA)
    print (text)
    print(middle)
    print(conclusion)
    print(fl.signature(0,'',0,''))
    print('bcde')


