

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepDeltaStepDetailsToolCallsFunctionObjectFunction(UniversalBaseModel):
    """
    The definition of the function that was called.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the function.
    """

    arguments: typing.Optional[str] = pydantic.Field(default=None)
    """
    The arguments passed to the function.
    """

    output: typing.Optional[str] = pydantic.Field(default=None)
    """
    The output of the function. This will be `null` if the outputs have not been [submitted](/docs/api-reference/runs/submitToolOutputs) yet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
