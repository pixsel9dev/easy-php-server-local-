PHP Local Server Starter
Türkçe Açıklama
Bu Python programı, belirtilen bir dizindeki PHP dosyalarını çalıştırarak yerel bir PHP sunucusu başlatmanıza olanak sağlar. Kullanıcı, sunucu için bir port numarası seçebilir ve PHP dosyalarını barındıracak bir dizin belirtir. Program, index.php dosyasını öncelikli olarak arar. Eğer index.php dosyası bulunmazsa, dizinde bulunan ilk PHP dosyasını çalıştırır.

Özellikler:
PHP yerleşik sunucusunu başlatır.
Kullanıcıdan port ve dosya dizini bilgisi alır.
PHP dosyalarını otomatik olarak bulur ve sunucuyu çalıştırır.
Sunucu başlatıldığında, belirtilen port üzerinden erişim sağlanabilir.
Gereksinimler:
Python 3.x
PHP'nin sisteminizde yüklü olması gerekiyor. PHP'nin yüklü olup olmadığını terminal üzerinden php -v komutuyla kontrol edebilirsiniz.
Kullanım:
Python dosyasını çalıştırın.
Port numarası girin (örneğin: 8000).
PHP dosyalarınızı barındıracak dizini belirtin.
Program, dizindeki PHP dosyasını bulacak ve PHP yerleşik sunucusunu başlatacaktır.
Sunucuyu durdurmak için Ctrl + C tuşlarını kullanabilirsiniz.
Kurulum:
PHP'yi indirip sisteminize kurun. PHP'nin sisteminize düzgün bir şekilde kurulup kurulmadığını terminal üzerinden şu komutla kontrol edebilirsiniz:
bash
Kodu kopyala
php -v
Python'un sisteminizde yüklü olması gerekir. Python'un yüklü olup olmadığını kontrol etmek için terminale şu komutu yazabilirsiniz:
bash
Kodu kopyala
python --version
Python programını çalıştırmak için terminal veya komut satırında şu komutu kullanabilirsiniz:
bash
Kodu kopyala
python php_local_server.py
Python Dosyasının Çalıştırılması:
bash
Kodu kopyala
$ python php_local_server.py
Örnek Çıktı:
javascript
Kodu kopyala
Yerel PHP Sunucu Yayınlama Programı
Kullanmak istediğiniz port (örneğin: 8000): 8000
Yayınlamak istediğiniz PHP dosyalarının dizinini girin: /path/to/php/files
index.php dosyası bulundu.
PHP sunucusu başlatılıyor... (0.0.0.0:8000)
PHP sunucusu başlatıldı: http://0.0.0.0:8000
Sunucu çalıştıktan sonra http://0.0.0.0:8000 adresinden PHP dosyanız erişilebilir olacaktır.

English Description
This Python program allows you to start a local PHP server by running PHP files from a specified directory. The user can select a port number for the server and provide a directory to host the PHP files. The program first looks for an index.php file. If index.php is not found, it will run the first PHP file it finds in the directory.

Features:
Starts the built-in PHP server.
Takes user input for the port and directory containing PHP files.
Automatically finds PHP files and runs them.
Once the server is started, it can be accessed through the specified port.
Requirements:
Python 3.x
PHP must be installed on your system. You can check if PHP is installed by running the php -v command in your terminal.
Usage:
Run the Python script.
Enter a port number (e.g., 8000).
Specify the directory where your PHP files are located.
The program will find the PHP file in the specified directory and start the PHP server.
To stop the server, press Ctrl + C.
Installation:
Download and install PHP. You can check if PHP is installed by running the following command in the terminal:
bash
Kodu kopyala
php -v
Make sure Python is installed on your system. You can check the version by running:
bash
Kodu kopyala
python --version
To run the Python program, use the following command in your terminal or command prompt:
bash
Kodu kopyala
python php_local_server.py
Running the Python Script:
bash
Kodu kopyala
$ python php_local_server.py
Sample Output:
yaml
Kodu kopyala
Local PHP Server Starter
Enter the port you want to use (e.g., 8000): 8000
Enter the directory containing PHP files: /path/to/php/files
index.php file found.
Starting PHP server... (0.0.0.0:8000)
PHP server started: http://0.0.0.0:8000
After the server starts, you can access your PHP file at http://0.0.0.0:8000.

Programın Çalışma Mantığı:
Kullanıcı Girdisi: Program, kullanıcıdan port numarası ve PHP dosyalarının bulunduğu dizini alır.
PHP Dosyasının Bulunması: Belirtilen dizinde önce index.php dosyası aratılır. Eğer bulunmazsa, ilk bulunan PHP dosyası kullanılır.
Sunucu Başlatılması: PHP'nin yerleşik sunucusu, belirtilen port üzerinden başlatılır ve kullanıcıya sunucunun çalıştığı adres gösterilir.
Sunucu Yönetimi: Program, sunucu çalışırken durmaksızın devam eder. Sunucuyu durdurmak için Ctrl + C tuşlarına basılabilir.
