

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .loan_identifier_type import LoanIdentifierType


class LoanIdentifier(UniversalBaseModel):
    """
    The information used to identify this loan by various parties to the transaction or other organizations.
    """

    loan_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LoanIdentifier"),
        pydantic.Field(alias="LoanIdentifier", description="The value of the identifier for the specified type."),
    ] = None
    """
    The value of the identifier for the specified type.
    """

    loan_identifier_type: typing_extensions.Annotated[
        typing.Optional[LoanIdentifierType],
        FieldMetadata(alias="LoanIdentifierType"),
        pydantic.Field(alias="LoanIdentifierType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
