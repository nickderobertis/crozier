

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_verification_of_employment_deal_voe25 import CreditFreddieVerificationOfEmploymentDealVoe25


class CreditFreddieVerificationOfEmploymentVoe25(UniversalBaseModel):
    """
    Verification of Employment Report
    """

    deal: typing_extensions.Annotated[
        CreditFreddieVerificationOfEmploymentDealVoe25, FieldMetadata(alias="DEAL"), pydantic.Field(alias="DEAL")
    ]
    schema_version: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="SchemaVersion"),
        pydantic.Field(alias="SchemaVersion", description="The Verification Of Employment (VOE) schema version."),
    ]
    """
    The Verification Of Employment (VOE) schema version.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
