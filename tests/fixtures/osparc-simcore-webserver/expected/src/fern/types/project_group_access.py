

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .group_id_int import GroupIdInt
from .service_key_version import ServiceKeyVersion


class ProjectGroupAccess(UniversalBaseModel):
    gid: GroupIdInt
    accessible: bool
    inaccessible_services: typing.Optional[typing.List[ServiceKeyVersion]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
