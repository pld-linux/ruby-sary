%define pkgname sary
Summary:	Ruby Binding of Sary
Summary(pl.UTF-8):	Wiązanie języka Ruby do biblioteki Sary
Name:		ruby-%{pkgname}
Version:	1.2.0
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages
Source0:	http://sary.sourceforge.net/%{pkgname}-ruby-%{version}.tar.gz
# Source0-md5:	c885abffea72f25cb0f6286770a78ac1
Patch0:		%{name}-no-version.patch
Patch1:		%{name}-ruby19.patch
URL:		http://sary.sourceforge.net/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	sary-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Binding of Sary.

%description -l pl.UTF-8
Wiązanie języka Ruby do biblioteki Sary.

%prep
%setup -q -n %{pkgname}-ruby-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC `pkg-config glib-2.0 --cflags`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.en.rd Reference.en.rd
%lang(ja) %doc README.ja.rd Reference.ja.rd
%attr(755,root,root) %{ruby_sitearchdir}/%{pkgname}.so
