Summary:	A Japanese reference/learning tool
Name:		kiten
Version:	15.08.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/kiten
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)

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

%files
%doc COPYING COPYING.DOC COPYING.LIB AUTHORS README
%doc %{_docdir}/HTML/en/kiten
%{_datadir}/applications/org.kde.kiten.desktop
%{_datadir}/applications/org.kde.kitenkanjibrowser.desktop
%{_datadir}/applications/kitenradselect.desktop
%{_datadir}/kiten
%{_bindir}/kiten
%{_bindir}/kitengen
%{_bindir}/kitenradselect
%{_bindir}/kitenkanjibrowser
%{_datadir}/appdata/kiten.appdata.xml
%{_datadir}/config.kcfg/kiten.kcfg
%{_iconsdir}/*/*/apps/kiten.*
%{_datadir}/fonts/kanjistrokeorders
%{_datadir}/kxmlgui5/kiten
%{_datadir}/kxmlgui5/kitenkanjibrowser
%{_datadir}/kxmlgui5/kitenradselect

#----------------------------------------------------------------------------

%define libkiten_major 5
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
%{_kde_libdir}/libkiten.so.%{libkiten_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkiten} = %{EVRD}
Conflicts:	kdeedu4-devel < 4.6.90

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_libdir}/libkiten.so
%{_includedir}/libkiten/

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
