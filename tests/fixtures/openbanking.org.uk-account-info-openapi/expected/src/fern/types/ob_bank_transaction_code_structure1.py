

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ObBankTransactionCodeStructure1(UniversalBaseModel):
    """
    Set of elements used to fully identify the type of underlying transaction resulting in an entry.
    """

    code: typing_extensions.Annotated[str, FieldMetadata(alias="Code")] = pydantic.Field()
    """
    Specifies the family within a domain.
    """

    sub_code: typing_extensions.Annotated[str, FieldMetadata(alias="SubCode")] = pydantic.Field()
    """
    Specifies the sub-product family within a specific family.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
