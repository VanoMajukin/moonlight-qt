Name: moonlight-qt
Version: 4.3.1
Release: alt1

Summary: Moonlight PC is an open source PC client for NVIDIA GameStream
License: GPL-3.0
Group: Networking/Remote access
Url: https://moonlight-stream.org/

# Source-url: https://github.com/moonlight-stream/moonlight-qt/releases/download/v%version/MoonlightSrc-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake rpm-macros-qt5
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: libssl-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_ttf-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: libva-devel
BuildRequires: libvdpau-devel
BuildRequires: libopus-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libalsa-devel
BuildRequires: libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavresample-devel libavutil-devel libpostproc-devel libswresample-devel libswscale-devel

%description
Moonlight PC is an open source PC client for NVIDIA GameStream, as used by the NVIDIA Shield.

%prep
%setup

%build
%qmake_qt5 PREFIX=%buildroot/usr moonlight-qt.pro
%make

%install
%makeinstall

%files
%_bindir/moonlight
%_desktopdir/com.moonlight_stream.Moonlight.desktop
%_iconsdir/hicolor/scalable/apps/moonlight.svg
%_datadir/metainfo/com.moonlight_stream.Moonlight.appdata.xml

%changelog
* Tue Aug 15 2023 Ivan Mazhukin <vanomj@altlinux.org> 4.3.1-alt1
- Initial build for Alt Sisyphus
