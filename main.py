import logging
logging.basicConfig(level=logging.INFO)
from ui import console_ui 
def main():
    students = []
    console_ui.show_menu(students)
if __name__ == "__main__":
    main()
