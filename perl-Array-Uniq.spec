#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Array
%define		pnam	Uniq
Summary:	Array::Uniq - pure Perl uniq module
Summary(pl):	Array::Uniq - czysto perlowy modu³ uniq
Name:		perl-Array-Uniq
Version:	0.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	208d737de9e0ead97df952a5d66bd406
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Similar functionality is available at shell prompts of *nix O/S.
This modules is attempting to provide the same to Perl programming,

%description -l pl
Podobna funkcjonalno¶æ jest dostêpna z poziomu pow³oki systemów
uniksowych. Ten modu³ jest prób± dostarczenia tego samego programom w
Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Array/Uniq.pm
%{_mandir}/man3/*
