import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.AudioContent import AudioContent
from src.Song import Song
from src.AcousticSong import AcousticSong
from src.LiveRecording import LiveRecording
from src.Podcast import Podcast
from src.Playlist import Playlist
from src.Library import Library


# ── ABSTRACTION ────────────────────────
class TestAbstraction(unittest.TestCase):

    def test_audio_content_is_abstract(self):
        with self.assertRaises(TypeError):
            AudioContent("Title", "Creator", 2024)


# ── SONG ─────────────

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Bohemian Rhapsody", "Queen", 1975, 354, "Rock")

    def test_attributes(self):
        self.assertEqual(self.song.get_title(), "Bohemian Rhapsody")
        self.assertEqual(self.song.get_creator(), "Queen")
        self.assertEqual(self.song.get_year(), 1975)
        self.assertEqual(self.song.get_genre(), "Rock")

    def test_duration_label(self):
        self.assertEqual(self.song.get_duration_label(), "5:54")

    def test_duration_label_zero_seconds(self):
        s = Song("Test", "Artist", 2020, 180, "Pop")
        self.assertEqual(s.get_duration_label(), "3:00")

    def test_play_output(self):
        result = self.song.play()
        self.assertIn("Bohemian Rhapsody", result)
        self.assertIn("Queen", result)
        self.assertIn("5:54", result)

    def test_get_info(self):
        info = self.song.get_info()
        self.assertIn("Song", info)
        self.assertIn("Bohemian Rhapsody", info)
        self.assertIn("Rock", info)


# ── ACOUSTIC SONG ──────

class TestAcousticSong(unittest.TestCase):

    def setUp(self):
        self.acoustic = AcousticSong("Blackbird", "The Beatles", 1968, 144, "Abbey Road Studios")

    def test_attributes(self):
        self.assertEqual(self.acoustic.get_title(), "Blackbird")
        self.assertEqual(self.acoustic.get_venue(), "Abbey Road Studios")
        self.assertEqual(self.acoustic.get_genre(), "Acoustic")

    def test_play_output(self):
        result = self.acoustic.play()
        self.assertIn("Blackbird", result)
        self.assertIn("Abbey Road Studios", result)

    def test_get_info(self):
        info = self.acoustic.get_info()
        self.assertIn("Acoustic", info)
        self.assertIn("Abbey Road Studios", info)


# ── LIVE RECORDING ──────────────────────────

class TestLiveRecording(unittest.TestCase):

    def setUp(self):
        self.live = LiveRecording("Don't Stop Me Now", "Queen", 1979, 210, "Hammersmith Odeon", "London")

    def test_attributes(self):
        self.assertEqual(self.live.get_concert_venue(), "Hammersmith Odeon")
        self.assertEqual(self.live.get_city(), "London")
        self.assertEqual(self.live.get_genre(), "Live")

    def test_play_output(self):
        result = self.live.play()
        self.assertIn("Don't Stop Me Now", result)
        self.assertIn("Hammersmith Odeon", result)
        self.assertIn("London", result)

    def test_get_info(self):
        info = self.live.get_info()
        self.assertIn("Live", info)
        self.assertIn("London", info)


# ── PODCAST ──────

class TestPodcast(unittest.TestCase):

    def setUp(self):
        self.podcast = Podcast("Lex Fridman Podcast", "Lex Fridman", 2024, 421, 195, "The Future of AI")

    def test_attributes(self):
        self.assertEqual(self.podcast.get_title(), "Lex Fridman Podcast")
        self.assertEqual(self.podcast.get_episode(), 421)
        self.assertEqual(self.podcast.get_topic(), "The Future of AI")

    def test_duration_over_one_hour(self):
        self.assertEqual(self.podcast.get_duration_label(), "3h 15m")

    def test_duration_under_one_hour(self):
        p = Podcast("Test", "Host", 2024, 1, 45, "Topic")
        self.assertEqual(p.get_duration_label(), "45m")

    def test_duration_exactly_one_hour(self):
        p = Podcast("Test", "Host", 2024, 1, 60, "Topic")
        self.assertEqual(p.get_duration_label(), "1h 00m")

    def test_play_output(self):
        result = self.podcast.play()
        self.assertIn("Episode 421", result)
        self.assertIn("The Future of AI", result)
        self.assertIn("Lex Fridman", result)

    def test_get_info(self):
        info = self.podcast.get_info()
        self.assertIn("Podcast", info)
        self.assertIn("Ep.421", info)


