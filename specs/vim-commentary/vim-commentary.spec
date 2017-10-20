%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-commentary
Version:        1.3
Release:        1%{?dist}
Summary:        commentary.vim comment stuff out
Group:          Applications/Editors

License:        VIM
URL:            https://github.com/tpope/vim-commentary
Source0:        https://github.com/tpope/vim-commentary/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
Comment stuff out. Use gcc to comment out a line (takes a count),
gc to comment out the target of a motion (for example, gcap to
comment out a paragraph), gc in visual mode to comment out the selection,
and gc in operator pending mode to target a comment.

You can also use it as a command, either with a range like :7,17Commentary,
or as part of a :global invocation like with :g/TODO/Commentary. That's it.


%prep
%setup -q


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,plugin} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%doc README.markdown
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*

%changelog
