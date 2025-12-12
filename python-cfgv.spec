%global pypi_name cfgv

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        2
Summary:        Validate configuration and produce human readable error messages
Group:          Development/Python
License:        MIT
URL:            https://github.com/asottile/cfgv
Source0:        https://files.pythonhosted.org/packages/source/c/cfgv/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Validate configuration and produce human readable error messages

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
