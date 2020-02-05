# HackContest
Some Tools for the UCL Hack Contest

In the fact of a hacking championship I decided to create 
these suit of tools which should help to force some password.

First one I decided to program a simple password generator.
It is designed for a pdf password brutforce.
Right now the generator can give random outputs with a pre-defined size.
All alphanumerical characters and these symbols [-,_,*,^,+,=,.,?,!] can appear
in the generated password.

You can call the Generator with import the module 'pwd_generator' from Script directory.
Example of call a generation of password with size 10 :

from Script import pwd_generator

pwd = pwd_generator.PwdGenerator(10)
pwd.generate()

Don't forget to generate it! Until the password is not generated the variable password is equal to a null string like "" and you can't access it with the 'legal' way.
