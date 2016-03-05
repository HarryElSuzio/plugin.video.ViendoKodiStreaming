from lib import main

try:
    myAddon = main.Main()
    myAddon.run(sys.argv)
except:
    traceback.print_exc(file = sys.stdout)
