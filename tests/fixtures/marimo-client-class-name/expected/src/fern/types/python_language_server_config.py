

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PythonLanguageServerConfig(UniversalBaseModel):
    """
    Configuration options for Python Language Server.

    pylsp handles completion, hover, go-to-definition, and diagnostics.
    """

    enable_flake8: typing.Optional[bool] = None
    enable_mypy: typing.Optional[bool] = None
    enable_pydocstyle: typing.Optional[bool] = None
    enable_pyflakes: typing.Optional[bool] = None
    enable_pylint: typing.Optional[bool] = None
    enable_ruff: typing.Optional[bool] = None
    enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
