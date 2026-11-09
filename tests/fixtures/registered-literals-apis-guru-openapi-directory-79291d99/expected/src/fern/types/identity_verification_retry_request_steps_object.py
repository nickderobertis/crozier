

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IdentityVerificationRetryRequestStepsObject(UniversalBaseModel):
    """
    Instructions for the `custom` retry strategy specifying which steps should be required or skipped.


    Note:


    This field must be provided when the retry strategy is `custom` and must be omitted otherwise.

    Custom retries override settings in your Plaid Template. For example, if your Plaid Template has `verify_sms` disabled, a custom retry with `verify_sms` enabled will still require the step.

    The `selfie_check` step is currently not supported on the sandbox server. Sandbox requests will silently disable the `selfie_check` step when provided.
    """

    documentary_verification: bool = pydantic.Field()
    """
    A boolean field specifying whether the new session should require or skip the `documentary_verification` step.
    """

    kyc_check: bool = pydantic.Field()
    """
    A boolean field specifying whether the new session should require or skip the `kyc_check` step.
    """

    selfie_check: bool = pydantic.Field()
    """
    A boolean field specifying whether the new session should require or skip the `selfie_check` step.
    """

    verify_sms: bool = pydantic.Field()
    """
    A boolean field specifying whether the new session should require or skip the `verify_sms` step.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
