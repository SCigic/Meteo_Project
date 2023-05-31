from tk_gui.main_window import MainWindow
from db_repos.db_repo import db_init


if __name__ == "__main__":
    
    db_init()


    main_window = MainWindow()
    main_window.mainloop()


