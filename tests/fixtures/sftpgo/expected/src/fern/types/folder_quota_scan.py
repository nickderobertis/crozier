

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FolderQuotaScan(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    folder name to which the quota scan refers
    """

    start_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    scan start time as unix timestamp in milliseconds
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
