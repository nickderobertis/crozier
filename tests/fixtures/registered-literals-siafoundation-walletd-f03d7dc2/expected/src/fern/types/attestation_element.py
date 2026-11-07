

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attestation import Attestation
from .hash256 import Hash256
from .state_element import StateElement


class AttestationElement(UniversalBaseModel):
    id: Hash256
    state_element: typing_extensions.Annotated[
        StateElement, FieldMetadata(alias="stateElement"), pydantic.Field(alias="stateElement")
    ]
    attestation: Attestation

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
