%bcond clang 1
%bcond avahi 1
%bcond gamin 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_pkg tdegames
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		Trinity Desktop Environment - Games
Version:		14.1.6
Release:		1
Group:			System/GUI/Other
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/core/%{tarball_name}-%{version}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_PROGRAM_PATH=%{tde_prefix}/bin
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DBUILD_ALL=ON -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-arts-devel >= %{version}
BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tdemultimedia-devel >= %{version}

BuildRequires:	trinity-tde-cmake >= %{version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	desktop-file-utils
BuildRequires:	fdupes
BuildRequires:	libtool

# AVAHI support
%{?with_avahi:BuildRequires:  pkgconfig(avahi-client)}

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# ATTR support
BuildRequires:  pkgconfig(libattr)

# GLIB2 support
BuildRequires:	pkgconfig(glib-2.0)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:		trinity-kdegames < %{EVRD}
Provides:		trinity-kdegames = %{EVRD}
Obsoletes:		trinity-kdegames-libs < %{EVRD}
Provides:		trinity-kdegames-libs = %{EVRD}

Requires: trinity-libtdegames1 = %{EVRD}
Requires: trinity-tdegames-card-data = %{EVRD}
Requires: trinity-atlantik = %{EVRD}
Requires: trinity-kasteroids = %{EVRD}
Requires: trinity-katomic = %{EVRD}
Requires: trinity-kbackgammon = %{EVRD}
Requires: trinity-kbattleship = %{EVRD}
Requires: trinity-kblackbox = %{EVRD}
Requires: trinity-kbounce = %{EVRD}
Requires: trinity-kenolaba = %{EVRD}
Requires: trinity-kfouleggs = %{EVRD}
Requires: trinity-kgoldrunner = %{EVRD}
Requires: trinity-kjumpingcube = %{EVRD}
Requires: trinity-klickety = %{EVRD}
Requires: trinity-klines = %{EVRD}
Requires: trinity-kmahjongg = %{EVRD}
Requires: trinity-kmines = %{EVRD}
Requires: trinity-knetwalk = %{EVRD}
Requires: trinity-kolf = %{EVRD}
Requires: trinity-konquest = %{EVRD}
Requires: trinity-kpat = %{EVRD}
Requires: trinity-kpoker = %{EVRD}
Requires: trinity-kreversi = %{EVRD}
Requires: trinity-ksame = %{EVRD}
Requires: trinity-kshisen = %{EVRD}
Requires: trinity-ksirtet = %{EVRD}
Requires: trinity-ksmiletris = %{EVRD}
Requires: trinity-ksnake = %{EVRD}
Requires: trinity-ksokoban = %{EVRD}
Requires: trinity-kspaceduel = %{EVRD}
Requires: trinity-ktron = %{EVRD}
Requires: trinity-ktuberling = %{EVRD}
Requires: trinity-twin4 = %{EVRD}
Requires: trinity-lskat = %{EVRD}
Requires: trinity-tdefifteen = %{EVRD}


%description
Games and gaming libraries for the Trinity Desktop Environment.
Included with this package are: kenolaba, kasteroids, kblackbox, kmahjongg,
kmines, konquest, kpat, kpoker, kreversi, ksame, kshisen, ksmiletris,
ksnake, ksirtet, katomic, kjumpingcube, ktuberling.

%files

##########

%package devel
Summary:	Development files for %{name} 
Group:		Amusements/Games/Other

Requires:	%{name} = %{EVRD}
Requires:	trinity-tdelibs-devel >= %{version}
Requires:	trinity-libtdegames-devel = %{EVRD}
Requires:	trinity-atlantik-devel = %{EVRD}
Requires:	trinity-kolf-devel = %{EVRD}

Obsoletes:		trinity-kdegames-devel < %{EVRD}
Provides:		trinity-kdegames-devel = %{EVRD}

%description devel
Install %{name}-devel if you wish to develop or compile games for the
TDE desktop.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/share/cmake/libtdegames.cmake
%{tde_prefix}/%{_lib}/pkgconfig/libtdegames.pc

##########

%package -n trinity-libtdegames1
Summary:	Trinity games library and common files
Group:		Amusements/Games/Other

%description -n trinity-libtdegames1
This library provides a common infrastructure for several of the
games in the TDE distribution. Features include standardized menu
items, high score handling, card display, and network connections
including chat capabilities.

This package is part of TDE, and a component of the TDE games module.

%files -n trinity-libtdegames1
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libtdegames.so.*
%dir %{tde_prefix}/share/apps/tdegames
%dir %{tde_prefix}/share/apps/tdegames/pics
%{tde_prefix}/share/apps/tdegames/pics/star.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/roll.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/highscore.png

##########

%package -n trinity-libtdegames-devel
Summary:	Trinity games library headers
Group:		Development/Libraries/Other
Requires:	trinity-libtdegames1 = %{EVRD}

%description -n trinity-libtdegames-devel
This package is necessary if you want to develop your own games using
the TDE games library.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-libtdegames-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/*.h
%{tde_prefix}/include/tde/kgame
%{tde_prefix}/%{_lib}/libtdegames.so
%{tde_prefix}/%{_lib}/libtdegames.la

##########

%package card-data
Summary:	Card decks for Trinity games
Group:		Amusements/Games/Other

%description card-data
Several different collections of card images for use by TDE games.

This package is part of Trinity, and a component of the TDE games module.

%files card-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/carddecks/

##########

%package -n trinity-atlantik
Summary:	TDE client for Monopoly-like network games
Group:		Amusements/Games/Board/Other

%description -n trinity-atlantik
This is a TDE client for playing Monopoly-like boardgames on the
monopd network.  It can play any board supported by the network
server, including the classic Monopoly game, as well as the Atlantik
game in which the property includes several major cities in North
America and Europe.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-atlantik
%defattr(-,root,root,-)
%{tde_prefix}/bin/atlantik
%{tde_prefix}/%{_lib}/libatlantic.so.*
%{tde_prefix}/%{_lib}/libatlantikclient.so.*
%{tde_prefix}/%{_lib}/libatlantikui.so.*
%{tde_prefix}/%{_lib}/trinity/tdeio_atlantik.la
%{tde_prefix}/%{_lib}/trinity/tdeio_atlantik.so
%{tde_prefix}/share/services/atlantik.protocol
%{tde_prefix}/share/applications/tde/atlantik.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/atlantik.png
%{tde_prefix}/share/apps/atlantik/
%{tde_prefix}/share/doc/tde/HTML/en/atlantik/
%{tde_prefix}/share/man/man*/atlantik.*

##########

%package -n trinity-atlantik-devel
Summary:	Development files for Atlantik
Group:		Development/Libraries/Other
Requires:	trinity-atlantik = %{EVRD}

%description -n trinity-atlantik-devel
This package contains header files for compiling programs against the
libraries which come with Atlantik.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-atlantik-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/atlantik
%{tde_prefix}/include/tde/atlantic
%{tde_prefix}/%{_lib}/libatlantic.so
%{tde_prefix}/%{_lib}/libatlantic.la
%{tde_prefix}/%{_lib}/libatlantikclient.so
%{tde_prefix}/%{_lib}/libatlantikclient.la
%{tde_prefix}/%{_lib}/libatlantikui.so
%{tde_prefix}/%{_lib}/libatlantikui.la

##########

%package -n trinity-kasteroids
Summary:	Asteroids for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kasteroids
You know this game.  It is based on Warwick Allison's QwSpriteField
widget.

The objective of kasteroids is to destroy all the asteroids on the
screen to advance to the next level. Your ship is destroyed if it
makes contact with an asteroid.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kasteroids
%defattr(-,root,root,-)
%{tde_prefix}/bin/kasteroids
%{tde_prefix}/share/icons/hicolor/*/apps/kasteroids.png
%{tde_prefix}/share/applications/tde/kasteroids.desktop
%{tde_prefix}/share/apps/kasteroids/
%{tde_prefix}/share/config.kcfg/kasteroids.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kasteroids/
%{tde_prefix}/share/man/man*/kasteroids.*

##########

%package -n trinity-katomic
Summary:	Atomic Entertainment game for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-katomic
This is a puzzle game, in which the object is to assemble a molecule
from its atoms on a Sokoban-like board.  On each move, an atom goes
as far as it can in a specified direction before being stopped by a
wall or another atom.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-katomic
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/katomic/
%{tde_prefix}/share/icons/hicolor/*/apps/katomic.png
%{tde_prefix}/share/applications/tde/katomic.desktop
%{tde_prefix}/bin/katomic
%{tde_prefix}/share/doc/tde/HTML/en/katomic/
%{tde_prefix}/share/man/man*/katomic.*

##########

%package -n trinity-kbackgammon
Summary:	A Backgammon game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kbackgammon
KBackgammon is a backgammon program for Trinity. It is based on the
code, ideas and concepts of KFibs (which is a FIBS client for
TDE1). For a short time, KBackgammon was called bacKgammon (if you
know somebody who is still using bacKgammon, please force them to
upgrade :-)).

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbackgammon
%defattr(-,root,root,-)
%{tde_prefix}/bin/kbackgammon
%{tde_prefix}/share/applications/tde/kbackgammon.desktop
%{tde_prefix}/share/apps/kbackgammon/
%{tde_prefix}/share/icons/hicolor/*/apps/kbackgammon.png
%{tde_prefix}/share/icons/hicolor/*/apps/kbackgammon_engine.png
%{tde_prefix}/share/doc/tde/HTML/en/kbackgammon/
%{tde_prefix}/share/man/man*/kbackgammon.*

