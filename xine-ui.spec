Name:		xine-ui
Summary:	A Free Video Player
Version:	0.99.7
Release:	1
License:	GPLv2+
Group:		Video
Source0:	http://downloads.sourceforge.net/project/xine/xine-lib/%{version}/%{name}-%{version}.tar.xz
URL:		http://xine.sourceforge.net/
Requires:	xine-plugins >= %{xineversion}-%{xinerel}
Requires:	curl	
Requires(post):	desktop-file-utils
Requires(postun):desktop-file-utils
BuildRequires:	aalib-devel
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
Buildrequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(nvtvsimple)
BuildRequires:	pkgconfig(xt)

%description 
xine is a free GPL-licensed video player for UNIX-like systems.

User interface for the X Window system.

%package	aa
Summary:	XINE - Ascii Art player
Group:		Video
Requires:	xine-plugins
Requires:	xine-aa

%description	aa
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with ascii art (text mode) output.

%package	fb
Summary:	XINE - framebuffer video player
Group:		Video
Requires:	xine-plugins

%description	fb
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with support for linux framebuffer output.


%prep
%setup -q

%build
export XINE_DOCPATH="%{_datadir}/doc/xine-ui"
%configure2_5x	--enable-vdr-keys \
		--with-caca \
		--with-aalib
%make

%install
%makeinstall_std transform=""
install -m644 misc/desktops/xine.desktop -D %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang xine-ui --all-name

rm -rf %{buildroot}%{_datadir}/doc
rm -rf %{buildroot}%{_datadir}/xine/desktop

%files -f xine-ui.lang
%doc AUTHORS ChangeLog README
%doc doc/README*
%{_bindir}/xine*
%{_datadir}/xine
%{_datadir}/pixmaps/*
%{_datadir}/applications/xine.desktop
%{_datadir}/applications/xine-ui.desktop
%{_datadir}/icons/hicolor/*/apps/xine*
%{_datadir}/mime/packages/xine-ui.xml
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files aa
%doc README
%{_bindir}/aaxine
%{_bindir}/cacaxine

%files fb
%doc README
%{_bindir}/fbxine
