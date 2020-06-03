grid = [[1,2,3],[4,5,6],[7,8,9]]   #这里是2D list。

rows = len(grid)                   #取了list的长度。

for row in range (rows):           #row是从零开始的。
    
    cols = len(grid[row])          #通过row的取值，找到每一个row里面一共几个项。
    
    for col in range (cols):       #从零开始，col中的每一个项都有了。
        
        print(grid[row][col])      #最后依次将每一个项print出来。

