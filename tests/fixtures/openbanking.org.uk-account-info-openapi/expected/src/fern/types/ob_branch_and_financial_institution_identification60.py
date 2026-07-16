

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification1 import Identification1
from .name1 import Name1
from .ob_external_financial_institution_identification4code import ObExternalFinancialInstitutionIdentification4Code
from .ob_postal_address6 import ObPostalAddress6


class ObBranchAndFinancialInstitutionIdentification60(UniversalBaseModel):
    """
    Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.
    This is the servicer of the beneficiary account.
    """

    identification: typing_extensions.Annotated[
        typing.Optional[Identification1], FieldMetadata(alias="Identification"), pydantic.Field(alias="Identification")
    ] = None
    name: typing_extensions.Annotated[
        typing.Optional[Name1], FieldMetadata(alias="Name"), pydantic.Field(alias="Name")
    ] = None
    postal_address: typing_extensions.Annotated[
        typing.Optional[ObPostalAddress6], FieldMetadata(alias="PostalAddress"), pydantic.Field(alias="PostalAddress")
    ] = None
    scheme_name: typing_extensions.Annotated[
        typing.Optional[ObExternalFinancialInstitutionIdentification4Code],
        FieldMetadata(alias="SchemeName"),
        pydantic.Field(alias="SchemeName"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
