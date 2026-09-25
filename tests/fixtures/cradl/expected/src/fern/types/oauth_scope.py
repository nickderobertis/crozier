

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ACTIONS_RUNS_READ = "actions.runs:read"
    """
    Read permissions
    """

    ACTIONS_RUNS_WRITE = "actions.runs:write"
    """
    Write permissions
    """

    ACTIONS_READ = "actions:read"
    """
    Read permissions
    """

    ACTIONS_WRITE = "actions:write"
    """
    Write permissions
    """

    AGENTS_RUNS_READ = "agents.runs:read"
    """
    Read permissions
    """

    AGENTS_RUNS_WRITE = "agents.runs:write"
    """
    Write permissions
    """

    AGENTS_STATISTICS_READ = "agents.statistics:read"
    """
    Read permissions
    """

    AGENTS_READ = "agents:read"
    """
    Read permissions
    """

    AGENTS_WRITE = "agents:write"
    """
    Write permissions
    """

    APPCLIENTS_READ = "appclients:read"
    """
    Read permissions
    """

    APPCLIENTS_WRITE = "appclients:write"
    """
    Write permissions
    """

    DOCUMENTS_READ = "documents:read"
    """
    Read permissions
    """

    DOCUMENTS_WRITE = "documents:write"
    """
    Write permissions
    """

    HOOKS_RUNS_READ = "hooks.runs:read"
    """
    Read permissions
    """

    HOOKS_RUNS_WRITE = "hooks.runs:write"
    """
    Write permissions
    """

    HOOKS_READ = "hooks:read"
    """
    Read permissions
    """

    HOOKS_WRITE = "hooks:write"
    """
    Write permissions
    """

    LOGS_READ = "logs:read"
    """
    Read permissions
    """

    MODELS_READ = "models:read"
    """
    Read permissions
    """

    MODELS_WRITE = "models:write"
    """
    Write permissions
    """

    ORGANIZATIONS_READ = "organizations:read"
    """
    Read permissions
    """

    ORGANIZATIONS_WRITE = "organizations:write"
    """
    Write permissions
    """

    PREDICTIONS_READ = "predictions:read"
    """
    Read permissions
    """

    PREDICTIONS_WRITE = "predictions:write"
    """
    Write permissions
    """

    USERS_READ = "users:read"
    """
    Read permissions
    """

    USERS_WRITE = "users:write"
    """
    Write permissions
    """

    VALIDATIONS_TASKS_READ = "validations.tasks:read"
    """
    Read permissions
    """

    VALIDATIONS_TASKS_WRITE = "validations.tasks:write"
    """
    Write permissions
    """

    VALIDATIONS_READ = "validations:read"
    """
    Read permissions
    """

    VALIDATIONS_WRITE = "validations:write"
    """
    Write permissions
    """

    WORKFLOWS_READ = "workflows:read"
    """
    Read permissions
    """

    WORKFLOWS_WRITE = "workflows:write"
    """
    Write permissions
    """

    def visit(
        self,
        actions_runs_read: typing.Callable[[], T_Result],
        actions_runs_write: typing.Callable[[], T_Result],
        actions_read: typing.Callable[[], T_Result],
        actions_write: typing.Callable[[], T_Result],
        agents_runs_read: typing.Callable[[], T_Result],
        agents_runs_write: typing.Callable[[], T_Result],
        agents_statistics_read: typing.Callable[[], T_Result],
        agents_read: typing.Callable[[], T_Result],
        agents_write: typing.Callable[[], T_Result],
        appclients_read: typing.Callable[[], T_Result],
        appclients_write: typing.Callable[[], T_Result],
        documents_read: typing.Callable[[], T_Result],
        documents_write: typing.Callable[[], T_Result],
        hooks_runs_read: typing.Callable[[], T_Result],
        hooks_runs_write: typing.Callable[[], T_Result],
        hooks_read: typing.Callable[[], T_Result],
        hooks_write: typing.Callable[[], T_Result],
        logs_read: typing.Callable[[], T_Result],
        models_read: typing.Callable[[], T_Result],
        models_write: typing.Callable[[], T_Result],
        organizations_read: typing.Callable[[], T_Result],
        organizations_write: typing.Callable[[], T_Result],
        predictions_read: typing.Callable[[], T_Result],
        predictions_write: typing.Callable[[], T_Result],
        users_read: typing.Callable[[], T_Result],
        users_write: typing.Callable[[], T_Result],
        validations_tasks_read: typing.Callable[[], T_Result],
        validations_tasks_write: typing.Callable[[], T_Result],
        validations_read: typing.Callable[[], T_Result],
        validations_write: typing.Callable[[], T_Result],
        workflows_read: typing.Callable[[], T_Result],
        workflows_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ACTIONS_RUNS_READ:
            return actions_runs_read()
        if self is OauthScope.ACTIONS_RUNS_WRITE:
            return actions_runs_write()
        if self is OauthScope.ACTIONS_READ:
            return actions_read()
        if self is OauthScope.ACTIONS_WRITE:
            return actions_write()
        if self is OauthScope.AGENTS_RUNS_READ:
            return agents_runs_read()
        if self is OauthScope.AGENTS_RUNS_WRITE:
            return agents_runs_write()
        if self is OauthScope.AGENTS_STATISTICS_READ:
            return agents_statistics_read()
        if self is OauthScope.AGENTS_READ:
            return agents_read()
        if self is OauthScope.AGENTS_WRITE:
            return agents_write()
        if self is OauthScope.APPCLIENTS_READ:
            return appclients_read()
        if self is OauthScope.APPCLIENTS_WRITE:
            return appclients_write()
        if self is OauthScope.DOCUMENTS_READ:
            return documents_read()
        if self is OauthScope.DOCUMENTS_WRITE:
            return documents_write()
        if self is OauthScope.HOOKS_RUNS_READ:
            return hooks_runs_read()
        if self is OauthScope.HOOKS_RUNS_WRITE:
            return hooks_runs_write()
        if self is OauthScope.HOOKS_READ:
            return hooks_read()
        if self is OauthScope.HOOKS_WRITE:
            return hooks_write()
        if self is OauthScope.LOGS_READ:
            return logs_read()
        if self is OauthScope.MODELS_READ:
            return models_read()
        if self is OauthScope.MODELS_WRITE:
            return models_write()
        if self is OauthScope.ORGANIZATIONS_READ:
            return organizations_read()
        if self is OauthScope.ORGANIZATIONS_WRITE:
            return organizations_write()
        if self is OauthScope.PREDICTIONS_READ:
            return predictions_read()
        if self is OauthScope.PREDICTIONS_WRITE:
            return predictions_write()
        if self is OauthScope.USERS_READ:
            return users_read()
        if self is OauthScope.USERS_WRITE:
            return users_write()
        if self is OauthScope.VALIDATIONS_TASKS_READ:
            return validations_tasks_read()
        if self is OauthScope.VALIDATIONS_TASKS_WRITE:
            return validations_tasks_write()
        if self is OauthScope.VALIDATIONS_READ:
            return validations_read()
        if self is OauthScope.VALIDATIONS_WRITE:
            return validations_write()
        if self is OauthScope.WORKFLOWS_READ:
            return workflows_read()
        if self is OauthScope.WORKFLOWS_WRITE:
            return workflows_write()
