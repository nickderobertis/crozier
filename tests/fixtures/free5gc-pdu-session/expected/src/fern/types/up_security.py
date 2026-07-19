

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .up_confidentiality import UpConfidentiality
from .up_integrity import UpIntegrity


class UpSecurity(UniversalBaseModel):
    up_integr: typing_extensions.Annotated[
        UpIntegrity, FieldMetadata(alias="upIntegr"), pydantic.Field(alias="upIntegr")
    ]
    up_confid: typing_extensions.Annotated[
        UpConfidentiality, FieldMetadata(alias="upConfid"), pydantic.Field(alias="upConfid")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
