class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


word = Text("hello")
print(word.duplicate())
Tlist = TrackableList();
Tlist.append(5)
Tlist.append(6)
print(Tlist)