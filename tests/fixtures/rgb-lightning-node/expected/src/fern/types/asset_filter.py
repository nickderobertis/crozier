

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AssetFilter_AnyOrNone(UniversalBaseModel):
    type: typing.Literal["AnyOrNone"] = "AnyOrNone"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssetFilter_None(UniversalBaseModel):
    type: typing.Literal["None"] = "None"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AssetFilter_Id(UniversalBaseModel):
    type: typing.Literal["Id"] = "Id"
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AssetFilter = typing_extensions.Annotated[
    typing.Union[AssetFilter_AnyOrNone, AssetFilter_None, AssetFilter_Id], pydantic.Field(discriminator="type")
]
