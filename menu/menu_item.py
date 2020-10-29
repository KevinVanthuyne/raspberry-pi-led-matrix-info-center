from menu.menu_component import MenuComponent


class MenuItem(MenuComponent):

    def display(self) -> None:
        print("-- {}".format(self.title))
