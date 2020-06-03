# One database record stored facts about one entity (animals,people,falilies,films,etc.)
# Fields:与entity相关的一些东西。e.g.与电影相关的有：开场音乐，演员，电影名，上映时间。。。。。。

class Animal():
    def __init__ (C,name,code,DOB,species):

        C.code=code
        C.name=name
        C.species=species
        C.DOB=DOB

PG1=Animal("ZRX","PG1","2019.11.7","pig")
print(PG1.name)
