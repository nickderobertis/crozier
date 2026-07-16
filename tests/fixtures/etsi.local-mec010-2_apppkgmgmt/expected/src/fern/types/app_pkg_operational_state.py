

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppPkgOperationalState(enum.StrEnum):
    """
    Operational state of the onboarded application package: Ã¢â‚¬Â¢ENABLED: the application package can be used for instantiation of new application instances. Ã¢â‚¬Â¢DISABLED: the application package cannot be used for further application instantiation requests.
    """

    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    def visit(self, enabled: typing.Callable[[], T_Result], disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is AppPkgOperationalState.ENABLED:
            return enabled()
        if self is AppPkgOperationalState.DISABLED:
            return disabled()
