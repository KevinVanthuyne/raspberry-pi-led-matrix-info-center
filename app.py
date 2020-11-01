from msvcrt import getch
from os import system

from menu.menu import Menu
from menu.menu_component import MenuComponent
from menu.menu_item import MenuItem

UP_ARROW_KEY = 72
DOWN_ARROW_KEY = 80
ESC_KEY = 27
ENTER_KEY = 13


def setup_menu() -> MenuComponent:
    """ Setup the main menu with all its sub menu's and menu items. """

    main_menu = Menu("MAIN MENU")
    weather_menu = Menu("Weather")
    settings_menu = Menu("Settings")

    weather_menu.add(MenuItem("Min & max temperature"))
    weather_menu.add(MenuItem("Rain forecast"))
    weather_menu.add(MenuItem("Day temperatures"))

    settings_menu.add(MenuItem("Reboot"))
    settings_menu.add(MenuItem("Shutdown"))

    main_menu.add(weather_menu)
    main_menu.add(settings_menu)

    return main_menu


def run() -> None:
    main_menu = setup_menu()

    while True:
        system('cls')
        main_menu.display()

        key = ord(getch())
        if key == ESC_KEY:
            break
        elif key == UP_ARROW_KEY:
            main_menu.previous()
        elif key == DOWN_ARROW_KEY:
            main_menu.next()
        elif key == ENTER_KEY:
            main_menu.select()


if __name__ == '__main__':
    run()
