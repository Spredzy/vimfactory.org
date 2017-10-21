%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-gitgutter
Version:        1.0
Release:        1%{?dist}
Summary:        A Vim plugin which shows a git diff in the gutter (sign column) and stages/undoes hunks.
Group:          Applications/Editors

License:        MIT
URL:            https://github.com/Spredzy/vim-gitgutter
Source0:        https://github.com/Spredzy/vim-gitgutter/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
A Vim plugin which shows a git diff in the 'gutter' (sign column).

It shows whether each line has been added, modified, and where lines
have been removed. You can also stage and undo individual hunks.


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
%license LICENCE
%doc README.mkd
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/autoload/*

%changelog
