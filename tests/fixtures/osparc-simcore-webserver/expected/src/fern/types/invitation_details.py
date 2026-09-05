

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trial_account_annotated import TrialAccountAnnotated
from .welcome_credits_annotated import WelcomeCreditsAnnotated


class InvitationDetails(UniversalBaseModel):
    trial_account_days: typing_extensions.Annotated[
        typing.Optional[TrialAccountAnnotated],
        FieldMetadata(alias="trialAccountDays"),
        pydantic.Field(alias="trialAccountDays"),
    ] = None
    extra_credits_in_usd: typing_extensions.Annotated[
        typing.Optional[WelcomeCreditsAnnotated],
        FieldMetadata(alias="extraCreditsInUsd"),
        pydantic.Field(alias="extraCreditsInUsd"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
