%global commit 90fd362eb2baadcb9db4dfbcc083696ac087216a
%global gittag v1.0.0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dm-writeboost-tools
Version:        %(t=%{gittag}; echo ${t:1})
Release:        1.git%{shortcommit}%{?dist}
Summary:        Nice tools for dm-writeboost. a.k.a. wbtools.

Group:          System Environment/Daemons
License:        GPLv2
URL:            https://github.com/akiradeveloper/%{name}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

Requires:       device-mapper
BuildRequires:  rust
BuildRequires:  cargo

# Disable the building of the debug package(s).
%define debug_package %{nil}

%description
Commandset to help users of dm-writeboost to analyze and report bugs. Written in Rust.


%prep
%autosetup -n %{name}-%{commit}


%build
cargo build --release --verbose

%check
cargo test

%install
%{__install} -d -m755 %{buildroot}%{_sbindir}
%{__install} %{_builddir}/%{name}-%{commit}/target/release/wb* %{buildroot}%{_sbindir}/

%{__install} -d -m755 %{buildroot}%{_defaultdocdir}/%{name}
for file in README.md LICENSE ChangeLog; do
    %{__mv} %{_builddir}/%{name}-%{commit}/$file %{buildroot}%{_defaultdocdir}/%{name}/
done

%files
%defattr(755,root,root)
%{_sbindir}/wb*
%defattr(-,root,root)
%{_defaultdocdir}/%{name}/

%changelog
* Mon Jan 23 2017 Kazuhisa Hara <kazuhisya@gmail.com> - 1.0.0-1.git90fd362
- updated to dm-writeboost-tools version 1.0.0
* Tue Jan 17 2017 Kazuhisa Hara <kazuhisya@gmail.com> - 0.1.0-1.git7fb9e16
- inital version
