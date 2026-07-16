

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class CreateMultipartUploadRequestMetadata(UniversalBaseModel):
    sha1checksum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sha1-checksum"),
        pydantic.Field(
            alias="sha1-checksum",
            description="The SHA1 checksum of the upload binary blob. Optionally\nbe provided and serves as an additional security check when\nlater processing the file in complete-external-upload endpoint.",
        ),
    ] = None
    """
    The SHA1 checksum of the upload binary blob. Optionally
    be provided and serves as an additional security check when
    later processing the file in complete-external-upload endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
