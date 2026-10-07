

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DiagnosticsConfig(UniversalBaseModel):
    """
    Configuration options for diagnostics.

        **Keys.**

        - `enabled`: if `True`, diagnostics will be shown in the editor
        - `sql_linter`: if `True`, SQL cells will have linting enabled
    """

    enabled: typing.Optional[bool] = None
    sql_linter: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
