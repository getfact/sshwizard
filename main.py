from wizard import Assberry
from settings import *
from commands import *

# devices
rpi_1 = Assberry(IP, PORT, USER, PASS, POWEROFF)
rpi_2 = Assberry(IP_2, PORT_2, USER_2, PASS_2, POWEROFF)
# an empty list
rpi_pool = []
# append the devices
rpi_pool.append(rpi_1)
rpi_pool.append(rpi_2)

def main():
    print('\nSSH Gang$ta\n')
    # connect the raspberrys via ssh
    for rpi in rpi_pool:
        try:
            rpi.login()
            rpi.logged_in = True
            print('{}@{} OK'.format(rpi.user, rpi.ip))
        except:
            rpi.logged_in = False
            print('{}@{} ERROR'.format(rpi.user, rpi.ip))

    # Execute the command
    print('\nResults:\n')
    for rpi in rpi_pool:
        if rpi.logged_in:
            rpi.command(rpi.cmd)
            print('Executed: {}@{} {}'.format(rpi.ip, rpi.user, rpi.cmd))
        else:
            print('Failed: {}@{} {}'.format(rpi.ip, rpi.user, rpi.cmd))
    print('')
main()

