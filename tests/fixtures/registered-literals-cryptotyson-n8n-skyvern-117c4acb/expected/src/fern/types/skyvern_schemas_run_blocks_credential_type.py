

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkyvernSchemasRunBlocksCredentialType(enum.StrEnum):
    SKYVERN = "skyvern"
    BITWARDEN = "bitwarden"
    ONE_PASSWORD = "1password"

    def visit(
        self,
        skyvern: typing.Callable[[], T_Result],
        bitwarden: typing.Callable[[], T_Result],
        one_password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SkyvernSchemasRunBlocksCredentialType.SKYVERN:
            return skyvern()
        if self is SkyvernSchemasRunBlocksCredentialType.BITWARDEN:
            return bitwarden()
        if self is SkyvernSchemasRunBlocksCredentialType.ONE_PASSWORD:
            return one_password()