##########

%package -n trinity-kbattleship
Summary:	Battleship game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kbattleship
This is an implementation of the Battleship game.  Each player tries
to be the first to sink all the opponent's ships by firing "blindly"
at them.  The game has options to play over a network connection or
against the computer.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbattleship
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kbattleship/
%{tde_prefix}/share/apps/zeroconf/_kbattleship._tcp
%{tde_prefix}/share/icons/hicolor/*/apps/kbattleship.png
%{tde_prefix}/share/applications/tde/kbattleship.desktop
%{tde_prefix}/bin/kbattleship
%{tde_prefix}/share/doc/tde/HTML/en/kbattleship/
%{tde_prefix}/share/man/man*/kbattleship.*

##########

%package -n trinity-kblackbox
Summary:	A simple logical game for the Trinity project
Group:		Amusements/Games/Board/Other

%description -n trinity-kblackbox
KBlackBox is a game of hide and seek played on an grid of boxes. Your
opponent (Random number generator, in this case) has hidden several
balls within this box. By shooting rays into the box and observing
where they emerge it is possible to deduce the positions of the
hidden balls. The fewer rays you use to find the balls, the lower
your score.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kblackbox
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kblackbox/
%{tde_prefix}/share/icons/hicolor/*/apps/kblackbox.png
%{tde_prefix}/share/applications/tde/kblackbox.desktop
%{tde_prefix}/bin/kblackbox
%{tde_prefix}/share/doc/tde/HTML/en/kblackbox/
%{tde_prefix}/share/man/man*/kblackbox.*

