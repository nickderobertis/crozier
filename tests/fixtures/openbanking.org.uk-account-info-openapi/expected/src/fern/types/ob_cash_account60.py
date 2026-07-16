

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identification0 import Identification0
from .name0 import Name0
from .ob_external_account_identification4code import ObExternalAccountIdentification4Code
from .secondary_identification import SecondaryIdentification


class ObCashAccount60(UniversalBaseModel):
    """
    Unambiguous identification of the account of the creditor, in the case of a debit transaction.
    """

    identification: typing_extensions.Annotated[
        typing.Optional[Identification0], FieldMetadata(alias="Identification")
    ] = None
    name: typing_extensions.Annotated[typing.Optional[Name0], FieldMetadata(alias="Name")] = None
    scheme_name: typing_extensions.Annotated[
        typing.Optional[ObExternalAccountIdentification4Code], FieldMetadata(alias="SchemeName")
    ] = None
    secondary_identification: typing_extensions.Annotated[
        typing.Optional[SecondaryIdentification], FieldMetadata(alias="SecondaryIdentification")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
