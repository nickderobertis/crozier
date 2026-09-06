

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_translation_request_state import GlobalResourcesSharedModelsTranslationRequestState


class GlobalResourcesSharedModelsTranslationRequest(UniversalBaseModel):
    """
    A request to translate specified strings into specified locales
    """

    approval_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ApprovalUserId"),
        pydantic.Field(
            alias="ApprovalUserId", description="The ID of the user from which approval for the request is required"
        ),
    ] = None
    """
    The ID of the user from which approval for the request is required
    """

    cc_email_addresses: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="CCEmailAddresses"),
        pydantic.Field(
            alias="CCEmailAddresses", description="Additional email addresses to CC on emails pertaining to the request"
        ),
    ]
    """
    Additional email addresses to CC on emails pertaining to the request
    """

    charge_to_account: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ChargeToAccount"),
        pydantic.Field(alias="ChargeToAccount", description="The account to charge for the request"),
    ]
    """
    The account to charge for the request
    """

    deadline: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="Deadline"),
        pydantic.Field(
            alias="Deadline",
            description="The date by which the translations in the request are needed. Defaults to 30 days from the current date",
        ),
    ]
    """
    The date by which the translations in the request are needed. Defaults to 30 days from the current date
    """

    id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="Id"), pydantic.Field(alias="Id", description="The ID of the request")
    ] = None
    """
    The ID of the request
    """

    locale_ids: typing_extensions.Annotated[
        typing.List[int],
        FieldMetadata(alias="LocaleIds"),
        pydantic.Field(
            alias="LocaleIds", description="Locale IDs to which these strings are requested to be translated"
        ),
    ]
    """
    Locale IDs to which these strings are requested to be translated
    """

    notes: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Additional notes or comments about the request"),
    ]
    """
    Additional notes or comments about the request
    """

    questions_user_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="QuestionsUserId"),
        pydantic.Field(
            alias="QuestionsUserId",
            description="The ID of the user to which to address questions regarding the request",
        ),
    ] = None
    """
    The ID of the user to which to address questions regarding the request
    """

    state: typing_extensions.Annotated[
        GlobalResourcesSharedModelsTranslationRequestState,
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="The state of the request"),
    ]
    """
    The state of the request
    """

    submitted_by: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="SubmittedBy"),
        pydantic.Field(alias="SubmittedBy", description="The ID of the User that submitted the request"),
    ] = None
    """
    The ID of the User that submitted the request
    """

    translator_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TranslatorEmail"),
        pydantic.Field(alias="TranslatorEmail", description="The email address for the translator"),
    ] = None
    """
    The email address for the translator
    """

    translator_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TranslatorName"),
        pydantic.Field(alias="TranslatorName", description="The name of the translator"),
    ] = None
    """
    The name of the translator
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
