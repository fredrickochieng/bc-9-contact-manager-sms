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
from docopt import docopt, DocoptExit
from t import ContactManager, add_record, search_record
from messenger import send_message


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
    intro = 'Interactive Mode'
    prompt = '(Contact_Manager)'
    file = None

    def add_contact(self, name, number):
        add_record(name, number)

    def search(self, name):
        search_record(name)

    def sms(self, name, message):
        send_message(name, message)

    @docopt_cmd
    def do_add(self, args):
        """Usage: add -n <name> -p <phonenumber>"""
        self.add_contact(args['<name>'], args['<phonenumber>'])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search search <name>"""
        self.search(args['<name>'])

    @docopt_cmd
    def do_text(self, args):
        """Usage: text <name> -m <message>..."""
        self.sms(args['<name>'], (" ".join(args['<message>'])))

    def do_quit(self, args):
        """Quits Interactive Mode."""

        print('Come again')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    my_interactive_mode().cmdloop()
print(opt)
