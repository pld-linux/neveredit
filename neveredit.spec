Summary:	Neveredit
Summary(pl):	Neveredit
Name:		neveredit
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		X11/Applicatiuons
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	f9f9f4768e0f4df60a51c538ea82e40a
Patch0:		%{name}-GTK2.patch
BuildRequires:	libnw-devel
BuildRequires:	wxGTK2-devel
URL:		http://openknights.sourceforge.net/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%prep
%setup -q -n %{name}

%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755, root, root) %{_bindir}/neveredit
