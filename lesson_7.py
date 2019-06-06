def SumOfThe( N,  data):
  s = 0
  rez = 0
  for i in range(N):
    s = s + data[i]
  print(s)
  for j in range(N):
    if s < 0 and data[j] > 0:
      print('Входяшие 1 - ',data[j])
      if s + data[j] == data[j]:
        rez = data[j]
    elif s < 0 and data[j] < 0:
      print('Входяшие 2 - ',data[j])
      if s - data[j] == data[j]:
        rez = data[j]
    elif s > 0 and data[j] > 0:
      print('Входяшие 3 - ',data[j])
      if s - data[j] == data[j]:
        rez = data[j]
    elif s > 0 and data[j] < 0:
      print('Входяшие 4 - ',data[j])
      if s + data[j] == data[j]:
        rez = data[j]
        
  print(rez)
