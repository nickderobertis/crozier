

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMvRomDownloadV2StatusResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the MV ROM download process, where "0" typically indicates that the download is in progress and "1" indicates that the download is complete.
    """

    progress: typing.Optional[str] = pydantic.Field(default=None)
    """
    The overall progress of the MV ROM download process as a percentage, ranging from "0" to "100"
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the item currently being downloaded or processed
    """

    ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current version of the firmware or software being updated
    """

    new_ver: typing.Optional[str] = pydantic.Field(default=None)
    """
    The new version of the firmware or software being updated to after the download is complete and successful verification is done.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
