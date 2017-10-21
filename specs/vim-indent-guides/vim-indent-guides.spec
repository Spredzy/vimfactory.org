%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-indent-guides
Version:        1.6
Release:        1%{?dist}
Summary:        A Vim plugin for visually displaying indent levels in code
Group:          Applications/Editors

License:        VIM
URL:            https://github.com/nathanaelkane/vim-indent-guides
Source0:        https://github.com/nathanaelkane/vim-indent-guides/archive/%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
Indent Guides is a plugin for visually displaying indent levels in Vim.

%prep
%setup -q


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
%doc README.markdown
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/autoload/*

%changelog
