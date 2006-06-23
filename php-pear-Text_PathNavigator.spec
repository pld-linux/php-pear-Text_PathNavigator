%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	PathNavigator
%define		_status		devel
%define		_pearname	Text_PathNavigator

Summary:	%{_pearname} - Provides convenient access to path substrings
Summary(pl):	%{_pearname} - Wygodny dostêp do elementów ¶cie¿ki
Name:		php-pear-%{_pearname}
Version:	0.1.0dev1
Release:	1
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4c667222c7ca9addfebd9e9aac7cece6
URL:		http://pear.php.net/package/Text_PathNavigator/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Text_PathNavigator class provides convenient access to
"/path/sub/strings".

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa Text_PathNavigator umo¿liwia dostêp do elementów ¶cie¿ki
("/sciezka/do/elementu").

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/examples/path.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Text/PathNavigator.php
