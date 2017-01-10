# dm-writeboost-rpm

| Package              | RPM        |
|:---------------------|:-----------|
| `dm-writeboost-dkms` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-dkms/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |
| `kmod-dm-writeboost` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-kmod/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |

This repository provides the dm-writeboost unofficial rpmbuild scripts for Red Hat Enterprise Linux, CentOS and Fedora.

dm-writeboost is block-level log-structured caching driver for Linux, influenced by Disk Caching Disk (DCD). It is written by Akira Hayakawa.

See Also: https://github.com/akiradeveloper/dm-writeboost


## Distro support

Working on:

- RHEL/CentOS 7 x86_64
	- `dkms` version
	    - When you try to build on el7, must enable the EPEL repository.
	- `kmod` version
		- RHEL7.3 / CentOS 7.3.1611 or higher.
- Fedora 23 or higher x86_64
	- `dkms` version only

Prerequisites:

- `dm-writeboost-dkms`
	- `dkms-1.95` or higher.
- `kmod-dm-writeboost`
	- `kernel-3.10.0-514.el7` or higher.

## Compiled Package


- You can find prebuilt rpm binary from here.
    - [FedoraCopr khara/dm-writeboost](https://copr.fedoraproject.org/coprs/khara/dm-writeboost/)


el7 dkms: (need epel repo)

```bash
$ sudo curl -sL -o /etc/yum.repos.d/khara-dm-writeboost.repo https://copr.fedoraproject.org/coprs/khara/dm-writeboost/repo/epel-7/khara-dm-writeboost-epel-7.repo
$ sudo yum install -y dm-writeboost-dkms
```

el7 kmod:

```bash
$ sudo curl -sL -o /etc/yum.repos.d/khara-dm-writeboost.repo https://copr.fedoraproject.org/coprs/khara/dm-writeboost/repo/epel-7/khara-dm-writeboost-epel-7.repo
$ sudo yum install -y kmod-dm-writeboost
```

fedora:

```bash
$ sudo dnf copr enable khara/dm-writeboost
$ sudo dnf install -y dm-writeboost-dkms 
```

## Disclaimer

- This repository and all files that are included in this, there is no relationship at all with the upstream and vendor.
