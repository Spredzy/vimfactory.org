# Vim Plugins Factory

The vimfactory.org project aims to create a platform to buid Operating System native packages for Vim plugins.

## Why ?

So why the need for yet another way to retrieve Vim plugins you might ask?
Aren't there already many Vim plugins managers out there?

Answer is yes, there are a numerous Vim plugins manager that exists out there.
To only name a few, there are [Vundle](https://github.com/VundleVim/Vundle.vim), [Pathtogen](https://github.com/tpope/vim-pathogen), [VimPlug](https://github.com/junegunn/vim-plug), and [NeoBundle](https://github.com/Shougo/neobundle.vim).

**But**, if you are on a UNIX based system, Vim plugins managers miss the point.
UNIX based systems provide already a package management system.
A plugin is simply yet another package. No need for extra tooling to retrieve them.

vimfactory.org provides a system to create native operating systems packages easily, and
all the details to submit those built packages to the UNIX based distribution of your choice.

By making Vim plugins an integral part of the system, it is easier to reach a broader crowd
of people and for them it becomes less intimitading to give Vim a try. Plugins are simply
yet another package.

## Usage

### Create new packages

TODO

### Install currently build packages while they get in the distro

vimfactory.org creates a valid repo for each platform it maintains so community can
use the Vim plugins via the package manager while the plugins make their way into
the distribution itself.

#### Fedora

This is true for Fedora, CentOS and RHEL (and its other derivatives).
Put the following content in `/etc/yum.repos.d/vimfactory.org.repo`

```
[vimfactory]
name=vimfactory repo
baseurl=http://repo.vimfactory.org/fedora/repos/26/noarch
enabled=1
gpgcheck=0
```

## List of available packages

| Name | Summary | License | URL |
|------|---------|---------|-----|
| vim-licences | Vim Plugin that Provides Commands to Add Licenses at the Top of the Buffer | [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) | https://github.com/antoyo/vim-licenses |
| vim-commentary | commentary.vim: comment stuff out | [Vim](https://spdx.org/licenses/Vim.html) | https://github.com/tpope/vim-commentary |
| vim-auto-pairs | Vim plugin, insert or delete brackets, parens, quotes in pair | [MIT](https://spdx.org/licenses/MIT.html) | https://github.com/jiangmiao/auto-pairs |
| vim-gist | vimscript for gist  | [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) | https://github.com/mattn/gist-vim |
| vim-webapi | vim interface to Web API | TBD | https://github.com/mattn/webapi-vim |
| vim-previm | Realtime preview by Vim. (Markdown, reStructuredText, textile) | [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) | https://github.com/kannokanno/previm |
| vim-open-browser | Open URI with your favorite browser from your most favorite editor | TBD | https://github.com/tyru/open-browser.vim |
| vim-gitgutter | A Vim plugin which shows a git diff in the gutter (sign column) and stages/undoes hunks. | [MIT](https://spdx.org/licenses/MIT.html) | https://github.com/Spredzy/vim-gitgutter |
| vim-gv | A git commit browser | TBD | https://github.com/Spredzy/gv.vim |

