Summary:	Linux Lexmark 1000/1100 Printer Driver
Name:		lm1100
Version:	1.0.2a
Release:	%mkrel 4
Group:		System/Printing
License:	GPL
URL:		http://www.linuxprinting.org/download/printing/lm1100/
Source:		http://www.linuxprinting.org/download/printing/lm1100/lm1100.%{version}.tar.gz
Patch0:		lm1100-1.0.2a-gcc32.patch
Patch1:		lm1100.1.0.2a-fix-compile-gcc-3.4.patch
Patch2:		lexmark2ppm.pl.patch
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

%build
%serverbuild

# Correct "friend" declarations for gcc 3.1
perl -p -i -e 's/friend Lexmark/friend class Lexmark/' *.h
# Remove extra qualifications '<class>::<member>' on class members, to make
# code compiling with gcc 4.1.1.
perl -p -i -e 's/\b[^\s:]+:://' *.h

%make CC="g++ $CXXFLAGS"

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
