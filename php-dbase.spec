%define modname dbase
%define dirname %{modname}
%define soname %{modname}.so
%define inifile 15_%{modname}.ini

Summary:	dBase database file access functions
Name:		php-%{modname}
Epoch:		1
Version:	5.1.0
Release:	2
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/dbase
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
Source1:	dbase.ini
BuildRequires:	php-devel >= 3:5.3.0

%description
These functions allow you to access records stored in dBase-format (dbf)
databases.

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


%changelog
* Wed Jun 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1:5.1.0-1mdv2012.0
+ Revision: 806375
- 5.1.0

* Thu May 03 2012 Oden Eriksson <oeriksson@mandriva.com> 1:5.0.1-5
+ Revision: 795421
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1:5.0.1-4
+ Revision: 761212
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1:5.0.1-3
+ Revision: 696405
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:5.0.1-2
+ Revision: 695378
- rebuilt for php-5.3.7

* Sun Mar 20 2011 Funda Wang <fwang@mandriva.org> 1:5.0.1-1
+ Revision: 647150
- import php-dbase


* Thu Feb 08 2007 Oden Eriksson <oeriksson@mandriva.com> 5.2.1-1mdv2007.0
+ Revision: 117391
- rebuilt against new upstream version (5.2.1)
- fix deps

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 5.2.0-1mdv2007.1
+ Revision: 77336
- rebuilt for php-5.2.0

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1mdv2007.1
+ Revision: 75192
- Import php-dbase

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.6-1
- rebuilt for php-5.1.6

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-2mdk
- rebuild

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.4-1mdk
- rebuilt for php-5.1.4

* Fri May 05 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.3-1mdk
- rebuilt for php-5.1.3

* Thu Feb 02 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-2mdk
- new group (Development/PHP) and iurt rebuild

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 5.1.2-1mdk
- rebuilt against php-5.1.2

* Tue Nov 29 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.1-1mdk
- rebuilt against php-5.1.1

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-1mdk
- rebuilt against php-5.1.0

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC4.1mdk
- rebuilt against php-5.1.0RC4

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.2mdk
- rebuilt to provide a -debug package too

* Sun Oct 02 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0-0.RC1.1mdk
- rebuilt against php-5.1.0RC1

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5-1mdk
- rebuilt against php-5.0.5 (Major security fixes)

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- rename the package

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4-1mdk
- 5.0.4

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-4mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-3mdk
- rebuilt against a non hardened-php aware php lib

* Sun Jan 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-2mdk
- rebuild due to hardened-php-0.2.6

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3-1mdk
- rebuilt for php-5.0.3

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2-1mdk
- rebuilt for php-5.0.2

* Sun Aug 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1-1mdk
- rebuilt for php-5.0.1

* Wed Aug 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.0-1mdk
- rebuilt for php-5.0.0
- major cleanups

* Thu Jul 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.8-1mdk
- rebuilt for php-4.3.8

* Tue Jul 13 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-2mdk
- remove redundant provides

* Tue Jun 15 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.7-1mdk
- rebuilt for php-4.3.7

* Mon May 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-2mdk
- use the %%configure2_5x macro
- move scandir to /etc/php.d

* Thu May 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 4.3.6-1mdk
- built for php 4.3.6

