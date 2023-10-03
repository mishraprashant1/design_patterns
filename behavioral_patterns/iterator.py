"""
The Iterator Design Pattern is a behavioral pattern that provides a way to access the elements of an aggregate object
(like a collection) sequentially without exposing the underlying structure of the object. It separates the
responsibility of accessing elements from the object itself, making it easier to iterate over the elements and providing
a consistent way to do so.

Let's explore this pattern with a real-life example:

Real-Life Example Problem:

Imagine you're building a music player application, and you want to create a playlist feature that allows users to play
songs one by one or shuffle them. You need a way to access and manage the songs in a playlist without exposing the
internal details of how the songs are stored.

Solution with the Iterator Pattern:

To solve this problem, you can use the Iterator Design Pattern:

Aggregate (Playlist): This represents the collection of songs. It has a method to create an iterator that can traverse
the songs in the playlist.

Iterator: The iterator is responsible for accessing the elements (songs) in the collection (playlist). It defines
methods like next to get the next element and has_next to check if there are more elements.

Concrete Iterators: These are specific implementations of the iterator for different types of collections (e.g., sequential, shuffled).
"""

from abc import ABC, abstractmethod
import random


# Aggregate: Playlist
class Playlist(ABC):
    @abstractmethod
    def create_iterator(self):
        pass


# Iterator
class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


# Concrete Iterator: SequentialPlaylistIterator
class SequentialPlaylistIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.current_index = 0

    def next(self):
        if self.has_next():
            song = self.playlist.songs[self.current_index]
            self.current_index += 1
            return song
        else:
            return None

    def has_next(self):
        return self.current_index < len(self.playlist.songs)


# Concrete Iterator: ShuffledPlaylistIterator
class ShuffledPlaylistIterator(Iterator):
    def __init__(self, playlist):
        self.playlist = playlist
        self.shuffled_songs = list(playlist.songs)
        random.shuffle(self.shuffled_songs)
        self.current_index = 0

    def next(self):
        if self.has_next():
            song = self.shuffled_songs[self.current_index]
            self.current_index += 1
            return song
        else:
            return None

    def has_next(self):
        return self.current_index < len(self.shuffled_songs)


# Concrete Aggregate: ConcretePlaylist
class ConcretePlaylist(Playlist):
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def create_iterator(self, sequential=True):
        if sequential:
            return SequentialPlaylistIterator(self)
        else:
            return ShuffledPlaylistIterator(self)


# Client code
if __name__ == "__main__":
    # Create a playlist
    playlist = ConcretePlaylist()
    playlist.add_song("Song 1")
    playlist.add_song("Song 2")
    playlist.add_song("Song 3")

    # Create iterators for the playlist
    sequential_iterator = playlist.create_iterator(sequential=True)
    shuffled_iterator = playlist.create_iterator(sequential=False)

    # Play songs sequentially
    print("Playing songs sequentially:")
    while sequential_iterator.has_next():
        print(sequential_iterator.next())

    # Play songs shuffled
    print("\nPlaying songs shuffled:")
    while shuffled_iterator.has_next():
        print(shuffled_iterator.next())
