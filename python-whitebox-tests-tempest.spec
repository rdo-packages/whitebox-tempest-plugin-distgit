%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%global service whitebox
%global plugin whitebox-tempest-plugin
%global module whitebox_tempest_plugin

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
This package contains Tempest tests of the "whitebox" variety. They verify \
things not exposed through the REST APIs. Additionally it provides a plugin \
to automatically load these tests into Tempest.

Name:       python-%{service}-tests-tempest
Version:    0.0.3
Release:    1%{?dist}
Summary:    Whitebox Tempest tests
License:    ASL 2.0
URL:        https://opendev.org/openstack/%{plugin}

Source0:    https://tarballs.opendev.org/openstack/%{plugin}/%{plugin}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:  https://tarballs.opendev.org/openstack/%{plugin}/%{plugin}-%{upstream_version}.tar.gz.asc
Source102:  https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%description
%{common_desc}

%package -n python3-%{service}-tests-tempest
Summary: %{summary}
%{?python_provide:%python_provide python3-%{service}-tests-tempest}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires:   crudini
Requires:   python3-paramiko >= 2.7.0
Requires:   python3-PyMySQL
Requires:   python3-tempest
Requires:   python3-oslo-log
Requires:   python3-oslo-serialization
Requires:   python3-oslo-config
Requires:   python3-sshtunnel

%description -n python3-%{service}-tests-tempest
%{common_desc}

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{plugin}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
%py_req_cleanup
# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{service}-tests-tempest
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/*.egg-info

%changelog
* Wed Sep 25 2024 RDO <dev@lists.rdoproject.org> 0.0.3-1
- Update to 0.0.3

