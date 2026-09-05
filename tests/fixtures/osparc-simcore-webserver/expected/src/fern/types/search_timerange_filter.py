

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SearchTimerangeFilter(UniversalBaseModel):
    from_: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Filter results before this date"),
    ] = None
    """
    Filter results before this date
    """

    until: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Filter results after this date
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
