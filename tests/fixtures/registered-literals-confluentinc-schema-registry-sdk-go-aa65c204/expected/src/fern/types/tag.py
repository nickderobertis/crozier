

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tag_entity_status import TagEntityStatus
from .time_boundary import TimeBoundary


class Tag(UniversalBaseModel):
    type_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeName"), pydantic.Field(alias="typeName")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]] = None
    entity_guid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entityGuid"), pydantic.Field(alias="entityGuid")
    ] = None
    entity_status: typing_extensions.Annotated[
        typing.Optional[TagEntityStatus], FieldMetadata(alias="entityStatus"), pydantic.Field(alias="entityStatus")
    ] = None
    propagate: typing.Optional[bool] = None
    validity_periods: typing_extensions.Annotated[
        typing.Optional[typing.List[TimeBoundary]],
        FieldMetadata(alias="validityPeriods"),
        pydantic.Field(alias="validityPeriods"),
    ] = None
    remove_propagations_on_entity_delete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="removePropagationsOnEntityDelete"),
        pydantic.Field(alias="removePropagationsOnEntityDelete"),
    ] = None
    entity_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entityType"), pydantic.Field(alias="entityType")
    ] = None
    entity_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="entityName"), pydantic.Field(alias="entityName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
