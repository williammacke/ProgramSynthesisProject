import numpy as np
from copy import deepcopy
from src.grammars.grammar import Gramamr

def combine_non_terminals(nt1, nt2):
    assert nt1.id == nt2.id
    expressions = set()
    e_ids = set()
    for e in nt1._expressions:
        expressions.add(deepcopy(e))
        e_ids.add(e.id)
    for e in nt2._expressions:
        if e.id in e_ids:
            continue
        expressions.add(deepcopy(e))
        e_ids.add(e.id)
    return NonTerminal(expressions, nt1.id)



def combine_members(m1, m2, env):
    g1 = m1._grammar
    g2 = m2._grammar
    g1_nt_ids = set(nt.id for nt g1._non_terminals)
    g2_nt_ids = {nt.id:nt for nt in g2._non_terminals}
    non_terminals = set()
    start = combine_non_terminals(g1._start, g2._start)
    for nt in g1._non_terminals:
        if nt == g1._start: continue
        if nt.id in g2_nt_ids:
            non_terminals.add(combine_non_terminals(nt, g2_nt_ids[nt.id]))
        else:
            if np.random.random() < 0.5:
                non_terminals.add(deepcopy(nt))
    for i in g2_nt_ids:
        if i in g1_nt_ids: 
            continue
        if np.random.random() < 0.5:
            non_terminals.add(deepcopy(g2_nt_ids[i]))
    grammar = Grammar(start, env, non_terminals)
    return Member(grammar, env)



def evolve_one_gen(population, env, expression_mutation=0.1, non_terminal_mutation=0.1):
    fit = np.array([p._fit for p in population])
    prob = np.exp(fit)
    prob /= np.sum(prob)
    npop = []
    while len(npop) < len(population):
        m1 = np.random.choice(population, p=prob)
        m2 = np.random.choice(population, p=prob)
        npop.append(combine_members(m1, m2, env)
    return npop



