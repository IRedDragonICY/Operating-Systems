# Python3 implementation of Memory Allocation Algorithms
def memory_allocation(blockSize, m, processSize, n, algorithm):
    print (f"\nMemory Allocation using {algorithm} fit algorithm")
    allocation = [-1] * n  
    for i in range(n):
        print(f"\nAllocating process {i + 1}...")
        idx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if idx == -1:
                    idx = j
                    print(f"Block {j + 1} is a potential fit")
                elif algorithm == 'best' and blockSize[idx] > blockSize[j]:  
                    idx = j
                    print(f"Block {j + 1} is a better fit")
                elif algorithm == 'worst' and blockSize[idx] < blockSize[j]:
                    idx = j 
                    print(f"Block {j + 1} is a worse fit")

        if idx != -1: 
            allocation[i] = idx
            print(f"Process {i + 1} allocated to block {idx + 1}")
            print(f"blockSize[{idx + 1}] = {blockSize[idx]} K - {processSize[i]} K = {blockSize[idx] - processSize[i]} K")
            blockSize[idx] -= processSize[i] 
            print(f"Block {idx + 1} remaining size: {blockSize[idx]} K")
        else:
            print(f"Process {i + 1} not allocated")
  
    print("\n{:^12} {:^18} {:^10}".format("Process No.", "Process Size (K)", "Block no."))
    for i in range(n): 
        if allocation[i] != -1:  
            print("{:^12} {:^18} {:^10}".format(i + 1, processSize[i], allocation[i] + 1))  
        else: 
            print("{:^12} {:^18} {:^10}".format(i + 1, processSize[i], "Not Allocated"))
    print("Remaining block size: ", end='')
    for i in range(m):
        print(f"{blockSize[i]} ", end='')
    print("\n")

# Driver code  
if __name__ == '__main__':  
    blockSize = [100, 500, 200, 300, 600]  
    processSize = [212, 417, 112, 426]  
    m = len(blockSize)  
    n = len(processSize)  

    memory_allocation(blockSize[:], m, processSize, n, 'first')
    memory_allocation(blockSize[:], m, processSize, n, 'best')
    memory_allocation(blockSize[:], m, processSize, n, 'worst')
