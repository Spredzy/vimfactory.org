%global vimfiles_root %{_datadir}/vim/vimfiles

Name:           vim-licenses
Version:        0.5
Release:        1%{?dist}
Summary:        Vim Plugin that Provides Commands to Add Licenses at the Top of the Buffer
Group:          Applications/Editors

License:        BSD
URL:            https://github.com/antoyo/vim-licenses
Source0:        https://github.com/antoyo/vim-licenses/archive/v%{version}.tar.gz

BuildArch:      noarch


Requires:       vim-common
Requires(post): vim
Requires(postun): vim

%description
This plugin provides commands to insert licenses at the top of the buffer.
If the license is already at the top of the buffer, nothing is added.
This plugin works for the most popular programming languages, including C, Java,
Objective-C, C++, C#, PHP, Python, JavaScript, Ruby, Perl, Asm and Haskell.

The HTML and CSS languages are also supported. It may work for other languages.

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
%license LICENSE
%doc README.md
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*

%changelog
