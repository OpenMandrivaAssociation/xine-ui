%define version 0.99.4
%define rel     8
%define	name    xine-ui
%define	xineversion 1.1.1
%define	xinerel	7.1

Name:		%name
Summary:	A Free Video Player
Version:	%version
Release:	%mkrel %rel
License:	GPL
Group:		Video
Source0:	http://prdownloads.sourceforge.net/xine/%name-%version.tar.bz2
Patch0:		xine-ui-cvs-vdr-events.patch
URL:		http://xine.sourceforge.net/
Requires:	xine-plugins >= %xineversion-%xinerel
Requires:	curl	
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: desktop-file-utils
BuildRequires:	aalib-devel
BuildRequires:	libcaca-devel
BuildRequires:	curl-devel
BuildRequires:	png-devel
Buildrequires:	libxine-devel >= %xineversion-%xinerel
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	libnvtvsimple-devel
%if %mdkversion >= 200700
BuildRequires:	libxt-devel
%else
BuildRequires:	X11-devel
%endif
#BuildRequires:	automake1.7
BuildRoot:	%_tmppath/%name-%version-%release-buildroot

%description 
xine is a free GPL-licensed video player for UNIX-like systems.

User interface for the X Window system.

%package	aa
Summary:	XINE - Ascii Art player
Group:		Video
Requires:	xine-plugins >= %xineversion-%xinerel
Requires:	xine-aa

%description	aa
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with ascii art (text mode) output.

%package	fb
Summary:	XINE - framebuffer video player
Group:		Video
Requires:	xine-plugins >= %xineversion-%xinerel

%description	fb
xine is a free GPL-licensed video player for UNIX-like systems.

User interface with support for linux framebuffer output.


%prep
%setup -q
%patch0 -p0

%build
export XINE_DOCPATH="%_datadir/doc/xine-ui-%version"
%configure2_5x --enable-vdr-keys
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std transform=""
install -D -m 644 misc/desktops/xine.desktop %buildroot%_datadir/applications/%name.desktop

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF 
?package(xine-ui):command="%{_bindir}/xine" title="Xine" longtitle="Xine Video Player" needs="X11" section="Multimedia/Video" icon="xine.png" 	mimetypes="video/mpeg,video/msvideo,video/quicktime,video/x-avi,video/x-ms-asf,video/x-ms-wmv,video/x-msvideo,application/ogg,application/x-ogg,audio/x-mp3,audio/x-mpeg,video/x-fli,audio/x-wav,application/x-matroska" accept_url="true" multiple_files="true" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Video;Player" \
  --add-category="AudioVideo;Video" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

#install icons
install -m644 misc/desktops/xine_48x48.png -D %{buildroot}%{_liconsdir}/xine.png
install -m644 misc/desktops/xine_32x32.png -D %{buildroot}%{_iconsdir}/xine.png
install -m644 misc/desktops/xine_16x16.png -D %{buildroot}%{_miconsdir}/xine.png

#language files
%find_lang xitk
%find_lang xine-ui
cat xitk.lang >> xine-ui.lang

rm -rf %buildroot%_datadir/doc
rm -rf %buildroot%_datadir/xine/desktop

%post
%update_menus
%{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null

%postun
%clean_menus
if [ -x %{_bindir}/update-desktop-database ]; then %{_bindir}/update-desktop-database %{_datadir}/applications > /dev/null ; fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f xine-ui.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc doc/README*
%_bindir/xine*
%_datadir/xine
%_datadir/pixmaps/*
%_datadir/applications/%name.desktop
%_mandir/man1/*
%lang(de) %_mandir/de/man1/*
%lang(es) %_mandir/es/man1/*
%lang(fr) %_mandir/fr/man1/*
%lang(pl) %_mandir/pl/man1/*
%_menudir/*
%_miconsdir/xine.png
%_liconsdir/xine.png
%_iconsdir/xine.png

%files aa
%defattr(-,root,root)
%doc README
%_bindir/aaxine
#%_bindir/cacaxine

%files fb
%defattr(-,root,root)
%doc README
%_bindir/fbxine


