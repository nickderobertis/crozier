

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CapabilityOwningAi(UniversalBaseModel):
    ai_id: typing_extensions.Annotated[str, FieldMetadata(alias="aiId"), pydantic.Field(alias="aiId")]
    name: str
    profile_handle: typing_extensions.Annotated[
        str, FieldMetadata(alias="profileHandle"), pydantic.Field(alias="profileHandle")
    ]
    handle: typing.Optional[str] = None
    avatar_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarUrl"), pydantic.Field(alias="avatarUrl")
    ] = None
    verified: bool
    classification: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
