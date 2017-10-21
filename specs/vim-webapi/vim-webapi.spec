%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-webapi
Version:        0.3
Release:        1%{?dist}
Summary:        An Interface to WEB APIs
Group:          Applications/Editors

License:        BSD
URL:            https://github.com/mattn/webapi-vim
Source0:        https://github.com/mattn/webapi-vim/archive/%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
An Interface to WEB APIs

%prep
%setup -q -n webapi-vim-%{version}


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {doc,autoload} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%doc README.md
%{vimfiles_root}/doc/*
%{vimfiles_root}/autoload/*

%changelog
