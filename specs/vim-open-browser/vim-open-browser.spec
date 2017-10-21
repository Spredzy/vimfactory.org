%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-open-browser
Version:        0.1.1
Release:        1%{?dist}
Summary:        Open URI with your favorite browser from your most favorite editor
Group:          Applications/Editors

License:        BSD
URL:            https://github.com/tyru/open-browser.vim
Source0:        https://github.com/tyru/open-browser.vim/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
Open URI with your favorite browser from your most favorite editor

%prep
%setup -q -n open-browser.vim-%{version}


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,autoload,plugin} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%{vimfiles_root}/doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/plugin/*

%changelog
