

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .preemption_capability import PreemptionCapability
from .preemption_vulnerability import PreemptionVulnerability


class Arp(UniversalBaseModel):
    priority_level: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="priorityLevel"), pydantic.Field(alias="priorityLevel")
    ] = None
    preempt_cap: typing_extensions.Annotated[
        PreemptionCapability, FieldMetadata(alias="preemptCap"), pydantic.Field(alias="preemptCap")
    ]
    preempt_vuln: typing_extensions.Annotated[
        PreemptionVulnerability, FieldMetadata(alias="preemptVuln"), pydantic.Field(alias="preemptVuln")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
