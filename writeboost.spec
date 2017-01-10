%global commit          37dc927f969c34947f2de49afd5bb4cc95078768
%global shortcommit     %(c=%{commit}; echo ${c:0:7}) 

Summary:        writeboost is a user-space utility to activate dm-writeboost device mappings.
Name:           writeboost
Version:        1.20160718
Release:        1.git%{shortcommit}%{?dist}
License:        GPLv2
BuildArch:      noarch
Group:          System Environment/Daemons
URL:            https://gitlab.com/onlyjob/writeboost
Requires:       device-mapper
BuildRequires:  systemd-units
BuildRequires:  perl-podlators
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root/

# Sources.
Source0:        %{url}/repository/archive.tar.gz?ref=%{version}#/%{name}-%{version}.tar.gz
Patch0:         writeboost-service-toggle-remain.patch

%description
writeboost is a user-space utility to activate dm-writeboost device mappings.

%prep
%setup -q -n %{name}-%{version}-%{commit}
%patch0 -p1

%build
make %{?_smp_mflags}

%install
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    %{__rm} -rf $RPM_BUILD_ROOT
fi

%{__install} -d $RPM_BUILD_ROOT%{_sbindir}
%{__install} -d $RPM_BUILD_ROOT%{_unitdir}
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}
%{__install} -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/{man5,man8}

%{__install} $RPM_BUILD_DIR/%{name}-%{version}-%{commit}/sbin/%{name} $RPM_BUILD_ROOT%{_sbindir}
%{__install} $RPM_BUILD_DIR/%{name}-%{version}-%{commit}/%{name}.service $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
%{__install} $RPM_BUILD_DIR/%{name}-%{version}-%{commit}/etc/%{name}tab $RPM_BUILD_ROOT%{_sysconfdir}/
%{__install} $RPM_BUILD_DIR/%{name}-%{version}-%{commit}/man/%{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8/
%{__install} $RPM_BUILD_DIR/%{name}-%{version}-%{commit}/man/%{name}tab.5 $RPM_BUILD_ROOT%{_mandir}/man5/


%clean
if [ "$RPM_BUILD_ROOT" != "/" ]; then
    %{__rm} -rf $RPM_BUILD_ROOT
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/%{name}tab
%defattr(755,root,root)
%{_sbindir}/%{name}
%defattr(644,root,root)
%{_unitdir}/%{name}.service

%doc
%{_mandir}/*/*.gz

%changelog
* Tue Jan 10 2017 Kazuhisa Hara <kazuhisya@gmail.com> - 1.20160718-1.git37dc927
- inital version
