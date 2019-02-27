# Ansible role: Vagrant

Installs Vagrant on Linux systems. :joy_cat:


## Role Variables

* `vagrant_version`:
    - Description: Vagrant version to install
    - Default: `latest`

* `vagrant_install_dir`:
    - Description: Destination directory for Vagrant binary file
    - Default: `/usr/local/bin`

* `vagrant_temp_dir`:
    - Description: Temporary directory used to download vagrant page for scraping
    - Default: `/tmp`


## Example Playbook

    - hosts: workstations
      roles:
        - name: viniciusfs.vagrant


## License

MIT


## Author Information

* Vinícius Figueiredo <viniciusfs@gmail.com>
