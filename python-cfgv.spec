# Created by pyp2rpm-3.3.5
%global pypi_name cfgv

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        1
Summary:        Validate configuration and produce human readable error messages
Group:          Development/Python
License:        MIT
URL:            https://github.com/asottile/cfgv
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
[![Build Status]( [![Azure DevOps coverage]( Validate configuration and produce
human readable error messages. Installationpip install cfgv Sample error
messagesThese are easier to see by example. Here's an example where I typo'd
true in a [pre-commit]() configuration.

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
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
