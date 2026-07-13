

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tokens_reward_display_properties import TokensRewardDisplayProperties
from .tokens_user_reward_availability_model import TokensUserRewardAvailabilityModel


class TokensBungieRewardDisplay(UniversalBaseModel):
    objective_display_properties: typing_extensions.Annotated[
        typing.Optional[TokensRewardDisplayProperties], FieldMetadata(alias="ObjectiveDisplayProperties")
    ] = None
    reward_display_properties: typing_extensions.Annotated[
        typing.Optional[TokensRewardDisplayProperties], FieldMetadata(alias="RewardDisplayProperties")
    ] = None
    user_reward_availability_model: typing_extensions.Annotated[
        typing.Optional[TokensUserRewardAvailabilityModel], FieldMetadata(alias="UserRewardAvailabilityModel")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