##########

%package -n trinity-kbounce
Summary:	Jezzball clone for the K Desktop Environment
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kbounce
This is a clone of the popular Jezzball game originally created by
Microsoft. Jezzball is one of the rare and simple games requiring
skill, timing, and patience in order to be successful.  A ball begins
to bounce off of an area enclosed by four borders (like a
square). You must move your pointer to certain areas within the
square. Upon clicking, a new border is constructed at a relatively
quick pace. You can change the direction of the borders by 90 degrees
as well. Ultimately, you must force the ball to bounce around in a
smaller, and smaller area as time goes by without the ball ever
touching the borders as they are being constructed. If a ball touches
a certain part of the border as it is being built, the game is over.
After 75% of the original space has been blocked off from the moving
ball, you advance one level, and one more ball is added to the mix in
the following level.

This game was previously known as kjezz.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kbounce
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kbounce/
%{tde_prefix}/share/applications/tde/kbounce.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kbounce.png
%{tde_prefix}/bin/kbounce
%{tde_prefix}/share/doc/tde/HTML/en/kbounce/
%{tde_prefix}/share/man/man*/kbounce.*

##########

%package -n trinity-kenolaba
Summary:	Enolaba board game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kenolaba
kenolaba is a simple board strategy game that is played by two
players. There are red and yellow pieces for each player. Beginning
from a start position where each player has 14 pieces, moves are
drawn until one player has pushed 6 pieces of his opponent out of the
board.

