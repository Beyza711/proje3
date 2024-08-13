from inventory import Item, Inventory

def main():
    """
    Kullanıcı etkileşimi için ana fonksiyon.
    Bu fonksiyon, kullanıcıya envanter yönetim sistemi ile ilgili seçenekler sunar
    ve kullanıcının seçimine göre işlemler yapar.
    """
    # Inventory sınıfından bir envanter nesnesi oluşturur
    inventory = Inventory()

    while True:
        # Kullanıcıya seçenekleri sunar
        print("\nEnvanter Yönetim Sistemi")
        print("1. Öğe Ekle")
        print("2. Öğe Güncelle")
        print("3. Öğe Kaldır")
        print("4. Tüm Öğeleri Listele")
        print("5. Çıkış")

        # Kullanıcının seçimini alır
        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            # Kullanıcıdan yeni öğe bilgilerini alır ve envantere ekler
            item_id = input("Öğe ID: ")
            name = input("Öğe Adı: ")
            quantity = int(input("Miktar: "))
            price = float(input("Fiyat: "))
            item = Item(item_id, name, quantity, price)
            inventory.add_item(item)
        elif choice == '2':
            # Kullanıcıdan güncellenecek öğe bilgilerini alır ve öğeyi günceller
            item_id = input("Güncellenecek Öğe ID: ")
            quantity = input("Yeni Miktar (boş bırakabilirsiniz): ")
            price = input("Yeni Fiyat (boş bırakabilirsiniz): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None
            inventory.update_item(item_id, quantity, price)
        elif choice == '3':
            # Kullanıcıdan kaldırılacak öğenin ID'sini alır ve öğeyi envanterden kaldırır
            item_id = input("Kaldırılacak Öğe ID: ")
            inventory.remove_item(item_id)
        elif choice == '4':
            # Envanterdeki tüm öğeleri listeler
            inventory.list_items()
        elif choice == '5':
            # Programı sonlandırır
            break
        else:
            # Geçersiz seçenek yapıldığında uyarı mesajı verir
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main()
