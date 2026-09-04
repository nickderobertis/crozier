

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostAuthorizationLinkTransactionRequestRequest(UniversalBaseModel):
    link_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="linkCode"),
        pydantic.Field(
            alias="linkCode", description="Link code as received by the wallet-app from the QR code scanning."
        ),
    ]
    """
    Link code as received by the wallet-app from the QR code scanning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
