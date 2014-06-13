# revision 32758
# category Package
# catalog-ctan /fonts/chess/skak
# catalog-date 2014-01-22 19:51:35 +0100
# catalog-license lppl
# catalog-version 1.5.2
Name:		texlive-skak
Version:	1.5.2
Release:	2
Summary:	Fonts and macros for typesetting chess games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/chess/skak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skak.doc.tar.xz
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
%{_texmfdistdir}/fonts/source/public/skak/skak10.mf
%{_texmfdistdir}/fonts/source/public/skak/skak15.mf
%{_texmfdistdir}/fonts/source/public/skak/skak20.mf
%{_texmfdistdir}/fonts/source/public/skak/skak30.mf
%{_texmfdistdir}/fonts/source/public/skak/skakbase.mf
%{_texmfdistdir}/fonts/source/public/skak/skakbrikker.mf
%{_texmfdistdir}/fonts/source/public/skak/skakf10.mf
%{_texmfdistdir}/fonts/source/public/skak/skakf10b.mf
%{_texmfdistdir}/fonts/source/public/skak/skakinf.mf
%{_texmfdistdir}/fonts/tfm/public/skak/skak10.tfm
%{_texmfdistdir}/fonts/tfm/public/skak/skak15.tfm
%{_texmfdistdir}/fonts/tfm/public/skak/skak20.tfm
%{_texmfdistdir}/fonts/tfm/public/skak/skak30.tfm
%{_texmfdistdir}/fonts/tfm/public/skak/skakf10.tfm
%{_texmfdistdir}/fonts/tfm/public/skak/skakf10b.tfm
%{_texmfdistdir}/tex/latex/skak/chess-workshop-symbols.sty
%{_texmfdistdir}/tex/latex/skak/skak.fd
%{_texmfdistdir}/tex/latex/skak/skak.sty
%{_texmfdistdir}/tex/latex/skak/uskak.fd
%doc %{_texmfdistdir}/doc/latex/skak/ChangeLog.md
%doc %{_texmfdistdir}/doc/latex/skak/LICENSE
%doc %{_texmfdistdir}/doc/latex/skak/README.md
%doc %{_texmfdistdir}/doc/latex/skak/THANKS
%doc %{_texmfdistdir}/doc/latex/skak/WC-2004-S-00007.tex
%doc %{_texmfdistdir}/doc/latex/skak/_region_.tex
%doc %{_texmfdistdir}/doc/latex/skak/andreas_wilm_1.tex
%doc %{_texmfdistdir}/doc/latex/skak/angletst.tex
%doc %{_texmfdistdir}/doc/latex/skak/debug_storegame.tex
%doc %{_texmfdistdir}/doc/latex/skak/demo-symbols.tex
%doc %{_texmfdistdir}/doc/latex/skak/fen_with_black.tex
%doc %{_texmfdistdir}/doc/latex/skak/font.tex
%doc %{_texmfdistdir}/doc/latex/skak/font2.tex
%doc %{_texmfdistdir}/doc/latex/skak/hightest.tex
%doc %{_texmfdistdir}/doc/latex/skak/informator.ps
%doc %{_texmfdistdir}/doc/latex/skak/informator.tex
%doc %{_texmfdistdir}/doc/latex/skak/ingo-bug1.tex
%doc %{_texmfdistdir}/doc/latex/skak/longmove_king_bug.tex
%doc %{_texmfdistdir}/doc/latex/skak/longmoves.tex
%doc %{_texmfdistdir}/doc/latex/skak/makefile
%doc %{_texmfdistdir}/doc/latex/skak/promotion_problem_Ulrike.tex
%doc %{_texmfdistdir}/doc/latex/skak/refman.ps
%doc %{_texmfdistdir}/doc/latex/skak/refman.tex
%doc %{_texmfdistdir}/doc/latex/skak/show.tex
%doc %{_texmfdistdir}/doc/latex/skak/skakdoc.ps
%doc %{_texmfdistdir}/doc/latex/skak/skakdoc.tex
%doc %{_texmfdistdir}/doc/latex/skak/special.map
%doc %{_texmfdistdir}/doc/latex/skak/syntax.tex
%doc %{_texmfdistdir}/doc/latex/skak/test1.tex
%doc %{_texmfdistdir}/doc/latex/skak/test2.tex
%doc %{_texmfdistdir}/doc/latex/skak/test_capture.tex
%doc %{_texmfdistdir}/doc/latex/skak/tuggame.ps
%doc %{_texmfdistdir}/doc/latex/skak/tuggame.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
