# Define the kmod package name here.
%define kmod_name dm-writeboost
%define version 2.2.6

# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kernel:  %define kernel 3.10.0-514.el7}
%{!?kversion: %define kversion %{kernel}.%{_target_cpu}}

Summary:        %{kmod_name} %{version} kmod package
Name:           %{kmod_name}-kmod
Version:        %{version}
Release:        1%{?dist}
Group:          System Environment/Kernel
License:        GPLv2
URL:            https://github.com/akiradeveloper/%{kmod_name}
BuildRequires:  perl
BuildRequires:  redhat-rpm-config

# kernel
Requires:       kernel >= %{kernel}
BuildRequires:  kernel = %{kernel}
BuildRequires:  kernel-devel = %{kernel}
BuildRequires:  kernel-headers = %{kernel}
BuildRequires:  kernel-abi-whitelists = %{kernel}

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root/
ExclusiveArch:  x86_64

# Sources.
Source0:        %{url}/archive/v%{version}.tar.gz
Source10:       kmodtool-%{kmod_name}-el7.sh
Patch0:         rhel73-workaround-issues-165.patch

# Magic hidden here.
%{expand:%(sh %{SOURCE10} rpmtemplate %{kmod_name} %{kversion} "")}

# Disable the building of the debug package(s).
%define debug_package %{nil}

%description
Log-structured Caching for Linux.
Kernel modules for %{kmod_name} %{version} .

%prep
%setup -n %{kmod_name}-%{version}
%patch0 -p1
echo "override %{kmod_name} * weak-updates/%{kmod_name}" > kmod-%{kmod_name}.conf

%build
cd src
KSRC=%{_usrsrc}/kernels/%{kversion}
%{__make} -C "${KSRC}" %{?_smp_mflags} modules M=$PWD


%install
%{__install} -d %{buildroot}/lib/modules/%{kversion}/extra/%{kmod_name}/
%{__install} src/%{kmod_name}.ko %{buildroot}/lib/modules/%{kversion}/extra/%{kmod_name}/
%{__install} -d %{buildroot}%{_sysconfdir}/depmod.d/
%{__install} kmod-%{kmod_name}.conf %{buildroot}%{_sysconfdir}/depmod.d/
for file in ChangeLog LICENSE README.md; do
    %{__install} -Dp -m0644 $file %{buildroot}%{_defaultdocdir}/kmod-%{kmod_name}-%{version}/$file
done

# strip the modules(s)
find %{buildroot} -type f -name \*.ko -exec %{__strip} --strip-debug \{\} \;

# Sign the modules(s)
%if %{?_with_modsign:1}%{!?_with_modsign:0}
# If the module signing keys are not defined, define them here.
%{!?privkey: %define privkey %{_sysconfdir}/pki/SECURE-BOOT-KEY.priv}
%{!?pubkey: %define pubkey %{_sysconfdir}/pki/SECURE-BOOT-KEY.der}
for module in $(find %{buildroot} -type f -name \*.ko);
do %{__perl} /usr/src/kernels/%{kversion}/scripts/sign-file \
sha256 %{privkey} %{pubkey} $module;
done
%endif

%clean
%{__rm} -rf %{buildroot}

%changelog
* Sat Jan  7 2017 Kazuhisa Hara <kazuhisya@gmail.com> - 2.2.6-1
- inital version
