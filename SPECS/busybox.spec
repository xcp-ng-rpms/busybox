Summary: Busybox binary providing simplified versions of system commands
Name: busybox
Version: 1.22.1
Release: 2
License: GPL
Group: System Environment/Daemons
#Source0: http://busybox.net/downloads/%{name}-%{version}.tar.bz2

Source0: https://repo.citrite.net:443/ctx-local-contrib/xs-opam/busybox-1.22.1.tar.bz2




%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.

%prep
%setup -q

%build
make defconfig
%{__make}

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/bin
install -m 755 busybox %{buildroot}/bin/busybox

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/bin/busybox
%doc


%changelog
* Mon Feb 27 2017 Christian Lindig <christian.lindig@citrix.com> - 1.22.1-2
- Download from internal mirror
* Tue Oct  7 2014 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.22.1-1
- Initial packaging