This game was previously known as kabalone, and was inspired by the
board game Abalone by Abalone SA, France.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kenolaba
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kenolaba/
%{tde_prefix}/share/icons/hicolor/*/apps/kenolaba.png
%{tde_prefix}/share/applications/tde/kenolaba.desktop
%{tde_prefix}/bin/kenolaba
%{tde_prefix}/share/doc/tde/HTML/en/kenolaba/
%{tde_prefix}/share/man/man*/kenolaba.*

##########

%package -n trinity-kfouleggs
Summary:	A TDE clone of the Japanese PuyoPuyo game
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kfouleggs
KFouleggs is a clone of the Japanese PuyoPuyo game, with advanced
features such as multiplayer games against human or AI, and network
play.  If you have played Tetris or one of its many clones, you will
find KFouleggs easy to learn.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kfouleggs
%defattr(-,root,root,-)
%{tde_prefix}/share/applications/tde/kfouleggs.desktop
%{tde_prefix}/share/apps/kfouleggs/
%{tde_prefix}/share/config.kcfg/kfouleggs.kcfg
%{tde_prefix}/bin/kfouleggs
%{tde_prefix}/share/icons/hicolor/*/apps/kfouleggs.png
%{tde_prefix}/share/doc/tde/HTML/en/kfouleggs/
%{tde_prefix}/share/man/man*/kfouleggs.*

##########

%package -n trinity-kgoldrunner
Summary:	A Trinity clone of the Loderunner arcade game
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kgoldrunner
KGoldrunner, a game of action and puzzle solving.  Run through the
maze, dodge your enemies, collect all the gold and climb up to the
next level.

You must guide the hero with the mouse or keyboard and collect all
the gold nuggets, then you can climb up into the next level.  Your
enemies are also after the gold and they will kill you if they catch
you!

The problem is you have no weapon to kill them.  All you can do is
run away, dig holes in the floor to trap them or lure them into some
area where they cannot hurt you.  After a short time a trapped enemy
climbs out of his hole, but if it closes before that, he will die and
reappear somewhere else.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kgoldrunner
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kgoldrunner/
%{tde_prefix}/share/icons/hicolor/*/apps/kgoldrunner.png
%{tde_prefix}/share/applications/tde/KGoldrunner.desktop
%{tde_prefix}/bin/kgoldrunner
%{tde_prefix}/share/doc/tde/HTML/en/kgoldrunner/
%{tde_prefix}/share/man/man*/kgoldrunner.*

##########

%package -n trinity-kjumpingcube
Summary:	Tactical one or two player game
Group:		Amusements/Games/Strategy/Other

%description -n trinity-kjumpingcube
KJumpingCube is a simple tactical game. You can play it against the
computer or against a friend. The playing field consists of squares
that contains points.  By clicking on the squares you can increase
the points and if the points reach a maximum the points will jump to
the squares neighbours and take them over. Winner is the one, who
owns all squares.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kjumpingcube
%defattr(-,root,root,-)
%{tde_prefix}/bin/kjumpingcube
%{tde_prefix}/share/icons/hicolor/*/apps/kjumpingcube.png
%{tde_prefix}/share/apps/kjumpingcube/
%{tde_prefix}/share/applications/tde/kjumpingcube.desktop
%{tde_prefix}/share/config.kcfg/kjumpingcube.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kjumpingcube/
%{tde_prefix}/share/man/man*/kjumpingcube.*

##########

%package -n trinity-klickety
Summary:	A Clickomania-like game for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-klickety
Klickety is an adaptation of the (perhaps) well-known Clickomania
game; it is very similar to the "same" game.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-klickety
%defattr(-,root,root,-)
%{tde_prefix}/bin/klickety
%{tde_prefix}/share/applications/tde/klickety.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/klickety.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/endturn.png
%{tde_prefix}/share/apps/klickety/
%{tde_prefix}/share/doc/tde/HTML/en/klickety/
%{tde_prefix}/share/man/man*/klickety.*

##########

%package -n trinity-klines
Summary:	Color lines for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-klines
KLines is a simple game. It is played by one player, so there is only
one winner :-). You play for fun and against the high score. It was
inspired by a well known game - "Color lines", written for DOS by
Olga Demina, Igor Demina, Igor Ivkin and Gennady Denisov back in
1992.

