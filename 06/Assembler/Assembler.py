import sys
import tempfile
import re
import Code

class Parser:
  # ファイル
  file = None
  temp_file = tempfile.TemporaryFile(mode="w+")
  # 現在のコマンド
  current_command = ""
  # これ以上コマンドがあるかどうか
  hasMoreCommands = True
  # パース後のファイル
  parsed_file = None
  def __init__(self):
    self.file = open(sys.argv[1], 'r', encoding='UTF-8')
    self.parsed_file = open(sys.argv[1] + ' result', 'w')

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
      return re.sub("@", "", self.current_command)
    else:
      re.sub("\(|\)", "", current_command)

  # 現C命令のdestニーモニックを返す。
  def dest(self, string):
    if string:
      return string
    else:
      return "null"

  # 現C命令のcompニーモニックを返す。
  def comp(self, string):
    if string:
      return string

  # 現C命令のcompニーモニックを返す。
  def jump(self, string):
    if string:
      return string
    else:
      return "null"

  def setup_before_parsing(self):
    while True:
      line = self.file.readline()

      if not line:
        break

      # 空白を削除
      line = re.sub(r"\s", "", line)

      if line[:2] != "//" and len(line) != 0:
        self.temp_file.write(line + "\n")
    self.temp_file.seek(0)
  
  def parse_c_command(self):
    dest = ""
    comp = ""
    jump = ""
    splited_c_command = re.match(r'(.+)(=|;)(.+)', self.current_command)
    operator = splited_c_command.group(2)
    if operator == ";":
      dest = self.dest(None)
      comp = self.comp(splited_c_command.group(1))
      jump = self.jump(splited_c_command.group(3))
    elif operator == "=":
      dest = self.dest(splited_c_command.group(1))
      comp = self.comp(splited_c_command.group(3))
      jump = self.jump(None)
    else:
      print("error")
    return dest, comp, jump


  def start_parsing(self):
    self.setup_before_parsing()
    # while self.hasMoreCommands:
    for i in range(5):
      self.advance()
      if self.commandType() in ["A_COMMAND", "L_COMMAND"]:
        print("symbol", self.symbol())
        result = Code.Code.assemble_a_command(self.symbol())
        print(result)
      else:
        result = self.parse_c_command()
        print(result[0],result[1],result[2])
        assembled_code = Code.Code.assemble_c_command(result)
        print(assembled_code)

def assemble():
  parser = Parser()
  parser.start_parsing()

if __name__ == "__main__":
  assemble()