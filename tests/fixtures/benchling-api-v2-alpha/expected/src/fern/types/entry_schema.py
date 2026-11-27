

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class EntrySchema(UniversalBaseModel):
    """
    Entry schema
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the entry schema
    """

    modified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="modifiedAt"),
        pydantic.Field(alias="modifiedAt", description="DateTime the Entry Schema was last modified"),
    ] = None
    """
    DateTime the Entry Schema was last modified
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the entry schema
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
