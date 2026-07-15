

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WebhookSupportMode(str, enum.Enum):
    """
    Mode of the webhook support.
    """

    NATIVE = "native"
    VIRTUAL = "virtual"
    NONE = "none"

    def visit(
        self,
        native: typing.Callable[[], T_Result],
        virtual: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookSupportMode.NATIVE:
            return native()
        if self is WebhookSupportMode.VIRTUAL:
            return virtual()
        if self is WebhookSupportMode.NONE:
            return none()
