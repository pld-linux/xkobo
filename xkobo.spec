Summary:	X11 space arcade game
Summary(fr):	Jeu d'arcade dans l'espace
Summary(pl):	Gra zrecznosciowa rozgrywajaca sie w kosmosie
Name:		xkobo
Version:	1.11+w01
Release:	1
Group:		X11/Applications/Games	
License:	GPL
Vendor:		Akira Higuchi <a-higuti@math.hokudai.ac.jp>
Source0:	http://www.redhead.dk/download/pub/Xkobo/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-%{version}-imake.patch
URL:		http://seki.math.hokudai.ac.jp:20080/xkobo-current.html
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_gamesdir	%{_usr}/games

%description
Xkobo is a arcade video game for X11. The goal is to destroy the enemi
bases. But the enemi will fire at you and send fighter spacecrafts to
get you. You'll have hours and hours of fun with this game.

%description -l fr
Xkobo est un jeux video d'arcade pour X11. Le but est de détruire les
bases enemies. Mais l'enemi fera feu sur vous et vous enverra des
navettes de chasse pour vous avoir. Vous aurez des heures et des
heures de plaisir avec ce jeu.

%description -l pl
Xkobo to gra zrêczno¶ciowa dla X11. Jej celem jest niszczenie wrogich baz.
Wrogowie jednak bêd± strzelaæ do Was i broniæ siê z pomoc± swojej floty.
Czeka Was du¿o godzin dobrej zabawy!

%prep

%setup -q

%patch0 -p1

%build
xmkmf -a
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%{__make} xkobo

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR="$RPM_BUILD_ROOT"
mv -f $RPM_BUILD_ROOT/%{_mandir}/man{1,6}

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README*
%attr(2755,games,games) %{_bindir}/xkobo
%{_mandir}/man6/*
%attr(0775,games,games) %dir %{_gamesdir}/xkobo-scores

%clean
rm -rf $RPM_BUILD_ROOT
