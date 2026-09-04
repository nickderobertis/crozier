

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostWalletBindingResponseResponse(UniversalBaseModel):
    wallet_user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="walletUserId"),
        pydantic.Field(
            alias="walletUserId",
            description="Unique identifier given to public-key and partner specific userId mapping.",
        ),
    ] = None
    """
    Unique identifier given to public-key and partner specific userId mapping.
    """

    certificate: typing.Optional[str] = pydantic.Field(default=None)
    """
    Key binder signed certificate.
    """

    expire_date_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expireDateTime"),
        pydantic.Field(alias="expireDateTime", description="Expire date time of the signed certificate."),
    ] = None
    """
    Expire date time of the signed certificate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
