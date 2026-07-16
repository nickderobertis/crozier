

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tokens_reward_availability_model import TokensRewardAvailabilityModel


class TokensUserRewardAvailabilityModel(UniversalBaseModel):
    availability_model: typing_extensions.Annotated[
        typing.Optional[TokensRewardAvailabilityModel],
        FieldMetadata(alias="AvailabilityModel"),
        pydantic.Field(alias="AvailabilityModel"),
    ] = None
    is_available_for_user: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsAvailableForUser"), pydantic.Field(alias="IsAvailableForUser")
    ] = None
    is_unlocked_for_user: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsUnlockedForUser"), pydantic.Field(alias="IsUnlockedForUser")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
