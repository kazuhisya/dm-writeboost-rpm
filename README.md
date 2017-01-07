# dm-writeboost-rpm

| Package              | RPM        |
|:---------------------|:-----------|
| `dm-writeboost-dkms` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-dkms/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |
| `kmod-dm-writeboost` | not yet... |

This repository provides the dm-writeboost unofficial rpmbuild scripts for Red Hat Enterprise Linux, CentOS and Fedora.

dm-writeboost is block-level log-structured caching driver for Linux, influenced by Disk Caching Disk (DCD). It is written by Akira Hayakawa

See Also: https://github.com/akiradeveloper/dm-writeboost


## Distro support

Working on:

- RHEL/CentOS 7 x86_64
    - When you try to build on el7, must enable the EPEL repository.
- Fedora 23 or higher x86_64

Prerequisites:

- `dkms`

## Compiled Package


- You can find prebuilt rpm binary from here
    - [FedoraCopr khara/dm-writeboost](https://copr.fedoraproject.org/coprs/khara/dm-writeboost/)



el7:

```bash
$ sudo curl -sL -o /etc/yum.repos.d/khara-dm-writeboost.repo https://copr.fedoraproject.org/coprs/khara/dm-writeboost/repo/epel-7/khara-dm-writeboost-epel-7.repo
$ sudo yum install -y dm-writeboost-dkms
```

fedora:

```bash
$ sudo dnf copr enable khara/dm-writeboost
$ sudo dnf install -y dm-writeboost-dkms 
```

## Disclaimer

- This repository and all files that are included in this, there is no relationship at all with the upstream and vendor.
