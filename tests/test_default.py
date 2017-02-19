import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_vagrant_package(Package):
    vagrant = Package('vagrant')

    assert vagrant.is_installed
    assert vagrant.version == '1:1.9.1'
