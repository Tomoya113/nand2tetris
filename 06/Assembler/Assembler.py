import sys
import tempfile
import re
import Code
from SymbolTable import SymbolTable

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
  # シンボルテーブル
  symbol_table = SymbolTable()
  
  def __init__(self):
    self.file = open(sys.argv[1], 'r', encoding='UTF-8')
    self.parsed_file = open(sys.argv[1] + '.result.hack', 'w')

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
      return re.sub("\(|\)", "", self.current_command)
  
  # シンボルを一旦探しておく
  def find_symbol(self):
    current_line = 0
    while True:
      self.advance()
      if not self.hasMoreCommands:
        break
      command_type = self.commandType()
      if command_type == "L_COMMAND":
        symbol = self.symbol()[:-1]
        self.symbol_table.addEntry(symbol, current_line)
      else:
        current_line += 1
    # 終わったら初期化
    self.temp_file.seek(0)
    self.hasMoreCommands = True

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
    self.find_symbol()
    result = ""
    while True:
      self.advance()
      if not self.hasMoreCommands:
        break
      if self.commandType() == "A_COMMAND":
        symbol = self.symbol()[:-1]
        if symbol.isdecimal():
          result = Code.Code.assemble_a_command(symbol)
        elif self.symbol_table.contains(symbol):
          parsed_symbol = self.symbol_table.getAddress(symbol)
          result = Code.Code.assemble_a_command(parsed_symbol)
        else:
          self.symbol_table.addEntry(symbol, None)
          parsed_symbol = self.symbol_table.getAddress(symbol)
          result = Code.Code.assemble_a_command(parsed_symbol)
        self.parsed_file.write(result + "\n")
      elif self.commandType() == "L_COMMAND":
        continue
      else:
        code = self.parse_c_command()
        result = Code.Code.assemble_c_command(code)
        print(result)
        self.parsed_file.write(result + "\n")

def assemble():
  parser = Parser()
  parser.start_parsing()

if __name__ == "__main__":
  assemble()