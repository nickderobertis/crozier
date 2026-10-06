

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role import Role
from .timestamp import Timestamp
from .timestamp_iso import TimestampIso


class ObjectData(UniversalBaseModel):
    """
    Result data for a timestamp in object format.
    """

    timestamp: Timestamp
    timestamp_iso: typing.Optional[TimestampIso] = None
    role: typing.Optional[Role] = None
    resource: typing.Optional[str] = pydantic.Field(default=None)
    """
    Series resource id, if applicable for all values.
    """

    metric: typing.Optional[str] = pydantic.Field(default=None)
    """
    Series metric, if applicable for all values.
    """

    aggregation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Series aggregation, if applicable for all values.
    """

    levels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Attribute level names used to key the values for this observation.
    
    Levels that are flattened have a dot-separated key.
    
    If all observations have the same attribute for a level, that level might be omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
