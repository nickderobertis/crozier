

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .satisfied_policy import SatisfiedPolicy
from .siacoin_element import SiacoinElement
from .siacoin_origin import SiacoinOrigin


class ConsensusV2SiacoinInput(UniversalBaseModel):
    """
    V2 siacoin input with origin information as returned by consensus block endpoints.
    """

    parent: SiacoinElement
    satisfied_policy: typing_extensions.Annotated[
        SatisfiedPolicy, FieldMetadata(alias="satisfiedPolicy"), pydantic.Field(alias="satisfiedPolicy")
    ]
    origin: SiacoinOrigin

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
