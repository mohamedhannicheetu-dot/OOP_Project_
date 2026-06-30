from .Song import Song


# ── INHERITANCE (2nd level) ────────────────────────────
# LiveRecording inherits from Song
class LiveRecording(Song):

    def __init__(self, title: str, artist: str, year: int, duration_secs: int, concert_venue: str, city: str):
        super().__init__(title, artist, year, duration_secs, genre="Live")
        self._concert_venue = concert_venue
        self._city = city

    def get_concert_venue(self) -> str:
        return self._concert_venue

    def get_city(self) -> str:
        return self._city

    # POLYMORPHISM — a live recording has no clean mid-song seek
    def skip_forward(self, current_position_secs: int) -> int:
        return self._duration_secs

    # POLYMORPHISM — LiveRecording play() mentions venue and city
    def play(self) -> str:
        return (
            f"♪  Playing LIVE '{self._title}' by {self._creator} "
            f"@ {self._concert_venue}, {self._city} [{self.get_duration_label()}]"
        )

    # POLYMORPHISM — LiveRecording's summary includes concert details
    def get_info(self) -> str:
        return (
            f"[Live] {self._title} — {self._creator} ({self._year}) "
            f"| {self._concert_venue}, {self._city} | {self.get_duration_label()}"
        )