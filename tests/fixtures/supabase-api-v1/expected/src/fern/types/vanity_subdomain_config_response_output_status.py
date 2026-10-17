

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VanitySubdomainConfigResponseOutputStatus(enum.StrEnum):
    NOT_USED = "not-used"
    CUSTOM_DOMAIN_USED = "custom-domain-used"
    ACTIVE = "active"

    def visit(
        self,
        not_used: typing.Callable[[], T_Result],
        custom_domain_used: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VanitySubdomainConfigResponseOutputStatus.NOT_USED:
            return not_used()
        if self is VanitySubdomainConfigResponseOutputStatus.CUSTOM_DOMAIN_USED:
            return custom_domain_used()
        if self is VanitySubdomainConfigResponseOutputStatus.ACTIVE:
            return active()
