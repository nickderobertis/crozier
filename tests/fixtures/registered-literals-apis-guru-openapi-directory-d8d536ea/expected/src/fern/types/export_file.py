

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExportFile(UniversalBaseModel):
    expiry_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiryDate"),
        pydantic.Field(alias="expiryDate", description="Expiry date-time for the fileUrl provided in this object."),
    ]
    """
    Expiry date-time for the fileUrl provided in this object.
    """

    file_url: typing_extensions.Annotated[
        str, FieldMetadata(alias="fileUrl"), pydantic.Field(alias="fileUrl", description="Link to download the file.")
    ]
    """
    Link to download the file.
    """

    name: str = pydantic.Field()
    """
    Name of the file.
    """

    object: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
