

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authentication_info_challenge_indicator import AuthenticationInfoChallengeIndicator
from .authentication_info_device_channel import AuthenticationInfoDeviceChannel
from .authentication_info_exemption_indicator import AuthenticationInfoExemptionIndicator
from .authentication_info_message_category import AuthenticationInfoMessageCategory
from .authentication_info_trans_status import AuthenticationInfoTransStatus
from .authentication_info_trans_status_reason import AuthenticationInfoTransStatusReason
from .authentication_info_type import AuthenticationInfoType
from .challenge_info import ChallengeInfo


class AuthenticationInfo(UniversalBaseModel):
    acs_trans_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="acsTransId"),
        pydantic.Field(
            alias="acsTransId",
            description="Universally unique transaction identifier assigned by the Access Control Server (ACS) to identify a single transaction.",
        ),
    ]
    """
    Universally unique transaction identifier assigned by the Access Control Server (ACS) to identify a single transaction.
    """

    challenge: typing.Optional[ChallengeInfo] = pydantic.Field(default=None)
    """
    Information about Strong Customer Authentication (SCA). Returned when `type` is **challenge**.
    """

    challenge_indicator: typing_extensions.Annotated[
        AuthenticationInfoChallengeIndicator,
        FieldMetadata(alias="challengeIndicator"),
        pydantic.Field(
            alias="challengeIndicator",
            description="Specifies a preference for receiving a challenge. Possible values:\n\n* **01**: No preference\n* **02**: No challenge requested\n* **03**: Challenge requested (preference)\n* **04**: Challenge requested (mandate)\n* **05**: No challenge requested (transactional risk analysis is already performed)\n* **07**: No challenge requested (SCA is already performed)\n* **08**: No challenge requested (trusted beneficiaries exemption of no challenge required)\n* **09**: Challenge requested (trusted beneficiaries prompt requested if challenge required)\n* **80**: No challenge requested (secure corporate payment with Mastercard)\n* **82**: No challenge requested (secure corporate payment with Visa)",
        ),
    ]
    """
    Specifies a preference for receiving a challenge. Possible values:
    
    * **01**: No preference
    * **02**: No challenge requested
    * **03**: Challenge requested (preference)
    * **04**: Challenge requested (mandate)
    * **05**: No challenge requested (transactional risk analysis is already performed)
    * **07**: No challenge requested (SCA is already performed)
    * **08**: No challenge requested (trusted beneficiaries exemption of no challenge required)
    * **09**: Challenge requested (trusted beneficiaries prompt requested if challenge required)
    * **80**: No challenge requested (secure corporate payment with Mastercard)
    * **82**: No challenge requested (secure corporate payment with Visa)
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt",
            description="Date and time in UTC of the cardholder authentication. \n\n[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.",
        ),
    ]
    """
    Date and time in UTC of the cardholder authentication. 
    
    [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.
    """

    device_channel: typing_extensions.Annotated[
        AuthenticationInfoDeviceChannel,
        FieldMetadata(alias="deviceChannel"),
        pydantic.Field(
            alias="deviceChannel",
            description="Indicates the type of channel interface being used to initiate the transaction. Possible values:\n\n* **app**\n* **browser**\n* **3DSRequestorInitiated** (initiated by a merchant when the cardholder is not available)",
        ),
    ]
    """
    Indicates the type of channel interface being used to initiate the transaction. Possible values:
    
    * **app**
    * **browser**
    * **3DSRequestorInitiated** (initiated by a merchant when the cardholder is not available)
    """

    ds_trans_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="dsTransID"),
        pydantic.Field(
            alias="dsTransID",
            description="Universally unique transaction identifier assigned by the DS (card scheme) to identify a single transaction.",
        ),
    ]
    """
    Universally unique transaction identifier assigned by the DS (card scheme) to identify a single transaction.
    """

    exemption_indicator: typing_extensions.Annotated[
        typing.Optional[AuthenticationInfoExemptionIndicator],
        FieldMetadata(alias="exemptionIndicator"),
        pydantic.Field(
            alias="exemptionIndicator",
            description="Indicates the exemption type that was applied to the authentication by the issuer, if exemption applied. Possible values:\n\n* **lowValue**\n* **secureCorporate**\n* **trustedBeneficiary**\n* **transactionRiskAnalysis**\n* **acquirerExemption**\n* **noExemptionApplied**\n* **visaDAFExemption**",
        ),
    ] = None
    """
    Indicates the exemption type that was applied to the authentication by the issuer, if exemption applied. Possible values:
    
    * **lowValue**
    * **secureCorporate**
    * **trustedBeneficiary**
    * **transactionRiskAnalysis**
    * **acquirerExemption**
    * **noExemptionApplied**
    * **visaDAFExemption**
    """

    in_psd2scope: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="inPSD2Scope"),
        pydantic.Field(alias="inPSD2Scope", description="Indicates if the purchase was in the PSD2 scope."),
    ]
    """
    Indicates if the purchase was in the PSD2 scope.
    """

    message_category: typing_extensions.Annotated[
        AuthenticationInfoMessageCategory,
        FieldMetadata(alias="messageCategory"),
        pydantic.Field(
            alias="messageCategory",
            description="Identifies the category of the message for a specific use case. Possible values:\n\n* **payment**\n* **nonPayment**",
        ),
    ]
    """
    Identifies the category of the message for a specific use case. Possible values:
    
    * **payment**
    * **nonPayment**
    """

    message_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="messageVersion"),
        pydantic.Field(
            alias="messageVersion",
            description="The `messageVersion` value as defined in the 3D Secure 2 specification.",
        ),
    ]
    """
    The `messageVersion` value as defined in the 3D Secure 2 specification.
    """

    risk_score: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="riskScore"),
        pydantic.Field(alias="riskScore", description="Risk score calculated from the transaction rules."),
    ] = None
    """
    Risk score calculated from the transaction rules.
    """

    three_ds_server_trans_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="threeDSServerTransID"),
        pydantic.Field(
            alias="threeDSServerTransID",
            description="The `threeDSServerTransID` value as defined in the 3D Secure 2 specification.",
        ),
    ]
    """
    The `threeDSServerTransID` value as defined in the 3D Secure 2 specification.
    """

    trans_status: typing_extensions.Annotated[
        AuthenticationInfoTransStatus,
        FieldMetadata(alias="transStatus"),
        pydantic.Field(
            alias="transStatus",
            description="The `transStatus` value as defined in the 3D Secure 2 specification. Possible values:\n\n* **Y**: Authentication / Account verification successful.\n* **N**: Not Authenticated / Account not verified. Transaction denied.\n* **U**: Authentication / Account verification could not be performed.\n* **I**: Informational Only / 3D Secure Requestor challenge preference acknowledged.\n* **R**: Authentication / Account verification rejected by the Issuer.",
        ),
    ]
    """
    The `transStatus` value as defined in the 3D Secure 2 specification. Possible values:
    
    * **Y**: Authentication / Account verification successful.
    * **N**: Not Authenticated / Account not verified. Transaction denied.
    * **U**: Authentication / Account verification could not be performed.
    * **I**: Informational Only / 3D Secure Requestor challenge preference acknowledged.
    * **R**: Authentication / Account verification rejected by the Issuer.
    """

    trans_status_reason: typing_extensions.Annotated[
        typing.Optional[AuthenticationInfoTransStatusReason],
        FieldMetadata(alias="transStatusReason"),
        pydantic.Field(
            alias="transStatusReason",
            description="Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values).",
        ),
    ] = None
    """
    Provides information on why the `transStatus` field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values).
    """

    type: AuthenticationInfoType = pydantic.Field()
    """
    The type of authentication performed. Possible values:
    
    * **frictionless**
    * **challenge**
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
