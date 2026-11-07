

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash256 import Hash256


class StateElement(UniversalBaseModel):
    leaf_index: typing_extensions.Annotated[int, FieldMetadata(alias="leafIndex"), pydantic.Field(alias="leafIndex")]
    merkle_proof: typing_extensions.Annotated[
        typing.Optional[typing.List[Hash256]], FieldMetadata(alias="merkleProof"), pydantic.Field(alias="merkleProof")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
