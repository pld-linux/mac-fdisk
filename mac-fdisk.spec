%define _ver    0.1
%define _rel    12
Summary:	A partitioning tool for Apple Macintosh-style partitioned disks
Summary(pl):	Narzêdzie do partycjonowania dysków Apple Macintosh
Name:		mac-fdisk
Version:	%{_ver}.%{_rel}
Release:	1
License:	BSD-like (Apple Computer, Inc.)
Group:		Applications/System
Source0:	http://http.us.debian.org/debian/pool/main/m/mac-fdisk/%{name}_%{_ver}.orig.tar.gz
# Source0-md5:	24476329fe86ef6ccf222e233e2a99f1
Source1:	http://http.us.debian.org/debian/pool/main/m/mac-fdisk/%{name}_%{_ver}-%{_rel}.diff.gz
# Source1-md5:	8eae6f5de740ec9f5678d6ed71fc3327
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
mac-fdisk is a Debian version of pdisk - partition utilitiy for
PowerPC computers. pmac-fdisk is a version of the PC partition format
utilities for PowerPC computers.

%description -l pl
mac-fdisk to debianowa wersja pdiska - narzêdzia tworz±cego partycje
dla komputerów PowerPC. pmac-fdisk to wersja narzêdzi tworz±cych
partycje PC dla komputerów PowerPC.

%prep
%setup -q -n %{name}-%{_ver}.orig
zcat %{SOURCE1} | patch -p1

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}"

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
