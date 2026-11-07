

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash256 import Hash256
from .state_element import StateElement
from .v2file_contract import V2FileContract


class V2FileContractElement(UniversalBaseModel):
    id: Hash256
    state_element: typing_extensions.Annotated[
        StateElement, FieldMetadata(alias="stateElement"), pydantic.Field(alias="stateElement")
    ]
    v2file_contract: typing_extensions.Annotated[
        V2FileContract, FieldMetadata(alias="v2FileContract"), pydantic.Field(alias="v2FileContract")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
