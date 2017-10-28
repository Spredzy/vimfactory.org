%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-ale
Version:        1.6.0
Release:        1%{?dist}
Summary:        Asynchronous Lint Engine
Group:          Applications/Editors

License:        BSD
URL:            https://github.com/w0rp/ale
Source0:        https://github.com/w0rp/ale/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
ALE makes use of NeoVim and Vim 8 job control functions and timers to run
linters on the contents of text buffers and return errors as text is changed
in Vim.

This allows for displaying warnings and errors in files being edited in Vim
before files have been saved back to a filesystem.

In other words, this plugin allows you to lint while you type.


%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {after,ale_linters,autoload,doc,ftplugin,plugin,syntax} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%license LICENSE
%doc README.md
%{vimfiles_root}/after/*
%{vimfiles_root}/ale_linters/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/doc/*
%{vimfiles_root}/ftplugin/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/syntax/*

%changelog
