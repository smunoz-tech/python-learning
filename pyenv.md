
>note: use webi https://webinstall.dev/pyenv/

pyenv is a tool for simple Python version management.

To install pyenv, please refer to the [Readme](https://github.com/pyenv/pyenv/).

## Troubleshooting / FAQ

### Suggested build environment

pyenv will try its best to download and compile the wanted Python version,
but sometimes compilation fails because of unmet system dependencies, or
compilation succeeds but the new Python version exhibits weird failures at
runtime. The following instructions are our recommendations for a sane build
environment.

* **Mac OS X:**

    If you haven't done so, install Xcode Command Line Tools
    (`xcode-select --install`) and [Homebrew](http://brew.sh/). Then:

    ```sh
    brew install openssl readline sqlite3 xz zlib tcl-tk
    ```
    
    For older operating systems `Homebrew` might not be available so install `pyenv` with: 
    
    ```sh
    curl https://pyenv.run | bash
    ```
    
    `xcode-select --install` might not be available on older macOS's so use [this script](https://gist.github.com/rtrouton/f92f263414aaeb946e54) instead or [this page](https://xcodereleases.com/) as well as directly from Apple downloads:

    https://developer.apple.com/download/more/

    And search for:
    ```
    command line tools <version number>
    ```
    like `command line tools 10.9`
 
    For dependencies use [MacPorts](https://www.macports.org/install.php):

    ```sh
    sudo port install pkgconfig openssl zlib xz gdbm tcl tk +quartz sqlite3 sqlite3-tcl
    ```

* **Ubuntu/Debian/Mint:**

    ```sh
    sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    ```

    If you are going build PyPy from source or install other Python flavors that require CLang, also install `llvm`.

* **CentOS/Fedora 21 and below:**

    ```sh
    yum install gcc make patch zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel
    ```

* **Amazon Linux 2:**

    ```sh
    yum install gcc make patch zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl11-devel tk-devel libffi-devel xz-devel
    ```
* **Fedora 22 and above:**

    ```sh
    dnf install make gcc patch zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel libuuid-devel gdbm-libs libnsl2
    ```

*  **Fedora Silverblue**

    ```sh
    toolbox enter
    sudo dnf update vte-profile  # https://github.com/containers/toolbox/issues/390
    sudo dnf install "@Development Tools" zlib-devel bzip2 bzip2-devel readline-devel sqlite \
    sqlite-devel openssl-devel xz xz-devel libffi-devel findutils tk-devel
    ```

* **openSUSE:**

    ```sh
    zypper install gcc automake bzip2 libbz2-devel xz xz-devel openssl-devel ncurses-devel \
    readline-devel zlib-devel tk-devel libffi-devel sqlite3-devel gdbm-devel make findutils patch
    ```

* **Arch Linux:**

    ```sh
    pacman -S --needed base-devel openssl zlib xz tk
    ```

* **Solus:**

    ```
    sudo eopkg it -c system.devel
    sudo eopkg install git gcc make zlib-devel bzip2-devel readline-devel sqlite3-devel openssl-devel tk-devel
    ```

* **Alpine Linux:**

    ```sh 
    apk add --no-cache git bash build-base libffi-dev openssl-dev bzip2-dev zlib-dev xz-dev readline-dev sqlite-dev tk-dev
    ```

    * Installation of Python 3.7 may fail due to Python 3.7.0 issue [#34555](https://bugs.python.org/issue34555). A workaround is to install the [linux system headers package](https://pkgs.alpinelinux.org/packages?name=linux-headers&branch=edge):

        ```sh
        apk add linux-headers 
        ```

* **Void Linux:**

    ```sh
    xbps-install base-devel libffi-devel bzip2-devel openssl openssl-devel readline readline-devel sqlite-devel xz liblzma-devel zlib zlib-devel
    ```


See also [Common build problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems) for further information.


### How is this better than pythonbrew and pythonz?

See [[Why pyenv?]]


### Python scripts or shell scripts that use python keep failing

If you experience failure while executing a script that issues `python` command or executes another python script:
 - try executing the command again in the appropriate `pyenv shell`
 - check if the command is a python script or invokes a python script and fix the shebang to `#!/usr/bin/env python`
 
Such failures usually show up as:
  - incompatible python version, but you are certain that you have correct version installed
  - module not found but you are certain that the module is installed
  - the issue can be traced back to something related to `PYTHONPATH`


### What is allowed in a `.python-version` file?

The string read from a `.python-version` file must match the name of an existing
directory in `~/.pyenv/versions/`. You can see the list of installed Python
versions with `pyenv versions`.

If you're using [python-build](https://github.com/pyenv/pyenv/blob/master/plugins/python-build), typically this will be one of the versions listed by the `pyenv versions` command.

Other version managers might allow fuzzy version matching on the string read
from `.python-version` file, e.g. they might allow "3.3" (without patch suffix)
to match the latest Python 3.3 release. **pyenv will not support this**, because
such behavior is unpredictable and therefore harmful.

[python-build]: ../../tree/master/plugins/python-build


### How to verify that I have set up pyenv correctly?

1.  Check that `pyenv` is in your PATH:

    ```sh
    which pyenv
    ```

2.  Check that pyenv's shims directory is in your PATH:

    ```sh
    echo $PATH | grep --color=auto "$(pyenv root)/shims"
    ```

    If not, see [Configure your shell's environment for pyenv] in the installation instructions.

[Configure your shell's environment for pyenv]: ../#basic-github-checkout


### pyenv is installed but things just aren't working for me!

Please search [existing issues][issues] and open a new one if you can't find any answers. Here's a script that dumps information about your current environment; you can use Gist to paste it online and share the URL to it in your bug report:

```sh
git clone https://github.com/pyenv/pyenv-doctor.git "$(pyenv root)/plugins/pyenv-doctor"
pyenv doctor
```

[issues]: https://github.com/pyenv/pyenv/issues
[Gist]: https://gist.github.com/


### Which shell startup file do I put pyenv config in?

Typically it's one of the following:

* bash: `~/.bash_profile`
* zsh: `~/.zshrc`
* ksh: `~/.kshrc`
* other: `~/.profile`

With bash on Ubuntu, you probably already have a `~/.profile`. In that case you
should add pyenv config there instead of creating a `~/.bash_profile`. However,
since this file is read only once per desktop login, you may achieve quicker
results by adding pyenv to `~/.bashrc` instead.

See [[Unix shell initialization]] for more info about how config files get
loaded.


### Debugging pyenv

The `PYENV_DEBUG` is the environment variable to debug logging in pyenv. You can try to enable debug logging by setting something in the environment variable like `PYENV_DEBUG=1 pyenv versions`.


### How to build CPython with Framework support on OS X

Some of 3rd party tool like [PyInstaller](https://github.com/pyinstaller/pyinstaller) might require CPython installation built with `--enable-framework`. You can build CPython with shared library as follows.

```sh
$ env PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.5.0
```

Note: You'd better not `export` `PYTHON_CONFIGURE_OPTS` cause it breaks building of some distros like `miniconda` and `anaconda`.


### How to build CPython with `--enable-shared`

Some of 3rd party tool like [PyInstaller](https://github.com/pyinstaller/pyinstaller) might require CPython installation built with `--enable-shared`. You can build CPython with shared library as follows.

```sh
$ env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.0
```

Since pyenv (precisely, python-build) will build CPython with configuring RPATH, you don't have to set `LD_LIBRARY_PATH` to specify library path on GNU/Linux.

### How to build CPython for maximum performance

Building CPython with `--enable-optimizations` will result in a faster interpreter at the cost of significantly longer build times.
Most notably, this enables PGO (profile guided optimization). While your mileage may vary, it is common for performance improvement from this to be in the ballpark of 30%.
```sh
env PYTHON_CONFIGURE_OPTS='--enable-optimizations --with-lto' PYTHON_CFLAGS='-march=native -mtune=native' pyenv install 3.6.0
```

You can also customize the task used for profile guided optimization by setting the `PROFILE_TASK` environment variable, for instance, `PROFILE_TASK='-m test.regrtest --pgo -j0'` will run much faster than the default task.
