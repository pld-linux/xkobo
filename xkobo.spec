Summary:	X11 space arcade game
Summary(fr.UTF-8):	Jeu d'arcade dans l'espace
Summary(pl.UTF-8):	Gra zręcznościowa rozgrywająca się w kosmosie
Name:		xkobo
Version:	1.11+w01
Release:	1
Group:		X11/Applications/Games
License:	GPL
Vendor:		Akira Higuchi <a-higuti@math.hokudai.ac.jp>
Source0:	http://www.redhead.dk/download/pub/Xkobo/%{name}-%{version}.tar.gz
# Source0-md5:	ff5365868ef825e34eb2504c0ed7a58f
#Source1:	%{name}.desktop
Patch0:		%{name}-imake.patch
Patch1:		%{name}-man.patch
URL:		http://seki.math.hokudai.ac.jp:20080/xkobo-current.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_scoredir	%{_var}/games

%description
Xkobo is a arcade video game for X11. The goal is to destroy the enemi
bases. But the enemi will fire at you and send fighter spacecrafts to
get you. You'll have hours and hours of fun with this game.

%description -l fr.UTF-8
Xkobo est un jeux video d'arcade pour X11. Le but est de détruire les
bases enemies. Mais l'enemi fera feu sur vous et vous enverra des
navettes de chasse pour vous avoir. Vous aurez des heures et des
heures de plaisir avec ce jeu.

%description -l pl.UTF-8
Xkobo to gra zręcznościowa dla X11. Jej celem jest niszczenie wrogich
baz. Wrogowie jednak będą strzelać do Was i bronić się z pomocą swojej
floty. Czeka Was dużo godzin dobrej zabawy!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
%{__make} xkobo \
	CDEBUGFLAGS="%{rpmcflags}" \
	HSCORE_DIR=%{_scoredir}/xkobo-scores

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR="$RPM_BUILD_ROOT" \
	HSCORE_DIR=%{_scoredir}/xkobo-scores

mv -f $RPM_BUILD_ROOT%{_mandir}/man{1,6}
mv -f $RPM_BUILD_ROOT%{_mandir}/man6/xkobo.{1,6}x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README*
%attr(2755,root,games) %{_bindir}/xkobo
%{_mandir}/man6/*
%attr(0775,root,games) %dir %{_scoredir}/xkobo-scores
