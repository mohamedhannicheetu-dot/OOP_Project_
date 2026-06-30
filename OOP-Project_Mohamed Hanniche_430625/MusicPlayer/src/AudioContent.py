from abc import ABC, abstractmethod


# ── ABSTRACTION ───────────────────────────────────────
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
    def skip_forward(self, current_position_secs: int) -> int:
        """
        Given the current playback position, return the new position
        after pressing the skip-forward button. Different content
        types skip differently because of how they are structured —
        a song can be skipped second-by-second, but a live recording
        has no clean mid-song jump points, so it skips to the start
        of the next track instead.
        """
        pass

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