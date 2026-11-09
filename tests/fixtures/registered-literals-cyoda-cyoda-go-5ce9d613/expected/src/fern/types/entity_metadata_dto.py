

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntityMetadataDto(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the entity
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current state of the entity in its workflow
    """

    creation_date: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationDate"),
        pydantic.Field(alias="creationDate", description="When the entity was created"),
    ] = None
    """
    When the entity was created
    """

    transition_for_latest_save: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transitionForLatestSave"),
        pydantic.Field(alias="transitionForLatestSave", description="The transition that triggered the latest save"),
    ] = None
    """
    The transition that triggered the latest save
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
