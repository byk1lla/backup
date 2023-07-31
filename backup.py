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
            print(f"{Fore.GREEN}{time.strftime('%H:%M:%S')} [info]{Fore.RESET} Backup Received! File Path: {dest_file}")
    except Exception as e:
        print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} An error occurred: {e}")
def print_help():
    print("Use: backup.py [OPTIONS]")
    print("Options:")
    print("--backup now : Takes Instant Backup.")
    print("--backup (number) : Takes automatic backups at specific time intervals.")
    print(" Example: --backup 2 (Here it takes backups at 2 hour intervals.)")

if __name__ == "__main__":
    init()  
    src_folder = "C:\\xampp\\htdocs" 
    dest_folder = "C:\\xampp\\Backup"  

    parser = argparse.ArgumentParser()
    parser.add_argument("--backup", nargs="?", const="now", help="Automatic Backup at certain time intervals. Example: --backup 2 (Takes backups at 2 hour intervals.)")
    args = parser.parse_args()

    if not args.backup or args.backup in ['-h', '--help']:
        print_help()
    elif args.backup:
        if args.backup == "now":
            take_backup(src_folder, dest_folder, False)
        else:
            try:
                interval_hours = int(args.backup)
                
                while True:
                    take_backup(src_folder, dest_folder, True)
                    print(f"{Fore.GREEN}{time.strftime('%H:%M:%S')} [info]{Fore.RESET} {interval_hours} Hours Periodically Backup to the Folder at Path {dest_folder}.")
                    time.sleep(interval_hours * 3600)
            except ValueError:
                 print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} Please enter a number.")
            except KeyboardInterrupt:
                 print(f"{Fore.RED}{time.strftime('%H:%M:%S')} [Error]{Fore.RESET} CTRL+C Executed!\nCanceling Operation...")
                 time.sleep(3);
                 exit(f"{Fore.RED}{time.strftime('%H:%M:%S')} Exit is in progress...")
