import os
import shutil
import time
import argparse
from colorama import init, Fore

def take_backup(src_folder, dest_folder, auto=False):
    try:
        backup_filename = f"backup_{time.strftime('%d-%m-%Y_%H.%M.%S')}"
        dest_file = os.path.join(dest_folder, backup_filename)
        if auto:
            shutil.make_archive(dest_file, 'zip', src_folder)
        else:
            shutil.make_archive(dest_file, 'zip', src_folder)
            print(f"{Fore.GREEN}{time.strftime('%H:%M:%S')} [info]{Fore.RESET} Backup Alındı! Dosya Yolu: {dest_file}")
    except Exception as e:
        print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} Bir hata oluştu: {e}")

def print_help():
    print("Kullanım: backup.py [OPTIONS]")
    print("Seçenekler:")
    print("--backup now        : Anlık Yedek Alır.")
    print("--backup (sayı)     : Belirli saat aralıklarıyla otomatik yedek alır.")
    print("                      Örnek: --backup 2 (Burada 2 Saat aralıkla Yedek Alıyor.)")

if __name__ == "__main__":
    init()  
    src_folder = "C:\\xampp\\htdocs" 
    dest_folder = "C:\\xampp\\Backup"  

    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", nargs="?", const="now", help="Belirli saat aralıklarıyla otomatik Yedek Alır. Örnek: --backup 2 (2 saat aralıklarla yedek alınır.)")
    args = parser.parse_args()

    if not args.backup or args.backup in ['-h', '--help']:
        print_help()
    elif args.backup:
        if args.backup == "now":
            take_backup(src_folder, dest_folder, False)
        else:
            try:
                interval_hours = int(args.backup)
                print(f"{Fore.GREEN}{time.strftime('%H:%M:%S')} [info]{Fore.RESET} {interval_hours} Saat Aralıkla Düzenli Olarak {dest_folder} Yolundaki Klasöre Backup Alınacak.")
                while True:
                    take_backup(src_folder, dest_folder, True)
                    time.sleep(interval_hours * 3600)
            except ValueError:
                 print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} Lütfen Bir Sayı Girin.")
            except KeyboardInterrupt:
                 print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} CTRL+C Yapıldı!\nİşlem İptal Ediliyor...")
                 time.sleep(3);
                 exit(f"{Fore.RED}{time.strftime('%H:%M:%S')} Çıkış yapılıyor...")
