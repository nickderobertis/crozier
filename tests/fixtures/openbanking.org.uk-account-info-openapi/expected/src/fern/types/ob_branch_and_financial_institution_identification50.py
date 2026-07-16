

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification1 import Identification1
from .ob_external_financial_institution_identification4code import ObExternalFinancialInstitutionIdentification4Code


class ObBranchAndFinancialInstitutionIdentification50(UniversalBaseModel):
    """
    Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.
    """

    identification: typing_extensions.Annotated[
        Identification1, FieldMetadata(alias="Identification"), pydantic.Field(alias="Identification")
    ]
    scheme_name: typing_extensions.Annotated[
        ObExternalFinancialInstitutionIdentification4Code,
        FieldMetadata(alias="SchemeName"),
        pydantic.Field(alias="SchemeName"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
