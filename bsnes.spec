#
# Spec file for package bsnes
#
# Copyright © 2018–2019 Markus S. <kamikazow@opensuse.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

%define _cxx g++

Name:             bsnes
Summary:          Super Nintendo Emulator
Version:          115
Release:          1
Group:            System/Emulators/Other

# https://github.com/byuu/bsnes/blob/master/LICENSE.txt
License:          GPL-3.0-only
URL:              https://byuu.org/emulation/bsnes/
Source0:          https://github.com/bsnes-emu/bsnes/archive/v%{version}.tar.gz
BuildRequires:    gcc gcc-c++
BuildRequires:    hicolor-icon-theme
BuildRequires:    sed
BuildRequires:    pkgconfig(alsa)
BuildRequires:    pkgconfig(ao)
BuildRequires:    pkgconfig(cairo)
BuildRequires:    pkgconfig(gl)
BuildRequires:    pkgconfig(gtk+-2.0)
BuildRequires:    pkgconfig(gtksourceview-2.0)
BuildRequires:    pkgconfig(libpulse)
BuildRequires:    pkgconfig(libudev)
BuildRequires:    pkgconfig(openal)
BuildRequires:    pkgconfig(sdl2)
BuildRequires:    pkgconfig(xext)
BuildRequires:    pkgconfig(xi)
BuildRequires:    pkgconfig(xinerama)
BuildRequires:    pkgconfig(xrandr)
BuildRequires:    pkgconfig(xxf86vm)
BuildRequires:    pkgconfig(xv)

Requires(post):   hicolor-icon-theme
Requires(postun): hicolor-icon-theme

%if 0%{?fedora} > 26
%undefine _debugsource_packages
%endif

%description
bsnes is a Super Nintendo / Super Famicom emulator.
It is a subset project of higan and focuses on performance, features, and ease of use.

%prep
%setup -q
sed -i "/flags += -march=native/d" ./bsnes/GNUmakefile

%build
export CCFLAGS='%{optflags}'
make %{?_smp_mflags} -C bsnes compiler="%{_cxx}" platform="linux"

%install
export CCFLAGS='%{optflags}'
make prefix=%{buildroot}%{_prefix} -C bsnes install

# Icon installed in wrong directory by default
install -d %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/
mv %{buildroot}/%{_datadir}/icons/%{name}.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
