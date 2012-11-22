Summary: A MySQL Replication Load Average with Performance Schema 
Name: mysql-repl-la
Version: 1.0.0
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0:%{name}-%{version}.tgz
Vendor: SaaS

BuildArch: noarch
URL: https://github.com/Sov1et/mysql-repl-la
BuildRoot: %{_tmppath}/%{name}-%{version}

Requires: mysql

%description
A MySQL Replication Load Average with Performance Schema

%prep
%setup -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/mysql-repl-la/
cp -ad * $RPM_BUILD_ROOT/usr/share/mysql-repl-la/

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/mysql < /usr/share/mysql-repl-la/install.sql

%files
%defattr(-,root,root)
/usr/share/mysql-repl-la

%changelog
* Thu Nov 22 2012 Viacheslav Biriukov  <v.v.biriukov@gmail.com> - 1.0.0-1
- Initial revision
