from menu.menu_component import MenuComponent


class Menu(MenuComponent):
    def __init__(self, title: str) -> None:
        super().__init__(title)
        self._menu_components = []

    def get_child(self, index: int) -> MenuComponent:
        """ :return: The sub menu on  """
        return self._menu_components[index]

    def add(self, composite_menu: MenuComponent) -> None:
        """ Adds the given menu to the list of submenu's """
        self._menu_components.append(composite_menu)

    def display(self) -> None:
        """ Prints out the current menu and all sub menu's """
        print("")
        print(self.title)
        print("--------------------------------------")
        for menu in self._menu_components:
            menu.display()
