import argparse
import os
import shutil
import sys

# Literals for the paths
TEMPLATE_PATH = r'C:/tempM122/vmware/vmTemplates/'
COPY_PATH = r'C:/tempM122/vmware/vmCopies/'


def main():
    """
    Main function
    """

    vmname, users = parse_arguments()
    check_folders(vmname)
    user_copy(vmname, users)


def parse_arguments():
    """
    Parse the arguments

    :param: None
    :return: the vmname
    :return: a list of users

    """

    return 'win10', ['user1', 'user2']  # TODO: remove this line


def check_folders(vmname):
    """
    Check if the folders exist
    :param: vmname -- the name of the vm to copy
    :return: None
    """
    pass


def user_copy(vm_name, users):
    """
    Create the folder for the user and control the copy process
    :param: vm_name -- the name of the vm to copy
    :param: users -- a list of users to create copies for
    :return: None
    """
    pass


def create_copies(vmname, user):
    """
    Copy the files from the template to the user folder, changing the name of the files
    :param: vmname -- the name of the vm to copy
    :param: user -- the user to create the copy for
    :return: None
    """
    pass


def update_config(vmname, user):
    """
    Update the configuration files
    :param: vmname -- the name of the vm to copy
    :param: user -- the user to create the copy for
    :return: None
    """
    pass


if __name__ == '__main__':
    main()
