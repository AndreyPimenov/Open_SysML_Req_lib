# Requirement attribute from the Standard:
# 1) identification
# 2) priority
# 3) criticality
# 4) risk
# 5) source
# 6) rationale
# 7) difficulty
# 8) type
#
# =============
#
# Magicdraw splits requirement and traceability:
# RQR:
# 1) name
# 2) identification
# 3) text
# 4) source
# 5) verify methods
# 6) Risk
# TRC:
# 1) Owner
# 2) Refined by
# 3) Traced to
# 4) Satisfy by
# 5) Master
# 6) Derived
# 7) Derived from
# 8) Verified by
#
# ==============
#
# Modelio:
# 1) name
# 2) definition
# 3) documentation
# 4) Origin
# 5) Benefit
# 6) Cost
# 7) Risk
# 8) Stability
# 9) Target Release
#
# ===============

class Requirement:
    def __init__(self): #object constructor
        self.id = 0
        self.Definition = " - "
        self.Origin = " - "
        self.Target= " - "


    def info(self):
        return self.id, self.Definition, self.Origin, self.Release

    def show(self, name = 'Unknown'):
        print ("Hello" + ", " + name + " !")


class Linker:
    # Derive, Refine, part, Satisfy, Verify
    pass


# Create naming - a,b,c,d,...o,p
N = {
    'a': set('f'),
    'b': set('ach'),
    'c': set(''),
    'd': set('ck'),

    'e': set('k'),
    'f': set(''),
    'g': set('a'),
    'h': set(''),

    'i': set('h'),
    'j': set('h'),
    'k': set('p'),
    'l': set('n'),

    'm': set('n'),
    'n': set('o'),
    'o': set('f'),
    'p': set('0'),

}