# ── POLYMORPHISM ─────

# ── POLYMORPHISM ─────
class TestPolymorphism(unittest.TestCase):

    def test_all_types_return_string_from_play(self):
        items = [
            Song("S", "A", 2020, 200, "Rock"),
            AcousticSong("S", "A", 2020, 200, "Venue"),
            LiveRecording("S", "A", 2020, 200, "Venue", "City"),
            Podcast("P", "H", 2020, 1, 60, "Topic"),
        ]
        for item in items:
            self.assertIsInstance(item.play(), str)

    def test_duration_label_format_differs_by_type(self):
        song    = Song("S", "A", 2020, 200, "Rock")
        podcast = Podcast("P", "H", 2020, 1, 195, "Topic")
        self.assertIn(":", song.get_duration_label())
        self.assertIn("h", podcast.get_duration_label())

    def test_play_outputs_differ_between_song_and_live(self):
        song = Song("Same Title", "Queen", 1975, 200, "Rock")
        live = LiveRecording("Same Title", "Queen", 1975, 200, "Wembley", "London")
        self.assertNotEqual(song.play(), live.play())

    def test_skip_forward_mechanisms_differ_by_type(self):
        song = Song("Song Title", "Artist", 2020, 200, "Rock")
        podcast = Podcast("Podcast Title", "Host", 2020, 1, 60, "Topic")
        live = LiveRecording("Live Title", "Artist", 2020, 200, "Venue", "City")

        # 1. Song should skip forward by 10 seconds (20 -> 30)
        self.assertEqual(song.skip_forward(20), 30)

        # 2. Podcast should skip forward by 30 seconds (20 -> 50)
        self.assertEqual(podcast.skip_forward(20), 50)

        # 3. Live Recording should jump straight to the end (20 -> 200)
        self.assertEqual(live.skip_forward(20), 200)

# ── PLAYLIST ───────────
class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("My List", "Alice")
        self.song = Song("S1", "A", 2020, 200, "Rock")

    def test_add_and_count(self):
        self.playlist.add(self.song)
        self.assertEqual(self.playlist.count(), 1)

    def test_remove_existing(self):
        self.playlist.add(self.song)
        result = self.playlist.remove("S1")
        self.assertTrue(result)
        self.assertEqual(self.playlist.count(), 0)

    def test_remove_nonexistent(self):
        result = self.playlist.remove("Ghost Song")
        self.assertFalse(result)

    def test_play_all_output(self):
        from io import StringIO
        self.playlist.add(Song("Bohemian Rhapsody", "Queen", 1975, 354, "Rock"))
        captured = StringIO()
        sys.stdout = captured
        self.playlist.play_all()
        sys.stdout = sys.__stdout__
        self.assertIn("Bohemian Rhapsody", captured.getvalue())


# ── LIBRARY ──────────────────────────

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = Library("My Library")
        self.s1 = Song("Bohemian Rhapsody", "Queen", 1975, 354, "Rock")
        self.s2 = Song("Don't Stop Me Now", "Queen", 1978, 210, "Rock")
        self.s3 = Song("Blinding Lights", "The Weeknd", 2019, 200, "Synthpop")
        for s in [self.s1, self.s2, self.s3]:
            self.lib.add(s)

    def test_find_by_title(self):
        found = self.lib.find_by_title("Bohemian Rhapsody")
        self.assertIs(found, self.s1)

    def test_find_by_title_case_insensitive(self):
        found = self.lib.find_by_title("bohemian rhapsody")
        self.assertIs(found, self.s1)

    def test_find_by_title_not_found(self):
        found = self.lib.find_by_title("Nonexistent")
        self.assertIsNone(found)

    def test_find_by_creator(self):
        results = self.lib.find_by_creator("Queen")
        self.assertEqual(len(results), 2)

    def test_find_by_creator_case_insensitive(self):
        results = self.lib.find_by_creator("queen")
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
