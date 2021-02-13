class SymbolTable:
  next_address = 16
  table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576
  }

  def __init__(self):
    return
  
  def addEntry(self, symbol, address):
    if address == None:
      self.table[symbol] = self.next_address
      self.next_address += 1
    else:
      self.table[symbol] = address

  def contains(self, symbol):
    if symbol in self.table.keys():
      return True
    else:
      return False
  
  def getAddress(self, symbol):
    return self.table[symbol]


# if command_type == "A_COMMAND":

#   current_address += 1
# elif command_type == "L_COMMAND":
#   symbol = self.symbol()
#   self.symbol_table.addEntry(symbol, current_address)
# else:
#   current_line += 1
#   continue