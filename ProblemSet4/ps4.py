# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def run_delayed(delay,vir_num,maxPOP,maxBirthProb,clearProb, resistances,hist,descript):
        viruses = []
        for i in range(vir_num):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, 0.005))
        patients = []
        populationOverTime = []
        populationResToGuttagonolOverTime = []
        for trial in range(numTrials):
            patients.append(TreatedPatient(viruses, maxPOP))
            populationOverTime.append([])
            populationResToGuttagonolOverTime.append([])
            for timeStep in range(delay):
                patients[trial].update()
                populationOverTime[trial].append(patients[trial].getTotalPop())
                populationResToGuttagonolOverTime[trial].append(patients[trial].getResistPop(['guttagonol']))
            patients[trial].addPrescription('guttagonol')
            for timeStep in range(delay,delay+150):
                patients[trial].update()
                populationOverTime[trial].append(patients[trial].getTotalPop())
                populationResToGuttagonolOverTime[trial].append(patients[trial].getResistPop(['guttagonol']))
        populationEnd = []
        for trial in range(numTrials):
            populationEnd.append(populationOverTime[trial][delay+149])
        pylab.subplot(2,3,hist)
        #pylab.plot(range(delay+150), populationOverTime_mean)
        #pylab.plot(range(delay+150), populationResToGuttagonolOverTime_mean)
        pylab.hist(populationEnd, 20)
        pylab.xlabel('Viruses at the last day')
        pylab.ylabel('Cases')
        pylab.title(descript)
        #pylab.legend([descript])
    
    
    from multiprocessing import Process
    p1 = Process(target = run_delayed(150,100,1000,0.1,0.05,{'guttagonol': False},1,'Normal'))
    p1.start()
    p2 = Process(target = run_delayed(150,200,1000,0.1,0.05,{'guttagonol': False},2,'Init VIR doubled'))
    p2.start()
    p3 = Process(target = run_delayed(150,100,2000,0.1,0.05,{'guttagonol': False},3,'maxPop doubled'))
    p3.start()
    p4 = Process(target = run_delayed(150,100,1000,0.2,0.05,{'guttagonol': False},4,'maxBrith doubled'))
    p4.start()
    p4 = Process(target = run_delayed(150,100,1000,0.1,0.1,{'guttagonol': False},5,'clearPob doubled'))
    p4.start()
    p4 = Process(target = run_delayed(150,100,1000,0.1,0.05,{'guttagonol': True},6,'Resistance Enabled'))
    p4.start()
    pylab.show()

#simulationDelayedTreatment(500)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def run_delayed(delay,vir_num,maxPOP,maxBirthProb,clearProb, resistances,hist,descript):
        viruses = []
        for i in range(vir_num):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, 0.005))
        patients = []
        populationOverTime = []
        populationResToGuttagonolOverTime = []
        for trial in range(numTrials):
            patients.append(TreatedPatient(viruses, maxPOP))
            populationOverTime.append([])
            populationResToGuttagonolOverTime.append([])
            for timeStep in range(150):
                patients[trial].update()
                populationOverTime[trial].append(patients[trial].getTotalPop())
            patients[trial].addPrescription('guttagonol')
            for timeStep in range(150,delay+150):
                patients[trial].update()
                populationOverTime[trial].append(patients[trial].getTotalPop())
            patients[trial].addPrescription('grimpex')
            for timeStep in range(delay+150,delay+300):
                patients[trial].update()
                populationOverTime[trial].append(patients[trial].getTotalPop())
        populationEnd = []
        for trial in range(numTrials):
            populationEnd.append(populationOverTime[trial][delay+299])
        pylab.subplot(2,2,hist)
        pylab.hist(populationEnd, 20)
        pylab.xlabel('Viruses at the last day')
        pylab.ylabel('Cases')
        pylab.title(descript)
        #pylab.legend([descript])
    
    
    from multiprocessing import Process
    p1 = Process(target = run_delayed(300,100,1000,0.1,0.05,{'guttagonol': False, 'grimpex': False},1,'300'))
    p1.start()
    p2 = Process(target = run_delayed(150,100,1000,0.1,0.05,{'guttagonol': False, 'grimpex': False},2,'150'))
    p2.start()
    p3 = Process(target = run_delayed(75,100,1000,0.1,0.05,{'guttagonol': False, 'grimpex': False},3,'75'))
    p3.start()
    p4 = Process(target = run_delayed(0,100,1000,0.1,0.05,{'guttagonol': False, 'grimpex': False},4,'0'))
    p4.start()
    pylab.show()


simulationTwoDrugsDelayedTreatment(1000)
