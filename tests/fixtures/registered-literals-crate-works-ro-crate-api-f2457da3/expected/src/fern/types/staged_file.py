

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .staged_file_status import StagedFileStatus


class StagedFile(UniversalBaseModel):
    """
    A file staged in a deposit, with its upload status.
    """

    file_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="fileId"),
        pydantic.Field(
            alias="fileId",
            description="The file entity's `@id` in the deposited metadata document. For attached files this is the crate-relative path.",
        ),
    ]
    """
    The file entity's `@id` in the deposited metadata document. For attached files this is the crate-relative path.
    """

    status: StagedFileStatus = pydantic.Field()
    """
    `pending` - staged in presigned mode and the bytes have not (yet) been observed; `received` - the bytes are held. Finalise remains the authoritative verification point.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The file's size in bytes, where declared or known.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
