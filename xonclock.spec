Summary:	Simple X on-screen analog clock
Summary(pl.UTF-8):	Prosty zegar analogowy na ekran
Name:		xonclock
Version:	0.0.8.6
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xonclock/%{name}-%{version}.tar.gz
# Source0-md5:	92e03a232540bf6906ca544a0496368b
Patch0:		%{name}-config.patch
URL:		http://xonclock.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xonclock is X on-screen analog clock displayer with assignable skins.

%description -l pl.UTF-8
xonclock wyświetla na ekranie zegarek analogowy z możliwością zmiany
jego wyglądu.

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
