## a ----> c
# b ----> x
#
def proporcionality(a, b, c, unit):
  sol = (c*b/a)
  print(r'Peter is paid %d %s \ for working %d hours. He will be paid %.2f %s \ for working %d hours.' % (b, unit, a, sol, unit, c))

proporcionality(10, 120, 40, '\\texteuro')

