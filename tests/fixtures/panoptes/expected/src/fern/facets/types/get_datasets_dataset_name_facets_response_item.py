

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetDatasetsDatasetNameFacetsResponseItem_Text(UniversalBaseModel):
    type: typing.Literal["text"] = "text"
    property: typing.Optional[str] = None
    name: typing.Optional[str] = None
    start_open: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="startOpen"), pydantic.Field(alias="startOpen")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GetDatasetsDatasetNameFacetsResponseItem_Range(UniversalBaseModel):
    type: typing.Literal["range"] = "range"
    property: typing.Optional[str] = None
    name: typing.Optional[str] = None
    min: typing.Optional[int] = None
    max: typing.Optional[int] = None
    step: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GetDatasetsDatasetNameFacetsResponseItem = typing_extensions.Annotated[
    typing.Union[GetDatasetsDatasetNameFacetsResponseItem_Text, GetDatasetsDatasetNameFacetsResponseItem_Range],
    pydantic.Field(discriminator="type"),
]
