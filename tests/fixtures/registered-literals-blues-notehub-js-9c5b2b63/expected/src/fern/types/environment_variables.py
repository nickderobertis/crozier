

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnvironmentVariables(UniversalBaseModel):
    environment_variable_notes: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.
    """

    environment_variables: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
