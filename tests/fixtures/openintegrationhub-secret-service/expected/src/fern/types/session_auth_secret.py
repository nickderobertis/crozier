

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SessionAuthSecret(UniversalBaseModel):
    auth_client_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="authClientId"), pydantic.Field(alias="authClientId")
    ]
    access_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ] = None
    input_fields: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="inputFields"), pydantic.Field(alias="inputFields")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
