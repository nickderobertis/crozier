

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1hour_state_permissions_item import V1HourStatePermissionsItem


class V1HourState(UniversalBaseModel):
    """
    Workflow state (for approval processes)
    """

    icon: typing.Optional[str] = None
    permissions: typing.List[V1HourStatePermissionsItem]
    id: int
    name: str
    color: str
    billed: bool
    locked: bool
    system_managed: bool
    custom: bool
    deleted: bool
    updated_at: int
    created_at: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
