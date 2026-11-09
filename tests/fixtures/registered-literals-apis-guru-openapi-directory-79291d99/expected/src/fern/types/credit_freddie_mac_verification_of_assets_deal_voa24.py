

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_loans_voa24 import CreditFreddieMacLoansVoa24
from .credit_freddie_mac_parties_voa24 import CreditFreddieMacPartiesVoa24
from .credit_freddie_mac_services_voa24 import CreditFreddieMacServicesVoa24


class CreditFreddieMacVerificationOfAssetsDealVoa24(UniversalBaseModel):
    """
    An object representing an Asset Report with Freddie Mac schema.
    """

    loans: typing_extensions.Annotated[
        CreditFreddieMacLoansVoa24, FieldMetadata(alias="LOANS"), pydantic.Field(alias="LOANS")
    ]
    parties: typing_extensions.Annotated[
        CreditFreddieMacPartiesVoa24, FieldMetadata(alias="PARTIES"), pydantic.Field(alias="PARTIES")
    ]
    services: typing_extensions.Annotated[
        CreditFreddieMacServicesVoa24, FieldMetadata(alias="SERVICES"), pydantic.Field(alias="SERVICES")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
