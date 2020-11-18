def arrangements(n, k, result=list()):
  if k == 0:
    print(result)
    return

  for index in range(n):
    new_result = list(result)
    new_result.append(index)
    
    arrangements(n, k - 1, new_result)

if __name__ == "__main__":
    arrangements(3, 3)