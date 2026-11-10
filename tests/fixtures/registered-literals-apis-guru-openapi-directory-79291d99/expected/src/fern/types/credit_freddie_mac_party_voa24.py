

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_party_individual_voa24 import CreditFreddieMacPartyIndividualVoa24
from .roles import Roles
from .taxpayer_identifiers import TaxpayerIdentifiers


class CreditFreddieMacPartyVoa24(UniversalBaseModel):
    """
    A collection of information about a single party to a transaction. Included direct participants like the borrower and seller as well as indirect participants such as the flood certificate provider.
    """

    individual: typing_extensions.Annotated[
        CreditFreddieMacPartyIndividualVoa24, FieldMetadata(alias="INDIVIDUAL"), pydantic.Field(alias="INDIVIDUAL")
    ]
    roles: typing_extensions.Annotated[Roles, FieldMetadata(alias="ROLES"), pydantic.Field(alias="ROLES")]
    taxpayer_identifiers: typing_extensions.Annotated[
        TaxpayerIdentifiers, FieldMetadata(alias="TAXPAYER_IDENTIFIERS"), pydantic.Field(alias="TAXPAYER_IDENTIFIERS")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