The main rules of the game are as simple as possible: you move (using
the mouse) marbles from cell to cell and build lines (horizontal,
vertical or diagonal). When a line contains 5 or more marbles, they
are removed and your score grows. After each turn the computer drops
three more marbles.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-klines
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/klines/
%{tde_prefix}/share/applications/tde/klines.desktop
%{tde_prefix}/bin/klines
%{tde_prefix}/share/config.kcfg/klines.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/klines.png
%{tde_prefix}/share/doc/tde/HTML/en/klines/
%{tde_prefix}/share/man/man*/klines.*

##########

%package -n trinity-kmahjongg
Summary:	The classic mahjongg game for Trinity project
Group:		Amusements/Games/Board/Other

%description -n trinity-kmahjongg
Your mission in this game is to remove all tiles from the game board. A
matching pair of tiles can be removed, if they are 'free', which means that
no other tiles block them on the left or right side.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kmahjongg
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kmahjongg/
%{tde_prefix}/share/icons/hicolor/*/apps/kmahjongg.png
%{tde_prefix}/share/applications/tde/kmahjongg.desktop
%{tde_prefix}/bin/kmahjongg
%{tde_prefix}/share/config.kcfg/kmahjongg.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kmahjongg/
%{tde_prefix}/share/man/man*/kmahjongg.*

##########

%package -n trinity-kmines
Summary:	Minesweeper for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kmines
KMines is the classic Minesweeper game. You must uncover all the
empty cases without blowing on a mine.

When you uncover a case, a number appears : it indicates how many
mines surround this case. If there is no number the neighbour cases
are automatically uncovered. In your process of uncovering secure
cases, it is very useful to put a flag on the cases which contain a
mine.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kmines
%defattr(-,root,root,-)
%{tde_prefix}/share/icons/hicolor/*/apps/kmines.png
%{tde_prefix}/share/applications/tde/kmines.desktop
%{tde_prefix}/share/apps/kmines/
%{tde_prefix}/bin/kmines
%{tde_prefix}/share/doc/tde/HTML/en/kmines/
%{tde_prefix}/share/man/man*/kmines.*

##########

%package -n trinity-knetwalk
Summary:	A game for system administrators
Group:		Amusements/Games/Board/Other

%description -n trinity-knetwalk
This game presents the player with a rectangular field consisting of
a server, several clients, and pieces of wire.  The object is to
rotate these elements until every client is connected to the server,
and no wires are left unconnected.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-knetwalk
%defattr(-,root,root,-)
%{tde_prefix}/bin/knetwalk
%{tde_prefix}/share/apps/knetwalk
%{tde_prefix}/share/icons/hicolor/*/apps/knetwalk.png
%{tde_prefix}/share/applications/tde/knetwalk.desktop
%{tde_prefix}/share/doc/tde/HTML/en/knetwalk/
%{tde_prefix}/share/man/man*/knetwalk.*

##########

%package -n trinity-kolf
Summary:	Minigolf game for TDE
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kolf
This is a minigolf game for TDE that allows you to go through different
golf courses and waste an exorbitant amount of time.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kolf
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/magic/kolf.magic
%{tde_prefix}/share/apps/kolf/
%{tde_prefix}/bin/kolf
%{tde_prefix}/share/applications/tde/kolf.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kolf.png
%{tde_prefix}/share/mimelnk/application/x-kolf.desktop
%{tde_prefix}/share/mimelnk/application/x-kourse.desktop
%{tde_prefix}/%{_lib}/libtdeinit_kolf.so
%{tde_prefix}/%{_lib}/libtdeinit_kolf.la
%{tde_prefix}/%{_lib}/trinity/kolf.la
%{tde_prefix}/%{_lib}/trinity/kolf.so
%{tde_prefix}/%{_lib}/libkolf.so.1
%{tde_prefix}/%{_lib}/libkolf.so.1.2.0
%{tde_prefix}/share/doc/tde/HTML/en/kolf/
%config(noreplace) %{_sysconfdir}/trinity/magic/kolf.magic.mgc
%{tde_prefix}/share/man/man*/kolf.*

##########

%package -n trinity-kolf-devel
Summary:	Development files for Kolf
Group:		Development/Libraries/Other
Requires:	trinity-kolf = %{EVRD}

