Summary:	Tool to generate documentation for Erlang and Elixir
Name:		ex_doc
Version:	0.34.2
Release:	1
License:	Apache v2.0
Group:		Development/Tools
Source0:	https://github.com/elixir-lang/ex_doc/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9d10b02ccf164f3571efe2b593f412a2
Source1:	https://repo.hex.pm/tarballs/earmark_parser-1.4.39.tar
# Source1-md5:	f4541e91891b213f09ffb9b20e2ca3ce
Source2:	https://repo.hex.pm/tarballs/easyhtml-0.3.2.tar
# Source2-md5:	0813574edda74add2aa0e6cda102765a
Source3:	https://repo.hex.pm/tarballs/floki-0.36.2.tar
# Source3-md5:	228ab5f1e324b0ebdf74b368ef0b039f
Source4:	https://repo.hex.pm/tarballs/jason-1.4.1.tar
# Source4-md5:	abba3e1577cebebb42936ec0b67a05c9
Source5:	https://repo.hex.pm/tarballs/makeup-1.1.2.tar
# Source5-md5:	afbbedb30fac9f624c1b6b5dd0010f0b
Source6:	https://repo.hex.pm/tarballs/makeup_c-0.1.1.tar
# Source6-md5:	68ccf7c3da96181d1c463b010ddbdb97
Source7:	https://repo.hex.pm/tarballs/makeup_elixir-0.16.2.tar
# Source7-md5:	7bde55455d0b66d7d2838fd50b1b9444
Source8:	https://repo.hex.pm/tarballs/makeup_erlang-1.0.0.tar
# Source8-md5:	144c1b1838fc2730c674bfab8a5baf99
Source9:	https://repo.hex.pm/tarballs/makeup_html-0.1.1.tar
# Source9-md5:	8805161dda84519a6754dbd316bae7e5
Source10:	https://repo.hex.pm/tarballs/nimble_parsec-1.4.0.tar
# Source10-md5:	bd05f136e479edd64804a6f512939f13
URL:		https://elixir-lang.org/
BuildRequires:	elixir
%requires_ge	erlang
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExDoc is a tool to generate documentation for Erlang and Elixir
projects.

%prep
%setup -q

mkdir deps
cd deps
for s in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	%{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10}; do
	fn=`basename $s`
	tar -Oxf $s contents.tar.gz | tar -zx --one-top-level=${fn%-*}
done

%build
LC_ALL=C.UTF-8; export LC_ALL
mix deps.get
MIX_ENV=prod mix escript.build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp -p ex_doc $RPM_BUILD_ROOT%{_bindir}
%{__sed} -e '1s,/usr/bin/env escript,/usr/bin/escript,' ex_doc > $RPM_BUILD_ROOT%{_bindir}/ex_doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/ex_doc
