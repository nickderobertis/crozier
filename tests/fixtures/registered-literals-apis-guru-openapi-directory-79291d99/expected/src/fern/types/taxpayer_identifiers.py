

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .taxpayer_identifier import TaxpayerIdentifier


class TaxpayerIdentifiers(UniversalBaseModel):
    """
    The collection of TAXPAYER_IDENTIFICATION elements
    """

    taxpayer_identifier: typing_extensions.Annotated[
        TaxpayerIdentifier, FieldMetadata(alias="TAXPAYER_IDENTIFIER"), pydantic.Field(alias="TAXPAYER_IDENTIFIER")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
