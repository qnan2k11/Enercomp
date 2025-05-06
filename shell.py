import enercomp
while True:
  text = input('EnerComp: ')
  result,error = enercomp.run(text)
  if error:
    print(error.string())
  else:
    print(result)