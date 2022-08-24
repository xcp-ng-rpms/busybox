%global package_speccommit fca4a7a2276854bbe403f684d96c19008776f2e1
%global usver 1.22.1
%global xsver 6
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v1.22.1

Summary: Busybox binary providing simplified versions of system commands
Name: busybox
Version: 1.22.1
Release: %{?xsrel}%{?dist}
License: GPL
Group: System Environment/Daemons
Source0: busybox-1.22.1.tar.bz2

BuildRequires: gcc

%{?_cov_buildrequires}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.

%prep
%autosetup -p1
%{?_cov_prepare}

%build
make defconfig
%{?_cov_wrap} %{__make}

%install
mkdir -p %{buildroot}/bin
install -m 755 busybox %{buildroot}/bin/busybox
%{?_cov_install}

%files
%defattr(-,root,root,-)
/bin/busybox
%doc

%{?_cov_results_package}

%changelog
* Tue May  3 2022 Mark Syms <mark.syms@citrix.com> - 1.22.1-6
- Fix Coverity build

* Fri Apr 29 2022 Rob Hoes <rob.hoes@citrix.com> - 1.22.1-5
- Bump release and rebuild

* Thu Apr 28 2022 Rob Hoes <rob.hoes@citrix.com> - 1.22.1-4
- Bump release and rebuild

* Mon Jan 04 2021 Rob Hoes <rob.hoes@citrix.com> - 1.22.1-3
- Rebuild for koji transition

* Mon Feb 27 2017 Christian Lindig <christian.lindig@citrix.com> - 1.22.1-2
- Download from internal mirror
* Tue Oct  7 2014 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.22.1-1
- Initial packaging
