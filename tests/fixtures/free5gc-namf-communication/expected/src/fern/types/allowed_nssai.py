

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .allowed_snssai import AllowedSnssai


class AllowedNssai(UniversalBaseModel):
    allowed_snssai_list: typing_extensions.Annotated[
        typing.List[AllowedSnssai], FieldMetadata(alias="allowedSnssaiList"), pydantic.Field(alias="allowedSnssaiList")
    ]
    access_type: typing_extensions.Annotated[
        AccessType, FieldMetadata(alias="accessType"), pydantic.Field(alias="accessType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
