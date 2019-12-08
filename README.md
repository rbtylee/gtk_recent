# gtk_recent
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/paypalme/rbtylee)  [![License](http://img.shields.io/badge/license-GPLv3-blue.svg?colorB=9977bb&style=plastic)](https://github.com/rbtylee/gtk_recent/blob/master/LICENSE)


Python script to add documents to the file recently-used.xbel, usually located in `~/.local/share`.

This program has only been tested and used on Linux (Debian/Ubuntu based) systems. Support for other operating systems is untested or not provided, but patches accepted.

# Why

As gtk based apps and possibly other applications update recently-used.xbel by default as the user opens and saves files, what is the need for this program?

* Users of command line appliacations may wish to "Bookmark" documents opened or edited to more easily access using gtk apps.
* Users of non gtk applications may wish to do the same, or use this command to add suppport for recently-used.xbel to their appllication.

The latter case provided the motivation for this script for use with [Bodhi Linux](https://www.bodhilinux.com/) and a few of the [EFL](https://www.enlightenment.org/about-efl.md) applications installed on Bodhi.

## Dependencies

* python
* python-gi
* python-magic (Optional, but recommended)

## Installation

It is recommended Bodhi 5.x users install from Bodhi's repo:

```ShellSession
sudo apt update
sudo apt install gtk-recent
```

Other users can install using `setup.py`. To install system wide:


```ShellSession
sudo python setup.py install 
```
> Note: setup.py does not install the optional python-magic module. It is recommended to install that using your package manager or by some other method (pip or manually). Also note, this is my first time using setup.py in a project, so I make no guarantees I have accomplished this correctly.

But as gtk_recent is just a single file one can install manually simply to moving the file to a lcoation in your path, say /usr/bin. Just be sure the needed dependencies are installed.

## Usage

Typical usage examples:<br><br>



Add myFile to recently-used.xbel with `application name="myapp" exec="&apos;myapp %u&apos"`.
>Note: File will only be added if the mime_type of myFile can be determined.

`gtk_recent myapp /path/to/myFile`


<br><br>Add myfile to recently-used.xbel with `application name="myApp" exec="&apos;myapp %u&apos"`.

>As before, File will only be added if the mime_type of myFile can be determined.

`gtk_recent -x myapp myApp /path/to/myFile`

<br><br>Add myFile to recently-used.xbel with `application name="myapp" exec="&apos;myapp %u&apos"`.

Sets mime type to `text/plain`
>Note: File will only be added if the mime_type is recognized by the program. (See Supported Mime Types)

`gtk_recent myapp /path/to/myFile "text/plain"`


<br><br>Add myFile to recently-used.xbel with `application name="myapp" exec="&apos;myapp %u&apos"`.
<br>Sets mime type to `application/foobar`

`gtk_recent -f myapp /path/to/myFile "application/foobar"`


<br><br>Add myFile to recently-used.xbel with `application name="myapp" exec="&apos;myapp %u&apos"`.
<br>Tries to determine mime type of myFile, but if unsuccessful sets mime type to `application/unknown`

`gtk_recent -f myapp /path/to/myFile`

## Supported Mime Types

gtk_recent recognizes by default:

* System mime types listed at `/etc/mime.types`
* User defined mime types listed at `~/mime.types`

Support for any other mime type can be forced by adding the -f argument, or by adding the mime type to one of the files listed above.

Mime types for files, if not specified in the commands positional arguments, is determined by python-magic if installed. But if python-magic is not installed, defaults to the result given by pythons mimetypes module.

## Reporting bugs

Please use the GitHub issue tracker for any bugs or feature suggestions:

> <https://github.com/rbtylee/gtk_recent/issues>

## Contributing

Help is always Welcome, as with all Open Source Projects the more people that help the better it gets!

Please submit patches to the code or documentation as GitHub pull requests! 
Please keep all patches [pep8](https://pypi.org/project/pep8/) and [pylint](https://www.pylint.org/) compliant.

Contributions must be licensed under this project's copyright (see LICENSE). 

# Support This Project

Donations to [Bodhi Linux](https://www.bodhilinux.com/donate/) would be greatly appreciate and keep our distro moving along. But if you like the work I do for Bodhi and wish to see more of it, I'd be happy about a donation. You can either donate via [PayPall](https://www.paypal.com/paypalme/rbtylee) or [Liberapay](https://liberapay.com/ylee/). 


