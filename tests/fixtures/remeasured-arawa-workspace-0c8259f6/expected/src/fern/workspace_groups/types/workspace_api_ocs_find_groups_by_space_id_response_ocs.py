

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.find_groups import FindGroups
from ...types.ocs_meta import OcsMeta


class WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: FindGroups

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
