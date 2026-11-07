

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InternalUserModel(UniversalBaseModel):
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    email: str
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]
    company_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
