

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .challenge_info_challenge_cancel import ChallengeInfoChallengeCancel
from .challenge_info_flow import ChallengeInfoFlow


class ChallengeInfo(UniversalBaseModel):
    challenge_cancel: typing_extensions.Annotated[
        typing.Optional[ChallengeInfoChallengeCancel],
        FieldMetadata(alias="challengeCancel"),
        pydantic.Field(
            alias="challengeCancel",
            description="Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. Possible values:\n* **00**: Data element is absent or value has been sent back with the key `challengeCancel`.\n* **01**: Cardholder selected **Cancel**.\n* **02**: 3DS Requestor cancelled Authentication.\n* **03**: Transaction abandoned.\n* **04**: Transaction timed out at ACS — other timeouts.\n* **05**: Transaction timed out at ACS — first CReq not received by ACS.\n* **06**: Transaction error.\n* **07**: Unknown.\n* **08**: Transaction time out at SDK.",
        ),
    ] = None
    """
    Indicator informing the Access Control Server (ACS) and the Directory Server (DS) that the authentication has been cancelled. Possible values:
    * **00**: Data element is absent or value has been sent back with the key `challengeCancel`.
    * **01**: Cardholder selected **Cancel**.
    * **02**: 3DS Requestor cancelled Authentication.
    * **03**: Transaction abandoned.
    * **04**: Transaction timed out at ACS — other timeouts.
    * **05**: Transaction timed out at ACS — first CReq not received by ACS.
    * **06**: Transaction error.
    * **07**: Unknown.
    * **08**: Transaction time out at SDK.
    """

    flow: ChallengeInfoFlow = pydantic.Field()
    """
    The flow used in the challenge. Possible values:
    
    * **PWD_OTP_PHONE_FL**: one-time password (OTP) flow via SMS
    * **PWD_OTP_EMAIL_FL**: one-time password (OTP) flow via email
    * **OOB_TRIGGER_FL**: out-of-band (OOB) flow
    """

    last_interaction: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="lastInteraction"),
        pydantic.Field(alias="lastInteraction", description="The last time of interaction with the challenge."),
    ]
    """
    The last time of interaction with the challenge.
    """

    phone_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="phoneNumber"),
        pydantic.Field(
            alias="phoneNumber", description="The last four digits of the phone number used in the challenge."
        ),
    ] = None
    """
    The last four digits of the phone number used in the challenge.
    """

    resends: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of times the one-time password (OTP) was resent during the challenge.
    """

    retries: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of retries used in the challenge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
