

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .lower_case_email_str import LowerCaseEmailStr


class InvitationGenerated(UniversalBaseModel):
    product_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="productName"), pydantic.Field(alias="productName")
    ]
    issuer: str
    guest: LowerCaseEmailStr
    trial_account_days: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="trialAccountDays"), pydantic.Field(alias="trialAccountDays")
    ] = None
    extra_credits_in_usd: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="extraCreditsInUsd"), pydantic.Field(alias="extraCreditsInUsd")
    ] = None
    created: dt.datetime
    invitation_link: typing_extensions.Annotated[
        str, FieldMetadata(alias="invitationLink"), pydantic.Field(alias="invitationLink")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
