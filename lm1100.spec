Summary:	Linux Lexmark 1000/1100 Printer Driver
Name:		lm1100
Version:	1.0.2a
Release:	%mkrel 16
Group:		System/Printing
License:	GPL
URL:		http://www.linuxprinting.org/download/printing/lm1100/
Source:		http://www.linuxprinting.org/download/printing/lm1100/lm1100.%{version}.tar.gz
Patch0:		lm1100-1.0.2a-gcc32.patch
Patch1:		lm1100.1.0.2a-fix-compile-gcc-3.4.patch
Patch2:		lexmark2ppm.pl.patch
Patch3:		lm1100.1.0.2a-LDFLAGS.diff
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Linux Lexmark 1000/1020/1100 Printer Driver. This filter converts a ppm file
into the  Lexmark 1000/1020/1100 internal format.

%prep

%setup -q -n %{name}.%{version}
%patch0 -p1
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%serverbuild

# Correct "friend" declarations for gcc 3.1
perl -p -i -e 's/friend Lexmark/friend class Lexmark/' *.h
# Remove extra qualifications '<class>::<member>' on class members, to make
# code compiling with gcc 4.1.1.
perl -p -i -e 's/\b[^\s:]+:://' *.h

%make CC="g++ $CXXFLAGS" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

# Executables (filter for usage with CUPS and printer emulator script for
# development and debugging (also debugging this RPM w/o Lexmark 1100).
install -m 0755 lm1100 %{buildroot}%{_bindir}
install -m 0755 lexmark2ppm.pl %{buildroot}%{_bindir}
install -m 0755 byteutil.pl %{buildroot}%{_bindir}

# Executables (filter for usage with CUPS and printer emulator script for
# development and debugging (also debugging this RPM w/o Lexmark 1100).
# LPD support
install -d %{buildroot}%{_libdir}/rhs/rhs-printfilters
[ -e ps-to-lm1100.fpi ] || mv ps-to-printer.fpi ps-to-lm1100.fpi # file name conflict
install -m 0755 ps-to-lm1100.fpi %{buildroot}%{_libdir}/rhs/rhs-printfilters
ln -s %{_bindir}/lm1100 %{buildroot}%{_libdir}/rhs/rhs-printfilters

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README RELEASE.* cmy.txt
%defattr(0755,root,root,0755)
%{_bindir}/lm1100
%{_bindir}/lexmark2ppm.pl
%{_bindir}/byteutil.pl
%{_libdir}/rhs/rhs-printfilters/lm1100
%{_libdir}/rhs/rhs-printfilters/ps-to-lm1100.fpi


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-15mdv2011.0
+ Revision: 666084
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-14mdv2011.0
+ Revision: 606414
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-13mdv2010.1
+ Revision: 520145
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2a-12mdv2010.0
+ Revision: 425985
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-11mdv2009.1
+ Revision: 318494
- use %%ldflags (P3)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2a-10mdv2009.0
+ Revision: 223118
- rebuild

* Fri Mar 28 2008 Anssi Hannula <anssi@mandriva.org> 1.0.2a-9mdv2008.1
+ Revision: 190804
- rebuild due to missing signature on x86_64

* Thu Jan 24 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-8mdv2008.1
+ Revision: 157339
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild with fixed %%serverbuild macro

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2a-6mdv2008.1
+ Revision: 152858
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2a-5mdv2008.1
+ Revision: 152856
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-4mdv2008.0
+ Revision: 75342
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-3mdv2008.0
+ Revision: 64162
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-2mdv2008.0
+ Revision: 61090
- rebuild

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-1mdv2008.0
+ Revision: 60979
- Import lm1100



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2a-1mdv2008.0
- initial Mandriva package

* Tue May 04 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-05-04 11:47:21 (59211)
- Added missing BuildRequires.

* Tue May 04 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-05-04 11:29:19 (59204)
- Updated URL/Source tags to new software location
- Removed lpd support

* Tue May 04 2004 Wanderlei Antonio Cavassin <cavassin@conectiva.com.br>
+ 2004-05-04 09:53:42 (59159)
- Forces rebuild.

* Sat Mar 15 2003 Claudio Matsuoka <claudio@conectiva.com>
+ 2003-03-15 14:39:34 (27506)
- fixed build for gcc 3.2

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 18:17:07 (8584)
- Imported package from 8.0.
