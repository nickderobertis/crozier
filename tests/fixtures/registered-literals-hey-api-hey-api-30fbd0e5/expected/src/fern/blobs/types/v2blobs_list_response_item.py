

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class V2BlobsListResponseItem(UniversalBaseModel):
    key: str
    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size in bytes of the object
    """

    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastModified"),
        pydantic.Field(alias="lastModified", description="Creation date of the object"),
    ] = None
    """
    Creation date of the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
