[ NOTE: the dontpad.com API appears to no longer be active; for an effective ans modern remote access tool, see github.com/Milazzo11/MIDPEM ]

This program allows for remote access using the wesite dontpad.com

Create two dontpad.com links, and insert them into the code.  The first link is for code execution, and needs to be setup.  The other does not.
The code should be written in Bash (or whatever the command line language is native to the infected systems).
Setup the first link as follows:
--------------------------------
*!
#:#
<write code here>
--------------------------------

The "!" symbol can be replaced with any character, and the "#" symbol must be replaced with a number.
The first number on the second line signals how many times the program should loop, and the second number denotes wait time between loops.
The second line can be kept blank, and the code will run only once.  Do not write any code on this line, however.

To execute code, replace whatever symbol is present in the "!" location.  It may take a few seconds for any active devices to detect this change, but the code will run.
Make sure to keep the asterix present before this character on the first line, and don't type multiple characters after it.

After a device has been infected with the program, it will alter the contents of the second link.
You can add a title to the second link as well and it will not be affected.
For example, the second link page may look as follows:
--------------------------------
ACTIVE SYSTEM LINKS:

http://dontpad.com/12pI91h10v1453E4r9MvM90aoCI5fg
http://dontpad.com/relCr9zl934S4bhjdjKTO56wne8vHb
--------------------------------

Each infected device will have a unique system ID that will correspond to a donpad.com link.
These links (accessible via the second link page) will show the results of the last code execution attempt recieved on that device.
Altering the contents of these pages has no effect on the program.

You can also deactivate certain devices from receiving code by placing a "%" symbol before its link on the second link page.
For example, if you had seven active system links like this:
--------------------------------
ACTIVE SYSTEM LINKS:

http://dontpad.com/12pI91h10v1453E4r9MvM90aoCI5fg
http://dontpad.com/relCr9zl934S4bhjdjKTO56wne8vHb
http://dontpad.com/B7Is373RpGcV4OmFae1DFBY96d9Oeh
http://dontpad.com/7tZ3E0dFJLGlqL3U048MX5pPb3wKCv
http://dontpad.com/2wXIEwHGNgeZjUIgehPKTiU0RsLtAF
http://dontpad.com/qrM4k78MqTWcDUTZ7x86J0l4VKINhX
http://dontpad.com/dlRKjbr9VTB13bLcNoVjcavyJnquYX
--------------------------------

You can rearrange the links as you like and insert an "%" symbol:
--------------------------------
ACTIVE SYSTEM LINKS:

http://dontpad.com/dlRKjbr9VTB13bLcNoVjcavyJnquYX
http://dontpad.com/12pI91h10v1453E4r9MvM90aoCI5fg
http://dontpad.com/7tZ3E0dFJLGlqL3U048MX5pPb3wKCv
http://dontpad.com/relCr9zl934S4bhjdjKTO56wne8vHb
%
http://dontpad.com/B7Is373RpGcV4OmFae1DFBY96d9Oeh
http://dontpad.com/2wXIEwHGNgeZjUIgehPKTiU0RsLtAF
http://dontpad.com/qrM4k78MqTWcDUTZ7x86J0l4VKINhX
--------------------------------

All the systems associated with the links below the "%" symbol will no longer run.
To re-enable them, simply remove the "%" symbol, and run the code like normal.

As of now, no antivirus services have been able to detect this program as malicious...
HOWEVER... no one likes getting infected with malware on their computer so please use this program for testing purposes only.
Thank you :)
