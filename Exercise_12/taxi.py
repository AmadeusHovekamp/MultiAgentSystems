from math import *
from itertools import *
def subsets(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)))
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
def partitions(iterable):
    s = list(iterable)
    return [[[s[0]] + list(t)] + p for t in powerset(s[1:]) for p in partitions(set(s[1:]) - set(t))] if s else [[]]


N = ['A', 'B', 'C', 'D']
graph = {
    'Start':[('A', 9), ('B', 10), ('D', 12)],
    'A':    [('Start', 9), ('B', 8), ('C', 7), ('D', 11)],
    'B':    [('Start', 10), ('A', 8), ('C', 13)],
    'C':    [('A', 7), ('B', 13), ('D', 14)],
    'D':    [('Start', 12), ('A', 11), ('C', 14)]
}

def dist(G, s, wp, vis=set()):
    # brute force
    return min((c + dist(G, w, set(wp) - set([w]), vis | set([w])) for w, c in G[s] if w not in vis), default=inf) if wp else 0

def v(S):
    # values in v are costs (i.e. negated utility)
    return dist(graph, 'Start', set(S))

def mu(S, i):
    # i is never in S when called from Shapley
    return v(S | set(i)) - v(S)

def Shapley(S, i):
    return sum(mu(set(o[:o.index(i)]), i) for o in permutations(S))/factorial(len(S))

def in_core(Psi):
    # use <= rather than >=, since v is a cost function
    return all(sum(Psi[i] for i in S) <= v(S) for S in subsets(Psi.keys()))


# a) (N, v)
print("N = ", N)
for S in powerset(N):
    print("v(", list(S), ") = ", v(S))
print()
# b) [4.5, 9.833333333333334, 11.5, 13.166666666666666]
print("Shapley Value: ", [Shapley(N, i) for i in N])
print()
print("Socially optimal coalition:")
# substitute max by min, since v is a cost function
cs = min(partitions(N),key=lambda x: sum(v(s) for s in x))
# c) [['A', 'B', 'C'], ['D']] ,  37 ,  [[4.833333333333333, 8.833333333333334, 11.333333333333334], [12.0]]
print("CS* = ", cs)
# d) [[4.833333333333333, 8.833333333333334, 11.333333333333334], [12.0]]
print("Shapley Values: ", [[Shapley(c, i) for i in c] for c in cs])
print()
# e) False [False, True]
print("In core: ", in_core({i: Shapley(N, i) for i in N}), [in_core({i: Shapley(c, i) for i in c}) for c in cs])
