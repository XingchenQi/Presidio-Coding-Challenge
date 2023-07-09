class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RED = '\u001b[31m'
    GREEN = '\u001b[32m'
    YELLOW = '\u001b[33m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


text = '''
 ██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║   ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██║▄▄ ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
╚██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
 ╚══▀▀═╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
'''

text_line_one = \
    colors.BLUE + " ██████╗ " + colors.ENDC + \
    colors.RED + "███████╗" + colors.ENDC + \
    colors.YELLOW + "███████╗" + colors.ENDC + \
    colors.BLUE + " █████╗ " + colors.ENDC + \
    colors.GREEN + "██████╗ " + colors.ENDC + \
    colors.RED + " ██████╗" + colors.ENDC + \
    colors.BLUE + "██╗  ██╗" + colors.ENDC

text_line_two = \
    colors.BLUE + "██╔═══██╗" + colors.ENDC + \
    colors.RED + "██╔════╝" + colors.ENDC + \
    colors.YELLOW + "██╔════╝" + colors.ENDC + \
    colors.BLUE + "██╔══██╗" + colors.ENDC + \
    colors.GREEN + "██╔══██╗" + colors.ENDC + \
    colors.RED + "██╔════╝" + colors.ENDC + \
    colors.BLUE + "██║  ██║" + colors.ENDC

text_line_three = \
    colors.BLUE + "██║   ██║" + colors.ENDC + \
    colors.RED + "███████╗" + colors.ENDC + \
    colors.YELLOW + "█████╗  " + colors.ENDC + \
    colors.BLUE + "███████║" + colors.ENDC + \
    colors.GREEN + "██████╔╝" + colors.ENDC + \
    colors.RED + "██║     " + colors.ENDC + \
    colors.BLUE + "███████║" + colors.ENDC

text_line_four = \
    colors.BLUE + "██║▄▄ ██║" + colors.ENDC + \
    colors.RED + "╚════██║" + colors.ENDC + \
    colors.YELLOW + "██╔══╝  " + colors.ENDC + \
    colors.BLUE + "██╔══██║" + colors.ENDC + \
    colors.GREEN + "██╔══██╗" + colors.ENDC + \
    colors.RED + "██║     " + colors.ENDC + \
    colors.BLUE + "██╔══██║" + colors.ENDC

text_line_five = \
    colors.BLUE + "╚██████╔╝" + colors.ENDC + \
    colors.RED + "███████║" + colors.ENDC + \
    colors.YELLOW + "███████╗" + colors.ENDC + \
    colors.BLUE + "██║  ██║" + colors.ENDC + \
    colors.GREEN + "██║  ██║" + colors.ENDC + \
    colors.RED + "╚██████╗" + colors.ENDC + \
    colors.BLUE + "██║  ██║" + colors.ENDC

text_line_six = \
    colors.BLUE + " ╚══▀▀═╝ " + colors.ENDC + \
    colors.RED + "╚══════╝" + colors.ENDC + \
    colors.YELLOW + "╚══════╝" + colors.ENDC + \
    colors.BLUE + "╚═╝  ╚═╝" + colors.ENDC + \
    colors.GREEN + "╚═╝  ╚═╝" + colors.ENDC + \
    colors.RED + " ╚═════╝" + colors.ENDC + \
    colors.BLUE + "╚═╝  ╚═╝" + colors.ENDC


text = f'\n\t{text_line_one}\n\t{text_line_two}\n\t{text_line_three}\n\t{text_line_four}\n\t{text_line_five}\n\t{text_line_six}'

text_basic = f'\n\t{text_line_one}\n\t{text_line_two}\n\t{text_line_three}\n\t{text_line_four}\n\t{text_line_five}\n\t{text_line_six}'

