%global pypi_name cfgv

Name:           python-%{pypi_name}
Version:        3.5.0
Release:        1
Summary:        Validate configuration and produce human readable error messages
Group:          Development/Python
License:        MIT
URL:            https://github.com/asottile/cfgv
Source0:        https://files.pythonhosted.org/packages/source/c/cfgv/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)

%description
Validate configuration and produce human readable error messages

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
