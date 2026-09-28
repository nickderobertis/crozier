

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2workspace_file_table_import import V2WorkspaceFileTableImport


class V2CreateTableImportDataOne(UniversalBaseModel):
    session: V2WorkspaceFileTableImport = pydantic.Field()
    """
    Created workspace-file import session.
    """

    upload_token: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="uploadToken"),
        pydantic.Field(
            alias="uploadToken", description="Always null; a workspace-file import has no upload to authorize."
        ),
    ] = None
    """
    Always null; a workspace-file import has no upload to authorize.
    """

    transfer: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Always null; a workspace-file import has no bytes to transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
