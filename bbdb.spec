Summary:	The Insidious Big Brother Database
Name:		bbdb
Version:	2.35
Release:	%mkrel 2
License:	GPL
Group:		Editors

Source:		ftp://ftp.sourceforge.net/pub/sourceforge/bbdb/%name-%version.tar.bz2

URL:		http://bbdb.sourceforge.net/
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires:	emacs xemacs texinfo 
BuildArch:	noarch
%define lispdir	%_datadir/emacs/site-lisp/bbdb
%define texdir	%_datadir/texmf/tex/plain/bbdb

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
rm -Rf $RPM_BUILD_ROOT

install -d %buildroot/%lispdir
install -m 644 lisp/bbdb*.el %buildroot/%lispdir
install -m 644 lisp/bbdb*.elc %buildroot/%lispdir

install -d %buildroot%_infodir
install -m 644 texinfo/bbdb.info* %buildroot/%_infodir 

install -d %buildroot/%texdir
install -m 644 tex/*.tex %buildroot/%texdir

install -d %buildroot/%_bindir
install -m 755 utils/*.pl %buildroot/%_bindir

install -d %buildroot/%_sysconfdir/emacs/site-start.d
cat << EOF > %buildroot/%_sysconfdir/emacs/site-start.d/%name-init.el
(add-to-list 'load-path "%lispdir")

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
rm -fr $RPM_BUILD_ROOT

%post
%_install_info %{name}.info
if [ -x %_bindir/texhash -a -e %_datadir/texmf/ls-R ]; then
	%_bindir/texhash
fi

%postun
%_remove_install_info %{name}.info

%files
%defattr (-,root,root)
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/%{name}-init.el
%lispdir/*
%texdir/*.tex
%_bindir/*
%doc %_infodir/*

