

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AuthorizationCodesSharedModelsAuthorizationCodeUser(UniversalBaseModel):
    email: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Email"), pydantic.Field(alias="Email")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Name"), pydantic.Field(alias="Name")
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="UserID"), pydantic.Field(alias="UserID")
    ] = None
    username: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Username"), pydantic.Field(alias="Username")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
