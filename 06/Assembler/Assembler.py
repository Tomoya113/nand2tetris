import sys
import tempfile

class Parser:
  # ファイル
  file = None
  temp_file = tempfile.TemporaryFile(mode="w+")
  # 現在のコマンド
  current_command = ""
  # これ以上コマンドがあるかどうか
  hasMoreCommands = True

  def __init__(self):
    self.file = open(sys.argv[1], 'r', encoding='UTF-8')

  # 入力から次のコマンドを読み、それを現在のコマンドにする
  def advance(self):
    self.current_command = self.file.readline()
    if not self.current_command:
      self.hasMoreCommands = False
    else:
      print(self.current_command)

  # 現在のコマンドの種類を返す。
  def commandType(self):
    
    print(first_two_letter)

  # 現コマンド@Xxxまたは(Xxx)のXxxを返す。AかLのときだけ返す。
  def symbol(self):
    print("hoge")

  # 現C命令のdestニーモニックを返す。
  def dest(self):
    print("hoge")

  # 現C命令のcompニーモニックを返す。
  def comp(self):
    print("hoge")

  # 現C命令のcompニーモニックを返す。
  def jump(self):
    print("hoge")

  def extract_unnecessary_line(self):
    while True:
      line = self.file.readline()

      if not line:
        break

      first_two_letter = line[:2]
      if first_two_letter != "//" and line != '\n':
        self.temp_file.write(line)
        


  def start_parsing(self):
    self.temp_file.write(word)
    # while self.hasMoreCommands:
    # for i in range(5):
    #   self.advance()
    #   current_command_type = self.commandType()

# tempfileを読み込む時に必要
# self.temp_file.seek(0)

def init():
  parser = Parser()
  parser.extract_unnecessary_line()
  # parser.start_parsing()
  

if __name__ == "__main__":
  init()