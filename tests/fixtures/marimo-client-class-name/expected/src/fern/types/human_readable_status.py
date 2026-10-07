

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .human_readable_status_code import HumanReadableStatusCode


class HumanReadableStatus(UniversalBaseModel):
    """
    Human-readable status for operation results.

        Attributes:
            code: Status code ("ok" or "error").
            title: Optional short title.
            message: Optional detailed description.
    """

    code: HumanReadableStatusCode
    message: typing.Optional[str] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
