

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class JobPhase(UniversalBaseModel):
    id: float
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    description: str
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    title: str
    status: str
    assigned_groups: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="assignedGroups"), pydantic.Field(alias="assignedGroups")
    ]
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
