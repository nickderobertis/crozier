

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationDataIdentificationMethod(enum.StrEnum):
    """
    Identifikationsmethode
    """

    VIDEO_IDENTIFICATION = "video_identification"
    ONLINE_IDENTIFICATION = "online_identification"
    PERSONAL_APPEARANCE = "personal_appearance"
    EID = "eid"

    def visit(
        self,
        video_identification: typing.Callable[[], T_Result],
        online_identification: typing.Callable[[], T_Result],
        personal_appearance: typing.Callable[[], T_Result],
        eid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationDataIdentificationMethod.VIDEO_IDENTIFICATION:
            return video_identification()
        if self is IdentificationDataIdentificationMethod.ONLINE_IDENTIFICATION:
            return online_identification()
        if self is IdentificationDataIdentificationMethod.PERSONAL_APPEARANCE:
            return personal_appearance()
        if self is IdentificationDataIdentificationMethod.EID:
            return eid()
