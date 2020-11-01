from menu.menu_component import MenuComponent


class Menu(MenuComponent):
    """ Menu object that contains submenu's """

    def __init__(self, title: str) -> None:
        super().__init__(title)
        self._menu_components = []
        self._current_menu_index = 0

    def get_child(self, index: int) -> MenuComponent:
        """ :return: The sub menu on  """
        return self._menu_components[index]

    def add(self, composite_menu: MenuComponent) -> None:
        """ Adds the given menu to the list of submenu's """
        self._menu_components.append(composite_menu)

    def display(self, selected: bool = False) -> None:
        """ Prints out the current menu and all sub menu's """
        print("")
        print(self.title)
        print("--------------------------------------")
        for menu in self._menu_components:
            if self._child_is_selected(menu):
                print(">> {}".format(menu.title))
            else:
                print("   {}".format(menu.title))

    def next(self) -> None:
        """ Increases the current menu index by one or resets it to 0 if the end of the menu was reached. """
        if self._current_menu_index < self._max_menu_index():
            self._current_menu_index += 1
        else:
            self._current_menu_index = 0

    def previous(self) -> None:
        """ Decreases the current menu index by one or resets it to the end of the menu if 0 was reached. """
        if self._current_menu_index > 0:
            self._current_menu_index -= 1
        else:
            self._current_menu_index = self._max_menu_index()

    def select(self) -> None:
        """
        TODO: Navigate to the selected sub menu if a Menu is selected or open the accompanying screen of the menu item.
        """
        print("Selected {}".format(self.get_child(self._current_menu_index).title))

    def _max_menu_index(self):
        return len(self._menu_components) - 1

    def _child_is_selected(self, menu: MenuComponent):
        return self._menu_components.index(menu) == self._current_menu_index
