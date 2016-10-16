#
# Conditional build:
%bcond_without	tests		# don't build and run tests

%include	/usr/lib/rpm/macros.java
Summary:	Keywhiz is a secret management solution
Name:		keywhiz
Version:	0.7.10
Release:	0.1
License:	Apache v2.0
Group:		Applications/System
Source0:	https://github.com/square/keywhiz/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/square/keywhiz
BuildRequires:	jpackage-utils
BuildRequires:	maven
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.556
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Keywhiz is a system for distributing and managing secrets.

%prep
%setup -q

%build
# https://github.com/square/keywhiz/blob/master/Dockerfile
mvn dependency:copy-dependencies -P docker --fail-never
mvn install -P docker

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUG-BOUNTY.md CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS README.md
