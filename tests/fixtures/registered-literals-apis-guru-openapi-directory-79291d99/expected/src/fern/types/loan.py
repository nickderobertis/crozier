

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .loan_identifiers import LoanIdentifiers


class Loan(UniversalBaseModel):
    """
    Information specific to a mortgage loan agreement between one or more borrowers and a mortgage lender.
    """

    loan_identifiers: typing_extensions.Annotated[
        LoanIdentifiers, FieldMetadata(alias="LOAN_IDENTIFIERS"), pydantic.Field(alias="LOAN_IDENTIFIERS")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
