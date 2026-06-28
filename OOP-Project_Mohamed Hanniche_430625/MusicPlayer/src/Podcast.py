from .AudioContent import AudioContent


# ── INHERITANCE ────────────────────────────────────────
# Podcast inherits from AudioContent.
# Represents a podcast episode with a host and episode number.
class Podcast(AudioContent):

    def __init__(self, title: str, host: str, year: int, episode: int, duration_mins: int, topic: str):
        super().__init__(title, host, year)
        self._episode = episode
        self._duration_mins = duration_mins
        self._topic = topic

    def get_episode(self) -> int:
        return self._episode

    def get_topic(self) -> str:
        return self._topic

    # POLYMORPHISM — Podcast play() mentions episode number and topic
    def play(self) -> str:
        return (
            f"🎙  Playing '{self._title}' — Episode {self._episode}: {self._topic} "
            f"with {self._creator} [{self.get_duration_label()}]"
        )

    # POLYMORPHISM — Podcast shows duration in hours and minutes
    def get_duration_label(self) -> str:
        if self._duration_mins >= 60:
            hours = self._duration_mins // 60
            mins = self._duration_mins % 60
            return f"{hours}h {mins:02d}m"
        return f"{self._duration_mins}m"

    # POLYMORPHISM — Podcast summary includes episode and topic
    def get_info(self) -> str:
        return (
            f"[Podcast] {self._title} — Ep.{self._episode}: {self._topic} "
            f"| Host: {self._creator} | {self.get_duration_label()}"
        )
