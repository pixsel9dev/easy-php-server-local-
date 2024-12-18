import os  
import subprocess

def start_php_server(directory, port):
    os.chdir(directory)  # Çalışma dizinini belirtilen dizine değiştir

    # PHP'nin yerleşik sunucusunu başlat (0.0.0.0 ile tüm ağ arayüzlerinden erişilebilir)
    command = f"php -S 0.0.0.0:{port}"
    try:
        process = subprocess.Popen(command, shell=True)
        print(f"PHP sunucusu başlatıldı: http://0.0.0.0:{port}")
        return process
    except Exception as e:
        print(f"Sunucu başlatılırken bir hata oluştu: {e}")
        return None

def find_php_file(directory):
    # Dizi içindeki tüm .php dosyalarını bul
    php_files = [f for f in os.listdir(directory) if f.endswith('.php')]
    
    # index.php öncelikli olarak kontrol edilir
    if "index.php" in php_files:
        print("index.php dosyası bulundu.")
        return "index.php"
    
    # Diğer php dosyalarını kontrol et
    if php_files:
        first_php_file = php_files[0]  # İlk bulunan PHP dosyasını al
        print(f"{first_php_file} dosyası bulundu. Sunucu başlatılacak...")
        return first_php_file
    
    print("Hiçbir PHP dosyası bulunamadı.")
    return None

def main():
    print("Yerel PHP Sunucu Yayınlama Programı")

    # Kullanıcıdan port ve dosya dizini al
    while True:
        try:
            port = int(input("Kullanmak istediğiniz port (örneğin: 8000): "))
            break
        except ValueError:
            print("Lütfen geçerli bir port numarası girin.")

    while True:
        directory = input("Yayınlamak istediğiniz PHP dosyalarının dizinini girin: ")
        # Dizin var mı kontrol et
        if os.path.isdir(directory):
            break
        else:
            print("Verilen dizin mevcut değil. Lütfen geçerli bir dizin girin.")

    # PHP dosyasını bul
    php_file = find_php_file(directory)

    if php_file is None:
        print("PHP dosyası bulunamadı, program sonlandırılıyor.")
        return

    # Sunucuyu başlat
    print(f"PHP sunucusu başlatılıyor... (0.0.0.0:{port})")
    server_process = start_php_server(directory, port)

    if server_process is None:
        print("Sunucu başlatılamadı, program sonlandırılıyor.")
        return

    try:
        while True:
            pass  # Sunucu çalışmaya devam eder
    except KeyboardInterrupt:
        print("\nSunucu durduruluyor...")
        server_process.terminate()
        print("Sunucu kapatıldı.")

if __name__ == "__main__":
    main()
