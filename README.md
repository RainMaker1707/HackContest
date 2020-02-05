# HackContest
Some Tools for the UCL Hack Contest.

In the fact of a hacking championship I decided to create 
these suit of tools which should help to force some password.

#PDF Password BrutForce

##PasswordGenerator

###Generate

First one I decided to program a simple password generator.
It is designed for a pdf password brutforce.

Right now the generator can give random outputs with a pre-defined size.
All alphanumerical characters and these symbols {- _ * ^ + = . ? !} can appear
in the generated password.

You can call the Generator with import the module 'pwd_generator' from Script directory.
Example of call a generation of password with size 10 :

from Script import pwd_generator

pwd = pwd_generator.PwdGenerator(10)
pwd.generate()

Don't forget to generate it! Until the password is not generated the variable password is equal to a null string like "" and you can't access it with the 'legal' way.

###set_size particularity

You'll can't change the size if you use a pattern, you'll have to set the pattern to None before set the size.
Second particularity if u decide to set the size the whole password will change because it is generated again without any pattern.

###Pattern

You can choose a pattern for the password generation if u want any pattern it simply pass an arguments more in the creation of the object.

You'll can change the pattern of the password after generation with the function set_pattern(new_pattern) which take a string or None as argument.

The pattern structure is "$$$$-$$$"
So symbol $ can be replaced by any other characters in the generator list but all others characters than $ stay at his place.
If you use a pattern with a different len than the size passed as argument in the creation of the generator the pattern len will define the password size.
