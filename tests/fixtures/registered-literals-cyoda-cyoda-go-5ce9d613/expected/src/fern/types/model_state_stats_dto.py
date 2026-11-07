

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ModelStateStatsDto(UniversalBaseModel):
    model_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="modelName"), pydantic.Field(alias="modelName", description="Entity Model Name")
    ]
    """
    Entity Model Name
    """

    model_version: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="modelVersion"),
        pydantic.Field(alias="modelVersion", description="Entity Model Version"),
    ]
    """
    Entity Model Version
    """

    state: str = pydantic.Field()
    """
    Entity State
    """

    count: int = pydantic.Field()
    """
    Entity Count
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
