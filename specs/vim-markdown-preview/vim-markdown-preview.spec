%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-markdown-preview
Version:        1.0
Release:        1%{?dist}
Summary:        A light Vim plugin for previewing markdown files in a browser - without having to leave Vim.
Group:          Applications/Editors

License:        MIT
URL:            https://github.com/Spredzy/vim-markdown-preview
Source0:        https://github.com/Spredzy/vim-markdown-preview/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
A small Vim plugin for previewing markdown files in a browser.

The aim of this plugin is to be light weight with minimal dependencies.
Thus, there is no polling engine or webserver involved.


%prep
%setup -q


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
