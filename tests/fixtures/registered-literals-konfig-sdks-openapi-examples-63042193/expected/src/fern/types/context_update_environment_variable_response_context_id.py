

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContextUpdateEnvironmentVariableResponseContextId(UniversalBaseModel):
    variable: str = pydantic.Field()
    """
    The name of the environment variable
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The date and time the environment variable was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The date and time the environment variable was updated
    """

    context_id: str = pydantic.Field()
    """
    ID of the context (UUID)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
