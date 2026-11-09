

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_verification_of_assets_voa24 import CreditFreddieMacVerificationOfAssetsVoa24
from .credit_freddie_verification_of_employment_voe25 import CreditFreddieVerificationOfEmploymentVoe25
from .request_id import RequestId


class CreditFreddieMacReportsGetResponse(UniversalBaseModel):
    """
    CreditFreddieMacReportsGetResponse defines the response schema for `/credit/freddie_mac/reports/get`
    """

    voa: typing_extensions.Annotated[
        typing.Optional[CreditFreddieMacVerificationOfAssetsVoa24],
        FieldMetadata(alias="VOA"),
        pydantic.Field(alias="VOA"),
    ] = None
    voe: typing_extensions.Annotated[
        typing.Optional[CreditFreddieVerificationOfEmploymentVoe25],
        FieldMetadata(alias="VOE"),
        pydantic.Field(alias="VOE"),
    ] = None
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
