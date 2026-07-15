

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ListDescription(UniversalBaseModel):
    color_count: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="colorCount")] = None
    description: typing.Optional[str] = None
    key: typing.Optional[str] = None
    license: typing.Optional[str] = None
    source: typing.Optional[str] = None
    title: typing.Optional[str] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
