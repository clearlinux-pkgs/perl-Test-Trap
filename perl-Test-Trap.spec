#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Trap
Version  : 0.3.4
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/E/EB/EBHANSSEN/Test-Trap-v0.3.4.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EB/EBHANSSEN/Test-Trap-v0.3.4.tar.gz
Summary  : 'Trap exit codes, exceptions, output, etc.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Data::Dump)

%description
Test-Trap
Primarily (but not exclusively) for use in test scripts: A block eval
on steroids, configurable and extensible, but by default trapping
(Perl) STDOUT, STDERR, warnings, exceptions, would-be exit codes, and
return values from boxed blocks of test code.

%package dev
Summary: dev components for the perl-Test-Trap package.
Group: Development
Provides: perl-Test-Trap-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-Trap package.


%prep
%setup -q -n Test-Trap-v0.3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Test/Trap.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/Trap/Builder.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/Trap/Builder/PerlIO.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/Trap/Builder/SystemSafe.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/Trap/Builder/TempFile.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Trap.3
/usr/share/man/man3/Test::Trap::Builder.3
/usr/share/man/man3/Test::Trap::Builder::PerlIO.3
/usr/share/man/man3/Test::Trap::Builder::SystemSafe.3
/usr/share/man/man3/Test::Trap::Builder::TempFile.3
