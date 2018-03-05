def flip_pancake(pancakes,i):
    top = pancakes[:i+1]
    top.reverse()
    return top + pancakes[i+1:]

def find_the_Largest_number(pancakes,length):
    index=1
    LargestNumber=pancakes[0]
    largest_index = 0
    while index<length:
        if pancakes[index]>LargestNumber:
            LargestNumber=pancakes[index]
            largest_index = index
        index+=1
    return LargestNumber,largest_index


def pancake_solver(pancakes,sortedLength):
    if sortedLength==len(pancakes):
        print(pancakes)
        return 0
    else:
        currentLargestNumber,currentLargestNumberPosition=find_the_Largest_number(pancakes,len(pancakes)-sortedLength)
       
        print(pancakes)

        print('currentLargestNumber: '+str(currentLargestNumber))
       
       
        if currentLargestNumberPosition == len(pancakes)-sortedLength-1:

            
            
            return 0 + pancake_solver(pancakes,sortedLength+1)
        else:
            if currentLargestNumberPosition==0:
                
               

                pancakes=flip_pancake(pancakes,len(pancakes)-1-sortedLength)

                
                
                return 1 + pancake_solver(pancakes,sortedLength+1)
            else:


                pancakes=flip_pancake(pancakes,currentLargestNumberPosition)
                print(pancakes)
                pancakes=flip_pancake(pancakes,len(pancakes)-1-sortedLength)
                
                return 2 + pancake_solver(pancakes,sortedLength+1)

array_number = input('Please enter a list of number to sort using pancake sort separate by a space: ')



numbers = array_number.split()

n = []

for i in numbers:

    n.append(int(i))




NumberOfFlip= pancake_solver(n,0)

print('Solvable in '+str(NumberOfFlip)+' move(s)')
    
