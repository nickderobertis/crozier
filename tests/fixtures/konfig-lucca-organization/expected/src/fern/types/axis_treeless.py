

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AxisTreeless(UniversalBaseModel):
    id: typing.Optional[int] = None
    name: typing.Optional[str] = None
    url: typing.Optional[str] = None
    multilingual_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="multilingualName"), pydantic.Field(alias="multilingualName")
    ]
    position: typing.Optional[int] = None
    parent_axis_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="parentAxisId"), pydantic.Field(alias="parentAxisId")
    ] = None
    is_active: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isActive"), pydantic.Field(alias="isActive")
    ] = None
    is_read_only: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isReadOnly"), pydantic.Field(alias="isReadOnly")
    ] = None
    is_nn_relation: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isNNRelation"), pydantic.Field(alias="isNNRelation")
    ] = None
    level: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
