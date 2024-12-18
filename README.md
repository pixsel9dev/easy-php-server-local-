PHP Local Server - README
Genel Açıklama (TR)
Bu program ile belirlediğiniz bir dizindeki PHP dosyalarını yerel sunucu üzerinden yayınlayabilirsiniz. Programda port numarasını ve PHP dosyalarının bulunduğu dizini seçtikten sonra PHP dosyalarınız yayına alınır. Ayrıca, proje dizininde birden fazla klasör ve dosya varsa, tüm PHP dosyaları yayına alınacaktır.

Program Kullanımı
1. Port Seçimi
İlk olarak, yayına almak istediğiniz port numarasını girmeniz gerekir (örneğin, 8000). Port numarasını seçerken, bu portun başka bir işlem tarafından kullanılmadığından emin olun.

2. Dizin Seçimi
Daha sonra, PHP dosyalarınızın bulunduğu dizini seçmeniz gerekecek. Eğer dizin geçerli değilse, program sizi uyaracaktır. Program, belirtilen dizindeki PHP dosyalarını yayına alacaktır. Eğer proje dizininde birden fazla klasör ve PHP dosyası varsa, bunların tümü yayına alınacaktır.

3. PHP Şartı
PHP'nin sisteminizde yüklü olması gerekmektedir. PHP'nin kurulu olup olmadığını kontrol etmek için terminal veya komut istemcisinde php -v komutunu çalıştırabilirsiniz. Eğer PHP kurulu değilse, PHP'yi sisteminize yüklemeniz gerekecektir.

PHP Yükleme:
PHP'yi yüklemek için sistem değişkenlerine (PATH) PHP'nin bulunduğu dizini eklemeniz gerekebilir. PHP'nin doğru şekilde yüklendiğini kontrol etmek için php -v komutunu kullanabilirsiniz.

4. Loglar
Programda, PHP sunucusunun çalıştığı süre boyunca logları rahatça görebilirsiniz. Eğer herhangi bir hata oluşursa, burada görüntülenir. Loglar, gelişen hataların tespit edilmesine yardımcı olabilir.

5. Sunucu Kapatma
Program çalıştığı sürece PHP sunucusu aktif kalır. Sunucu kapanması için Ctrl + C tuşlarına basarak programdan çıkabilirsiniz. Bu işlem sunucuyu güvenli bir şekilde kapatacaktır.

Sistem Gereksinimleri
Python 3.x: Program Python 3.x sürümüyle uyumludur.
PHP: PHP'nin yüklü olması gerekmektedir. PHP'yi yüklemek ve kontrol etmek için php -v komutunu kullanabilirsiniz.
Terminal/Komut İstemcisi: Programın çalışabilmesi için terminal veya komut istemcisinin erişilebilir olması gerekmektedir.
Katkıda Bulunma
Programa katkıda bulunabilirsiniz, ancak lütfen bu projede ana yapımcı olarak beni kabul edin. Herhangi bir katkı yaparken, başkalarına saygılı ve açık bir şekilde katkıda bulunun. Yapılan her katkı, projeye dahil edilmeden önce gözden geçirilecektir.

English Version
This program allows you to publish PHP files locally by selecting a directory containing PHP files and choosing a port number. If there are multiple directories with PHP and other files in the project directory, they will also be published.

Usage
1. Port Selection
First, you need to enter the port number you want to use for the local server (for example, 8000). Ensure that the port you choose is not already being used by another process.

2. Directory Selection
Then, you need to select the directory containing your PHP files. If the directory is invalid, the program will warn you. The program will publish all PHP files in the given directory. If there are multiple directories and PHP files in the project directory, they will all be published.

3. PHP Requirement
PHP must be installed on your system. To check if PHP is installed, you can run the php -v command in your terminal or command prompt. If PHP is not installed, you will need to install it.

PHP Installation:
You may need to add PHP's path to your system environment variables (PATH) for proper operation. You can verify if PHP is correctly installed using the php -v command.

4. Logs
You can easily view logs of the PHP server's activity throughout its operation. Any errors will be displayed here as well. These logs help in diagnosing any issues or errors during the program’s operation.

5. Server Shutdown
The server remains active while the program is running. To stop the server, press Ctrl + C to terminate the program. This will safely shut down the server.

System Requirements
Python 3.x: The program is compatible with Python 3.x.
PHP: PHP must be installed. Use php -v to verify the installation.
Terminal/Command Prompt: Access to a terminal or command prompt is required for the program to function.
Contributing
You are welcome to contribute to the project, but please acknowledge me as the main developer of the project. When contributing, make sure to be respectful and clear. All contributions will be reviewed before being merged into the project.
