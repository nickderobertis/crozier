

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ContentContentRepresentation(UniversalBaseModel):
    name: typing.Optional[str] = None
    path: typing.Optional[str] = None
    validation_string: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="validationString"), pydantic.Field(alias="validationString")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
