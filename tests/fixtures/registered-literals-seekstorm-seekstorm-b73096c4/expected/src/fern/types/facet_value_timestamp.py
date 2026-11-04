

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FacetValueTimestamp(UniversalBaseModel):
    """
    Unix timestamp: the number of seconds since 1 January 1970
    """

    timestamp: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(alias="Timestamp", description="Unix timestamp: the number of seconds since 1 January 1970"),
    ]
    """
    Unix timestamp: the number of seconds since 1 January 1970
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
