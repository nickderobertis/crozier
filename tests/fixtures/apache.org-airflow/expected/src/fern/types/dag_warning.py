

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DagWarning(UniversalBaseModel):
    dag_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The dag_id.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    The message for the dag warning.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when this warning was logged.
    """

    warning_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The warning type for the dag warning.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
