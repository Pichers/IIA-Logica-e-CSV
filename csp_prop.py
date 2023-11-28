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

    # for formula in formulas:
    #     for literal in prop_symbols(formula):
    #         literal_str = str(literal)
    #         if literal_str not in variables:
    #             variables.append(literal_str)
    
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
                
            # n = isNegative(p)

            # if var in symbols and len(domains[var_str]) > 1:
            #     if len(symbols) == 1:
            #         if n:
            #             domains[var_str] = [False]
            #         else:
            #             domains[var_str] = [True]
            # if len(domains[var_str]) == 1 and len(symbols) == 1 and var in symbols:
            #     if domains[var_str] == [True]:

            # domains[var] = [True] if (len(prop_symbols(p)) == 1) and (p == literal) else [False, True]

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
        # print("\n")
            # symbols = prop_symbols(formula)
            # if variable in symbols:
            #     other_symbols = [s for s in symbols if s != expr(variable)]
            #     neighbors[variable].extend(other_symbols)

    # for formula in formulas:
    #     if len(prop_symbols(formula)) == 1:
    #         constraints[formula] = []
    #     elif len(prop_symbols(formula)) == 2:
    #         constraints[formula] = [formula]
    #     else:
    #         constraints[formula] = []
    #         for literal in prop_symbols(formula):
    #             constraints[formula].append(literal)

    return CSP(variables_str, domains, neighbors, None)

def value(exp):
    exp_str = str(exp)
    til = '~'
    return til  not in exp_str
