from .AudioContent import AudioContent


# ── COMPOSITION ────────────────────────────────────────
# Playlist is composed of AudioContent objects.
class Playlist:

    def __init__(self, name: str, owner: str):
        self._name = name
        self._owner = owner
        self._items: list[AudioContent] = []

    def get_name(self) -> str:
        return self._name

    def get_owner(self) -> str:
        return self._owner

    def add(self, content: AudioContent):
        self._items.append(content)

    def remove(self, title: str):
        for item in self._items:
            if item.get_title() == title:
                self._items.remove(item)
                return True
        return False

    def count(self) -> int:
        return len(self._items)

    # POLYMORPHISM 
    def play_all(self):
        print(f"\n=== {self._name} (owner: {self._owner}) ===")
        if not self._items:
            print("  (playlist is empty)")
            return
        for item in self._items:
            print(" ", item.play())
        print()

    def show_contents(self):
        print(f"\nPlaylist: '{self._name}' — {self.count()} item(s)")
        for i, item in enumerate(self._items, 1):
            print(f"  {i}. {item.get_info()}")
        print()
