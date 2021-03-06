# Generated by rust2rpm 10
%bcond_with check
%global debug_package %{nil}

%global crate mockito

Name:           rust-%{crate}
Version:        0.22.0
Release:        1%{?dist}
Summary:        HTTP mocking for Rust

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/mockito
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
HTTP mocking for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages
which use "color" feature of "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+colored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+colored-devel %{_description}

This package contains library source intended for building other packages
which use "colored" feature of "%{crate}" crate.

%files       -n %{name}+colored-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Tue Nov 19 19:43:38 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.22.0-1
- Update to 0.22.0

* Fri Aug 09 14:55:06 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.20.0-1
- Update to 0.20.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 21 21:05:16 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.1-2
- Regenerate

* Sun Apr 28 09:31:27 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.17.1-1
- Initial package
