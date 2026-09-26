

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1state_permissions_item import V1StatePermissionsItem


class V1State(UniversalBaseModel):
    id: int
    name: str
    icon: typing.Optional[str] = None
    color: str
    billed: bool
    locked: bool
    system_managed: bool
    custom: bool
    deleted: bool
    updated_at: int
    created_at: int
    permissions: typing.List[V1StatePermissionsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
