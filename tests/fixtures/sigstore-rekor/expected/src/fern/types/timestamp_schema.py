

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .timestamp_schema_tsr import TimestampSchemaTsr


class TimestampSchema(UniversalBaseModel):
    """
    Schema for RFC3161 entries
    """

    tsr: TimestampSchemaTsr = pydantic.Field()
    """
    Information about the tsr file associated with the entry
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
