

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class UpdateAvatarRequestType(str, enum.Enum):
    UPLOADED = "uploaded"
    CUSTOM = "custom"
    GRAVATAR = "gravatar"
    SYSTEM = "system"

    def visit(
        self,
        uploaded: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
        gravatar: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateAvatarRequestType.UPLOADED:
            return uploaded()
        if self is UpdateAvatarRequestType.CUSTOM:
            return custom()
        if self is UpdateAvatarRequestType.GRAVATAR:
            return gravatar()
        if self is UpdateAvatarRequestType.SYSTEM:
            return system()
