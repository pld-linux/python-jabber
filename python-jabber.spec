%include	/usr/lib/rpm/macros.python

%define		module	jabber

Summary:	"jabber.py" python module for Jabber applications
Summary(pl):	Modu�y Pythona "jabber.py" dla aplikacji Jabber
Name:		python-%{module}
Version:	0.4
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/jabberpy/jabberpy%{version}-0.tar.gz
# Source0-md5:	4fc5e10c83bb12e61fbc36bb4424ad79
URL:		http://jabberpy.sourceforge.net/
BuildRequires:	python-modules
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jabber.py is a Python module for the Jabber instant messaging
protocol. jabber.py deals with the xml parsing and socket code,
leaving the programmer to concentrate on developing quality Jabber
based applications with Python.

%description -l pl
jabber.py to modu� Pythona do protoko�u komunikatora Jabber. jabber.py
obs�uguje analizowanie XML i gniazda, pozwalaj�c programi�cie
skoncentrowa� si� na tworzeniu w Pythonie wysokiej jako�ci aplikacji
opartych na Jabberze.

%prep
%setup -q -n jabberpy%{version}-0

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%{py_sitedir}/*.py[co]
%{_examplesdir}/%{name}-%{version}
