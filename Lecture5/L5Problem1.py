import random

def noReplacementSimulation(numTrials):
    same_balls = 0
    for i in range(numTrials):
        balls = ['red', 'red', 'red', 'green', 'green', 'green']
        for i in range(3):
            taken_ball =  random.choice(balls)
            balls.remove(taken_ball)
        if 'red' not in balls or 'green' not in balls:
            same_balls += 1
    print same_balls/float(numTrials)

for i in range(5):
    noReplacementSimulation(1000)
