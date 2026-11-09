

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BarSourceDataName(UniversalBaseModel):
    first_name: typing_extensions.Annotated[str, FieldMetadata(alias="firstName"), pydantic.Field(alias="firstName")]
    last_name: typing_extensions.Annotated[str, FieldMetadata(alias="lastName"), pydantic.Field(alias="lastName")]
    middle_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="middleName"), pydantic.Field(alias="middleName")
    ] = None
    name: str
    prefix: typing.Optional[str] = None
    suffix: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
