import FunctionLibrary as fl
EC = 'Rs.{:.2f}'.format(400000)
ECT = '(Four lakh only)'
NW ='''Construction of C.C. Bath Ghat including changing room at BADABANDHA of KAUDIAMUNDA
'''
HA = 'out of 14 th C.F.C. (2016-17) head of account'
text = '''\n\tThis Estimate consists of two nos bath ghats with C.C.(1:3:6) metal concrete and C.C.(1:2:4) chips concrete wearing coat on the treads of the steps. The tank is full of water . It is to be dewatered by using a 10 HP diesel driven PUMP. The bed is filled up with slushy soil which is to be removed by manual labour
  '''
middle = '''\n\tThis estimate has been prepared based on Analysis of Rates 2006. Schedule of Rates - 2014 has been taken into Account.Prevailing Labour rateshave been taken into account at framing of the estimate.'''
conclusion = '''\n\tAll works will be executed as per guidance of engineer-in-charge.'''











if __name__ == "__main__":
    

    print('\n\tThis estimate amounting to',EC+ECT,'has been framed to meet the probable expenditure towards',NW+HA+text)


    print(middle)
    print(conclusion)
    print(fl.signature(0,'',0,''))
    


