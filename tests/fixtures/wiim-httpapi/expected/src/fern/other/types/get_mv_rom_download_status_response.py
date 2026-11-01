

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMvRomDownloadStatusResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the MV ROM download process, where "0" typically indicates that the download is in progress and "1" indicates that the download is complete.
    """

    count: typing.Optional[str] = pydantic.Field(default=None)
    """
    The total number of items to be downloaded
    """

    dcount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of items that have been downloaded so far
    """

    wcount: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of items that are currently being downloaded
    """

    tsize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The total size of the items to be downloaded, in bytes
    """

    dsize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The size of the items that have been downloaded so far, in bytes
    """

    wsize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The size of the items that are currently being downloaded, in bytes
    """

    csize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The size of the items that have been downloaded and verified, in bytes
    """

    cdsize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The size of the items that have been downloaded but not yet verified, in bytes
    """

    cwsize: typing.Optional[str] = pydantic.Field(default=None)
    """
    The size of the items that are currently being downloaded but not yet verified, in bytes
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
