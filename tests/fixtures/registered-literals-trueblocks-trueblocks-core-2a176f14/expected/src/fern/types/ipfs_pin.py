

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class IpfsPin(UniversalBaseModel):
    """
    internal-use only data model detailing a single remote or local ipfs pinned file
    """

    cid: typing.Optional[str] = pydantic.Field(default=None)
    """
    the CID of the file
    """

    date_pinned: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="datePinned"),
        pydantic.Field(alias="datePinned", description="the date the CID was first created"),
    ] = None
    """
    the date the CID was first created
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    the status of the file (one of [all|pinned|unpinned|pending])
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    the size of the file in bytes
    """

    file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fileName"),
        pydantic.Field(alias="fileName", description="the metadata name of the pinned file"),
    ] = None
    """
    the metadata name of the pinned file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
