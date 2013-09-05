import debugger

debugger = debugger.debugger()

pid = raw_input("Enter the PID of the process to attach to:")

debugger.attach(int(pid))

debugger.detach()
