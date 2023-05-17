class TransactionQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, transaction):
        self.queue.append(transaction)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]


class Transaction:
    def __init__(self, customer_name, transaction_type):
        self.customer_name = customer_name
        self.transaction_type = transaction_type


transaction_queue = TransactionQueue()

while True:
    print("\n=== Menu ===")
    print("1. Tambahkan Transaksi")
    print("2. Layani Transaksi Berikutnya")
    print("3. Hapus Transaksi yang Telah Dilayani")
    print("0. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        customer_name = input("Masukkan nama pelanggan: ")
        transaction_type = input("Masukkan jenis transaksi: ")
        transaction = Transaction(customer_name, transaction_type)
        transaction_queue.enqueue(transaction)
        print("Transaksi ditambahkan ke dalam antrean.")

    elif choice == "2":
        if transaction_queue.is_empty():
            print("Antrean transaksi kosong.")
        else:
            next_transaction = transaction_queue.dequeue()
            print(
                f"Transaksi berikutnya: {next_transaction.customer_name} - {next_transaction.transaction_type}")

    elif choice == "3":
        if transaction_queue.is_empty():
            print("Antrean transaksi kosong.")
        else:
            removed_transaction = transaction_queue.dequeue()
            print(
                f"Transaksi {removed_transaction.customer_name} - {removed_transaction.transaction_type} telah dihapus.")

    elif choice == "0":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
