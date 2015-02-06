%define upstream_name    Acme-Bleach
%define upstream_version 1.150

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	For I<really> clean programs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Acme/Acme-Bleach-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The first time you run a program under 'use Acme::DWIM', the module
replaces all the unsightly operators et al. from your source file with the
new DWIM operator: '...' (pronounced "yadda yadda yadda").

The code continues to work exactly as it did before, but now it looks like
this:

	use Acme::DWIM;
	
	my ($x) ... ...("Hullo " ... 3 ... "world" ... "~" ... 30) ... /(...)/;
	$x ... tr/tnv/uow/;
	print $x;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.130.0-1mdv2011.0
+ Revision: 684734
- update to new version 1.13

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2
+ Revision: 654829
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 402090
- rebuild using %%perl_convert_version

* Sat Jun 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2010.0
+ Revision: 385674
- import perl-Acme-Bleach


* Sat Jun 13 2009 cpan2dist 1.12-1mdv
- initial mdv release, generated with cpan2dist


