

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ANALYTICS_READ = "analytics:read"
    """
    Read access to analytics
    """

    ANALYTICS_WRITE = "analytics:write"
    """
    Write access to analytics
    """

    ANALYTICS_CONFIG_READ = "analytics_config:read"
    """
    Read access to analytics config
    """

    ANALYTICS_CONFIG_WRITE = "analytics_config:write"
    """
    Write access to analytics config
    """

    AUTH_READ = "auth:read"
    """
    Read access to auth
    """

    AUTH_WRITE = "auth:write"
    """
    Write access to auth
    """

    DATABASE_READ = "database:read"
    """
    Read access to database
    """

    DATABASE_WRITE = "database:write"
    """
    Write access to database
    """

    DOMAINS_READ = "domains:read"
    """
    Read access to domains
    """

    DOMAINS_WRITE = "domains:write"
    """
    Write access to domains
    """

    EDGE_FUNCTIONS_READ = "edge_functions:read"
    """
    Read access to edge functions
    """

    EDGE_FUNCTIONS_WRITE = "edge_functions:write"
    """
    Write access to edge functions
    """

    ENVIRONMENT_READ = "environment:read"
    """
    Read access to environment
    """

    ENVIRONMENT_WRITE = "environment:write"
    """
    Write access to environment
    """

    ORGANIZATIONS_READ = "organizations:read"
    """
    Read access to organizations
    """

    ORGANIZATIONS_WRITE = "organizations:write"
    """
    Write access to organizations
    """

    PROJECTS_READ = "projects:read"
    """
    Read access to projects
    """

    PROJECTS_WRITE = "projects:write"
    """
    Write access to projects
    """

    REST_READ = "rest:read"
    """
    Read access to rest
    """

    REST_WRITE = "rest:write"
    """
    Write access to rest
    """

    SECRETS_READ = "secrets:read"
    """
    Read access to secrets
    """

    SECRETS_WRITE = "secrets:write"
    """
    Write access to secrets
    """

    STORAGE_READ = "storage:read"
    """
    Read access to storage
    """

    STORAGE_WRITE = "storage:write"
    """
    Write access to storage
    """

    def visit(
        self,
        analytics_read: typing.Callable[[], T_Result],
        analytics_write: typing.Callable[[], T_Result],
        analytics_config_read: typing.Callable[[], T_Result],
        analytics_config_write: typing.Callable[[], T_Result],
        auth_read: typing.Callable[[], T_Result],
        auth_write: typing.Callable[[], T_Result],
        database_read: typing.Callable[[], T_Result],
        database_write: typing.Callable[[], T_Result],
        domains_read: typing.Callable[[], T_Result],
        domains_write: typing.Callable[[], T_Result],
        edge_functions_read: typing.Callable[[], T_Result],
        edge_functions_write: typing.Callable[[], T_Result],
        environment_read: typing.Callable[[], T_Result],
        environment_write: typing.Callable[[], T_Result],
        organizations_read: typing.Callable[[], T_Result],
        organizations_write: typing.Callable[[], T_Result],
        projects_read: typing.Callable[[], T_Result],
        projects_write: typing.Callable[[], T_Result],
        rest_read: typing.Callable[[], T_Result],
        rest_write: typing.Callable[[], T_Result],
        secrets_read: typing.Callable[[], T_Result],
        secrets_write: typing.Callable[[], T_Result],
        storage_read: typing.Callable[[], T_Result],
        storage_write: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ANALYTICS_READ:
            return analytics_read()
        if self is OauthScope.ANALYTICS_WRITE:
            return analytics_write()
        if self is OauthScope.ANALYTICS_CONFIG_READ:
            return analytics_config_read()
        if self is OauthScope.ANALYTICS_CONFIG_WRITE:
            return analytics_config_write()
        if self is OauthScope.AUTH_READ:
            return auth_read()
        if self is OauthScope.AUTH_WRITE:
            return auth_write()
        if self is OauthScope.DATABASE_READ:
            return database_read()
        if self is OauthScope.DATABASE_WRITE:
            return database_write()
        if self is OauthScope.DOMAINS_READ:
            return domains_read()
        if self is OauthScope.DOMAINS_WRITE:
            return domains_write()
        if self is OauthScope.EDGE_FUNCTIONS_READ:
            return edge_functions_read()
        if self is OauthScope.EDGE_FUNCTIONS_WRITE:
            return edge_functions_write()
        if self is OauthScope.ENVIRONMENT_READ:
            return environment_read()
        if self is OauthScope.ENVIRONMENT_WRITE:
            return environment_write()
        if self is OauthScope.ORGANIZATIONS_READ:
            return organizations_read()
        if self is OauthScope.ORGANIZATIONS_WRITE:
            return organizations_write()
        if self is OauthScope.PROJECTS_READ:
            return projects_read()
        if self is OauthScope.PROJECTS_WRITE:
            return projects_write()
        if self is OauthScope.REST_READ:
            return rest_read()
        if self is OauthScope.REST_WRITE:
            return rest_write()
        if self is OauthScope.SECRETS_READ:
            return secrets_read()
        if self is OauthScope.SECRETS_WRITE:
            return secrets_write()
        if self is OauthScope.STORAGE_READ:
            return storage_read()
        if self is OauthScope.STORAGE_WRITE:
            return storage_write()
