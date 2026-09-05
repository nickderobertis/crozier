

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Oa1ThreeLeggedSecret(UniversalBaseModel):
    auth_client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authClientId"),
        pydantic.Field(alias="authClientId", description="Id of the auth client this secret was created with"),
    ]
    """
    Id of the auth client this secret was created with
    """

    access_token: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessToken"), pydantic.Field(alias="accessToken")
    ]
    access_token_secret: typing_extensions.Annotated[
        str, FieldMetadata(alias="accessTokenSecret"), pydantic.Field(alias="accessTokenSecret")
    ]
    scope: typing.Optional[str] = None
    expires: typing.Optional[str] = None
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