%description -n trinity-kolf-devel
This package contains headers and development libraries for compiling
Kolf plugins.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kolf-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kolf
%{tde_prefix}/%{_lib}/libkolf.la
%{tde_prefix}/%{_lib}/libkolf.so

##########

%package -n trinity-konquest
Summary:	TDE based GNU-Lactic Konquest game
Group:		Amusements/Games/Strategy/Other

%description -n trinity-konquest
This the TDE version of Gnu-Lactic Konquest, a multi-player strategy
game. The goal of the game is to expand your interstellar empire
across the galaxy and, of course, crush your rivals in the process.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-konquest
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/konquest/
%{tde_prefix}/share/icons/hicolor/*/apps/konquest.png
%{tde_prefix}/share/applications/tde/konquest.desktop
%{tde_prefix}/bin/konquest
%{tde_prefix}/share/doc/tde/HTML/en/konquest/
%{tde_prefix}/share/man/man*/konquest.*

##########

%package -n trinity-kpat
Summary:	Trinity solitaire patience game
Group:		Amusements/Games/Board/Card

%description -n trinity-kpat
KPatience is a collection of 14 card games. All the games are single
player games.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kpat
%defattr(-,root,root,-)
%{tde_prefix}/share/icons/hicolor/*/apps/kpat.png
%{tde_prefix}/share/apps/kpat/
%{tde_prefix}/share/applications/tde/kpat.desktop
%{tde_prefix}/bin/kpat
%{tde_prefix}/share/doc/tde/HTML/en/kpat/
%{tde_prefix}/share/man/man*/kpat.*

##########

%package -n trinity-kpoker
Summary:	Trinity based Poker clone
Group:		Amusements/Games/Board/Card

%description -n trinity-kpoker
KPoker is a TDE compliant clone of those highly addictive pocket
video poker games which are sometimes called "Videopoker" as well.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kpoker
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kpoker/
%{tde_prefix}/share/icons/hicolor/*/apps/kpoker.png
%{tde_prefix}/share/applications/tde/kpoker.desktop
%{tde_prefix}/bin/kpoker
%{tde_prefix}/share/doc/tde/HTML/en/kpoker/
%{tde_prefix}/share/man/man*/kpoker.*

##########

%package -n trinity-kreversi
Summary:	Reversi for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kreversi
Reversi is a simple strategy game that is played by two
players. There is only one type of piece - one side of it is black,
the other white. If a player captures a piece on the board, that
piece is turned and belongs to that player. The winner is the person
that has more pieces of his own color on the board and if there are
no more moves possible.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kreversi
%defattr(-,root,root,-)
%{tde_prefix}/bin/kreversi
%{tde_prefix}/share/applications/tde/kreversi.desktop
%{tde_prefix}/share/apps/kreversi/
%{tde_prefix}/share/config.kcfg/kreversi.kcfg
%{tde_prefix}/share/icons/crystalsvg/*/actions/lastmoves.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/legalmoves.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/lastmoves.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/legalmoves.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/kreversi.png
%{tde_prefix}/share/doc/tde/HTML/en/kreversi/
%{tde_prefix}/share/man/man*/kreversi.*

##########

%package -n trinity-ksame
Summary:	SameGame for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-ksame
KSame is a simple game. It's played by one player, so there is only
one winner :-) You play for fun and against the high score. It has
been inspired by SameGame, that is only famous on the Macintosh
platform.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksame
%defattr(-,root,root,-)
%{tde_prefix}/bin/ksame
%{tde_prefix}/share/icons/hicolor/*/apps/ksame.png
%{tde_prefix}/share/apps/ksame/
%{tde_prefix}/share/applications/tde/ksame.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ksame/
%{tde_prefix}/share/man/man*/ksame.*

##########

%package -n trinity-kshisen
Summary:	Shisen-Sho for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-kshisen
KShisen-Sho is a single-player-game similar to Mahjongg and uses the
same set of tiles as Mahjongg.

The object of the game is to remove all tiles from the field.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kshisen
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kshisen/
%{tde_prefix}/share/config.kcfg/kshisen.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kshisen.png
%{tde_prefix}/share/applications/tde/kshisen.desktop
%{tde_prefix}/bin/kshisen
%{tde_prefix}/share/doc/tde/HTML/en/kshisen/
%{tde_prefix}/share/man/man*/kshisen.*

