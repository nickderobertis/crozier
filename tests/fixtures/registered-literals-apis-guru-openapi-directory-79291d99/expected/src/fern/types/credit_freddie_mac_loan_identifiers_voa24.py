

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .loan_identifier import LoanIdentifier


class CreditFreddieMacLoanIdentifiersVoa24(UniversalBaseModel):
    """
    Collection of current and previous identifiers for this loan.
    """

    loan_identifier: typing_extensions.Annotated[
        typing.List[LoanIdentifier], FieldMetadata(alias="LOAN_IDENTIFIER"), pydantic.Field(alias="LOAN_IDENTIFIER")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
