

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class DocumentsImportFromRequestExpected(UniversalBaseModel):
    """
    Integrity pins, enforced when present. When absent, the server-observed values become authoritative.
    """

    size_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sizeBytes"),
        pydantic.Field(
            alias="sizeBytes", description="Checked against the source's declared Content-Length before the transfer."
        ),
    ] = None
    """
    Checked against the source's declared Content-Length before the transfer.
    """

    sha256: typing.Optional[str] = pydantic.Field(default=None)
    """
    Checked against the server-observed digest after the transfer. Required when dedupMode is reuse-existing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
