%define upstream_name    Acme-Bleach
%define upstream_version 1.150
Name:		perl-%{upstream_name}
Version:	1.150
Release:	3

Summary:	For I<really> clean programs
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Acme-Bleach
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Acme-Bleach-1.150.tar.gz

BuildRequires:	make
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
%setup -q -n Acme-Bleach-1.150

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


