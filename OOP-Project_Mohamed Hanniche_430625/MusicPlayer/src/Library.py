from .AudioContent import AudioContent


# ── COMPOSITION ────────────────────────────────────────
# Library holds the full collection of audio content.
# Also not part of the inheritance tree.
class Library:

    def __init__(self, name: str):
        self._name = name
        self._collection: list[AudioContent] = []

    def add(self, content: AudioContent):
        self._collection.append(content)

    def find_by_title(self, title: str) -> AudioContent | None:
        for item in self._collection:
            if item.get_title().lower() == title.lower():
                return item
        return None

    def find_by_creator(self, creator: str) -> list[AudioContent]:
        return [item for item in self._collection if item.get_creator().lower() == creator.lower()]

    def show_all(self):
        print(f"\n=== {self._name} — {len(self._collection)} item(s) ===")
        for item in self._collection:
            print(f"  {item.get_info()}")
        print()
