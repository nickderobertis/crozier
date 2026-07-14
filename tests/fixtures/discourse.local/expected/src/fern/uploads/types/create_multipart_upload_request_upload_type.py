

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreateMultipartUploadRequestUploadType(str, enum.Enum):
    AVATAR = "avatar"
    PROFILE_BACKGROUND = "profile_background"
    CARD_BACKGROUND = "card_background"
    CUSTOM_EMOJI = "custom_emoji"
    COMPOSER = "composer"

    def visit(
        self,
        avatar: typing.Callable[[], T_Result],
        profile_background: typing.Callable[[], T_Result],
        card_background: typing.Callable[[], T_Result],
        custom_emoji: typing.Callable[[], T_Result],
        composer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateMultipartUploadRequestUploadType.AVATAR:
            return avatar()
        if self is CreateMultipartUploadRequestUploadType.PROFILE_BACKGROUND:
            return profile_background()
        if self is CreateMultipartUploadRequestUploadType.CARD_BACKGROUND:
            return card_background()
        if self is CreateMultipartUploadRequestUploadType.CUSTOM_EMOJI:
            return custom_emoji()
        if self is CreateMultipartUploadRequestUploadType.COMPOSER:
            return composer()
