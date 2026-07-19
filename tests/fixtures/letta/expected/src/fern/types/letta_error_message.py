

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LettaErrorMessage(UniversalBaseModel):
    """
    Error messages are used to notify the client of an error that occurred during the agent's execution.
    """

    run_id: str = pydantic.Field()
    """
    The ID of the run.
    """

    error_type: str = pydantic.Field()
    """
    The type of error.
    """

    message: str = pydantic.Field()
    """
    The error message.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional error detail.
    """

    seq_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The sequence ID for cursor-based pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
