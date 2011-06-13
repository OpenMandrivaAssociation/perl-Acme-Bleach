%define upstream_name    Acme-Bleach
%define upstream_version 1.13

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    For I<really> clean programs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Acme/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
