
%define realname   Acme-Bleach
%define version    1.12
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    For I<really> clean programs
Source:     http://www.cpan.org/modules/by-module/Acme/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel


BuildArch: noarch

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
%setup -q -n %{realname}-%{version} 

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


