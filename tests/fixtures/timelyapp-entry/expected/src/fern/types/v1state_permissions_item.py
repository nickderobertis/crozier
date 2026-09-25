

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1StatePermissionsItem(UniversalBaseModel):
    id: int
    role_id: int
    state_id: int
    team_lead: bool
    project_lead: bool
    operation: str
    updated_at: int
    created_at: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
