
def toList(NestedTuple):
    return list(map(toList, NestedTuple)) if isinstance(NestedTuple, (list, tuple)) else NestedTuple

def Init():
    global minSpeed
    global vehTypesEquipped
    global vehsAttributes
    global vehsAttNames
    global vehTypesSpeial 
    minSpeed = CurrentScript.AttValue('minSpeed')

    vehsAttributes = []
    vehsAttNames = []
    vehTypesAttributes = Vissim.Net.VehicleTypes.GetMultipleAttributes(['No', 'ReceiveSignalInformation','isSpecial'])
    vehTypesEquipped = [x[0] for x in vehTypesAttributes if x[1]]
    vehTypesSpeial = [x[0] for x in vehTypesAttributes if x[2]]

def GetVissimDataVehicles():

    global vehsAttributes
    global vehsAttNames
    vehsAttributesNames = ['No', 'VehType\\No', 'Lane\\Link\\No', 'DesSpeed', 'OrgDesSpeed', 'DistanceToSigHead', 'SpeedMaxForGreenStart', 'SpeedMinForGreenEnd', 'Speed', 'Pos', 'Lane\Link']
    vehsAttributes = toList(Vissim.Net.Vehicles.GetMultipleAttributes(vehsAttributesNames))


    vehsAttNames = {}
    cnt = 0
    for att in vehsAttributesNames:
        vehsAttNames.update({att: cnt})
        cnt += 1


def factorial(f):
    if f == 0:
        return 1
    else:
        return f * factorial(f-1)

def comert(l):
    from math import e
    proportion_of_CAVs=0.25
    arrival=600
    sum1 = 0

    ttt=5
    k=l
    while k <= 90:
        f1 = (pow((1 - proportion_of_CAVs),k)) * ( pow(arrival/60,k) * pow(e,-(arrival/60)) / factorial(k))
        sum1 = sum1 + f1
        k = k + 1

    n = l
    sum2 = 0
    while n <= 90:
        sum2 = sum2 + n * (pow((1 - proportion_of_CAVs),n)) * ( pow(arrival/60,n) * pow(e,-(arrival/60)) / factorial(n)) / sum1
        n = n + 1
    return round(sum2+pow(e,ttt*(arrival/3600)))+1

