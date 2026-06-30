from .Song import Song


# ── INHERITANCE (2nd level) ─────────────────────
class AcousticSong(Song):

    def __init__(self, title: str, artist: str, year: int, duration_secs: int, venue: str):
        super().__init__(title, artist, year, duration_secs, genre="Acoustic")
        self._venue = venue

    def get_venue(self) -> str:
        return self._venue

    # POLYMORPHISM — AcousticSong plays differently, mentioning the venue.
    def play(self) -> str:
        return (
            f"♪  Playing acoustic version of '{self._title}' by {self._creator} "
            f"(recorded at {self._venue}) [{self.get_duration_label()}]"
        )

    # POLYMORPHISM — AcousticSong's summary includes venue
    def get_info(self) -> str:
        return (
            f"[Acoustic] {self._title} — {self._creator} "
            f"({self._year}) | Recorded at {self._venue} | {self.get_duration_label()}"
        )