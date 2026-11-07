

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency
from .hash256 import Hash256
from .siafund_output import SiafundOutput
from .state_element import StateElement


class SiafundElement(UniversalBaseModel):
    id: Hash256
    state_element: typing_extensions.Annotated[
        StateElement, FieldMetadata(alias="stateElement"), pydantic.Field(alias="stateElement")
    ]
    siafund_output: typing_extensions.Annotated[
        SiafundOutput, FieldMetadata(alias="siafundOutput"), pydantic.Field(alias="siafundOutput")
    ]
    claim_start: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="claimStart"), pydantic.Field(alias="claimStart")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
