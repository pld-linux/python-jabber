%include	/usr/lib/rpm/macros.python

%define		module	jabber
%define pre	pre1

Summary:	"jabber.py" python module for Jabber applications
Summary(pl):	Modu³y Pythona "jabber.py" dla aplikacji Jabber
Name:		python-%{module}
Version:	0.5
Release:	0.%{pre}.3
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/jabberpy/jabberpy-%{version}-%{pre}.tar.gz
# Source0-md5:	884dda8ecac56065b2b7763fc5483f67
URL:		http://jabberpy.sourceforge.net/
BuildRequires:	python-modules
BuildRequires:	python-devel
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jabber.py is a Python module for the Jabber instant messaging
protocol. jabber.py deals with the XML parsing and socket code,
leaving the programmer to concentrate on developing quality Jabber
based applications with Python.

%description -l pl
jabber.py to modu³ Pythona do protoko³u komunikatora Jabber. jabber.py
obs³uguje analizowanie XML-a i gniazda, pozwalaj±c programi¶cie
skoncentrowaæ siê na tworzeniu w Pythonie wysokiej jako¶ci aplikacji
opartych na Jabberze.

%prep
%setup -q -n jabberpy

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{pre}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{pre}

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}
echo "jabber" > $RPM_BUILD_ROOT%{py_sitescriptdir}/jabber.pth
rm -f $RPM_BUILD_ROOT%{py_sitedir}/jabber/*.py
# Workaround for http://sourceforge.net/tracker/index.php?func=detail&aid=897527&group_id=30215&atid=398567
touch $RPM_BUILD_ROOT%{py_sitedir}/jabber/__init__.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README
%{py_sitescriptdir}/jabber.pth
%dir %{py_sitedir}/jabber
%{py_sitedir}/jabber/__init__.py
%{py_sitedir}/jabber/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}-%{pre}
%{_examplesdir}/%{name}-%{version}-%{pre}/*
