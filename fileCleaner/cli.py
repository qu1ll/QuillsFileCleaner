import os
import click
from loguru import logger

@click.group()
@click.pass_context
@logger.catch
def cli(ctx) -> None:
    """ Utility """
    
@click.command()
@click.pass_obj
@logger.catch
def fullClean(ctx) -> None:
    """ Clean up all files within downloads folder (with few exceptions)"""
    exe()
    logger.info(f"Downloads File Cleaned")

@click.command()
@click.pass_obj
@logger.catch
def exe(ctx) -> None:
    """ Delete all exe's within the downloads folder"""
    # downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    test_downloads_path = "C:\\Users\\ebixby\\OneDrive - Liberty University\\Documents\\VS Code\\Downloads Cleanup\\fileCleaner\\Test Folder"
    downloads_path = test_downloads_path
    for file_name in os.listdir(downloads_path):
        if file_name.endswith(".exe"):
            file_path = os.path.join(downloads_path, file_name)
            os.remove(file_path)
            logger.info(f"Deleted {file_path}")

cli.add_command(fullClean)
cli.add_command(exe)

cli(obj=dict(config=None, verbosity='info'))