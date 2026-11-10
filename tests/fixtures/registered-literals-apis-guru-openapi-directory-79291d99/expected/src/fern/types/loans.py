

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .loan import Loan


class Loans(UniversalBaseModel):
    """
    A collection of loans that are part of a single deal.
    """

    loan: typing_extensions.Annotated[Loan, FieldMetadata(alias="LOAN"), pydantic.Field(alias="LOAN")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
