

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetOrdersResponseDownloadFilesItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the downloadable file
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user-facing name for the downloadable file
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The hosted location for the downloadable file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
