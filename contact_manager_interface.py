# This example uses docopt with the built in cmd module to demonstrate an
# interactive command application.
"""
Usage:
    contact_manager -n <name> -p <phonenumber>    add new contact
    contact_manager search <name>                 search for a contact
    contact_manager send <name> -m <message>      send SMS
    contact_manager (-i | --interactive)
    contact_manager (-h | --help | --version)
Options:
    -i, --interactive                             Interactive Mode
    -h, --help                                    Show this screen and exit.
    
"""

import sys
import cmd
import os
from docopt import docopt, DocoptExit
from contact_manager import ContactManager, send_text
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print("invalid command! try again")
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class my_interactive_mode (cmd.Cmd):
    os.system('cls')
    init()
    font = Figlet(font='speed')                             #colossal
    print(Fore.CYAN + font.renderText('N u n t i u s'))
    intro = 'Interactive Mode'
    prompt = '(Contact_Manager)'
    file = None

    create_new_contact = ContactManager()

    def add_contact(self, name, number):
        print  self.create_new_contact.add_record(name, number)

    def search(self, name):
        print self.create_new_contact.search_record(name)

    def sms(self, name, message):
        print send_text(name, message)

    @docopt_cmd
    def do_add(self, args):
        """Usage: add -n <name> -p <phonenumber>"""
        self.add_contact(args['<name>'], args['<phonenumber>'])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search <name>"""
        self.search(args['<name>'])

    @docopt_cmd
    def do_text(self, args):
        """Usage: text <name> -m <message>"""
        self.sms(args['<name>'], args['<message>'])

    def do_quit(self, args):
        """Quits Interactive Mode."""

        print('Come again')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    my_interactive_mode().cmdloop()
print(opt)