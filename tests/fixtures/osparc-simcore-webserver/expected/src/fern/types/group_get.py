

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_access_rights import GroupAccessRights
from .group_id_int import GroupIdInt


class GroupGet(UniversalBaseModel):
    gid: GroupIdInt = pydantic.Field()
    """
    the group's unique ID
    """

    label: str = pydantic.Field()
    """
    the group's display name
    """

    description: str
    thumbnail: typing.Optional[str] = pydantic.Field(default=None)
    """
    a link to the group's thumbnail
    """

    access_rights: typing_extensions.Annotated[
        GroupAccessRights, FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ]
    inclusion_rules: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="inclusionRules"),
        pydantic.Field(alias="inclusionRules"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
