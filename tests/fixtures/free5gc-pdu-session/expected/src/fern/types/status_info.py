

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cause import Cause
from .resource_status import ResourceStatus


class StatusInfo(UniversalBaseModel):
    resource_status: typing_extensions.Annotated[
        ResourceStatus, FieldMetadata(alias="resourceStatus"), pydantic.Field(alias="resourceStatus")
    ]
    cause: typing.Optional[Cause] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
