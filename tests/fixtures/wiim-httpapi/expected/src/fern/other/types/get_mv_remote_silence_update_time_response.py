

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMvRemoteSilenceUpdateTimeResponse(UniversalBaseModel):
    start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start time of the MV remote silence period in "HH:mm" format
    """

    end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The end time of the MV remote silence period in "HH:mm" format
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
