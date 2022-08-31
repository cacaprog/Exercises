''''
Se você precisa store multiple elements, use arrays and lists

Com as arrays, os elementos são alocados lado a lado
Nas listas eles tem os endereços do próximo elemento (sequencial)
Arrays são mais rápidas para leitura
Linked Lists são mais rápidas para inserir e deletar elementos
Todos os elementos em uma array devem ser do mesmo tipo (int, doubles...)
'''

# Finds the smallest value in an array
def findSmallest(arr):
  # Stores the smallest value
  smallest = arr[0]
  # Stores the index of the smallest value
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest_index = i
      smallest = arr[i]      
  return smallest_index

# Sort array
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print(selectionSort([5, 3, 6, 2, 10]))

#find the smallest element