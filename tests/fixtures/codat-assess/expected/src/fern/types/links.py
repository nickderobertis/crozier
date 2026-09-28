

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hal_ref import HalRef


class Links(UniversalBaseModel):
    current: HalRef
    next: typing.Optional[HalRef] = None
    previous: typing.Optional[HalRef] = None
    self_: typing_extensions.Annotated[HalRef, FieldMetadata(alias="self"), pydantic.Field(alias="self")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
