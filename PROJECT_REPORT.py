import FunctionLibrary as fl
EC = 'Rs.{:.2f}'.format(200000)
ECT = '(Two lakh only)'
NW ='''Construction of C.C. road from Fabsi Harijan Pada Bye-pass road to AWC Building
'''
HA = 'out of G.G.Y. (2016-17) head of account'
text = '''\n\tThe road from Fabsi Harijan Pada Bye-pass road to AWC Building has to be paved with cement concrete (1:2:4) using 12 mm size c.b.g. chips crust over sub-base of C.C.(1:3:6) using 40 mm size c.b.g. metal.To make go of the rain water of the coinciding school area a hume pipe of 2.50m length of NP-2 type and 300mm dia has been provided. Hence the road has been heightened by filling sand in the subgrade in an average height of 0.30m.
  '''
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
    


