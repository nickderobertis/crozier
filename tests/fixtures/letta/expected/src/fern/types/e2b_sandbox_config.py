

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class E2BSandboxConfig(UniversalBaseModel):
    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time limit for the sandbox (in seconds).
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    The E2B template id (docker image).
    """

    pip_requirements: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of pip packages to install on the E2B Sandbox
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
