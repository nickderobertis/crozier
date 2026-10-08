

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BasedpyrightServerConfig(UniversalBaseModel):
    """
    Configuration options for basedpyright Language Server.

    basedpyright handles completion, hover, go-to-definition, and diagnostics,
    but we only use it for diagnostics.
    """

    enabled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
