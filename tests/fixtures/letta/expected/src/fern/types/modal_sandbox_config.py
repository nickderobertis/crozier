

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .modal_sandbox_config_language import ModalSandboxConfigLanguage


class ModalSandboxConfig(UniversalBaseModel):
    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time limit for the sandbox (in seconds).
    """

    pip_requirements: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of pip packages to install in the Modal sandbox
    """

    npm_requirements: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of npm packages to install in the Modal sandbox
    """

    language: typing.Optional[ModalSandboxConfigLanguage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
