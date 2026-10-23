

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .survey_blocks_item import SurveyBlocksItem
from .survey_display_option import SurveyDisplayOption
from .survey_endings_item import SurveyEndingsItem
from .survey_hidden_fields import SurveyHiddenFields
from .survey_metadata import SurveyMetadata
from .survey_recaptcha import SurveyRecaptcha
from .survey_single_use import SurveySingleUse
from .survey_status import SurveyStatus
from .survey_styling import SurveyStyling
from .survey_survey_closed_message import SurveySurveyClosedMessage
from .survey_type import SurveyType
from .survey_variables_item import SurveyVariablesItem
from .survey_welcome_card import SurveyWelcomeCard
from .survey_workspace_overwrites import SurveyWorkspaceOverwrites


class Survey(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the survey
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="The date and time the survey was created"),
    ]
    """
    The date and time the survey was created
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="The date and time the survey was last updated"),
    ]
    """
    The date and time the survey was last updated
    """

    name: str = pydantic.Field()
    """
    The name of the survey
    """

    redirect_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="redirectUrl"),
        pydantic.Field(alias="redirectUrl", description="The URL to redirect to after the survey is completed"),
    ] = None
    """
    The URL to redirect to after the survey is completed
    """

    type: SurveyType = pydantic.Field()
    """
    The type of the survey
    """

    status: SurveyStatus = pydantic.Field()
    """
    The status of the survey
    """

    thank_you_message: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="thankYouMessage"),
        pydantic.Field(alias="thankYouMessage", description="The thank you message of the survey"),
    ] = None
    """
    The thank you message of the survey
    """

    show_language_switch: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showLanguageSwitch"),
        pydantic.Field(alias="showLanguageSwitch", description="Whether to show the language switch"),
    ] = None
    """
    Whether to show the language switch
    """

    show_thank_you_message: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showThankYouMessage"),
        pydantic.Field(alias="showThankYouMessage", description="Whether to show the thank you message"),
    ] = None
    """
    Whether to show the thank you message
    """

    welcome_card: typing_extensions.Annotated[
        SurveyWelcomeCard,
        FieldMetadata(alias="welcomeCard"),
        pydantic.Field(alias="welcomeCard", description="The welcome card configuration"),
    ]
    """
    The welcome card configuration
    """

    display_progress_bar: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="displayProgressBar"),
        pydantic.Field(alias="displayProgressBar", description="Whether to display the progress bar"),
    ] = None
    """
    Whether to display the progress bar
    """

    pin: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pin of the survey
    """

    created_by: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="The user who created the survey"),
    ] = None
    """
    The user who created the survey
    """

    workspace_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The Workspace ID of the survey"),
    ]
    """
    The Workspace ID of the survey
    """

    environment_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="environmentId"),
        pydantic.Field(alias="environmentId", description="Deprecated alias for workspaceId."),
    ]
    """
    Deprecated alias for workspaceId.
    """

    blocks: typing.List[SurveyBlocksItem] = pydantic.Field()
    """
    The blocks of the survey
    """

    endings: typing.List[SurveyEndingsItem] = pydantic.Field()
    """
    The endings of the survey
    """

    hidden_fields: typing_extensions.Annotated[
        SurveyHiddenFields,
        FieldMetadata(alias="hiddenFields"),
        pydantic.Field(alias="hiddenFields", description="Hidden fields configuration"),
    ]
    """
    Hidden fields configuration
    """

    variables: typing.List[SurveyVariablesItem] = pydantic.Field()
    """
    Survey variables
    """

    display_option: typing_extensions.Annotated[
        SurveyDisplayOption,
        FieldMetadata(alias="displayOption"),
        pydantic.Field(alias="displayOption", description="Display options for the survey"),
    ]
    """
    Display options for the survey
    """

    recontact_days: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="recontactDays"),
        pydantic.Field(alias="recontactDays", description="Days before recontacting"),
    ] = None
    """
    Days before recontacting
    """

    display_limit: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="displayLimit"),
        pydantic.Field(alias="displayLimit", description="Display limit for the survey"),
    ] = None
    """
    Display limit for the survey
    """

    auto_close: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="autoClose"),
        pydantic.Field(alias="autoClose", description="Auto close time in seconds"),
    ] = None
    """
    Auto close time in seconds
    """

    auto_complete: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="autoComplete"),
        pydantic.Field(alias="autoComplete", description="Auto complete time in seconds"),
    ] = None
    """
    Auto complete time in seconds
    """

    delay: float = pydantic.Field()
    """
    Delay before showing survey
    """

    survey_closed_message: typing_extensions.Annotated[
        typing.Optional[SurveySurveyClosedMessage],
        FieldMetadata(alias="surveyClosedMessage"),
        pydantic.Field(alias="surveyClosedMessage", description="Message shown when survey is closed"),
    ] = None
    """
    Message shown when survey is closed
    """

    segment_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="segmentId"),
        pydantic.Field(alias="segmentId", description="ID of the segment"),
    ] = None
    """
    ID of the segment
    """

    workspace_overwrites: typing_extensions.Annotated[
        typing.Optional[SurveyWorkspaceOverwrites],
        FieldMetadata(alias="workspaceOverwrites"),
        pydantic.Field(alias="workspaceOverwrites", description="Workspace-specific overwrites"),
    ] = None
    """
    Workspace-specific overwrites
    """

    styling: typing.Optional[SurveyStyling] = pydantic.Field(default=None)
    """
    Survey styling configuration
    """

    single_use: typing_extensions.Annotated[
        SurveySingleUse,
        FieldMetadata(alias="singleUse"),
        pydantic.Field(alias="singleUse", description="Single use configuration"),
    ]
    """
    Single use configuration
    """

    is_verify_email_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isVerifyEmailEnabled"),
        pydantic.Field(alias="isVerifyEmailEnabled", description="Whether email verification is enabled"),
    ]
    """
    Whether email verification is enabled
    """

    inline_triggers: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="inlineTriggers"),
        pydantic.Field(alias="inlineTriggers", description="Inline triggers configuration"),
    ] = None
    """
    Inline triggers configuration
    """

    is_back_button_hidden: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isBackButtonHidden"),
        pydantic.Field(alias="isBackButtonHidden", description="Whether the back button is hidden"),
    ]
    """
    Whether the back button is hidden
    """

    is_auto_progressing_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isAutoProgressingEnabled"),
        pydantic.Field(
            alias="isAutoProgressingEnabled", description="Whether auto-progress is enabled for eligible question types"
        ),
    ]
    """
    Whether auto-progress is enabled for eligible question types
    """

    recaptcha: typing.Optional[SurveyRecaptcha] = pydantic.Field(default=None)
    """
    Google reCAPTCHA configuration
    """

    metadata: SurveyMetadata = pydantic.Field()
    """
    Custom link metadata for social sharing
    """

    display_percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="displayPercentage"),
        pydantic.Field(alias="displayPercentage", description="The display percentage of the survey"),
    ] = None
    """
    The display percentage of the survey
    """

    questions: typing.List[typing.Any] = pydantic.Field()
    """
    The questions of the survey.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Survey)
