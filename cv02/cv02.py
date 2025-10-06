#!/usr/bin/env python3

class LP():
    def __init__(self, name, release_date, artist, duration):
        self._name = name
        self._release_date = release_date
        self._artist = artist
        self._duration = duration

    def __str__(self):
        out = "| {1:^4} | {0:^20} | {2:^20} | {3:^8} |".format(self._name, self._release_date, self._artist, self._duration)
        return out

class Library():
    def __init__(self):
        self._library = list()

    def add_LP(self, lp):
        self._library.append(lp)

    def remove_LP(self, lp):
        self._library.remove(lp)

    def clean_library(self):
        self._library.clear()

    def print_library(self):
        print(str(self))

    def seed_library(self):
        self.add_LP(LP("Paradise City", 1989, "Guns n roses", 100))
        self.add_LP(LP("Swiming", 1989, "MAC Miller", 120))
        self.add_LP(LP("Banditi di prag", 2009, "KABAT", 90))

    def __str__(self):
        out =  "|{}|\n".format("-"*70);
        out += "|  ID  | YEAR |         NAME         |        ARTIST        | DURATION |\n"
        out += "|{}|\n".format("-"*70);
        i = 0
        for lp in self._library:
            out += "| {0:^4} {1}\n".format(i,str(lp));
            i+=1
        out += "|{}|\n".format("-"*70);
        return out

    def delete_LP_index(self, i):
        self._library.pop(i)

def main():
    library = Library();

    while True:
        print("|--------------------|")
        print("|        MENU        |")
        print("|--------------------|")
        print("(1) - add new LP")
        print("(2) - remove LP")
        print("(3) - clean library")
        print("(4) - print library")
        print("(5) - seed library")
        print("(q) - exit")

        choice = input("Enter your choice: ")

        if (choice[0] == "1"):
            name = input("Enter name: ")
            release_date = input("Enter release date: ")
            artist = input("Enter artist: ")
            duration = input("Enter duration: ")
            lp = LP(name, int (release_date), artist, int (duration))
            library.add_LP(lp)
            continue
        elif (choice[0] == "2"):
            library.print_library()
            i = input("enter ID to delete: ")
            try:
                index = int(i)
                library.delete_LP_index(index)
            except ValueError:
                input("ERROR: Invalid ID")
            except IndexError:
                input("ERROR: ID is out of range")
        elif (choice[0] == "3"):
            library.clean_library()
            continue
        elif (choice[0] == "4"):
            library.print_library()
            input("Press enter to continue...")
            continue
        elif (choice[0] == "5"):
            library.seed_library()
        elif (choice[0] == "q"):
            print("Goodbye!")
            exit(0)
if __name__ == "__main__":
    main()
