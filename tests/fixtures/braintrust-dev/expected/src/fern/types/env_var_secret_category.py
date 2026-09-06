

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnvVarSecretCategory(enum.StrEnum):
    """
    The category of the secret: env_var for regular environment variables, ai_provider for AI provider API keys
    """

    ENV_VAR = "env_var"
    AI_PROVIDER = "ai_provider"
    SANDBOX_PROVIDER = "sandbox_provider"

    def visit(
        self,
        env_var: typing.Callable[[], T_Result],
        ai_provider: typing.Callable[[], T_Result],
        sandbox_provider: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnvVarSecretCategory.ENV_VAR:
            return env_var()
        if self is EnvVarSecretCategory.AI_PROVIDER:
            return ai_provider()
        if self is EnvVarSecretCategory.SANDBOX_PROVIDER:
            return sandbox_provider()
