

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CpsSummary(UniversalBaseModel):
    avail_cpu_slots: typing_extensions.Annotated[
        int, FieldMetadata(alias="availCpuSlots"), pydantic.Field(alias="availCpuSlots")
    ]
    avail_mem_slots: typing_extensions.Annotated[
        int, FieldMetadata(alias="availMemSlots"), pydantic.Field(alias="availMemSlots")
    ]
    avail_slots: typing_extensions.Annotated[int, FieldMetadata(alias="availSlots"), pydantic.Field(alias="availSlots")]
    name: str
    num_nodes: typing_extensions.Annotated[int, FieldMetadata(alias="numNodes"), pydantic.Field(alias="numNodes")]
    number_kgs: typing_extensions.Annotated[int, FieldMetadata(alias="numberKgs"), pydantic.Field(alias="numberKgs")]
    running_kgs: typing_extensions.Annotated[int, FieldMetadata(alias="runningKgs"), pydantic.Field(alias="runningKgs")]
    workers_pool: typing_extensions.Annotated[
        str, FieldMetadata(alias="workersPool"), pydantic.Field(alias="workersPool")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
