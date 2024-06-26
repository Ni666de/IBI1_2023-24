def favorite_bond_actor(birth_year):
    bond_actors = {
        1973: "Roger Moore",
        1987: "Timothy Dalton",
        1995: "Pierce Brosnan",
        2006: "Daniel Craig"
    }
    age_18 = birth_year + 18
    for start_year, actor in bond_actors.items():
        if start_year <= age_18 < start_year + 13:  
            return actor
    return "Unknown"  

birth_year = 1980  
print(f"The favorite Bond actor for someone born in {birth_year} is {favorite_bond_actor(birth_year)}.")
