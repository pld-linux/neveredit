Summary:	Neveredit - editor for Neverwinter Nights game files
Summary(pl):	Neveredit - edytor plików gry Neverwinter Nights
Name:		neveredit
Version:	0.7b2
Release:	0.2
License:	GPL
Group:		X11/Applicatiuons
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	36e1f8ed9aa258498f56ca9ec99bbb69
Patch0:		%{name}-GTK2.patch
URL:		http://openknights.sourceforge.net/
#BuildRequires:	libnw-devel
BuildRequires:	wxGTK2-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Neveredit strives to be an editor for files from Bioware's game
Neverwinter Nights. One day it may have all of the functionality of
Bioware's Windows tools, and maybe more. For now, it strives to
achieve basic editing functionality on non-Windows platforms. This
means that this is alpha quality software, and will at the current
stage likely do bad things to your files.

%description -l pl
Neveredit stara siê byæ edytorem plików gry Neverwinter Nights firmy
Bioware. Byæ mo¿e pewnego dnia bêdzie mia³ funkcjonalno¶æ narzêdzi
Bioware dla Windows a mo¿e nawet wiêcej. Aktualnie stara siê osi±gn±æ
podstawow± funkcjonalno¶æ edytora dla platform niewindowsowych.
Oznacza to, ¿e Neveredit jest wci±¿ programem klasy alfa i w obecnej
jego formie jest wysoce prawdopodobne, ¿e zepsuje modyfikowane pliki.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README*
%{py_sitescriptdir}/neveredit