def PRRP():
    sss=0.7

    maxgreen=35

    mingreen=5
    
    SimSec = Vissim.Net.Simulation.SimulationSecond
    if SimSec <=1:

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('ContrByCOM',True)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')



        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenTimeDuration',7)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',7)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',7)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenTimeDuration',7)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',2)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',11)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',20)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',29)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd',9)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd',18)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd',27)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd',36)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('MaxDist',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('MaxDist',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('MaxDist',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('MaxDist',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('Lspecial',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('Lspecial',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('Lspecial',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('Lspecial',False)
        Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', False)









    GetVissimDataVehicles()



    
    Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Cycduration', round(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration') ))
    Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('SimSecs',Vissim.Net.Simulation.SimulationSecond)
    for vehAttributes in vehsAttributes:
        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
            if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                Link = vehAttributes[vehsAttNames['Lane\Link']]
                if Link =='1' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')!= 'GREEN' or Link =='7' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')!= 'GREEN' or Link =='5' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')!= 'GREEN' or Link =='3' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')!= 'GREEN':                    
                    Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', True)






    if Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('Basedspecial')!=True:        
        for vehAttributes in vehsAttributes:
            if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                if float(vehAttributes[vehsAttNames['Speed']]) < 2:
                    Link = vehAttributes[vehsAttNames['Lane\Link']]
                    if Link =='1':
                        if vehAttributes[vehsAttNames['DistanceToSigHead']] > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('MaxDist'):
                             Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('MaxDist', round(vehAttributes[vehsAttNames['DistanceToSigHead']]/3))
                        
                    if Link =='7':
                        if vehAttributes[vehsAttNames['DistanceToSigHead']] > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('MaxDist'):
                             Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('MaxDist', round(vehAttributes[vehsAttNames['DistanceToSigHead']]/3))


                    if Link =='5':
                        if vehAttributes[vehsAttNames['DistanceToSigHead']] > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('MaxDist'):
                             Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('MaxDist', round(vehAttributes[vehsAttNames['DistanceToSigHead']]/3))


                    if Link =='3':
                        if vehAttributes[vehsAttNames['DistanceToSigHead']] > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('MaxDist'):
                             Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('MaxDist', round(vehAttributes[vehsAttNames['DistanceToSigHead']]/3))
            continue



        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('MaxDist'))/sss)+1, maxgreen))

        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('MaxDist'))/sss)+1, maxgreen))

        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('MaxDist'))/sss)+1, maxgreen))

        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('MaxDist'))/sss)+1, maxgreen))


        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))


        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))



        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))




        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))                       


        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
      


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')



            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='5':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),25)+1))                                     
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('Lspecial',True)

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('MaxDist',0)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('Lspecial',False)







        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')             


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='7':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),25)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('Lspecial',True)


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('MaxDist',0)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('Lspecial',False)



        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED') 

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='1':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),25)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('Lspecial',True)


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('MaxDist',0)

                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('Lspecial',False)

        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='3':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),25)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('Lspecial',True)

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+2:    
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('MaxDist',0)

                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('Lspecial',False)








    if Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('Basedspecial')==True:        

        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenTimeDuration',mingreen)

        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',mingreen)
            
        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',mingreen)
            
        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('Lspecial')!=True:
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenTimeDuration',mingreen)



        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))


        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))



        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))




        if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenEnd', max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenTimeDuration')))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',max(SimSec,Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd'))+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenTimeDuration'))
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+3)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenTimeDuration'))                       


        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
      


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')



            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='5':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),15)+1))                                    
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('Lspecial',True)

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+2:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('MaxDist',0)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('Lspecial',False)


                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] not in vehTypesSpeial  or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']]=='1' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='7' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='5' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='3' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
                            Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', False)







        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')             


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='7':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),15)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('Lspecial',True)


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')+2:                 
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('MaxDist',0)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('Lspecial',False)

                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] not in vehTypesSpeial  or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']]=='1' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='7' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='5' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='3' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
                            Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', False)







        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED') 

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='1':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),15)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('Lspecial',True)


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('GreenEnd')+2:             
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('MaxDist',0)

                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('Lspecial',False)

                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] not in vehTypesSpeial  or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']]=='1' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='7' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='5' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='3' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
                            Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', False)





        if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenStart')-1:
            if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-1:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','GREEN')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')


        if  Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState') == 'GREEN':
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')


            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-3:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-2:
                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial:
                            Link = vehAttributes[vehsAttNames['Lane\Link']]
                            if Link =='3':
                                if float(vehAttributes[vehsAttNames['DistanceToSigHead']])>0:
                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('GreenTimeDuration',min(round(comert(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('MaxDist'))/sss)+1, maxgreen)+ round(float(vehAttributes[vehsAttNames['DistanceToSigHead']])*3.6/max(float(vehAttributes[vehsAttNames['Speed']]),15)+1))                                    

                                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('Lspecial',True)

            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')-1:
                if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('GreenEnd')+2:    
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('SigState','RED')
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('MaxDist',0)

                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).SetAttValue ('Lspecial',False)

                    for vehAttributes in vehsAttributes:
                        if vehAttributes[vehsAttNames['VehType\No']] not in vehTypesSpeial  or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']]=='1' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(9).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='7' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='5' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('SigState')== 'GREEN' or   vehAttributes[vehsAttNames['VehType\No']] in vehTypesSpeial and   vehAttributes[vehsAttNames['Lane\Link']] =='3' and Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(12).AttValue ('SigState')== 'GREEN':
                            Vissim.Net.SignalControllers.ItemByKey(1).SetAttValue ('Basedspecial', False)



















