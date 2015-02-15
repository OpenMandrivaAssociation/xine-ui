Summary:	A Free Video Player
Name:		xine-ui
Version:	0.99.9
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://xine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/xine/xine-lib/%{version}/%{name}-%{version}.tar.xz
Source1:	xine-opendvd.desktop
Patch0:		xine-ui-0.99.7-locale.patch
BuildRequires:	aalib-devel
BuildRequires:	jpeg-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(caca)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpng)
Buildrequires:	pkgconfig(libxine)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(nvtvsimple)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
Requires:	curl
Requires:	xine-plugins

%description
xine is a free GPL-licensed video player for UNIX-like systems.

User interface for the X Window system.

%package	aa
Summary:	XINE - Ascii Art player
Requires:	xine-plugins
Requires:	xine-aa

%description	aa
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with ascii art (text mode) output.

%package	fb
Summary:	XINE - framebuffer video player
Requires:	xine-plugins

%description	fb
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with support for linux framebuffer output.

%prep
%setup -q
%patch0 -p1

%build
export XINE_DOCPATH="%{_datadir}/doc/xine-ui"
%configure2_5x	--enable-vdr-keys \
		--with-caca \
		--with-aalib
%make

%install
%makeinstall_std transform=""
install -m644 misc/desktops/xine.desktop -D %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m644 %{SOURCE1} -D %{buildroot}%{_datadir}/apps/solid/actions/xine-opendvd.desktop

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
%{_datadir}/apps/solid/actions/xine-opendvd.desktop
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

