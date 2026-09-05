

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Oa2AuthorizationCodeSecret(UniversalBaseModel):
    auth_client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authClientId"),
        pydantic.Field(alias="authClientId", description="Id of the auth client this secret was created with"),
    ]
    """
    Id of the auth client this secret was created with
    """

    refresh_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="refreshToken"), pydantic.Field(alias="refreshToken")
    ] = None
    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    scope: typing.Optional[str] = None
    expires: dt.datetime = pydantic.Field()
    """
    Date object in UTC
    """

    external_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalId"), pydantic.Field(alias="externalId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
