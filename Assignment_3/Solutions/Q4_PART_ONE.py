import pandas as pd
loc= "/Users/Sneha/Documents/python/Python_assignments/Assignment_3/Data/movies_awards.csv"
data = pd.read_csv(loc)
var=data[['Title','Awards']].dropna()
var['Awards_won']=0
var['Awards_nominated']=0
var['Prime_Awards_nominated']=0
var['Oscar_Awards_nominated']=0
var['Golden_Globe_nominated']=0
var['BAFTA_nominated']=0
var['Prime_Awards_won']=0
var['Oscar_Awards_won']=0
var['Golden_Globe_won']=0
var['BAFTA_won']=0
global column
#var['val']=var['Awards'].map(lambda x: x.split())
temp_val=0

def win(c):
    global temp_val
    if 'win' in c:
        va=c.split()
        if "win" in va:
            temp_val = int(va[va.index('win')-1])
        if "wins" in va:
            temp_val = int(va[va.index('wins') - 1])
        if "wins." in va:
            temp_val = int(va[va.index('wins.') - 1])
        if "win." in va:
            temp_val = int(va[va.index('win.') - 1])
        return temp_val
    else:
        return 0

def nom(c):
        global temp_val
        if 'nomination' in c:
            va = c.split()
            if "nomination" in va:
                temp_val = int(va[va.index('nomination') - 1])
            if "nominations" in va:
                temp_val = int(va[va.index('nominations') - 1])
            if "nomination." in va:
                temp_val = int(va[va.index('nomination.') - 1])
            if "nominations." in va:
                temp_val = int(va[va.index('nominations.') - 1])
            return temp_val
        else:
            return 0

def won_award(c):
    if "Won" in c and "Golden" in c:
        va = c.split()
        return int(va[1])
    if "Won" in c and "Oscar" in c:
        va = c.split()
        return int(va[1])
    if "Won" in c and "Primetime" in c:
        va = c.split()
        return int(va[1])
    if "Won" in c and "BAFTA" in c:
        va = c.split()
        return int(va[1])
    else:
        return 0

def nom_award(c):
    if "Nominated" in c and "Golden" in c:
        va = c.split()
        return int(va[2])
    if "Nominated" in c and "Oscar" in c:
        va = c.split()
        return int(va[2])
    if "Nominated" in c and "Primetime" in c:
        va = c.split()
        return int(va[2])
    if "Nominated" in c and "BAFTA" in c:
        va = c.split()
        return int(va[2])
    else:
        return 0
var['Awards_won']= var['Awards'].map(win)
var['Awards_nominated']= var['Awards'].map(nom)

var['Golden_Globe_won']=var['Awards'].map(lambda x: won_award(x) if "Golden" in x else 0 )
var['Oscar_Awards_won']=var['Awards'].map(lambda x: won_award(x) if "Oscar" in x else 0)
var['Prime_Awards_won']=var['Awards'].map(lambda x: won_award(x)if "Primetime" in x else 0)
var['BAFTA_won']=var['Awards'].map(lambda x: won_award(x)if "BAFTA" in x else 0)

var['Golden_Globe_nominated']=var['Awards'].map(lambda x: nom_award(x) if "Golden" in x else 0 )
var['Oscar_Awards_nominated']=var['Awards'].map(lambda x: nom_award(x) if "Oscar" in x else 0)
var['Prime_Awards_nominated']=var['Awards'].map(lambda x: nom_award(x)if "Primetime" in x else 0)
var['BAFTA_nominated']=var['Awards'].map(lambda x: nom_award(x)if "BAFTA" in x else 0)

var['Total']= var.sum(axis=1)

print(var.head())

var.to_csv('output_Q4_PART_ONE.csv',index = False)