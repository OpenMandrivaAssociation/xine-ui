%define version 0.99.5
%define	name    xine-ui
%define	xineversion 1.1.1
%define	xinerel	7.1

Name:		%name
Summary:	A Free Video Player
Version:	%version
Release:	%mkrel 3
License:	GPL
Group:		Video
Source0:	http://prdownloads.sourceforge.net/xine/%name-%version.tar.bz2
URL:		http://xine.sourceforge.net/
Requires:	xine-plugins >= %xineversion-%xinerel
Requires:	curl	
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires: desktop-file-utils
BuildRequires:	aalib-devel
#BuildRequires:	libcaca-devel
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

%build
export XINE_DOCPATH="%_datadir/doc/xine-ui-%version"
%configure2_5x --enable-vdr-keys --without-caca --with-aalib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std transform=""
install -D -m 644 misc/desktops/xine.desktop %buildroot%_datadir/applications/%name.desktop

%if 0
xinelist=$(pkg-config --variable xine_list libxine)
perl -pi -e "s^MimeType=.*^MimeType=$($xinelist)^" $RPM_BUILD_ROOT%{_datadir}/applications/*
%endif

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Video;Player" \
  --add-category="AudioVideo;Video" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


#language files
%find_lang xitk
%find_lang xine-ui
cat xitk.lang >> xine-ui.lang

rm -rf %buildroot%_datadir/doc
rm -rf %buildroot%_datadir/xine/desktop

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor
%clean_desktop_database

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
%_datadir/icons/hicolor/*/apps/xine*
%_mandir/man1/*
%lang(de) %_mandir/de/man1/*
%lang(es) %_mandir/es/man1/*
%lang(fr) %_mandir/fr/man1/*
%lang(pl) %_mandir/pl/man1/*

%files aa
%defattr(-,root,root)
%doc README
%_bindir/aaxine
#%_bindir/cacaxine

%files fb
%defattr(-,root,root)
%doc README
%_bindir/fbxine


