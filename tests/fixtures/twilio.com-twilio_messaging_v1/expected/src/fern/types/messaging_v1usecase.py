

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1Usecase(UniversalBaseModel):
    usecases: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Human readable use case details (usecase, description and purpose) of Messaging Service Use Cases.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
