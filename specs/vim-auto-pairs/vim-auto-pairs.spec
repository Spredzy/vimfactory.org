%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-auto-pairs
Version:        1.3.1
Release:        1%{?dist}
Summary:        Vim plugin, insert or delete brackets, parens, quotes in pair
Group:          Applications/Editors

License:        MIT
URL:            https://github.com/jiangmiao/auto-pairs
Source0:        https://github.com/jiangmiao/auto-pairs/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
Insert or delete brackets, parens, quotes in pair.


%prep
%setup -q -n auto-pairs-%{version}


%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar {plugin} %{buildroot}%{vimfiles_root}

%post
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%postun
> %{vimfiles_root}/doc/tags || :
vim -c ":helptags %{vimfiles_root}/doc" -c ":q" &> /dev/null || :

%files
%doc README.md
%{vimfiles_root}/plugin/*

%changelog
