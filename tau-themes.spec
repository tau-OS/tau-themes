%define adw_version 1.7

Summary:        tauOS GTK Themes
Name:           tau-themes
Version:        1.1
Release:        1.7
License:        GPLv3
URL:            https://tauos.co
Source0:        README.md
Source1:        LICENSE
Source2:        https://github.com/lassekongo83/adw-gtk3/archive/refs/tags/v%adw_version.tar.gz
Patch0:         adw-gtk3-accent-colours.patch
BuildArch:      noarch
BuildRequires:  sassc
BuildRequires:  meson
BuildRequires:  ninja-build

Requires: tau-themes-adw

%description
A set of GTK Themes for tauOS

%package adw
Summary:        The theme from libadwaita ported to GTK-3
Provides:       adw-gtk3
Provides:       adw-gtk3-git
Conflicts:      adw-gtk3
Conflicts:      adw-gtk3-git

%description adw
The theme from libadwaita ported to GTK-3

%prep
%setup -c -T -D -q -a 2
cd adw-gtk3-%adw_version
%patch0 -p1

%build
cd adw-gtk3-%adw_version
%meson
%meson_build

%install

# Install licenses
mkdir -p licenses
install -pm 0644 %SOURCE1 licenses/LICENSE
install -pm 0644 %SOURCE0 README.md
cd adw-gtk3-%adw_version
%meson_install

%files
%license licenses/LICENSE
%doc README.md

%files adw
%{_datadir}/themes/adw-gtk3/*
%{_datadir}/themes/adw-gtk3-dark/*

%changelog
* Thu Apr 21 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1.7
- Update adw-gtk3 to v1.7
- Update Build System

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-2
- Add accent colours

* Thu Apr 7 2022 Jamie Murphy <jamie@fyralabs.com> - 1.1-1
- Initial Release
