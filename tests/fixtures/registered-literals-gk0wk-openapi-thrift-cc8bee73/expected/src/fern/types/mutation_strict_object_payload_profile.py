

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mutation_strict_object_payload_profile_source import MutationStrictObjectPayloadProfileSource


class MutationStrictObjectPayloadProfile(UniversalBaseModel):
    source: MutationStrictObjectPayloadProfileSource
    region: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
