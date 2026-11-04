

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .context_parameter_value import ContextParameterValue


class ContextParameter(UniversalBaseModel):
    key: str
    description: typing.Optional[str] = None
    source: "ContextParameterSource"
    value: typing.Optional[ContextParameterValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .context_parameter_source import ContextParameterSource

update_forward_refs(ContextParameter, ContextParameterSource=ContextParameterSource)
