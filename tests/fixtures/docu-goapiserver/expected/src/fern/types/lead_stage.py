

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LeadStage(UniversalBaseModel):
    """
    Lead Stage.
    """

    stage: str = pydantic.Field()
    """
    Stage name. The GET response can include source-specific stage names; PATCH accepts only its six documented stage properties.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source stage state as a string or null, rather than the boolean used by PATCH.
    """

    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
