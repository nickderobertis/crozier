

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_loan_voa24 import CreditFreddieMacLoanVoa24


class CreditFreddieMacLoansVoa24(UniversalBaseModel):
    """
    A collection of loans that are part of a single deal.
    """

    loan: typing_extensions.Annotated[
        CreditFreddieMacLoanVoa24, FieldMetadata(alias="LOAN"), pydantic.Field(alias="LOAN")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
