

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AdditionalField(UniversalBaseModel):
    name: str
    value: str
    is_date: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDate"), pydantic.Field(alias="isDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
