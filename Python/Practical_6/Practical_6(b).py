print("\nTo Write a python program for Tower Of Hanoi Scenario\n") 
def TowerOfHanoi(n, s, d, i): 
    if n == 1: 
        print("Move disk 1 from source ",s," to destination ",d) 
        return 
    TowerOfHanoi(n-1, s, i, d) 
    print("Move disk",n,"from source ",s," to destination ",d) 
    TowerOfHanoi(n-1, i, d, s) 
n =int(input("Enter number of disk : ")) 
TowerOfHanoi(n, 'A', 'B', 'C')