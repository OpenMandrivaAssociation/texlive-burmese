# revision 15878
# category Package
# catalog-ctan /language/burmese
# catalog-date 2006-12-21 23:43:15 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-burmese
Version:	20061221
Release:	1
Summary:	Basic Support for Writing Burmese
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/burmese
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/burmese.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
This package provides basic support for writing Burmese. The
package provides a preprocessor (written in Perl), an Adobe
Type 1 font, and LaTeX macros.

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
%{_texmfdistdir}/fonts/map/dvips/burmese/burmese.map
%{_texmfdistdir}/fonts/tfm/public/burmese/burm.tfm
%{_texmfdistdir}/fonts/type1/public/burmese/burm.pfb
%{_texmfdistdir}/tex/latex/burmese/birm.sty
%{_texmfdistdir}/tex/latex/burmese/ubirm.fd
%doc %{_texmfdistdir}/doc/fonts/burmese/burmguide.pdf
#- source
%doc %{_texmfdistdir}/source/latex/burmese/birm.pl
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
