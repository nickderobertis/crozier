

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .crm_field_details_type import CrmFieldDetailsType


class CrmFieldDetailsTypeRead(CrmFieldDetailsType):
    is_custom_field: typing_extensions.Annotated[
        bool, FieldMetadata(alias="isCustomField"), pydantic.Field(alias="isCustomField")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
