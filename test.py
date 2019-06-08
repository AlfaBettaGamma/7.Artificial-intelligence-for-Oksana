def SumOfThe( N,  data):
  s = 0
  rez = 0
  for i in range(N):
    s = s + data[i]
  for j in range(N):
    if s < 0 and data[j] > 0:
      if s + data[j] == data[j]:
        rez = data[j]
    elif s < 0 and data[j] < 0:
      if s - data[j] == data[j]:
        rez = data[j]
    elif s > 0 and data[j] > 0:
      if s - data[j] == data[j]:
        rez = data[j]
    elif s > 0 and data[j] < 0:
      if s + data[j] == data[j]:
        rez = data[j]
        
  return rez