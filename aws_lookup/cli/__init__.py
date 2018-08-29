import click
from pretty_json import format_json

from aws_lookup import settings
from aws_lookup.core import get_services


@click.group(invoke_without_command=True, context_settings=settings.CLI_CONTEXT_SETTINGS)
@click.option('--version', is_flag=True, help='print the aws-lookup version and exit')
@click.argument('service', required=False)
@click.pass_context
def cli(ctx, service, *args, **kwargs):
    if kwargs.get('version', False):
        return click.echo('aws-lookup version: {}'.format(settings.VERSION))

    # kwargs['logger'] = settings.get_logger()

    if service in ctx.help_option_names:
        return click.echo(ctx.get_help())

    # if service is None return list of services
    return service.echo(format_json(get_services()))
