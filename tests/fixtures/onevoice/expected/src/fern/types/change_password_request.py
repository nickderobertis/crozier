

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChangePasswordRequest(UniversalBaseModel):
    current_password: typing_extensions.Annotated[
        str, FieldMetadata(alias="currentPassword"), pydantic.Field(alias="currentPassword")
    ]
    new_password: typing_extensions.Annotated[
        str, FieldMetadata(alias="newPassword"), pydantic.Field(alias="newPassword")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
