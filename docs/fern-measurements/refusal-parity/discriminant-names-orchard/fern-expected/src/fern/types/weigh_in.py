

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WeighIn(UniversalBaseModel):
    grams: typing.Optional[int] = None
    scale_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="scaleId"), pydantic.Field(alias="scaleId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
