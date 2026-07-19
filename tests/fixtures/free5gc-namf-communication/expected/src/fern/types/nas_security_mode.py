

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ciphering_algorithm import CipheringAlgorithm
from .integrity_algorithm import IntegrityAlgorithm


class NasSecurityMode(UniversalBaseModel):
    integrity_algorithm: typing_extensions.Annotated[
        IntegrityAlgorithm, FieldMetadata(alias="integrityAlgorithm"), pydantic.Field(alias="integrityAlgorithm")
    ]
    ciphering_algorithm: typing_extensions.Annotated[
        CipheringAlgorithm, FieldMetadata(alias="cipheringAlgorithm"), pydantic.Field(alias="cipheringAlgorithm")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
