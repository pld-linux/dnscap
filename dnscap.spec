#
%define		_snap	080302
Summary:	Network capture utility for DNS traffic
Summary(pl.UTF-8):	Zamiennik tcpdumpa dla ruchu DNS
Name:		dnscap
Version:	0.%{_snap}
Release:	1
License:	ISC
Group:		Applications/Networking
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	e5451875e01551568e46a3c461641311
URL:		http://public.oarci.net/tools/dnscap/
BuildRequires:	bind-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Network capture utility designed specifically for DNS traffic. It is
expected to be used for gathering continuous research or audit traces.

%prep
%setup -q -n %{name}

%build
%{__make} \
	PORTCFLAGS="%{rpmcflags}" \
	CDEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install dnscap $RPM_BUILD_ROOT%{_bindir}
install dnscap.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
