%define	_beta	b1
Summary:	Neveredit - editor for Neverwinter Nights game files
Summary(pl.UTF-8):	Neveredit - edytor plików gry Neverwinter Nights
Name:		neveredit
Version:	0.8.2
Release:	0.%{_beta}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/neveredit/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	c768b17e501807da1d36a2039affb15d
Patch0:		%{name}-GTK2.patch
URL:		http://openknights.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	python-Numeric
Requires:	python-PyOpenGL
Requires:	python-numarray
Requires:	python-wxPython
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Neveredit strives to be an editor for files from Bioware's game
Neverwinter Nights. One day it may have all of the functionality of
Bioware's Windows tools, and maybe more. For now, it strives to
achieve basic editing functionality on non-Windows platforms. This
means that this is alpha quality software, and will at the current
stage likely do bad things to your files.

%description -l pl.UTF-8
Neveredit stara się być edytorem plików gry Neverwinter Nights
firmy Bioware. Być może pewnego dnia będzie miał funkcjonalność
narzędzi Bioware dla Windows a może nawet więcej. Aktualnie stara
się osiągnąć podstawową funkcjonalność edytora dla platform
niewindowsowych. Oznacza to, że Neveredit jest wciąż programem
klasy alfa i w obecnej jego formie jest wysoce prawdopodobne, że
zepsuje modyfikowane pliki.

%prep
%setup -q -n %{name}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/neveredit
%{py_sitescriptdir}/*.egg-info
