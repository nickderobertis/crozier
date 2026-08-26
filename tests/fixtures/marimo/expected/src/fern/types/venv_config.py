

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VenvConfig(UniversalBaseModel):
    """
    Configuration for external Python environment in home sandbox mode.

        Allows specifying an existing virtualenv to use instead of creating
        ephemeral sandboxes per notebook. Only applies in home sandbox mode.

        **Keys.**

        - `path`: path to a virtualenv directory (absolute or relative to
          pyproject.toml)
        - `writable`: if true, marimo will manage script metadata (inline
          dependencies). Defaults to false.
    """

    path: typing.Optional[str] = None
    writable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
