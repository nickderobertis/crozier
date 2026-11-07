

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .satisfied_policy import SatisfiedPolicy
from .siacoin_element import SiacoinElement


class V2SiacoinInput(UniversalBaseModel):
    parent: SiacoinElement
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
