%define upstream_name    Parse-Nessus-ENX
%define upstream_version 1.1

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Extract information from Nessus Extend NSR files
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DK/DKYGER/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
Requires:	perl(Exporter)
BuildArch:	noarch

%description
This module is designed to extract information from Extended NSR (ENX)
files. Certain functions have been designed to return certain sets of data,
such as service banners and OS versions. Other functions have been
provided that will return more specific information, such as all IPs
listening on a given port or all IPs associated with a specified plugin
id.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README MANIFEST
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Oct 03 2011 Leonardo Coelho <leonardoc@mandriva.com> 1.100.0-1mdv2012.0
+ Revision: 702625
- first mandriva version
- Created package structure for 'perl-Parse-Nessus-ENX'.

