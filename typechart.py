from collections import defaultdict

# Create the type chart with format:
# typechart['defending type']['attacking type']
# If the defending and/or attacking type relation is not specified in the
# chart, return 1.0.
typechart = defaultdict(lambda: defaultdict(lambda: 1.0))

typechart['normal'].update(fighting=2.0, ghost=0.0)
typechart['fire'].update(fire=0.5, water=2.0, grass=0.5, ice=0.5, ground=2.0, bug=0.5, rock=2.0, steel=0.5, fairy=0.5)
typechart['water'].update(fire=0.5, water=0.5, electric=2.0, grass=2.0, ice=0.5, steel=0.5)
typechart['electric'].update(electric=0.5, ground=2.0, flying=0.5, steel=0.5)
typechart['grass'].update(fire=2.0, water=0.5, electric=0.5, grass=0.5, ice=2.0, poison=2.0, ground=0.5, flying=2.0, bug=2.0)
typechart['ice'].update(fire=2.0, ice=0.5, fighting=2.0, rock=2.0, steel=2.0)
typechart['fighting'].update(flying=2.0, psychic=2.0, bug=0.5, rock=0.5, dark=0.5, fairy=2.0)
typechart['poison'].update(grass=0.5, fighting=0.5, poison=0.5, ground=2.0, psychic=2.0, bug=0.5, fairy=0.5)
typechart['ground'].update(water=2.0, electric=0.0, grass=2.0, ice=2.0, poison=0.5, rock=0.5)
typechart['flying'].update(electric=2.0, grass=0.5, ice=2.0, fighting=0.5, ground=0.0, bug=0.5, rock=2.0)
typechart['psychic'].update(fighting=0.5, psychic=0.5, bug=2.0, ghost=2.0, dark=2.0)
typechart['bug'].update(fire=2.0, grass=0.5, fighting=0.5, ground=0.5, flying=2.0, rock=2.0)
typechart['rock'].update(normal=0.5, fire=0.5, water=2.0, grass=2.0, fighting=2.0, poison=0.5, ground=2.0, flying=0.5, steel=2.0)
typechart['ghost'].update(normal=0.0, fighting=0.0, poison=0.5, bug=0.5, ghost=2.0, dark=2.0)
typechart['dragon'].update(fire=0.5, water=0.5, electric=0.5, grass=0.5, ice=2.0, dragon=2.0, fairy=2.0)
typechart['dark'].update(fighting=2.0, psychic=0.0, bug=2.0, ghost=0.5, dark=0.5, fairy=2.0)
typechart['steel'].update(normal=0.5, fire=2.0, grass=0.5, ice=0.5, fighting=2.0, poison=0.0, ground=2.0, flying=0.5, psychic=0.5, bug=0.5, rock=0.5, dragon=0.5, steel=0.5, fairy=0.5)
typechart['fairy'].update(fighting=0.5, poison=2.0, bug=0.5, dragon=0.0, dark=0.5, steel=2.0)

'''
This is more out of curiosity than anything useful, but, if a Pokemon was all 18 types, then it would have
8 immunities: normal, fighting, ghost, ground, electric, poison, psychic, dragon
4 resistances: dark (1/2), steel (1/2), grass (1/16), bug (1/16)
5 neutrals: fire, water, ice, fairy, flying
1 weakness: rock (2)
CODE:

alltypes = defaultdict(lambda: 1.0)
for type_, dict_ in typechart.items():
  for t, e in dict_.items():
    alltypes[t] *= e
print(alltypes)

OUTPUT:
defaultdict(<function <lambda> at 0x7f0596ad2e18>, {'fighting': 0.0, 'ghost': 0.0, 'fire': 1.0, 'water': 1.0, 'grass': 0.0625, 'ice': 1.0, 'ground': 0.0, 'bug': 0.0625, 'rock': 2.0, 'steel': 0.5, 'fairy': 1.0, 'electric': 0.0, 'flying': 1.0, 'poison': 0.0, 'psychic': 0.0, 'dark': 0.5, 'normal': 0.0, 'dragon': 0.0})
'''
