from __future__ import annotations

from abc import ABC, abstractmethod


class MenuComponent(ABC):
    """  Abstract menu component, extended by Menu and MenuItem. """

    def __init__(self, title: str) -> None:
        super().__init__()
        self.title = title

    @property
    def title(self) -> str:
        """ Title of the menu to display. """
        return self._title

    @title.setter
    def title(self, title: str) -> None:
        self._title = title

    @abstractmethod
    def get_child(self, index: int) -> MenuComponent:
        """ Get the child composite menu with the given index of this menu if it has one. """
        raise NotImplemented

    @abstractmethod
    def add(self, composite_menu: MenuComponent) -> None:
        """ Add a composite menu to this menu. """
        raise NotImplemented

    @abstractmethod
    def display(self, selected: bool = False) -> None:
        """
        Displays the menu.
        :param selected: if the current menu is selected or not.
        """
        raise NotImplemented

    @abstractmethod
    def next(self) -> None:
        """ Go to the next menu item in the list. """
        raise NotImplemented

    @abstractmethod
    def previous(self) -> None:
        """ Go to the previous menu item in the list. """
        raise NotImplemented

    @abstractmethod
    def select(self) -> None:
        """ Select the current menu item. """
        raise NotImplemented
