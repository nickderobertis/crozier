

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ParseGetJobResponseError(UniversalBaseModel):
    """
    Present once the job has ``failed`` — the failure code + message.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stable error code.
    """

    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
