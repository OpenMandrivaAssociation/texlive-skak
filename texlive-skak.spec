Name:		texlive-skak
Version:	61719
Release:	1
Summary:	Fonts and macros for typesetting chess games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/chess/skak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skak.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros and fonts in Metafont format which
can be used to typeset chess games using PGN, and to show
diagrams of the current board in a document. The package builds
on work by Piet Tutelaers -- the main novelty is the use of PGN
for input instead of the more cumbersome coordinate notation
(g1f3 becomes the more readable Nf3 in PGN). An Adobe Type 1
implementation of skak's fonts is available as package skaknew;
an alternative chess notational scheme is available in package
texmate, and a general mechanism for selecting chess fonts is
provided in chessfss.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/*/public/skak
%{_texmfdistdir}/tex/latex/skak
%doc %{_texmfdistdir}/doc/latex/skak

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
