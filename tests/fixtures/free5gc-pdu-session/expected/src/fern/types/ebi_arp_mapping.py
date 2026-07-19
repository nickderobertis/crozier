

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .arp import Arp


class EbiArpMapping(UniversalBaseModel):
    eps_bearer_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="epsBearerId"), pydantic.Field(alias="epsBearerId")
    ]
    arp: Arp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
