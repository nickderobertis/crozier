

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ValidateAction(UniversalBaseModel):
    """
    Validate action parameters.
    """

    prompt: str = pydantic.Field()
    """
    Validation criteria or condition to check
    """

    model: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional model configuration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
