

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccessTokenRequest(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId", description="Your Client ID obtainable by logging into your UniCourt account."
        ),
    ]
    """
    Your Client ID obtainable by logging into your UniCourt account.
    """

    client_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientSecret"),
        pydantic.Field(
            alias="clientSecret", description="Your Client Secret ID obtainable by logging into your UniCourt account."
        ),
    ]
    """
    Your Client Secret ID obtainable by logging into your UniCourt account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
