from __future__ import print_function

import click

import leapp.workflows
from leapp.tool.commands.workflow import workflow
from leapp.logger import configure_logger
from leapp.tool.utils import requires_project, find_project_basedir
from leapp.repository.scan import scan_repo


@workflow.command('runx')
@click.argument('name')
@requires_project
def cli(name):
    configure_logger()
    repository = scan_repo(find_project_basedir('.'))
    repository.load()
    for wf in leapp.workflows.get_workflows():
        if wf.name.lower() == name.lower():
            wf().run()