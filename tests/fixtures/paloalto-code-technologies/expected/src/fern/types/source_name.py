

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourceName(enum.StrEnum):
    VCS_WEBHOOKS = "VCS Webhooks"
    VCS_APP = "VCS App"
    VCS_DEPLOY_KEY = "VCS DeployKey"
    CI_CREDENTIALS = "CI Credentials"
    CI_PLUGINS = "CI Plugins"
    CI_FILES = "CI Files"
    VCS_CREDENTIALS = "VCS Credentials"
    PIPELINE_CONFIGURATIONS = "Pipeline Configurations"
    PIPELINE_TOOLS = "Pipeline Tools"
    INTEGRATIONS = "Integrations"

    def visit(
        self,
        vcs_webhooks: typing.Callable[[], T_Result],
        vcs_app: typing.Callable[[], T_Result],
        vcs_deploy_key: typing.Callable[[], T_Result],
        ci_credentials: typing.Callable[[], T_Result],
        ci_plugins: typing.Callable[[], T_Result],
        ci_files: typing.Callable[[], T_Result],
        vcs_credentials: typing.Callable[[], T_Result],
        pipeline_configurations: typing.Callable[[], T_Result],
        pipeline_tools: typing.Callable[[], T_Result],
        integrations: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourceName.VCS_WEBHOOKS:
            return vcs_webhooks()
        if self is SourceName.VCS_APP:
            return vcs_app()
        if self is SourceName.VCS_DEPLOY_KEY:
            return vcs_deploy_key()
        if self is SourceName.CI_CREDENTIALS:
            return ci_credentials()
        if self is SourceName.CI_PLUGINS:
            return ci_plugins()
        if self is SourceName.CI_FILES:
            return ci_files()
        if self is SourceName.VCS_CREDENTIALS:
            return vcs_credentials()
        if self is SourceName.PIPELINE_CONFIGURATIONS:
            return pipeline_configurations()
        if self is SourceName.PIPELINE_TOOLS:
            return pipeline_tools()
        if self is SourceName.INTEGRATIONS:
            return integrations()
