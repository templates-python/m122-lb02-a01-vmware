"""
Setup the files for testing
"""
import os
import shutil
def main():
    """
    Main function
    """
    cleanup()
    setup()

def cleanup():
    """
    Cleanup all the files in c:\tempM122\vmware
    """

    path = r'c:\tempM122\vmware'
    if os.path.exists(path):
        shutil.rmtree(path)

def setup():
    """
    Copy all folders and files from c:\tempM122\setup to c:\tempM122\vmware
    """
    path = r'c:\tempM122\setup'
    dest = r'c:\tempM122\vmware'
    shutil.copytree(path, dest)


if __name__ == '__main__':
    main()