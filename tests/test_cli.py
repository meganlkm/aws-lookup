from unittest import TestCase

from click.testing import CliRunner

from aws_lookup import cli as aws_lookup_cli
from aws_lookup.settings import VERSION

CMD_OPTS = ['--version', '-h,', '?,', '--help']


class CLITest(TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_cmd_help(self):
        for help_flag in ['--help', '?', '-h']:
            result = self.runner.invoke(aws_lookup_cli.cli, [help_flag])
            for opt in CMD_OPTS:
                self.assertIn(opt, result.output)

    def test_cmd_version(self):
        result = self.runner.invoke(aws_lookup_cli.cli, ['--version'])
        self.assertEquals('aws-lookup version: {}\n'.format(VERSION), result.output)
