def resolve_simple(clause1, clause2):
    for literal in clause1:
        if -literal in clause2:
            new_clause = (clause1 | clause2) - {literal, -literal}
            return new_clause
    return None

def is_satisfiable(clauses):
    while True:
        new_clauses = []
       
        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                resolvent = resolve_simple(clauses[i], clauses[j])
                if resolvent is not None:
                    if not resolvent:
                        return False
                    if resolvent not in clauses and resolvent not in new_clauses:
                        new_clauses.append(resolvent)
       
        if not new_clauses:
            return True  
       
        clauses.extend(new_clauses)
"""
clauses = [
   {1, -2},  
   {-1, 3},  
   {-3},  
   {2},    
]

clauses=[
	{ 1, -2, 3 },
	{ 2, 3 },
	{ -1, 3 },
	{ 2, -3 },
	{ -2 },

]
"""

clauses = [
    {1, -2, 3},   # (A ∨ ¬B ∨ C)
    {2, 3},       # (B ∨ C)
    {-1, 3},      # (¬A ∨ C)
    {2, -3},      # (B ∨ ¬C)
    {-2},         # (¬B)
]


print("Satisfiabil?", is_satisfiable(clauses))