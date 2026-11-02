

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Firing(UniversalBaseModel):
    id: typing.Optional[str] = None
    peak_celsius: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="peakCelsius"), pydantic.Field(alias="peakCelsius")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
