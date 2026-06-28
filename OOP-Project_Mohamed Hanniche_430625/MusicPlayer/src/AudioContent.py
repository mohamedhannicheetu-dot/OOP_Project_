from abc import ABC, abstractmethod


# ── ABSTRACTION ────────────────────────────────────────
# AudioContent is the abstract base class for all playable
# content. It cannot be instantiated directly.
class AudioContent(ABC):

    def __init__(self, title: str, creator: str, year: int):
        self._title = title       # protected attributes (ENCAPSULATION)
        self._creator = creator
        self._year = year

    # Getters — controlled access to internal data
    def get_title(self) -> str:
        return self._title

    def get_creator(self) -> str:
        return self._creator

    def get_year(self) -> int:
        return self._year

    # Abstract methods — every subclass MUST implement these
    @abstractmethod
    def play(self) -> str:
        """Return a string describing what happens when this content plays."""
        pass

    @abstractmethod
    def get_duration_label(self) -> str:
        """Return a human-readable duration string (format varies by type)."""
        pass

    @abstractmethod
    def get_info(self) -> str:
        """Return a summary line describing this content."""
        pass
