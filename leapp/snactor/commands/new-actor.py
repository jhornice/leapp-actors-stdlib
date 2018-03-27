import os
import sys

from leapp.snactor.utils import find_project_basedir, make_class_name, make_name, requires_project
from leapp.utils.clicmd import command, command_arg, UsageError


@command('new-actor', help='Creates a new actor')
@command_arg('actor-name')
@requires_project
def cli(args):
    actor_name = args.actor_name
    basedir = find_project_basedir('.')

    actors_dir = os.path.join(basedir, 'actors')
    if not os.path.isdir(actors_dir):
        os.mkdir(actors_dir)

    actor_dir = os.path.join(actors_dir, actor_name.lower())
    if not os.path.isdir(actor_dir):
        os.mkdir(actor_dir)

    actor_test_dir = os.path.join(actor_dir, 'tests')
    if not os.path.isdir(actor_test_dir):
        os.mkdir(actor_test_dir)

    actor_path = os.path.join(actor_dir, 'actor.py')
    if os.path.exists(actor_path):
        raise UsageError("File already exists: {}".format(actor_path))

    with open(actor_path, 'w') as f:
        f.write('''from leapp.actors import Actor


class {actor_class}(Actor):
    name = '{actor_name}'
    description = 'For the actor {actor_name} has been no description provided.'
    consumes = ()
    produces = ()
    tags = ()

    def process(self):
        pass
'''.format(actor_class=make_class_name(actor_name), actor_name=make_name(actor_name)))

    sys.stdout.write("New actor {} has been created at {}\n".format(make_class_name(actor_name),
                                                                    os.path.realpath(actor_path)))
