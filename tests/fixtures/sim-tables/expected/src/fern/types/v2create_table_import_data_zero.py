

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2create_table_import_data_zero_transfer import V2CreateTableImportDataZeroTransfer
from .v2upload_backed_table_import import V2UploadBackedTableImport


class V2CreateTableImportDataZero(UniversalBaseModel):
    session: V2UploadBackedTableImport = pydantic.Field()
    """
    Created upload-backed import session.
    """

    upload_token: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="uploadToken"),
        pydantic.Field(alias="uploadToken", description="Signed token for upload control requests."),
    ]
    """
    Signed token for upload control requests.
    """

    transfer: V2CreateTableImportDataZeroTransfer = pydantic.Field()
    """
    Signed CSV upload instructions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
