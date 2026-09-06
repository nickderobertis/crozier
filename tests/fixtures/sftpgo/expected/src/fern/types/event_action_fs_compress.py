

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EventActionFsCompress(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full path to the (zip) archive to create. The parent dir must exist
    """

    paths: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    paths to add the archive
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
