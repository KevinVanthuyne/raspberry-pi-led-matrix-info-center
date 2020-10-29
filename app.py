from menu.menu import Menu
from menu.menu_item import MenuItem


def run() -> None:
    main_menu = Menu("MAIN MENU")
    weather_menu = Menu("WEATHER")
    settings_menu = Menu("SETTINGS")

    weather_menu.add(MenuItem("Min & max temperature"))
    weather_menu.add(MenuItem("Rain forecast"))
    weather_menu.add(MenuItem("Day temperatures"))

    settings_menu.add(MenuItem("Reboot"))
    settings_menu.add(MenuItem("Shutdown"))

    main_menu.add(weather_menu)
    main_menu.add(settings_menu)

    main_menu.display()


if __name__ == '__main__':
    run()
