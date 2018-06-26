# dm-writeboost-rpm [![Circle CI](https://circleci.com/gh/kazuhisya/dm-writeboost-rpm/tree/master.svg?style=shield)](https://circleci.com/gh/kazuhisya/dm-writeboost-rpm/tree/master)

| Package              | RPM        |
|:---------------------|:-----------|
| `dm-writeboost-dkms` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-dkms/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |
| `kmod-dm-writeboost` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-kmod/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |
| `dm-writeboost-tools` | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/dm-writeboost-tools/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |
| `writeboost` (user-space utility) | [![FedoraCopr](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/package/writeboost/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/khara/dm-writeboost/) |

This repository provides the dm-writeboost unofficial rpmbuild scripts for Red Hat Enterprise Linux, CentOS and Fedora.

- `dm-writeboost` is block-level log-structured caching driver for Linux, influenced by Disk Caching Disk (DCD). It is written by Akira Hayakawa.
    - See Also: https://github.com/akiradeveloper/dm-writeboost
- `dm-writeboost-tools` is commandset to help users of dm-writeboost to analyze and report bugs.
    - See Also: https://github.com/akiradeveloper/dm-writeboost-tools
- `writeboost` is a user-space utility to activate dm-writeboost device mappings. It is written by Dmitry Smirnov.
    - See Also: https://gitlab.com/onlyjob/writeboost

## Distro support

Working on:

- RHEL/CentOS 7 x86_64
    - `dkms` version
        - When you try to install or build on el7, must enable the EPEL repository.
    - `kmod` version
        - RHEL7.5 / CentOS 7.5.1804 or higher.
    - You can choose either version of `dkms` or `kmod`. (Cannot use both at the same system!)
- Fedora x86_64
    - `dkms` version only

Prerequisites:

- `dm-writeboost-dkms`
    - `dkms-1.95` or higher.
- `kmod-dm-writeboost`
    - `kernel-3.10.0-862.el7` or higher.

## Compiled Package


- You can find prebuilt rpm binary from here.
    - [FedoraCopr khara/dm-writeboost](https://copr.fedoraproject.org/coprs/khara/dm-writeboost/)


el7 dkms: (need epel repo)

```bash
$ sudo yum install -y epel-release
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

## Sample Usage

### 1. Install Packages

Sample: el7, dkms, tools and user-space utility.

```bash
$ sudo yum install -y epel-release
$ sudo curl -sL -o /etc/yum.repos.d/khara-dm-writeboost.repo https://copr.fedoraproject.org/coprs/khara/dm-writeboost/repo/epel-7/khara-dm-writeboost-epel-7.repo
$ sudo yum install -y dm-writeboost-dkms dm-writeboost-tools writeboost
```

### 2. Edit Configfile

- `/etc/writeboosttab`

Sample:

```bash
## dm-writeboost "tab" (mappings) file, see writeboosttab(5).
##{DM target name}    {cached block device e.g. HDD}    {caching block device e.g. SSD}    [options]
##
## wb_hdd     /dev/disk/by-uuid/2e8260bc-024c-4252-a695-a73898c974c7     /dev/disk/by-partuuid/43372b68-3407-45fa-9b2f-61afe9c26a68    writeback_threshold=70,sync_data_interval=3600
##
wbdev     /dev/sdb     /dev/sdc    writeback_threshold=70
```

### 3. Activate writeboost device

```
$ sudo wbcreate wbdev /dev/sdb /dev/sdc --reformat --writeback_threshold=70
```

### 4. Other as needed ...

- enable init service...

```
$ sudo systemctl enable writeboost.service
```

- mkfs...

```
$ sudo mkfs.xfs /dev/mapper/wbdev
```

- check status...

```
$ sudo dmsetup status wbdev | sudo wbstatus
```


- mount setting on fstab...

```
/dev/mapper/wbdev    /mnt/wb xfs     defaults        0 0
```

If you are using a large caching device, occasionally `mount` may time out.
In such cases it may be improved with the following workaround.

- Edit: `/usr/lib/systemd/system/writeboost.service`
    - Please increase `TimeoutStartSec`

```
TimeoutStartSec=600
```

- Edit: `/etc/fstab`

```
/dev/mapper/wbdev /data defaults,x-systemd.requires=writeboost.service 0 0
```

or

```
/dev/mapper/wbdev /data auto,nofail,x-systemd.device-timeout=1200 0 0
```


## Disclaimer

- This repository and all files that are included in this, there is no relationship at all with the upstream and vendor.
