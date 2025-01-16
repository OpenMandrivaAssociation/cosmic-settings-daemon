%undefine _debugsource_packages
%global crate cosmic-settings-daemon

Name:           cosmic-settings-daemon
Version:        1.0.0
Release:        0.alpha5.1
Summary:        Settings daemon for the COSMIC Desktop Environment
Group:          COSMIC
# Zlib OR Apache-2.0 OR MIT
License:        0BSD OR MIT OR Apache-2.0 AND Apache-2.0 AND Apache-2.0 OR MIT AND Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-3.0-or-later AND ISC AND MIT AND MIT OR Apache-2.0 AND MIT OR Apache-2.0 OR CC0-1.0 AND MIT OR Apache-2.0 OR Zlib AND MIT OR Zlib OR Apache-2.0 AND MPL-2.0 AND Unlicense OR MIT AND Zlib AND Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/pop-os/cosmic-settings-daemon
Source0:        https://github.com/pop-os/cosmic-settings-daemon/archive/epoch-%{version}-alpha.5.1/%{name}-epoch-%{version}-alpha.5.1.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-settings-daemon at the specified commit
# * cargo vendor > vendor-config-%%{shortcommit}.toml
# * tar -pczf vendor-%%{shortcommit}.tar.gz vendor
Source1:        vendor.tar.xz
# * mv vendor-config-%%{shortcommit}.toml ..
Source2:        cargo_config

BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  cargo
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pam)
#BuildRequires:  just

Requires:       acpid
#Requires:       adw-gtk3-theme

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5.1 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%make_build

%install
%make_install

%files
%license LICENSE
%{_bindir}/cosmic-settings-daemon
%{_datadir}/cosmic/com.system76.CosmicSettings.Shortcuts/*
%{_datadir}/polkit-1/rules.d/cosmic-settings-daemon.rules
