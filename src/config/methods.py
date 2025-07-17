from src.config.colors import *

def CheckQuery(type, result):
    
    if result.rowcount > 0:
        print(green(f"{type} deleted successfully!"))
        return True

    print(red(f"{type} not found or not deleted."))
    return False