##########

%package -n trinity-ksirtet
Summary:	Tetris and Puyo-Puyo games for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-ksirtet
This program is a clone of the well known game Tetris. You must fit
the falling pieces to form full lines. You can rotate and translate
the falling piece. The game ends when no more piece can fall ie when
your incomplete lines reach the top of the board.

Every time you have destroyed 10 lines, you gain a level and the
pieces fall quicker (exactly the piece falls from a line each
1/(1+level) second).

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksirtet
%defattr(-,root,root,-)
%{tde_prefix}/share/applications/tde/ksirtet.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/ksirtet.png
%{tde_prefix}/share/apps/ksirtet/
%{tde_prefix}/bin/ksirtet
%{tde_prefix}/share/config.kcfg/ksirtet.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/ksirtet/
%{tde_prefix}/share/man/man*/ksirtet.*

##########

%package -n trinity-ksmiletris
Summary:	Tetris like game for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ksmiletris
This is a game with falling blocks composed of different types of
smilies. The object of the game is to "crack a smile" by guiding
blocks so there are two or more of the same symbol vertically.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksmiletris
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/ksmiletris/
%{tde_prefix}/share/icons/hicolor/*/apps/ksmiletris.png
%{tde_prefix}/share/applications/tde/ksmiletris.desktop
%{tde_prefix}/bin/ksmiletris
%{tde_prefix}/share/doc/tde/HTML/en/ksmiletris/
%{tde_prefix}/share/man/man*/ksmiletris.*

##########

%package -n trinity-ksnake
Summary:	Snake Race for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ksnake
Snake Race is a game of speed and agility. You are a hungry snake and
are trying to eat all the apples in the room before getting out!

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksnake
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/ksnake/
%{tde_prefix}/share/config.kcfg/ksnake.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/ksnake.png
%{tde_prefix}/share/applications/tde/ksnake.desktop
%{tde_prefix}/bin/ksnake
%{tde_prefix}/share/doc/tde/HTML/en/ksnake/
%{tde_prefix}/share/man/man*/ksnake.*

##########

%package -n trinity-ksokoban
Summary:	Sokoban game for Trinity
Group:		Amusements/Games/Strategy/Other

%description -n trinity-ksokoban
The first sokoban game was created in 1982 by Hiroyuki Imabayashi at
the Japanese company Thinking Rabbit, Inc. "Sokoban" is japanese for
"warehouse keeper". The idea is that you are a warehouse keeper
trying to push crates to their proper locations in a warehouse.

The problem is that you cannot pull the crates or step over them. If
you are not careful, some of the crates can get stuck in wrong places
and/or block your way.

It can be rather difficult just to solve a level. But if you want to
make it even harder, you can try to minimise the number of moves
and/or pushes you use to solve the level.

To make the game more fun for small kids (below 10 years or so), some
collections with easier levels are also included in KSokoban. These
are marked (easy) in the level collection menu. Of course, these
levels can be fun for adults too, for example if you don't want to
expose yourself to too much mental strain.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ksokoban
%defattr(-,root,root,-)
%{tde_prefix}/share/applications/tde/ksokoban.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/ksokoban.png
%{tde_prefix}/bin/ksokoban
%{tde_prefix}/share/doc/tde/HTML/en/ksokoban/
%{tde_prefix}/share/man/man*/ksokoban.*

##########

%package -n trinity-kspaceduel
Summary:	Arcade two-player space game for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-kspaceduel
KSpaceduel is an space arcade game for two players.

Each player controls a ship that flies around the sun and tries to
shoot at the other ship. You can play KSpaceduel with another person,
against the computer, or you can have the computer control both ships
and play each other.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-kspaceduel
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kspaceduel/
%{tde_prefix}/share/icons/hicolor/*/apps/kspaceduel.png
%{tde_prefix}/share/applications/tde/kspaceduel.desktop
%{tde_prefix}/bin/kspaceduel
%{tde_prefix}/share/config.kcfg/kspaceduel.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kspaceduel/
%{tde_prefix}/share/man/man*/kspaceduel.*

##########

