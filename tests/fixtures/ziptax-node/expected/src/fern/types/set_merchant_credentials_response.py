

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SetMerchantCredentialsResponse(UniversalBaseModel):
    merchant_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="merchantId"),
        pydantic.Field(alias="merchantId", description="UUID of the merchant whose credentials were set."),
    ]
    """
    UUID of the merchant whose credentials were set.
    """

    message: str = pydantic.Field()
    """
    Human-readable description of the result.
    """

    status: str = pydantic.Field()
    """
    Result status of the operation (e.g. 'success').
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
