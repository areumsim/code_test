### Song


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_in_repeating_playlist(self):
        songSet = set([self.name])

        next = self.next
        while next is not None:
            if next.name in songSet:
                return True
            songSet.add(next.name)
            next = next.next

        return False


first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_in_repeating_playlist())
