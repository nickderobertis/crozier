

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_access import FileAccess
from .id import Id


class File(UniversalBaseModel):
    """
    A file with file-specific metadata. For files that are also represented as MediaObject entities in the RO-Crate, the file `id` and the MediaObject entity `id` are identical.
    """

    id: Id = pydantic.Field()
    """
    RO-Crate ID that uniquely identifies this file.
    """

    filename: str = pydantic.Field()
    """
    The name of the file.
    """

    media_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="mediaType"),
        pydantic.Field(alias="mediaType", description="The MIME type of the file."),
    ]
    """
    The MIME type of the file.
    """

    size: int = pydantic.Field()
    """
    The size of the file in bytes.
    """

    access: FileAccess = pydantic.Field()
    """
    Access information for this file, including content permissions and enrolment details.
    """

    ro_crate_id: typing_extensions.Annotated[
        typing.Optional[Id],
        FieldMetadata(alias="roCrateId"),
        pydantic.Field(
            alias="roCrateId",
            description="Optional core — present only when `deposit.supported` is `true`.\n\nThe RO-Crate whose deposit supplied this file's bytes. Singular, because a file's bytes arrive in exactly one deposit. May be absent for files predating any RO-Crate, or where the implementation withholds it.",
        ),
    ] = None
    """
    Optional core — present only when `deposit.supported` is `true`.
    
    The RO-Crate whose deposit supplied this file's bytes. Singular, because a file's bytes arrive in exactly one deposit. May be absent for files predating any RO-Crate, or where the implementation withholds it.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
