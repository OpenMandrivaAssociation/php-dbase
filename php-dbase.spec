%define modname dbase
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 15_%{modname}.ini

Summary:	dBase database file access functions
Name:		php-%{modname}
Epoch:		1
Version:	5.0.1
Release:	%mkrel 5
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/dbase
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
Source1:	dbase.ini
BuildRequires:	php-devel >= 3:5.3.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
These functions allow you to access records stored in dBase-format (dbf) databases.

%prep

%setup -q -n %{modname}-%{version}
[ "../package*.xml" != "/" ] && mv ../package*.xml .

cp %{SOURCE1} %{inifile}

%build
%serverbuild
phpize
%configure2_5x --with-libdir=%{_lib}
%make
mv modules/*.so .

%install
rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m0755 %{soname} %{buildroot}%{_libdir}/php/extensions/
install -m0644 %{inifile} %{buildroot}%{_sysconfdir}/php.d/%{inifile}

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CREDITS package*.xml 
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
