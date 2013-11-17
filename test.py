import debugger
from debugger_defines import *

debugger = debugger.debugger()

pid = raw_input("Enter the PID of the process to attach to:")

debugger.attach(int(pid))

printf = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % printf

debugger.bp_set_hw(printf,1,HW_EXECUTE)
debugger.run()
