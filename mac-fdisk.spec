Summary:	A partitioning tool for Apple Macintosh-style partitioned disks
Summary(pl):	Narzêdzie do partycjonowania dysków Apple Macintosh
Name:		mac-fdisk
Version:	0.1
Release:	0.1
License:	Apple Computers
Group:		Applications/System
Source0:	http://http.us.debian.org/debian/pool/main/m/mac-fdisk/%{name}_%{version}.orig.tar.gz
# Source0-md5:	24476329fe86ef6ccf222e233e2a99f1
Source1:	http://http.us.debian.org/debian/pool/main/m/mac-fdisk/%{name}_%{version}-8.diff.gz
# Source1-md5:	5dea1f9f8d44fe89c00322c315633443
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
mac-fdisk is a Debian version of pdisk - partition utilitiy for
PowerPC computers. pmac-fdisk is a version of the PC partition format
utilities for PowerPC computers.

%description -l pl
mac-fdisk to Debianowa wersja pdiska - narzêdzia tworz±cego partycje
dla komputerów PowerPC.

%prep
%setup -q -n %{name}-%{version}.orig
zcat %{SOURCE1} | patch -p1

%build
%{__make} CC="%{__cc}" LDFLAGS="%{rpmldflags}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install fdisk $RPM_BUILD_ROOT%{_sbindir}/pmac-fdisk
install pdisk $RPM_BUILD_ROOT%{_sbindir}/mac-fdisk
install mac-fdisk.8.in $RPM_BUILD_ROOT%{_mandir}/man8/mac-fdisk.8
install pmac-fdisk.8.in $RPM_BUILD_ROOT%{_mandir}/man8/pmac-fdisk.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY debian/copyright debian/changelog
%attr(755,root,root) %{_sbindir}/mac-fdisk
%attr(755,root,root) %{_sbindir}/pmac-fdisk
%{_mandir}/man8/*
