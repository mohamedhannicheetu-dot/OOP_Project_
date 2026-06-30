from src.Song import Song
from src.AcousticSong import AcousticSong
from src.LiveRecording import LiveRecording
from src.Podcast import Podcast
from src.Playlist import Playlist
from src.Library import Library
from src.AudioContent import AudioContent

if __name__ == "__main__":

    # ── Create content ─────────────────────────────────
    song1    = Song("Bohemian Rhapsody", "Queen", 1975, 354, "Rock")
    song2    = Song("Blinding Lights", "The Weeknd", 2019, 200, "Synthpop")
    acoustic = AcousticSong("Blackbird", "The Beatles", 1968, 144, "Abbey Road Studios")
    live     = LiveRecording("Don't Stop Me Now", "Queen", 1979, 210, "Hammersmith Odeon", "London")
    podcast1 = Podcast("Lex Fridman Podcast", "Lex Fridman", 2024, 421, 195, "The Future of AI")
    podcast2 = Podcast("Huberman Lab", "Andrew Huberman", 2023, 88, 72, "Sleep & Recovery")

    # ── Library ────────────────────────────────────────
    library = Library("My Music Library")
    for item in [song1, song2, acoustic, live, podcast1, podcast2]:
        library.add(item)

    library.show_all()

    # ── Search ─────────────────────────────────────────
    print("=== Search by creator: Queen ===")
    results = library.find_by_creator("Queen")
    for r in results:
        print(f"  {r.get_info()}")

    print("\n=== Search by title: Blackbird ===")
    found = library.find_by_title("Blackbird")
    if found:
        print(f"  {found.get_info()}")

    # ── Playlist ───────────────────────────────────────
    playlist = Playlist("Evening Mix", "Alice")
    playlist.add(song1)
    playlist.add(acoustic)
    playlist.add(live)
    playlist.add(podcast1)

    playlist.show_contents()
    playlist.play_all()

    # ── Polymorphism demonstration ─────────────────────
    print("=== Polymorphism: skip_forward() differs by mechanism ===")
    items: list[AudioContent] = [song1, acoustic, live, podcast1]
    for item in items:
        new_pos = item.skip_forward(current_position_secs=20)
        print(f"  {type(item).__name__:15} | from 0:20s, skip_forward() -> {new_pos}s")

    # ── Abstraction test ───────────────────────────────
    print("\n=== Abstraction test ===")
    try:
        AudioContent("Test", "Nobody", 2024)
    except TypeError as e:
        print(f"  Cannot instantiate AudioContent directly: {e}")