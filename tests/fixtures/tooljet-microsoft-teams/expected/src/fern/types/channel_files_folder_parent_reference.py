

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChannelFilesFolderParentReference(UniversalBaseModel):
    drive_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="driveId"), pydantic.Field(alias="driveId")
    ] = None
    drive_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="driveType"), pydantic.Field(alias="driveType")
    ] = None
    id: typing.Optional[str] = None
    path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
