

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CompanyContactItem(UniversalBaseModel):
    contact_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactType"), pydantic.Field(alias="contactType")
    ]
    contact_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="contactValue"), pydantic.Field(alias="contactValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
