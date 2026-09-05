

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .executable_access_rights import ExecutableAccessRights
from .group_id_int import GroupIdInt
from .service_release import ServiceRelease


class NodeServiceGet(UniversalBaseModel):
    key: str
    release: ServiceRelease
    owner: typing.Optional[GroupIdInt] = pydantic.Field(default=None)
    """
    Service owner primary group id or None if ownership still not defined
    """

    my_access_rights: typing_extensions.Annotated[
        ExecutableAccessRights, FieldMetadata(alias="myAccessRights"), pydantic.Field(alias="myAccessRights")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
