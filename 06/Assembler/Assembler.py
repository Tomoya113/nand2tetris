import sys

def init():
  print(sys.argv[1])
  file = open(sys.argv[1], 'r', encoding='UTF-8')
  row_no = 0
  while True:
    line = file.readline()
    if line:
      row_no += 1
      print(row_no, ":", line)
    else:
      break
  file.close()

if __name__ == "__main__":
  init()