%package -n trinity-ktron
Summary:	Tron clone for the K Desktop Environment
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ktron
The object of the game is to avoid running into walls, your own tail,
and that of your opponent.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ktron
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktron
%{tde_prefix}/share/icons/hicolor/*/apps/ktron.png
%{tde_prefix}/share/applications/tde/ktron.desktop
%{tde_prefix}/share/apps/ktron/
%{tde_prefix}/share/config.kcfg/ktron.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/ktron/
%{tde_prefix}/share/man/man*/ktron.*

##########

%package -n trinity-ktuberling
Summary:	Potato Guy for Trinity
Group:		Amusements/Games/Action/Arcade

%description -n trinity-ktuberling
KTuberling is a game intended for small children. Of course, it may
be suitable for adults who have remained young at heart.

It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.  Similarly, you have a penguin on which you can drop
other stuff.

There is no winner for the game. The only purpose is to make the
funniest faces you can.

There is a museum (like a "Madame Tusseau" gallery) where you can
find many funny examples of decorated potatoes. Of course, you can
send your own creations to the programmer, Eric Bischoff, who will
include them in the museum if he gets some spare time.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-ktuberling
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktuberling
%{tde_prefix}/share/icons/hicolor/*/apps/ktuberling.png
%{tde_prefix}/share/applications/tde/ktuberling.desktop
%{tde_prefix}/share/apps/ktuberling/
%{tde_prefix}/share/mimelnk/application/x-tuberling.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ktuberling/
%{tde_prefix}/share/man/man*/ktuberling.*

##########

%package -n trinity-twin4
Summary:	Connect Four clone for Trinity
Group:		Amusements/Games/Board/Other

%description -n trinity-twin4
Four wins is a game for two players. Each player is represented by a
colour (yellow and red). The goal of the game is to get four
connected pieces of your colour into a row, column or any
diagonal. This is done by placing one of your pieces into any of the
seven columns. A piece will begin to fill a column from the bottom,
i.e. it will fall down until it reaches the ground level or another
stone. After a move is done it is the turn of the other player. This
is repeated until the game is over, i.e. one of the players has four
pieces in a row, column or diagonal or no more moves are possible
because the board is filled.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-twin4
%defattr(-,root,root,-)
%{tde_prefix}/bin/twin4
%{tde_prefix}/bin/twin4proc
%{tde_prefix}/share/apps/twin4/
%{tde_prefix}/share/config.kcfg/twin4.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/twin4.png
%{tde_prefix}/share/applications/tde/twin4.desktop
%{tde_prefix}/share/doc/tde/HTML/en/twin4/
%{tde_prefix}/share/man/man*/twin4.*
%{tde_prefix}/share/man/man*/twin4proc.*

##########

%package -n trinity-lskat
Summary:	Lieutnant Skat card game for Trinity
Group:		Amusements/Games/Board/Card

%description -n trinity-lskat
Lieutnant Skat (from German Offiziersskat) is a card game for two
players. It is roughly played according to the rules of Skat but with
only two players and simplified rules.

Every player has a set of cards in front of him/her, half of them
covered and half of them open. Both players try to win more than 60
of the 120 possible points. After 16 moves all cards are played and
the game ends.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-lskat
%defattr(-,root,root,-)
%{tde_prefix}/bin/lskat
%{tde_prefix}/bin/lskatproc
%{tde_prefix}/share/apps/lskat/
%{tde_prefix}/share/icons/hicolor/*/apps/lskat.png
%{tde_prefix}/share/applications/tde/lskat.desktop
%{tde_prefix}/share/doc/tde/HTML/en/lskat/
%{tde_prefix}/share/man/man*/lskat.*
%{tde_prefix}/share/man/man*/lskatproc.*

##########

%package -n trinity-tdefifteen
Summary:	Puzzle-solving game for Trinity
Group:		Amusements/Games

%description -n trinity-tdefifteen
TDEFifteen is a sliding puzzle that consists of a frame of numbered square
tiles in random order with one tile missing.

This package is part of Trinity, and a component of the TDE games module.

%files -n trinity-tdefifteen
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdefifteen
%{tde_prefix}/share/applications/tde/tdefifteen.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/tdefifteen.png
%{tde_prefix}/share/man/man*/tdefifteen.*

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a

# Links duplicate files
%fdupes "%{?buildroot}"

