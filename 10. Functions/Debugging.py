
import pdb as pdp


def seq(n):
    for i in range(n):
        print(i)
        pdp.set_trace() # It will create a breakpoint at this point program will stop and we can perform interactive debugging

seq(4)