

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12(UniversalBaseModel):
    id: str
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None
    last_active_at: typing.Optional[dt.datetime] = None
    created_by: str
    provider_id: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
    information about the object in a structured format, and querying for objects via API or the dashboard.
    
    Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
    512 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
