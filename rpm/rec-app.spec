%global commit  7afef69a2c097323c828f87287bb47bc4c5e71eb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200424

%global sysname rec_app
%global uuid    com.github.amikha1lov.%{sysname}

Name:           rec-app
Version:        0.1.0
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        User friendly Open Source screencaster for Linux written in GTK
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/amikha1lov/rec_app
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)

Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       python3-pulsectl
Requires:       python3-pydbus
Requires:       slop

#Recommends:     gstreamer1-plugins-ugly

%description
User friendly Open Source screencaster for Linux written in GTK. Using free
GStreamer modules and not depend on FFmpeg.


%prep
%autosetup -n %{sysname}-%{commit} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}
install -m 0644 -Dp data/icons/%{uuid}.png \
    %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{uuid}.png
install -m 0644 -Dp data/icons/%{uuid}-symbolic.png \
    %{buildroot}%{_datadir}/icons/hicolor/symbolic/apps/%{uuid}-symbolic.png


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license COPYING
%doc README.md CREDITS
%{_bindir}/%{sysname}
%{_datadir}/%{sysname}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_metainfodir}/*.appdata.xml


%changelog
* Fri Apr 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200424git7afef69
- Update to latest git snapshot
- Add missing dep

* Sun Feb 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200223gitf6d8678
- Update to latest git snapshot

* Wed Feb 19 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200219gitccd1e90
- Update to latest git snapshot

* Sat Feb 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200208git5b6cda4
- Update to latest git snapshot

* Sat Jan 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.0-1.20200125git2fddefb
- Update to latest git snapshot

* Sat Jan 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-7.20200125git78505f6
- Add symbolic icon

* Fri Jan 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20200124git3655672
- Add new icon

* Thu Jan 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-5.20200123git37b0fe3
- Update to latest git snapshot

* Wed Jan 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20200122git0ce555c
- Update to latest git snapshot

* Mon Jan 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20200120git8121a4f
- Update to latest git snapshot

* Sat Jan 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20200118git79dc497
- Update to latest git snapshot

* Sat Jan 18 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20200118git4cc704a
- Initial package
