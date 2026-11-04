

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deduplicated_ref_container_inner import DeduplicatedRefContainerInner


class DeduplicatedRefContainer(UniversalBaseModel):
    inner: typing.Optional[DeduplicatedRefContainerInner] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
