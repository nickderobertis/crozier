

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.auth_challenge import AuthChallenge


class PostWalletBindingRequestRequest(UniversalBaseModel):
    individual_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="individualId"), pydantic.Field(alias="individualId", description="User Id (UIN/VID).")
    ]
    """
    User Id (UIN/VID).
    """

    auth_factor_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authFactorType"),
        pydantic.Field(alias="authFactorType", description="Auth factor type to be binded for the provided key."),
    ]
    """
    Auth factor type to be binded for the provided key.
    """

    format: str = pydantic.Field()
    """
    Format of the auth factor type supported in the wallet app.This is not stored, this value is only validated to check if its a supported format in the keybinder implementation.
    """

    challenge_list: typing_extensions.Annotated[
        typing.List[AuthChallenge], FieldMetadata(alias="challengeList"), pydantic.Field(alias="challengeList")
    ]
    public_key: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="key to be binded in JWK format."),
    ]
    """
    key to be binded in JWK format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
