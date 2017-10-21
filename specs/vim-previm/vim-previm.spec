%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-previm
Version:        0.3
Release:        1%{?dist}
Summary:        Vim plugin for preview
Group:          Applications/Editors

License:        BSD
URL:            https://github.com/kannokanno/previm
Source0:        https://github.com/kannokanno/previm/archive/%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
Vim plugin for preview.

%prep
%setup -q -n previm-%{version}


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
%license LICENSE
%doc README-en.mkd
%{vimfiles_root}/doc/*
%{vimfiles_root}/autoload/*
%{vimfiles_root}/plugin/*

%changelog
