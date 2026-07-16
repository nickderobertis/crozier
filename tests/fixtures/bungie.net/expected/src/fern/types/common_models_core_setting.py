

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class CommonModelsCoreSetting(UniversalBaseModel):
    child_settings: typing_extensions.Annotated[
        typing.Optional[typing.List["CommonModelsCoreSetting"]],
        FieldMetadata(alias="childSettings"),
        pydantic.Field(alias="childSettings"),
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    identifier: typing.Optional[str] = None
    image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imagePath"), pydantic.Field(alias="imagePath")
    ] = None
    is_default: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDefault"), pydantic.Field(alias="isDefault")
    ] = None
    summary: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CommonModelsCoreSetting)
