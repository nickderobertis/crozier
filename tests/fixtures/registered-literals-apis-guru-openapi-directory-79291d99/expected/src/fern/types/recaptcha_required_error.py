

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RecaptchaRequiredError(UniversalBaseModel):
    """
    The request was flagged by Plaid's fraud system, and requires additional verification to ensure they are not a bot.
    """

    common_causes: str = pydantic.Field()
    """
    Plaid's fraud system detects abusive traffic and considers a variety of parameters throughout Item creation requests. When a request is considered risky or possibly fraudulent, Link presents a reCAPTCHA for the user to solve.
    """

    display_message: str
    error_code: str = pydantic.Field()
    """
    RECAPTCHA_REQUIRED
    """

    error_type: str = pydantic.Field()
    """
    RECAPTCHA_ERROR
    """

    http_code: str = pydantic.Field()
    """
    400
    """

    link_user_experience: str = pydantic.Field()
    """
    Your user will be prompted to solve a Google reCAPTCHA challenge in the Link Recaptcha pane. If they solve the challenge successfully, the user's request is resubmitted and they are directed to the next Item creation step.
    """

    troubleshooting_steps: str = pydantic.Field()
    """
    Link will automatically guide your user through reCAPTCHA verification. As a general rule, we recommend instrumenting basic fraud monitoring to detect and protect your website from spam and abuse.
    
    If your user cannot verify their session, please submit a Support ticket with the following identifiers: `link_session_id` or `request_id`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
