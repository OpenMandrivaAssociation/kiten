Name: kiten
Summary: A Japanese reference/learning tool
Version: 4.8.3
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL: http://edu.kde.org/kiten
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}

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
%_kde_appsdir/kiten
%_kde_appsdir/kitenradselect
%_kde_bindir/kiten
%_kde_bindir/kitengen
%_kde_bindir/kitenradselect
%_kde_bindir/kitenkanjibrowser
%_kde_iconsdir/*/*/apps/kiten.*
%_kde_datadir/applications/kde4/kiten.desktop
%_kde_datadir/config.kcfg/kiten.kcfg
%_kde_appsdir/kitenkanjibrowser
%_datadir/fonts/kanjistrokeorders
%doc  COPYING COPYING.DOC COPYING.LIB AUTHORS README
%doc %_kde_docdir/HTML/en/kiten

#---------------------------------------------

%define libkiten_major 4
%define libkiten %mklibname kiten %{libkiten_major}

%package -n %libkiten
Summary: Runtime library for Kiten
Group: System/Libraries

%description -n %libkiten
libkiten is a library for managing a variety of japanese cross-language
dictionaries through a common interface. It provides a light abstraction layer
over various types of japanese dictionaries, with a simple facility for adding
more types.

%files -n %libkiten
%_kde_libdir/libkiten.so.%{libkiten_major}*

#---------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/KDE and Qt
Requires: kdelibs4-devel
Requires: %libkiten = %version-%release
Conflicts: kdeedu4-devel < 4.6.90

%description  devel
Files needed to build applications based on %{name}.

%files devel
%_kde_libdir/libkiten.so
%_includedir/libkiten/

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde4 	
%make

%install
%makeinstall_std -C build

