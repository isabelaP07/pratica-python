def split_and_join(line):
   
    line = 'this is a string'
    line = line.split(" ")
    print(line)
    
    line = "-".join(line)
    print(line)

    line = input()
    result = split_and_join(line)
    print(result)