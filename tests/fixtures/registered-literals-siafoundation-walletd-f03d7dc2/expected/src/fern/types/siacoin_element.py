

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash256 import Hash256
from .siacoin_output import SiacoinOutput
from .state_element import StateElement


class SiacoinElement(UniversalBaseModel):
    id: Hash256
    state_element: typing_extensions.Annotated[
        StateElement, FieldMetadata(alias="stateElement"), pydantic.Field(alias="stateElement")
    ]
    siacoin_output: typing_extensions.Annotated[
        SiacoinOutput, FieldMetadata(alias="siacoinOutput"), pydantic.Field(alias="siacoinOutput")
    ]
    maturity_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="maturityHeight"), pydantic.Field(alias="maturityHeight")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
