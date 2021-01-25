from urllib import parse

pin = "./in.csv"
pout = "./data.csv"

fin = open(pin, 'r', encoding='UTF-8')
fout = open(pout, 'w', encoding='UTF-8')

bhead = True

for line in fin:
  items = line.split(',')
  sout = line.strip('\n')
  if bhead == True:
    bhead = False
  else:
    sout = sout + "," + 'https://twitter.com/search?q='
    sout = sout + parse.quote('シグルリ ' + items[0])
  sout = sout + '\n'
  fout.write(sout)


fin.close()
fout.close()

