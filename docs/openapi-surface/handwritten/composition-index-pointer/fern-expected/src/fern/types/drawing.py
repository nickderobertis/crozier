

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Drawing(UniversalBaseModel):
    name: typing.Optional[str] = None
    first_shape: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="firstShape"), pydantic.Field(alias="firstShape")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
