

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InitialTable(UniversalBaseModel):
    csv_data: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="csvData"),
        pydantic.Field(alias="csvData", description="blobId of data"),
    ] = None
    """
    blobId of data
    """

    template_table_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateTableID"),
        pydantic.Field(alias="templateTableID", description="Template table API id"),
    ] = None
    """
    Template table API id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
