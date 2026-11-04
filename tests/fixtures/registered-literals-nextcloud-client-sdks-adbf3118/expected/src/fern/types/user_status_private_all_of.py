

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserStatusPrivateAllOf(UniversalBaseModel):
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageId"), pydantic.Field(alias="messageId")
    ] = None
    message_is_predefined: typing_extensions.Annotated[
        bool, FieldMetadata(alias="messageIsPredefined"), pydantic.Field(alias="messageIsPredefined")
    ]
    status_is_user_defined: typing_extensions.Annotated[
        bool, FieldMetadata(alias="statusIsUserDefined"), pydantic.Field(alias="statusIsUserDefined")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
