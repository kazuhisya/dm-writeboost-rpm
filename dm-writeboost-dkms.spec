%define module_name dm-writeboost
%define version 2.2.6
%define dkmslibdir %{_prefix}/lib/dkms

Summary:        %{module_name} %{version} dkms package
Name:           %{module_name}-dkms
Version:        %{version}
Release:        1dkms%{?dist}
License:        GPLv2
BuildArch:      noarch
Group:          System Environment/Kernel
URL:            https://github.com/akiradeveloper/%{module_name}
Requires:       dkms >= 1.95
Requires:       device-mapper
BuildRequires:  dkms
BuildRequires:  redhat-rpm-config
%if %{defined kernel_module_package_buildreqs}
BuildRequires:  %kernel_module_package_buildreqs
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root/

# Sources.
Source0:        %{url}/archive/fix-165.tar.gz

%description
Log-structured Caching for Linux.
Kernel modules for %{module_name} %{version} in a DKMS wrapper.

%prep
## %setup -q -n %{module_name}-%{version}
%setup -q -n %{module_name}-fix-165

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    %{__rm} -rf $RPM_BUILD_ROOT
fi

%{__mkdir} -p $RPM_BUILD_ROOT%{_usrsrc}/%{module_name}-%{version}/
%{__mv} ./src/* $RPM_BUILD_ROOT%{_usrsrc}/%{module_name}-%{version}

%{__mkdir} -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
%{__mv} ./doc/* $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/

for file in ChangeLog LICENSE README.md ; do
    %{__mv} ./$file $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/
done

%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    %{__rm} -rf $RPM_BUILD_ROOT
fi

%post
for POSTINST in %{dkmslibdir}/common.postinst %{_datarootdir}/%{module_name}/postinst; do
    if [ -f $POSTINST ]; then
        $POSTINST %{module_name} %{version} %{_datarootdir}/%{module_name}
        exit $?
    fi
    echo "WARNING: $POSTINST does not exist."
done
echo -e "ERROR: DKMS version is too old and %{module_name} was not"
echo -e "built with legacy DKMS support."
echo -e "You must either rebuild %{module_name} with legacy postinst"
echo -e "support or upgrade DKMS to a more current version."
exit 1

%preun
echo -e
echo -e "Uninstall of %{module_name} module (version %{version}) beginning:"
dkms remove -m %{module_name} -v %{version} --all --rpm_safe_upgrade
exit 0

%files
%defattr(-,root,root)
%{_usrsrc}
%{_defaultdocdir}/%{name}/

%changelog
* Sat Jan  7 2017 Kazuhisa Hara <kazuhisya@gmail.com> - 2.2.6-1
- inital version
