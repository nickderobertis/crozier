

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ChannelSummary(UniversalBaseModel):
    owners_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ownersCount"), pydantic.Field(alias="ownersCount")
    ] = None
    members_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="membersCount"), pydantic.Field(alias="membersCount")
    ] = None
    guests_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="guestsCount"), pydantic.Field(alias="guestsCount")
    ] = None
    has_members_from_other_tenants: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasMembersFromOtherTenants"),
        pydantic.Field(alias="hasMembersFromOtherTenants"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
