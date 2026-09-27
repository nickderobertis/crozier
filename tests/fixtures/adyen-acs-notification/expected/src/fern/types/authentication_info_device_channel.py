

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInfoDeviceChannel(enum.StrEnum):
    """
    Indicates the type of channel interface being used to initiate the transaction. Possible values:

    * **app**
    * **browser**
    * **3DSRequestorInitiated** (initiated by a merchant when the cardholder is not available)
    """

    APP = "app"
    BROWSER = "browser"
    THREE_DS_REQUESTOR_INITIATED = "ThreeDSRequestorInitiated"

    def visit(
        self,
        app: typing.Callable[[], T_Result],
        browser: typing.Callable[[], T_Result],
        three_ds_requestor_initiated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationInfoDeviceChannel.APP:
            return app()
        if self is AuthenticationInfoDeviceChannel.BROWSER:
            return browser()
        if self is AuthenticationInfoDeviceChannel.THREE_DS_REQUESTOR_INITIATED:
            return three_ds_requestor_initiated()
