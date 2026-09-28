

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationDecisionStatus(enum.StrEnum):
    """
    The status of the authentication.

    Possible values:

    * **refused**

    * **proceed**

    For more information, refer to [Authenticate cardholders using the Authentication SDK](https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/authenticate-cardholders/).
    """

    PROCEED = "proceed"
    REFUSED = "refused"

    def visit(self, proceed: typing.Callable[[], T_Result], refused: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationDecisionStatus.PROCEED:
            return proceed()
        if self is AuthenticationDecisionStatus.REFUSED:
            return refused()
