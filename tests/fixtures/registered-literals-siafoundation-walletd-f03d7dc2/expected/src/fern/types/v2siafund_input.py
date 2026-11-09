

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .satisfied_policy import SatisfiedPolicy
from .siafund_element import SiafundElement


class V2SiafundInput(UniversalBaseModel):
    parent: SiafundElement
    claim_address: typing_extensions.Annotated[
        Address, FieldMetadata(alias="claimAddress"), pydantic.Field(alias="claimAddress")
    ]
    satisfied_policy: typing_extensions.Annotated[
        SatisfiedPolicy, FieldMetadata(alias="satisfiedPolicy"), pydantic.Field(alias="satisfiedPolicy")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
