Name:		texlive-play
Version:	20170414
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
%{_texmfdistdir}/tex/latex/play
%doc %{_texmfdistdir}/doc/latex/play
#- source
%doc %{_texmfdistdir}/source/latex/play

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
