from operator import itemgetter

class file:
    """файл"""
    def __init__(self, id, name, size, catId):
        self.id = id
        self.name = name
        self.size = size
        self.catId = catId
 
class cat:
    """каталог"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class fileCat:
    """
    'файлы каталога' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, catId, fileId):
        self.catId = catId
        self.fileId = fileId

cats = [cat(1, "D:\программы на python"),
        cat(2, "D:\отчёты по лабам"),
        cat(3, "C:\игры")]

files = [file(1,"Hello world.py",1,1),
         file(2,"лаб 2 отчёт",100,2),
         file(3,"game.py",3000,1)]

filesCats = [fileCat(1,1),
             fileCat(2,2),
             fileCat(1,3),
             fileCat(3,3)]

catsId = [c.id for c in cats]
oneToMany = [(f.name, f.size, cats[catsId.index(f.catId)].name) for f in files]

filesId = [f.id for f in files]
manyToMany = [(files[filesId.index(fc.fileId)].name,
                files[filesId.index(fc.fileId)].size,
                cats[catsId.index(fc.catId)].name)
                for fc in filesCats]

def task1(oneToMany):
    word1 = "г"
    catsE1 = [c.name for c in cats if word1 in c.name]
    filesE1 = [otm[0] for otm in oneToMany for c in catsE1 if otm[2] == c]
    return catsE1, filesE1

def task2(oneToMany):
    return sorted([[c.name, round(sum([otm[1] for otm in oneToMany if otm[2] == c.name])/(lambda x: 1 if x==0 else x)(len([otm[1] for otm in oneToMany if otm[2] == c.name])))] for c in cats], key=itemgetter(1),reverse=True)
    
def task3(manyToMany):
    char3 = "g"
    return [[f.name,[mtm[2] for mtm in manyToMany if mtm[0]==f.name]] for f in files if f.name[0] == char3]

if __name__ == '__main__':
    print(task1(oneToMany))
    print(task2(oneToMany))
    print(task3(manyToMany))






















