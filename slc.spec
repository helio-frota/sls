Name:           sls
Version:        0.1.0
Release:        1%{?dist}
Summary:        A simple ls command
License:        MIT 
URL:            https://github.com/helio-frota/sls 
Source0:        v%{version}.tar.gz 

%description
A simple ls command.

%prep
%autosetup

%build
sh build.sh

%install
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/sls

%changelog
* Sat Mar 30 2019 Helio Frota <me@heliofrota.dev> - 0.1.0-1
- A foo version of the package
