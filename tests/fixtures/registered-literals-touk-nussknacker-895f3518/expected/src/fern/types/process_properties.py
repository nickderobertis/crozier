

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .process_additional_fields import ProcessAdditionalFields


class ProcessProperties(UniversalBaseModel):
    additional_fields: typing_extensions.Annotated[
        ProcessAdditionalFields, FieldMetadata(alias="additionalFields"), pydantic.Field(alias="additionalFields")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
