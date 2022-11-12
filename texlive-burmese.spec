Name:		texlive-burmese
Version:	25185
Release:	1
Summary:	Basic Support for Writing Burmese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/burmese
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides basic support for writing Burmese. The
package provides a preprocessor (written in Perl), an Adobe
Type 1 font, and LaTeX macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/burmese/burmese.map
%{_texmfdistdir}/fonts/tfm/public/burmese/burm.tfm
%{_texmfdistdir}/fonts/type1/public/burmese/burm.pfb
%{_texmfdistdir}/tex/latex/burmese/birm.sty
%{_texmfdistdir}/tex/latex/burmese/ubirm.fd
%doc %{_texmfdistdir}/doc/fonts/burmese/burmguide.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/burmese/birm.pl

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
