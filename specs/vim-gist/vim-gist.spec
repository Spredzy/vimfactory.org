%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-gist
Version:        7.3
Release:        1%{?dist}
Summary:        vimscript for gist
Group:          Applications/Editors

License:        VIM
URL:            https://github.com/mattn/gist-vim
Source0:        https://github.com/mattn/gist-vim/archive/%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires:       vim-webadmin
Requires(post): vim
Requires(postun): vim

%description
This is a vimscript for creating gists (http://gist.github.com).


%prep
%setup -q -n gist-vim-%{version}


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,plugin,autoload} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%doc README.md
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/autoload/*

%changelog
