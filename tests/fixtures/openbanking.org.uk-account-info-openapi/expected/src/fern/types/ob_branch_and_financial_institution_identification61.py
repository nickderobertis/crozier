

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification2 import Identification2
from .name1 import Name1
from .ob_external_financial_institution_identification4code import ObExternalFinancialInstitutionIdentification4Code
from .ob_postal_address6 import ObPostalAddress6


class ObBranchAndFinancialInstitutionIdentification61(UniversalBaseModel):
    """
    Financial institution servicing an account for the creditor.
    """

    identification: typing_extensions.Annotated[
        typing.Optional[Identification2], FieldMetadata(alias="Identification")
    ] = None
    name: typing_extensions.Annotated[typing.Optional[Name1], FieldMetadata(alias="Name")] = None
    postal_address: typing_extensions.Annotated[
        typing.Optional[ObPostalAddress6], FieldMetadata(alias="PostalAddress")
    ] = None
    scheme_name: typing_extensions.Annotated[
        typing.Optional[ObExternalFinancialInstitutionIdentification4Code], FieldMetadata(alias="SchemeName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
