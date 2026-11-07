

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ImageData(UniversalBaseModel):
    """
    Model returns information about the queried mediaID
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the requested media resource
    """

    entity_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    type of entity associated to the media file
    """

    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the entity associated to the media file
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    size of the media file
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    type of media
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
