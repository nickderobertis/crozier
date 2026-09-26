

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetMerchantCredentialsResponse(UniversalBaseModel):
    api_key: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="apiKey"),
        pydantic.Field(alias="apiKey", description="TaxCloud API key currently associated with the merchant."),
    ]
    """
    TaxCloud API key currently associated with the merchant.
    """

    connection_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="connectionId"),
        pydantic.Field(
            alias="connectionId", description="TaxCloud connection ID currently associated with the merchant."
        ),
    ]
    """
    TaxCloud connection ID currently associated with the merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
