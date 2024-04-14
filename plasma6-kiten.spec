#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	A Japanese reference/learning tool
Name:		plasma6-kiten
Version:	24.02.2
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kiten
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/kiten/-/archive/%{gitbranch}/kiten-%{gitbranchd}.tar.bz2#/kiten-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kiten-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6Crash)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
Kiten is a Japanese reference/learning tool.

Kiten features:
* Search with english keyword, Japanese reading, or a Kanji string on a
  list of EDICT files.
* Search with english keyword, Japanese reading, number of strokes, grade
  number, or a Kanji on a list of KANJIDIC files.
* Comes with all necessary files.
* Very fast.
* Limit searches to only common entries.
* Nested searches of results possible.
* Compact, small, fast interface.
* Global KDE keybindings for searching highlighted strings.
* Learning dialog. (One can even open up multiple ones and have them sync
  between each other.)
* Browse Kanji by grade.
* Add Kanji to a list for later learning.
* Browse list, and get quizzed on them.

%files -f kiten.lang
%{_datadir}/applications/org.kde.kiten.desktop
%{_datadir}/applications/org.kde.kitenkanjibrowser.desktop
%{_datadir}/applications/org.kde.kitenradselect.desktop
%{_datadir}/kiten
%{_bindir}/kiten
%{_bindir}/kitenradselect
%{_bindir}/kitenkanjibrowser
%{_datadir}/metainfo/*.xml
%{_datadir}/config.kcfg/kiten.kcfg
%{_iconsdir}/*/*/apps/kiten.*
%{_datadir}/fonts/kanjistrokeorders

#----------------------------------------------------------------------------

%define libkiten_major 6
%define libkiten %mklibname kiten %{libkiten_major}

%package -n %{libkiten}
Summary:	Runtime library for Kiten
Group:		System/Libraries

%description -n %{libkiten}
libkiten is a library for managing a variety of japanese cross-language
dictionaries through a common interface. It provides a light abstraction layer
over various types of japanese dictionaries, with a simple facility for adding
more types.

%files -n %{libkiten}
%{_libdir}/libkiten.so.%{libkiten_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libkiten} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_libdir}/libkiten.so
%{_includedir}/libkiten/

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n kiten-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kiten --with-html
