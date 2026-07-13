

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserHardLinkedUserMembership(UniversalBaseModel):
    cross_save_overridden_membership_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="CrossSaveOverriddenMembershipId")
    ] = None
    cross_save_overridden_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="CrossSaveOverriddenType")
    ] = None
    membership_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipId")] = None
    membership_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="membershipType")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
