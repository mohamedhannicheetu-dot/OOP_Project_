OOP Music Player 

Topic: Music

Idea: A music player

Classes:
- AudioContent (abstract base class)
- Song (inherits AudioContent)
- AcousticSong (inherits Song)
- LiveRecording (inherits Song)
- Podcast (inherits AudioContent)
- Playlist (composition)
- Library (composition)

OOP Concepts used:
- Abstraction: AudioContent cannot be instantiated directly
- Inheritance: Song, Podcast inherit from AudioContent
              AcousticSong and LiveRecording inherit from Song
- Encapsulation: protected attributes with getters.
- Polymorphism: play(), get_duration_label(), get_info()
                
Tests: unittest covering all classes (30 tests)
