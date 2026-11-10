

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .credit_freddie_mac_loan_identifiers_voa24 import CreditFreddieMacLoanIdentifiersVoa24


class CreditFreddieMacLoanVoa24(UniversalBaseModel):
    """
    Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender.
    """

    loan_identifiers: typing_extensions.Annotated[
        CreditFreddieMacLoanIdentifiersVoa24,
        FieldMetadata(alias="LOAN_IDENTIFIERS"),
        pydantic.Field(alias="LOAN_IDENTIFIERS"),
    ]
    loan_role_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LoanRoleType"),
        pydantic.Field(alias="LoanRoleType", description='Type of loan. The value can only be "SubjectLoan"'),
    ]
    """
    Type of loan. The value can only be "SubjectLoan"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
