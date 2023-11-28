from logic import *
from csp import *

def csp_prop(formulas):
    variables = set()
    variables_str = set()
    domains = {}
    neighbors = {}
    
    propkb = PropKB()

    for f in formulas:
        propkb.tell(f)
        for literal in prop_symbols(f):
            variables.add(literal)
            variables_str.add(str(literal))
    variables = sorted(variables)
    variables_str = sorted(variables_str)
    
    for i in range(len(variables)):
        var = variables[i]
        var_str = variables_str[i]

        domains[var_str] = [False, True]

        for p in propkb.clauses:
            symbols = prop_symbols(p)

            if len(symbols) == 1:
                v = value(p)
                if var in symbols:

                    if (len(domains[var_str]) <= 1) and (v not in domains[var_str]):
                        domains[var_str] = []
                    elif v:
                        domains[var_str] = [True]
                    else:
                        domains[var_str] = [False]

    for i in range(len(variables)):
        variable = variables[i]
        variable_str = variables_str[i]

        neighbors[variable_str] = []

        for p in propkb.clauses:
            ss = prop_symbols(p)
            if variable in ss:
                for s in ss:
                    s_str = str(s)
                    if s_str != variable_str and (s_str not in neighbors[variable_str]):
                        neighbors[variable_str].append(s_str)

    def constraints(var1, val1, var2, val2):
        kb = PropKB()
        result = True

        if val1 == False:
            newVar1 = expr('~' + var1)
            kb.tell(newVar1)
        elif val1 == True:
            newVar1 = expr(var1)
            kb.tell(newVar1)

        if val2 == False:
            newVar2 = expr('~' + var2)
            kb.tell(newVar2)
        elif val2 == True:
            newVar2 = expr(var2)
            kb.tell(newVar2)

        for p in propkb.clauses:
            symbols = prop_symbols(p)

            if (var1 in symbols) or (var2 in symbols):
                if kb.ask_if_true(p) == False:
                    return False
                # result = result and kb.ask_if_true(p, False)
        return True


    return CSP(variables_str, domains, neighbors, constraints)

def value(exp):
    exp_str = str(exp)
    return '~'  not in exp_str


try:
    formulas={expr('VA | VP'),expr('AV | AP'),expr('PV | PA'),expr('VP'),expr('VA ==> ~VP'),expr('AP ==> ~AV'),\
          expr('PA ==> ~PV'),expr('VA ==> ~PA'),expr('PV ==> ~AV'),expr('VP ==> ~AP')}
    dancam_csp=csp_prop(formulas)
    r = backtracking_search(dancam_csp)
    print('Assignment = ',r)
except Exception as e:
    print(repr(e))