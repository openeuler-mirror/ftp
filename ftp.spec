Name:           ftp
Version:        0.17
Release:        81
Summary:        The standard UNIX FTP (File Transfer Protocol) client
License:        BSD with advertising
URL:            https://en.wikipedia.org/wiki/File_Transfer_Portocol
Source0:        https://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-ftp-%{version}.tar.gz

#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0001:      netkit-ftp-0.17-pre20000412.pasv-security.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0002:      netkit-ftp-0.17-acct.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0003:      netkit-ftp.usagi-ipv6.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0004:      netkit-ftp-0.17-segv.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0005:      netkit-ftp-0.17-volatile.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0006:      netkit-ftp-0.17-runique_mget.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0007:      netkit-ftp-locale.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0008:      netkit-ftp-0.17-printf.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0009:      netkit-ftp-0.17-longint.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0010:      netkit-ftp-0.17-vsftp165083.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0011:      netkit-ftp-0.17-C-Frame121.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0012:      netkit-ftp-0.17-data.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0013:      netkit-ftp-0.17-multihome.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0014:      netkit-ftp-0.17-longnames.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0015:      netkit-ftp-0.17-multiipv6.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0016:      netkit-ftp-0.17-nodebug.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0017:      netkit-ftp-0.17-stamp.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0018:      netkit-ftp-0.17-sigseg.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0019:      netkit-ftp-0.17-size.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0020:      netkit-ftp-0.17-fdleak.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0021:      netkit-ftp-0.17-fprintf.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0022:      netkit-ftp-0.17-bitrate.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0023:      netkit-ftp-0.17-arg_max.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0024:      netkit-ftp-0.17-case.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0025:      netkit-ftp-0.17-chkmalloc.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0026:      netkit-ftp-0.17-man.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0027:      netkit-ftp-0.17-acct_ovl.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0028:      netkit-ftp-0.17-remove-nested-include.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0029:      netkit-ftp-0.17-linelen.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0030:      netkit-ftp-0.17-active-mode-option.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0031:      netkit-ftp-0.17-commands-leaks.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0032:      netkit-ftp-0.17-lsn-timeout.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0033:      netkit-ftp-0.17-getlogin.patch
#PATCH-FIX-https://bugzilla.redhat.com/ patch from fedora project
Patch0034:      netkit-ftp-0.17-token.patch

#PATCH-FIX-OPENEULER need to backport
Patch6000:      netkit-ftp-0.17-linelen-segfault.patch

BuildRequires:  glibc-devel readline-devel ncurses-devel perl-interpreter gcc

%description
The ftp package provides the standard UNIX command-line FTP (File Transfer Protocol) client.
FTP is a widely used protocol for transferring files over the Internet and for archiving files.
If your system is on a network, you should install ftp in order to do file transfers.

%package        help
Summary:        Documents for autogen
Buildarch:      noarch

%description    help
Man pages and other related documents.

%prep
%autosetup -n netkit-%{name}-%{version} -p1

%build
sh configure --with-c-compiler=%{__cc} --enable-ipv6
perl -pi -e '
    s,^CC=.*$,CC=cc,;
    s,-O2,\$(RPM_OPT_FLAGS) -D_GNU_SOURCE -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64,;
    s,^LDFLAGS=.*$,LDFLAGS=\$(RPM_LD_FLAGS),;
    s,^BINDIR=.*$,BINDIR=%{_bindir},;
    s,^MANDIR=.*$,MANDIR=%{_mandir},;
    s,^SBINDIR=.*$,SBINDIR=%{_sbindir},;
    ' MCONFIG
%make_build

%install
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install -d ${RPM_BUILD_ROOT}%{_mandir}/man5

%make_install INSTALLROOT=${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/*ftp

%files help
%{_mandir}/man1/*ftp.*
%{_mandir}/man5/netrc.*

%changelog
* Fri Apr 28 2023 liweiganga <liweiganga@uniontech.com> - 0.17-81
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:support llvm compiler

* Tue Dec 15 2020 xihaochen <xihaochen@huawei.com> - 0.17-80
- Type:requirement
- Id:NA
- SUG:NA
- DESC:update url, source url

* Wed Sep 11 2019 openEuler jimmy<dukaitian@huawei.com> - 0.17-79
- Package init jimmy
