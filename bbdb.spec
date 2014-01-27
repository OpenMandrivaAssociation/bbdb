Summary:	The Insidious Big Brother Database
Name:		bbdb
Version:	2.36
Release:	2
License:	GPL
Group:		Editors
Source:		ftp://ftp.sourceforge.net/pub/sourceforge/bbdb/%{name}-%{version}.tar.bz2
URL:		http://bbdb.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	emacs xemacs texinfo 
BuildArch:	noarch
%define lispdir	%{_datadir}/emacs/site-lisp/bbdb
%define texdir	%{_datadir}/texmf/tex/plain/bbdb

%description
BBDB is a rolodex-like database program for GNU Emacs which is tightly
integrated with the Emacs mail and news readers (Gnus, MH-E, and
RMAIL.)

%prep
%setup -q
perl -pi -e 's:^#!/usr/local/bin/perl5?:#!/usr/bin/perl:' utils/*.pl

%build
%configure
make bbdb rmail mhe gnus info

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{lispdir}
install -m 644 lisp/bbdb*.el %{buildroot}/%{lispdir}
install -m 644 lisp/bbdb*.elc %{buildroot}/%{lispdir}

install -d %{buildroot}%{_infodir}
install -m 644 texinfo/bbdb.info* %{buildroot}/%{_infodir}

install -d %{buildroot}/%{texdir}
install -m 644 tex/*.tex %{buildroot}/%{texdir}

install -d %{buildroot}/%{_bindir}
install -m 755 utils/*.pl %{buildroot}/%{_bindir}

install -d %{buildroot}/%{_sysconfdir}/emacs/site-start.d
cat << EOF > %{buildroot}/%{_sysconfdir}/emacs/site-start.d/%{name}-init.el
(add-to-list 'load-path "%{lispdir}")

;(require 'bbdb)

; Since the syntax-checking of phone numbers only works with American
; phone numbers the syntax-checking is disabled by default.
(setq bbdb-north-american-phone-numbers-p nil)

; Set the coding system in order to prevent problems with non-ASCII
; characters.  The available coding systems can be displayed with
; (list-coding-systems).
;(modify-coding-system-alist 'file "\\.bbdb" 'emacs-mule)

;(bbdb-initialize 'gnus 'mh-e 'rmail 'sendmail 'message 'sc 'w3)
EOF

%clean
rm -fr %{buildroot}

%post
if [ -x %{_bindir}/texhash -a -e %{_datadir}/texmf/ls-R ]; then
	%{_bindir}/texhash
fi


%files
%defattr (-,root,root)
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}-init.el
%{lispdir}/*
%{texdir}/*.tex
%{_bindir}/*
%doc %{_infodir}/*



%changelog
* Thu Sep 29 2011 Andrey Bondrov <abondrov@mandriva.org> 2.36-1mdv2012.0
+ Revision: 701980
- New version: 2.36

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.35-6mdv2011.0
+ Revision: 616713
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.35-5mdv2010.0
+ Revision: 424021
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.35-4mdv2009.0
+ Revision: 243169
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 2.35-2mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import bbdb


* Mon Jul 31 2006 Lenny Cartier <lenny@mandriva.com> 2.35-2mdv2007.0
- rebuild

* Wed Apr 20 2005 Lenny Cartier <lenny@mandriva.com> 2.35-1mdk
- 2.35

* Tue Jan 27 2004 Juan Quintela <quintela@anano> 2.34-6mdk
- rebuild.

* Wed Oct 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.34-5mdk
- do not use %%make macro

* Tue Aug 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.34-4mdk
- rebuild

* Sun Apr 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.34-3mdk
- adjust buildrequires
- fix previous changelog

* Thu Jan 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.34-2mdk
- rebuild

* Sun May 12 2002 Yves Duret <yduret@mandrakesoft.com> 2.34-1mdk
- version 2.34

* Sat Aug 25 2001 Lenny Cartier <lenny@mandrakesoft.com> 2.32-1mdk
- updated by Andreas Voegele <voegelas@users.sourceforge.net> 
	- new upstream version
	- set BuildArch to noarch
	- moved Lisp files into sub directory
	- added init script
	- fixed perl scripts
	- put TeX files into /usr/share/texmf/tex/plain/bbdb
	- /usr/bin/texhash is called in the post-installation script
	- the syntax-checking of phone numbers is disabled by default

* Wed Jun 27 2001  Lenny Cartier <lenny@mandrakesoft.com> 2.00.06-6mdk
- rebuild

* Thu Jan 04 2001 David BAUDENS <baudens@mandrakesoft.com> 2.00.06-5mdk
- Fix BuildRequires

* Tue Dec 12 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.00.06-4mdk
- fix url
- add install-info

* Tue Aug 22 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.00.06-3mdk
- macros
- BM

* Thu Apr 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.00.06-2mdk
- fix group
- fix sources permission

* Thu Jan 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 2.00.06-1mdk
- mandrake build
- v2.00.06
- updated the filelist 
