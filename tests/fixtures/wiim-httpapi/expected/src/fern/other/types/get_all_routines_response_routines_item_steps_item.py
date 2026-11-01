

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAllRoutinesResponseRoutinesItemStepsItem(UniversalBaseModel):
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of the step
    """

    payload: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Payload for the step
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
