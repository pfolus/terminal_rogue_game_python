def print_game_over():
    import os
    import random
    from time import sleep
    colors = ['\033[94m', '\033[92m', '\033[93m', '\033[91m']

    for times in range(26):

        os.system("clear")



        print(random.choice(colors) + '''

     .----------------.  .----------------.  .----------------.  .----------------.    .----------------.  .----------------.  .----------------.  .----------------.
    | .--------------. || .--------------. || .--------------. || .--------------. |  | .--------------. || .--------------. || .--------------. || .--------------. |
    | |    ______    | || |      __      | || | ____    ____ | || |  _________   | |  | |     ____     | || | ____   ____  | || |  _________   | || |  _______     | |
    | |  .' ___  |   | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |  | |   .'    `.   | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | |
    | | / .'   \_|   | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |  | |  /  .--.  \  | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | |
    | | | |    ____  | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |  | |  | |    | |  | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | |
    | | \ `.___]  _| | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |  | |  \  `--'  /  | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | |
    | |  `._____.'   | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |  | |   `.____.'   | || |     \_/      | || | |_________|  | || | |____| |___| | |
    | |              | || |              | || |              | || |              | |  | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |  | '--------------' || '--------------' || '--------------' || '--------------' |
     '----------------'  '----------------'  '----------------'  '----------------'    '----------------'  '----------------'  '----------------'  '----------------' ''' + '\033[0m')

        sleep(0.25)

def print_you_won():
    import os
    os.system("clear")
    print('''





















                                                                            ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
                                                                            ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
                                                                             ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
                                                                              ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
                                                                               ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
                                                                               ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝





















    ''')
