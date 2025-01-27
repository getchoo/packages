# Generated by rust2rpm 24
%bcond_without check

%global crate hyperfine

Name:           rust-hyperfine
Version:        1.16.1
Release:        1%{?dist}
Summary:        Command-line benchmarking tool

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyperfine
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          hyperfine-fix-metadata-auto.diff

BuildRequires:  anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
A command-line benchmarking tool.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-MIT
%doc CHANGELOG.md
%doc README.md
%{_bindir}/hyperfine

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
