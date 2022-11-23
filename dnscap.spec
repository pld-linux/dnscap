Summary:	Network capture utility for DNS traffic
Summary(pl.UTF-8):	Zamiennik tcpdumpa dla ruchu DNS
Name:		dnscap
Version:	2.1.0
Release:	1
License:	BSD-like/distributable
Group:		Networking/Utilities
Source0:	https://www.dns-oarc.net/files/dnscap/%{name}-%{version}.tar.gz
# Source0-md5:	5a6a2497c818b00ebd5f0f49fc94a636
URL:		https://www.dns-oarc.net/tools/dnscap
BuildRequires:	groff
BuildRequires:	ldns-devel
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Network capture utility designed specifically for DNS traffic. It is
expected to be used for gathering continuous research or audit traces.

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*%{_bindir}/env\s+perl(\s|$),#!%{__perl}\1,' \
      plugins/rssm/dnscap-rssm-rssac002

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTORS README.md
%attr(755,root,root) %{_bindir}/dnscap
%attr(755,root,root) %{_bindir}/dnscap-rssm-rssac002
%dir %{_libdir}/dnscap
%attr(755,root,root) %{_libdir}/dnscap/*.so
%{_mandir}/man1/dnscap.1*
%{_mandir}/man1/dnscap-rssm-rssac002.1*
