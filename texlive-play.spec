# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/play
# catalog-date 2007-01-13 20:56:44 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-play
Version:	20070113
Release:	10
Summary:	Typeset drama using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/play
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class and style file that supports the typesetting of plays,
including options for line numbering.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/play/play.cls
%{_texmfdistdir}/tex/latex/play/play.sty
%doc %{_texmfdistdir}/doc/latex/play/README
#- source
%doc %{_texmfdistdir}/source/latex/play/play.dtx
%doc %{_texmfdistdir}/source/latex/play/play.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070113-2
+ Revision: 754980
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070113-1
+ Revision: 719275
- texlive-play
- texlive-play
- texlive-play
- texlive-play

