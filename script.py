import os

class Computer:
    def __init__(self):
        print(f'{self} : created')
        self.cpu = CPU()

    def __str__(self):
        return 'Computer'
    
    def instruct(self, instruction):
        print(f'{self} : recieved instruction')
        self.cpu.instruct(instruction)

class CPU:
    def __init__(self):
        print(f'{self} : created')
        self.cu = CU()

    def __str__(self):
        return 'CPU'

    def instruct(self, instruction):
        print(f'{self} : recieved instruction')
        self.cu.instruct(instruction)

class CU:
    def __init__(self):
        print(f'{self} : created')
        self.alu = ALU()
        self.registers = Registers()

    def __str__(self):
        return 'CU'

    def instruct(self, instruction):
        print(f'{self} : recieved instruction')
        self.decode(instruction)
    
    def decode(self, instruction):
        print(f'{self} : decoding {instruction}')
        opcode = instruction[:6]
        rs = instruction[6:11]
        rt = instruction[11:16]
        rd = instruction[16:21]
        immd = instruction[21:]

        if opcode == '001000':
            self.addi(rs, rt, immd)
        
        if opcode == '100000':
            self.add(rs, rt, rd)

    def addi(self, rs, rt, immd):
        print(f'{self} : addi detected')
        print(f'{self} : rs-{rs}, rt-{rt}, imm-{immd}')
        data = self.registers.fetch(rs)
        result = self.alu.add(data, immd)
        self.registers.store(rt, result)
    
    def add(self, rs, rt, rd):
        print(f'{self} : add detected')
        print(f'{self} : rs-{rs}, rt-{rt}, rd-{rd}')
        data1 = self.registers.fetch(rs)
        data2 = self.registers.fetch(rt)
        result = self.alu.add(data1, data2)
        self.registers.store(rd, result)

class ALU:
    def __init__(self):
        print(f'{self} : created')

    def __str__(self):
        return 'ALU'
    
    def add(self, num1, num2):
        print(f'{self} : adding {num1} and {num2}')
        result = bin(int(num1, 2) + int(num2, 2))
        print(f'{self} : result is {result}')
        return result

class Registers:
    def __init__(self):
        print(f'{self} : created')
        self.dict = {'00000':'0b0'}

    def __str__(self):
        return 'Registers'
    
    def store(self, address, data):
        print(f'{self} : storing {data} at address {address}')
        self.dict[address] = data
        print(f'{self} : {list(self.dict.items())}')

    def fetch(self, address):
        print(f'{self} : fetching data at address {address}')
        print(f'{self} : result is {self.dict[address]}')
        return self.dict[address]

def run():
    os.system('clear')

    computer = Computer()
    print()

    a = '00100000000000010000000000001010'
    b = '00100000000000100000000000000101'
    c = '10000000001000100001100000000000'

    print('System : storing 10 in register 1')
    computer.instruct(a)
    print()

    print('System : storing 5 in register 2')
    computer.instruct(b)
    print()

    print('System : adding registers 1 and 2, storing in 3')
    computer.instruct(c)
    print()

run()

#6 opcode, 5 rs, 5 rt, 5 rd, 11 immd

#storing 10 in register 1
#addi
#001000, 00000, 00001, 00000, 00000001010

#storing 5 in register 2
#addi
#001000, 00000, 00010, 00000, 00000000101

#adding registers 1 and 2, storing in 3
#add
#100000, 00001, 00010, 00011, 00000000000