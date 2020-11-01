from menu.menu_component import MenuComponent


class MenuItem(MenuComponent):
    """ Leaf menu object that has no submenu's """

    def get_child(self, index: int) -> None:
        """ :return: None because MenuItems don't have sub menus. """
        return None

    def add(self, composite_menu: MenuComponent) -> None:
        """ Submenu's can't be added to MenuItems. """
        raise NotImplemented

    def display(self, selected: bool = False) -> None:
        """
        Prints the menu item to the console.
        :param selected: if the current menu is selected or not.
        """
        if selected:
            print("  {}".format(self.title))
        else:
            print("> {}".format(self.title))

    def next(self) -> None:
        """ Menu items don't contain other menu items so next item can't be selected """
        raise NotImplemented

    def previous(self) -> None:
        """ Menu items don't contain other menu items so previous item can't be selected """
        raise NotImplemented

    def select(self) -> None:
        """ TODO: Selecting a MenuItem will open the accompanying screen """
        raise NotImplemented
