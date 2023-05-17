class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


def add_book(stack):
    title = input("Masukkan judul buku: ")
    author = input("Masukkan pengarang buku: ")
    book = Book(title, author)
    stack.push(book)
    print("Buku berhasil ditambahkan ke dalam tumpukan.")


def remove_book(stack):
    if not stack.is_empty():
        removed_book = stack.pop()
        print(
            f"Buku '{removed_book.title}' oleh {removed_book.author} dihapus dari tumpukan.")
    else:
        print("Tumpukan kosong. Tidak ada buku yang dapat dihapus.")


def display_top_book(stack):
    if not stack.is_empty():
        top_book = stack.peek()
        print("Buku teratas:")
        print(f"Judul: {top_book.title}")
        print(f"Pengarang: {top_book.author}")
    else:
        print("Tumpukan kosong. Tidak ada buku yang ditampilkan.")


def main():
    stack = Stack()
    while True:
        print("\nPilih operasi:")
        print("1. Tambahkan buku")
        print("2. Hapus buku terakhir")
        print("3. Tampilkan buku teratas")
        print("4. Keluar")
        choice = input("Masukkan pilihan (1/2/3/4): ")

        if choice == "1":
            add_book(stack)
        elif choice == "2":
            remove_book(stack)
        elif choice == "3":
            display_top_book(stack)
        elif choice == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
