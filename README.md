# MCUPS

日本語版→ [README_JA.md](https://github.com/sonyaearth-offical/backpak/blob/main/README_JA.md)

MCUPS is a CLI software that provides backup functionality for Minecraft servers developed by sonyaEarth (sonyakun).

## Features

- Support for backing up to a local directory accessible from the server only (e.g. C drive or D drive in Windows).
- Ability to customize backup configuration using a JSON file.
- Intuitive command-line interface for easy use.
- Easy installation with the command `pip install .`
- Configure the path to the backup configuration file by setting the environment variable `BACKPAK_CONFIG`.

## Usage

To use MCUPS, you need to have Python 3.6 or higher installed on your server.

1. Clone the MCUPS repository.
2. Install MCUPS using `pip install .`
3. Set the environment variable `BACKPAK_CONFIG` to the path of your backup configuration file.
4. Run the backup command by running the following command: `mcups create [config_number]`. Replace `[config_number]` with the number of the backup configuration in your configuration file.

## Future Work

MCUPS currently supports backups to a local directory only. We plan to add support for backup to FTP/SFTP servers in the near future.
