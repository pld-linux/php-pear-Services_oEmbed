%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_oEmbed
Summary:	%{_pearname} - A package for consuming oEmbed
Summary(pl.UTF-8):	%{_pearname} - pakiet do obsługi oEmebed
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	3
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	31a8d924e4e157e62b3eac04fa00e2b6
URL:		http://pear.php.net/package/Services_oEmbed/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(curl)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(xml)
#Requires:	php-libxml
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.4.3
Requires:	php-pear-Net_URL2 >= 0.2.0
Requires:	php-pear-PEAR >= 1.4.0b1
Requires:	php-pear-Validate >= 0.8.4
Obsoletes:	php-pear-Services_oEmbed-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
oEmbed (http://www.oembed.com) is an open specification for
discovering more information about URI's. oEmbed services return
structure meta-data about a URI (e.g. type of object, title, author
information, thumbnail details, etc.).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
oEmebed (http://www.oembed.com) to otwarta specyfikacja opisująca
sposób odkrywania informacji o URI. Usługa oEmebed zwraca strukturę
zawierającą metadane o URI (n.p. typ obiektu, tytuł, informacja o
autorze, informacja o miniaturkach, itp.).

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
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/oEmbed
%{php_pear_dir}/Services/oEmbed.php
