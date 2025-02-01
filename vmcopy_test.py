import os
import shutil
import stat
import sys

import pytest

from vmcopy import check_folders, user_copy, create_copies, update_config, main, parse_arguments

# Literals for the paths
TEMPLATE_PATH = r'C:/tempM122/vmware/vmTemplates/'
COPY_PATH = r'C:/tempM122/vmware/vmCopies/'

def test_parse_arguments(mock_vm_copy, mock_check_folders):
    """
    Test the parse_arguments function
    :param: None
    :return: None
    """
    # Too few arguments
    with pytest.raises(SystemExit):
        # with unittest.mock.patch('sys.argv', ['vmcopy', 'vmLinux']):
        sys.argv = ['vmcopy', 'vmLinux']
        parse_arguments()

    sys.argv = ['vmcopy', 'vmLinux', '-u', 'user1', '-u', 'user2']
    vmname, users = parse_arguments()
    assert vmname == 'vmLinux'
    assert users == ['user1', 'user2']


def test_check_folders(setup_folders):
    """
    Test the check_folders function
    """
    # Check if the template folder exists
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        assert check_folders('vmname') == 'Template "vmname" does not exist\n'
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2
    # Check if the folder for the copies exists
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        assert check_folders('vmSomething') == 'Destination folder for "vmname" not found\n'
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 3

    assert check_folders('vmLinux') is None


def test_vm_copy(setup_folders, mock_create_copies, mock_update_config):
    """
    Test the vm_copy function
    """
    user_copy('vmLinux', ['user1', 'user2'])
    assert os.path.isdir(r'c:/tempM122/vmware/vmCopies/vmLinux/user1')
    assert os.path.isdir(r'c:/tempM122/vmware/vmCopies/vmLinux/user2')


def test_create_copies(setup_folders, mock_vm_copy):
    """
    Test the create_copies function
    """
    user_copy('vmLinux', ['musterh'])
    create_copies('vmLinux', 'musterh')
    file_list = os.listdir(r'c:/tempM122/vmware/vmCopies/vmLinux/musterh')
    assert len(file_list) >= 8
    expected_files = [
        'vmLinux_musterh-s001.vmdk',
        'vmLinux_musterh-s002.vmdk',
        'vmLinux_musterh-s003.vmdk',
        'vmLinux_musterh.nvram',
        'vmLinux_musterh.vmdk',
        'vmLinux_musterh.vmsd',
        'vmLinux_musterh.vmx',
        'vmLinux_musterh.vmxf',
        'vmware-1.log',
        'vmware.log',
    ]
    assert file_list == expected_files

def test_update_config(setup_folders):
    """
    Test the update_config function
    """
    update_config('vmConfig', 'ghwalin')
    # read the content of the vmx file
    with open(r'c:/tempM122/vmware/vmCopies/vmConfig/ghwalin/vmConfig_ghwalin.vmx') as f:
        content = f.read()
    assert 'nvram = "vmConfig_ghwalin.nvram"' in content
    assert 'scsi0:0.fileName = "vmConfig_ghwalin.vmdk"' in content
    assert 'displayName = "vmConfig_ghwalin"' in content
    assert 'extendedConfigFile = "vmConfig_ghwalin.vmxf"' in content

    # read the content of the vmxf file
    with open(r'c:/tempM122/vmware/vmCopies/vmConfig/ghwalin/vmConfig_ghwalin.vmxf') as f:
        content = f.read()
    assert '<vmxPathName type="string">vmConfig_ghwalin.vmx</vmxPathName>' in content

    # read the content of the vmdk file
    with open(r'c:/tempM122/vmware/vmCopies/vmConfig/ghwalin/vmConfig_ghwalin.vmdk') as f:
        content = f.read()
    assert '"vmConfig_ghwalin-s001.vmdk"' in content
    assert '"vmConfig_ghwalin-s002.vmdk"' in content
    assert '"vmConfig_ghwalin-s003.vmdk"' in content


''' Fixtures to simulate functions'''
@pytest.fixture
def setup_folders():
    """
    Setup the folders for the tests
    :param: None
    :return: None
    """
    # remove folder c:/tempM122/vmware
    shutil.rmtree(r'c:/tempM122/vmware/', onerror=remove_readonly)
    # copy folder c:/tempM122/setup to c:/tempM122/vmware
    shutil.copytree(r'c:/tempM122/setup', r'c:/tempM122/vmware')

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)


@pytest.fixture
def mock_check_folders(monkeypatch):
    def check_folders(vmname):
        """
        Mock the check_folders function
        :param: vmname -- the name of the vm to check
        :return: None
        """
        pass

    monkeypatch.setattr('vmcopy.check_folders', check_folders)

@pytest.fixture
def mock_create_copies(monkeypatch):
    def create_copies(vmname, users):
        """
        Mock the create_copies function
        :param: vmname -- the name of the vm to copy
        :param: user -- the user to create the copy for
        :return: None
        """
        pass

    monkeypatch.setattr('vmcopy.create_copies', create_copies)


@pytest.fixture
def mock_update_config(monkeypatch):
    def update_config(vmname, user):
        """
        Mock the update_config function
        :param: vmname -- the name of the vm to copy
        :param: user -- the user to create the copy for
        :return: None
        """
        pass

    monkeypatch.setattr('vmcopy.update_config', update_config)

@pytest.fixture
def mock_vm_copy(monkeypatch):
    def vm_copy(vm_name, users):
        """
        Mock the vm_copy function
        :param: vm_name -- the name of the vm to copy
        :param: users -- a list of users to create copies for
        :return: None
        """
        pass
    monkeypatch.setattr('vmcopy.vm_copy', vm_copy)

