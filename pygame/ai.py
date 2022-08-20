from gameTest import Creature

def StateToNae(creatures):

    clauses = {ii+kk : [] for ii in ['a','b','c'] for kk in ['True','False']}

    for creature in creatures:
        for gene in ['a', 'b', 'c']:
            if creature.genes[gene] != None:
                clauses[gene+(str(creature.genes[gene]))] += [creature]

    print(clauses)


def NaeToNae3(clause):
    k = len(clause)
    if k == 1:
        return ()
    if k == 2:
        return ()
    
def Nae3ToGraph():
    pass

def GraphToHamiltonian():
    pass

