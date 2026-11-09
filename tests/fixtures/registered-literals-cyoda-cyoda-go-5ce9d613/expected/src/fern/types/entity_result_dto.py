

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entity_metadata_dto import EntityMetadataDto


class EntityResultDto(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the result (typically "ENTITY")
    """

    data: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    The entity data as a JSON object
    """

    meta: typing.Optional[EntityMetadataDto] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
