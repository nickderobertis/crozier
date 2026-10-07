

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .basedpyright_server_config import BasedpyrightServerConfig
from .pyrefly_language_server_config import PyreflyLanguageServerConfig
from .python_language_server_config import PythonLanguageServerConfig
from .ty_language_server_config import TyLanguageServerConfig


class LanguageServersConfig(UniversalBaseModel):
    """
    Configuration options for language servers.

        **Keys.**

        - `pylsp`: the pylsp config
        - `basedpyright`: the basedpyright config
        - `ty`: the ty config
        - `pyrefly`: the pyrefly config
    """

    basedpyright: typing.Optional[BasedpyrightServerConfig] = None
    pylsp: typing.Optional[PythonLanguageServerConfig] = None
    pyrefly: typing.Optional[PyreflyLanguageServerConfig] = None
    ty: typing.Optional[TyLanguageServerConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
