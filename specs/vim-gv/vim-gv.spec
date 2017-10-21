%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-gv
Version:        1.0
Release:        1%{?dist}
Summary:        A git commit browser
Group:          Applications/Editors

License:        MIT
URL:            https://github.com/Spredzy/gv.vim
Source0:        https://github.com/Spredzy/gv.vim/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
A git commit browser.


%prep
%setup -q -n gv.vim-%{version}


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar plugin %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%doc README.md
%{vimfiles_root}/plugin/*

%changelog
