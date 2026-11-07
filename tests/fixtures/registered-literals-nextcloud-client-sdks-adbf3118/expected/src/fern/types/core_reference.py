

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .core_reference_open_graph_object import CoreReferenceOpenGraphObject


class CoreReference(UniversalBaseModel):
    rich_object_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="richObjectType"), pydantic.Field(alias="richObjectType")
    ]
    rich_object: typing_extensions.Annotated[
        typing.Dict[str, typing.Dict[str, typing.Any]],
        FieldMetadata(alias="richObject"),
        pydantic.Field(alias="richObject"),
    ]
    open_graph_object: typing_extensions.Annotated[
        CoreReferenceOpenGraphObject, FieldMetadata(alias="openGraphObject"), pydantic.Field(alias="openGraphObject")
    ]
    accessible: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
