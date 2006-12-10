Summary:	Simple X on-screen analog clock
Summary(pl):	Prosty zegar analogowy na ekran
Name:		xonclock
Version:	0.0.8.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xonclock/%{name}-%{version}.tar.gz
# Source0-md5:	4a8a602c75ba27bd45e0491a0d36983e
Patch0:		%{name}-config.patch
URL:		http://xonclock.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xonclock is X on-screen analog clock displayer with assignable skins.

%description -l pl
xonclock wy�wietla na ekranie zegarek analogowy z mo�liwo�ci� zmiany
jego wygl�du.

%prep
%setup -q
%patch0 -p1

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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*