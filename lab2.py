def List():
    List = []
    print(List)
    List = ['sohamroy']
    print(List)
    List = ["soham", "roy", "soham"]
    print(List[0])
    print(List[2])
    List = [['soham', 'roy'] , ['soham']]
    print(List)
    List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
    print(List)
    List = [1, 2, 'Soham', 4, 'For', 6, 'Soham']
    print(List) 
  
def typ():
    Tuple1 = ()  
    print (Tuple1)
    Tuple1 = ('Soham', 'Roy') 
    print(Tuple1)
    list1 = [1, 2, 4, 5, 6]
    print(tuple(list1))
    Tuple1 = ('Soham') 
    n = 5 
    for i in range(int(n)): 
        Tuple1 = (Tuple1,) 
        print(Tuple1)
    Tuple1 = tuple('Soham')
    print(Tuple1)
    Tuple1 = (5, 'Welcome', 7, 'Soham') 
    print(Tuple1)
    Tuple1 = (0, 1, 2, 3) 
    Tuple2 = ('python', 'soham') 
    Tuple3 = (Tuple1, Tuple2)  
    print(Tuple3)
    Tuple1 = ('Soham',) * 3 
    print(Tuple1)
def set():
    set1 = set()  
    print(set1)
    set1 = set("SohamRoy")
    print(set1)
    String = 'SohamRoySoham'
    set1 = set(String)
    print(set1)
    set1 = set(["Soham", "Roy", "Soham"])
    print(set1)
    set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5]) 
    print(set1)
    set1 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
    print(set1)
set()
    
