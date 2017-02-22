# Ansible role: Vagrant

Installs Vagrant in Ubuntu Desktop.


## Role Variables

* `vagrant_version`:
    - Description: Vagrant version to install
    - Default: `1.9.1`

* `vagrant_arch`:
    - Description: System arch to install
    - Default: `x86_64`

* `vagrant_url`:
    - Description: URL for installation package
    - Default: `https://releases.hashicorp.com/vagrant/{{ vagrant_version }}/vagrant_{{ vagrant_version }}_{{ vagrant_arch }}.deb`

* `vagrant_destionation`:
    - Description: Temporary directory used to download vagrant package
    - Default: `/tmp`

## Example Playbook

    - hosts: workstations
      roles:
        - { role: viniciusfs.vagrant }


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
