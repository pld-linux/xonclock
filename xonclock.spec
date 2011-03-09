Summary:	Simple X on-screen analog clock
Summary(pl.UTF-8):	Prosty zegar analogowy na ekran
Name:		xonclock
Version:	0.0.9.3
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/xonclock/%{name}-%{version}.tar.gz
# Source0-md5:	3505b6ab52244bd9399936a3a1ed6351
Patch0:		%{name}-config.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-freetype.patch
Patch3:		%{name}-link.patch
URL:		http://xonclock.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 1:2.1.9
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel >= 2:1.2.13
BuildRequires:	libtiff-devel >= 3.8.2
BuildRequires:	xorg-lib-libXpm-devel >= 3.5.5
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xonclock is X on-screen analog clock displayer with assignable skins.

%description -l pl.UTF-8
xonclock wyświetla na ekranie zegarek analogowy z możliwością zmiany
jego wyglądu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS src/xonclockrc-example
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/xonclock.1*
