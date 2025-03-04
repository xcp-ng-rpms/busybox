%global package_speccommit 07bac995d386c78d61bb776d685fb4f47de36ffb
%global usver 1.22.1
%global xsver 7
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global package_srccommit v1.22.1

Summary: Busybox binary providing simplified versions of system commands
Name: busybox
Version: 1.22.1
Release: %{?xsrel}%{?dist}
License: GPL
Group: System Environment/Daemons
Source0: busybox-1.22.1.tar.bz2
Source1: config
Patch0: udhcpc-fix-OPTION_6RD-parsing-could-overflow-its-mal.patch
Patch1: udhcp-fix-a-SEGV-on-malformed-RFC1035-encoded-domain.patch
Patch2: udhcpc-check-read-of-option-length-byte-to-be-within.patch
Patch3: udhcpc-check-read-of-overload-option-data-byte-to-be.patch
Patch4: udhcpc-check-that-4-byte-options-are-indeed-4-byte-c.patch
Patch5: udhcpc-when-decoding-DHCP_SUBNET-ensure-it-is-4-byte.patch

%{?_cov_buildrequires}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.

%prep
%autosetup -p1
%{?_cov_prepare}

%build
cp %SOURCE1 .config
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
* Thu Aug 15 2024 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.22.1-7
- Only compile udhcpd
- CA-394144: Backport fix for CVE-2018-20679 and others

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
