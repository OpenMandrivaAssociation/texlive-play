Name:		texlive-play
Version:	20070113
Release:	1
Summary:	Typeset drama using LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/play
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/play.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A class and style file that supports the typesetting of plays,
including options for line numbering.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
