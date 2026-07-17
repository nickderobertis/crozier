

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_id import ResourceId
from .upload_read_status import UploadReadStatus


class UploadRead(UniversalBaseModel):
    resource_id: typing_extensions.Annotated[
        typing.Optional[ResourceId], FieldMetadata(alias="resourceId"), pydantic.Field(alias="resourceId")
    ] = None
    status: UploadReadStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
