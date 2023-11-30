#!/usr/bin/python
import dis

with open("hidden_4.pyc", "rb") as file:
    code = file.read()

instructions = dis.get_instructions(code)

names = {instr.argval for instr in instructions if instr.opname == 'LOAD_NAME' and not instr.argval.startswith('__')}
for name in sorted(names):
    print(name)
