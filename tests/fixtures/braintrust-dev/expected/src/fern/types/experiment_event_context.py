

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExperimentEventContext(UniversalBaseModel):
    """
    Context is additional information about the code that produced the experiment event. It is essentially the textual counterpart to `metrics`. Use the `caller_*` attributes to track the location in code which produced the experiment event
    """

    caller_functionname: typing.Optional[str] = pydantic.Field(default=None)
    """
    The function in code which created the experiment event
    """

    caller_filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the file in code where the experiment event was created
    """

    caller_lineno: typing.Optional[int] = pydantic.Field(default=None)
    """
    Line of code where the experiment event was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
