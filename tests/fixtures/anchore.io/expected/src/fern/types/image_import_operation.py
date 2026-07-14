

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .image_import_operation_status import ImageImportOperationStatus


class ImageImportOperation(UniversalBaseModel):
    """
    An import record, creating a unique identifier for referencing the operation as well as its state
    """

    created_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    status: typing.Optional[ImageImportOperationStatus] = None
    uuid_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uuid")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
