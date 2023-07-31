# Automatic Backup Script

This repository contains a Python script that allows you to automatically take backups of a specified folder. The script uses the `shutil` library to create a ZIP archive of the source folder and stores it in the destination folder.

## Features

- Take a backup of a folder manually or automatically at specified intervals.
- Zip the backup files to save disk space.
- Customizable backup intervals.

## Usage

To use the script, follow the steps below:

1. Clone this repository to your local machine or download the `backup.py` file.

2. Make sure you have Python installed on your system.

3. Modify the `src_folder` and `dest_folder` variables in the script to specify the source folder you want to back up and the destination folder where you want to store the backups.

4. Run the script with the following options:

   - `--backup now`: Takes an immediate backup of the source folder.
   - `--backup (interval)`: Takes automatic backups at specified intervals. Replace `(interval)` with the number of hours between each backup.

   Example: To take backups every 2 hours, run: `python backup.py --backup 2`

5. If you run the script without any options or use the `-h` or `--help` option, it will display the help message with available options.

## Requirements

- Python 3.x
- `colorama` library (install it using `pip install colorama`)

## Disclaimer

This script is provided as-is, without any warranty. Use it at your own risk. Before running the script, make sure to test it on non-production environments.

## Contributing

Feel free to open an issue or submit a pull request if you find any bugs or want to improve the script.

## License

This project is licensed under the [MIT License](LICENSE).
