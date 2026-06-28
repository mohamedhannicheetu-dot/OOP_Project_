from .AudioContent import AudioContent


# ── INHERITANCE ────────────────────────────────────────
# Song inherits from AudioContent.
# Represents a single music track with an artist and duration.
class Song(AudioContent):

    def __init__(self, title: str, artist: str, year: int, duration_secs: int, genre: str):
        super().__init__(title, artist, year)
        self._duration_secs = duration_secs
        self._genre = genre

    def get_genre(self) -> str:
        return self._genre

    # POLYMORPHISM — Song's version of play()
    def play(self) -> str:
        return f"♪  Playing '{self._title}' by {self._creator} [{self.get_duration_label()}]"

    # POLYMORPHISM — Song shows duration as m:ss
    def get_duration_label(self) -> str:
        mins, secs = divmod(self._duration_secs, 60)
        return f"{mins}:{secs:02d}"

    # POLYMORPHISM — Song's summary includes genre
    def get_info(self) -> str:
        return (
            f"[Song] {self._title} — {self._creator} "
            f"({self._year}) | {self._genre} | {self.get_duration_label()}"
        )
