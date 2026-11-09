

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .env_var import EnvVar


class EnvTreeJsonNode(UniversalBaseModel):
    app_label: typing.Optional[str] = None
    app_uid: typing.Optional[str] = None
    children: typing.List["EnvTreeJsonNode"]
    device_uid: typing.Optional[str] = None
    fleet_label: typing.Optional[str] = None
    fleet_uid: typing.Optional[str] = None
    inherited_var_count: int
    type: str
    url: typing.Optional[str] = None
    var_count: int
    variables: typing.List[EnvVar]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EnvTreeJsonNode)
