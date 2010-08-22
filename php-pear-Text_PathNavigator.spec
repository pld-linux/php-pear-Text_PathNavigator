%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	PathNavigator
%define		_status		devel
%define		_pearname	Text_PathNavigator
%define		subver	dev2
%define		rel		1
Summary:	%{_pearname} - Provides convenient access to path substrings
Summary(pl.UTF-8):	%{_pearname} - Wygodny dostęp do elementów ścieżki
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	0.%{subver}.%{rel}
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	ef4473eeb6787495e70f59f529464a42
URL:		http://pear.php.net/package/Text_PathNavigator/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Text_PathNavigator class provides convenient access to
"/path/sub/strings".

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa Text_PathNavigator umożliwia dostęp do elementów ścieżki
("/sciezka/do/elementu").

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# don't care for tests
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/PathNavigator.php
