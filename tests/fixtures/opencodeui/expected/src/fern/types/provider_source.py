

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderSource(enum.StrEnum):
    ENV = "env"
    CONFIG = "config"
    CUSTOM = "custom"
    API = "api"

    def visit(
        self,
        env: typing.Callable[[], T_Result],
        config: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderSource.ENV:
            return env()
        if self is ProviderSource.CONFIG:
            return config()
        if self is ProviderSource.CUSTOM:
            return custom()
        if self is ProviderSource.API:
            return api()
