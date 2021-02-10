import sys
import tempfile
import re

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
    self.current_command = self.temp_file.readline()
    if not self.current_command:
      self.hasMoreCommands = False
    else:
      return

  # 現在のコマンドの種類を返す。
  def commandType(self):
    first_letter = self.current_command[:1]
    if first_letter == "@":
      return "A_COMMAND"
    elif first_letter == "(":
      return "L_COMMAND"
    else:
      return "C_COMMAND"

  # 現コマンド@Xxxまたは(Xxx)のXxxを返す。AかLのときだけ返す。
  def symbol(self):
    if self.current_command[:1] == "@":
      print(re.sub("@", "", self.current_command))
    else:
      re.sub("\(|\)", "", current_command)

  # 現C命令のdestニーモニックを返す。
  def dest(self):
    return

  # 現C命令のcompニーモニックを返す。
  def comp(self):
    return

  # 現C命令のcompニーモニックを返す。
  def jump(self):
    return

  def extract_unnecessary_line(self):
    while True:
      line = self.file.readline()

      if not line:
        break
      # 空白を削除
      line = re.sub(r"\s", "", line)
      if line[:2] != "//" and len(line) != 0:
        self.temp_file.write(line + "\n")
        
  def start_parsing(self):
    self.extract_unnecessary_line()
    self.temp_file.seek(0)
    # while self.hasMoreCommands:
    for i in range(5):
      self.advance()
      print("current_command", self.current_command)
      current_command_type = self.commandType()
      if current_command_type == "A_COMMAND" or current_command_type == "L_COMMAND":
        self.symbol()
      else:
        continue
        # self.dest()
        # self.comp()
        # self.jump()

def init():
  parser = Parser()
  parser.start_parsing()

if __name__ == "__main__":
  init()