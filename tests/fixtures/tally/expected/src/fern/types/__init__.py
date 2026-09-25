



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .allow_multiple import AllowMultiple
    from .allowed_files import AllowedFiles
    from .allowed_files_application_item import AllowedFilesApplicationItem
    from .allowed_files_audio_item import AllowedFilesAudioItem
    from .allowed_files_image_item import AllowedFilesImageItem
    from .allowed_files_text_item import AllowedFilesTextItem
    from .allowed_files_video_item import AllowedFilesVideoItem
    from .block import (
        Block,
        Block_CalculatedFields,
        Block_Captcha,
        Block_Checkbox,
        Block_Checkboxes,
        Block_ConditionalLogic,
        Block_Divider,
        Block_Dropdown,
        Block_DropdownOption,
        Block_Embed,
        Block_EmbedAudio,
        Block_EmbedVideo,
        Block_FileUpload,
        Block_FormTitle,
        Block_Heading1,
        Block_Heading2,
        Block_Heading3,
        Block_HiddenFields,
        Block_Image,
        Block_InputDate,
        Block_InputEmail,
        Block_InputLink,
        Block_InputNumber,
        Block_InputPhoneNumber,
        Block_InputText,
        Block_InputTime,
        Block_Label,
        Block_LinearScale,
        Block_Matrix,
        Block_MatrixColumn,
        Block_MatrixRow,
        Block_MultiSelect,
        Block_MultiSelectOption,
        Block_MultipleChoice,
        Block_MultipleChoiceOption,
        Block_PageBreak,
        Block_Payment,
        Block_Question,
        Block_RankingOption,
        Block_Rating,
        Block_RespondentCountry,
        Block_Signature,
        Block_Text,
        Block_Textarea,
        Block_Title,
        Block_WalletConnect,
    )
    from .block_payload import BlockPayload
    from .block_type import BlockType
    from .block_uuid import BlockUuid
    from .button import Button
    from .calculated_field import CalculatedField
    from .calculated_field_type import CalculatedFieldType
    from .calculated_field_value import CalculatedFieldValue
    from .calculated_fields_block import CalculatedFieldsBlock
    from .calculated_fields_block_group_type import CalculatedFieldsBlockGroupType
    from .calculated_fields_payload import CalculatedFieldsPayload
    from .captcha_block import CaptchaBlock
    from .captcha_block_group_type import CaptchaBlockGroupType
    from .captcha_payload import CaptchaPayload
    from .checkbox_block import CheckboxBlock
    from .checkbox_block_group_type import CheckboxBlockGroupType
    from .checkbox_payload import CheckboxPayload
    from .checkboxes_block import CheckboxesBlock
    from .checkboxes_block_group_type import CheckboxesBlockGroupType
    from .color_code_options import ColorCodeOptions
    from .column_list_uuid import ColumnListUuid
    from .column_ratio import ColumnRatio
    from .column_uuid import ColumnUuid
    from .conditional import Conditional, Conditional_Group, Conditional_Single
    from .conditional_action import ConditionalAction
    from .conditional_action_payload import ConditionalActionPayload
    from .conditional_action_payload_calculate import ConditionalActionPayloadCalculate
    from .conditional_action_payload_calculate_operator import ConditionalActionPayloadCalculateOperator
    from .conditional_action_payload_calculate_value import ConditionalActionPayloadCalculateValue
    from .conditional_action_payload_jump_to_page import ConditionalActionPayloadJumpToPage
    from .conditional_action_type import ConditionalActionType
    from .conditional_logic_block import ConditionalLogicBlock
    from .conditional_logic_block_group_type import ConditionalLogicBlockGroupType
    from .conditional_logic_payload import ConditionalLogicPayload
    from .conditional_logic_payload_logical_operator import ConditionalLogicPayloadLogicalOperator
    from .currency import Currency
    from .decimal_separator import DecimalSeparator
    from .default_answer_number import DefaultAnswerNumber
    from .default_answer_string import DefaultAnswerString
    from .disable_days import DisableDays
    from .divider_block import DividerBlock
    from .divider_block_group_type import DividerBlockGroupType
    from .divider_payload import DividerPayload
    from .dropdown_block import DropdownBlock
    from .dropdown_block_group_type import DropdownBlockGroupType
    from .dropdown_option_block import DropdownOptionBlock
    from .dropdown_option_block_group_type import DropdownOptionBlockGroupType
    from .dropdown_option_payload import DropdownOptionPayload
    from .embed_audio_block import EmbedAudioBlock
    from .embed_audio_block_group_type import EmbedAudioBlockGroupType
    from .embed_audio_payload import EmbedAudioPayload
    from .embed_block import EmbedBlock
    from .embed_block_group_type import EmbedBlockGroupType
    from .embed_payload import EmbedPayload
    from .embed_payload_display import EmbedPayloadDisplay
    from .embed_payload_height import EmbedPayloadHeight
    from .embed_payload_type import EmbedPayloadType
    from .embed_payload_width import EmbedPayloadWidth
    from .embed_provider import EmbedProvider
    from .embed_url import EmbedUrl
    from .embed_video_block import EmbedVideoBlock
    from .embed_video_block_group_type import EmbedVideoBlockGroupType
    from .embed_video_payload import EmbedVideoPayload
    from .event_type import EventType
    from .field import Field
    from .field_block_group_uuid import FieldBlockGroupUuid
    from .field_question_type import FieldQuestionType
    from .field_type import FieldType
    from .field_uuid import FieldUuid
    from .file_upload_block import FileUploadBlock
    from .file_upload_block_group_type import FileUploadBlockGroupType
    from .file_upload_payload import FileUploadPayload
    from .file_upload_payload_max_file_size_unit import FileUploadPayloadMaxFileSizeUnit
    from .form import Form
    from .form_payments_item import FormPaymentsItem
    from .form_settings import FormSettings
    from .form_status import FormStatus
    from .form_title_block import FormTitleBlock
    from .form_title_block_group_type import FormTitleBlockGroupType
    from .form_title_payload import FormTitlePayload
    from .form_title_payload_cover_settings import FormTitlePayloadCoverSettings
    from .get_current_user_response import GetCurrentUserResponse
    from .get_form_response import GetFormResponse
    from .group_conditional import GroupConditional
    from .group_conditional_payload import GroupConditionalPayload
    from .group_conditional_payload_logical_operator import GroupConditionalPayloadLogicalOperator
    from .group_uuid import GroupUuid
    from .has_default_answer import HasDefaultAnswer
    from .has_max_characters import HasMaxCharacters
    from .has_max_choices import HasMaxChoices
    from .has_min_characters import HasMinCharacters
    from .has_min_choices import HasMinChoices
    from .heading1block import Heading1Block
    from .heading1block_group_type import Heading1BlockGroupType
    from .heading1payload import Heading1Payload
    from .heading2block import Heading2Block
    from .heading2block_group_type import Heading2BlockGroupType
    from .heading2payload import Heading2Payload
    from .heading3block import Heading3Block
    from .heading3block_group_type import Heading3BlockGroupType
    from .heading3payload import Heading3Payload
    from .hidden_field import HiddenField
    from .hidden_fields_block import HiddenFieldsBlock
    from .hidden_fields_block_group_type import HiddenFieldsBlockGroupType
    from .hidden_fields_payload import HiddenFieldsPayload
    from .html import Html
    from .image_block import ImageBlock
    from .image_block_group_type import ImageBlockGroupType
    from .image_payload import ImagePayload
    from .image_payload_images_item import ImagePayloadImagesItem
    from .input_date_block import InputDateBlock
    from .input_date_block_group_type import InputDateBlockGroupType
    from .input_date_payload import InputDatePayload
    from .input_date_payload_date_range import InputDatePayloadDateRange
    from .input_date_payload_format import InputDatePayloadFormat
    from .input_date_payload_start_week_on import InputDatePayloadStartWeekOn
    from .input_email_block import InputEmailBlock
    from .input_email_block_group_type import InputEmailBlockGroupType
    from .input_email_payload import InputEmailPayload
    from .input_link_block import InputLinkBlock
    from .input_link_block_group_type import InputLinkBlockGroupType
    from .input_link_payload import InputLinkPayload
    from .input_number_block import InputNumberBlock
    from .input_number_block_group_type import InputNumberBlockGroupType
    from .input_number_payload import InputNumberPayload
    from .input_phone_number_block import InputPhoneNumberBlock
    from .input_phone_number_block_group_type import InputPhoneNumberBlockGroupType
    from .input_phone_number_payload import InputPhoneNumberPayload
    from .input_text_block import InputTextBlock
    from .input_text_block_group_type import InputTextBlockGroupType
    from .input_text_payload import InputTextPayload
    from .input_time_block import InputTimeBlock
    from .input_time_block_group_type import InputTimeBlockGroupType
    from .input_time_payload import InputTimePayload
    from .invite import Invite
    from .is_first_option import IsFirstOption
    from .is_folded import IsFolded
    from .is_hidden import IsHidden
    from .is_last_option import IsLastOption
    from .is_required import IsRequired
    from .label_block import LabelBlock
    from .label_block_group_type import LabelBlockGroupType
    from .label_payload import LabelPayload
    from .linear_scale_block import LinearScaleBlock
    from .linear_scale_block_group_type import LinearScaleBlockGroupType
    from .linear_scale_payload import LinearScalePayload
    from .list_forms_response import ListFormsResponse
    from .list_workspaces_response import ListWorkspacesResponse
    from .matrix_block import MatrixBlock
    from .matrix_block_group_type import MatrixBlockGroupType
    from .matrix_column_block import MatrixColumnBlock
    from .matrix_column_block_group_type import MatrixColumnBlockGroupType
    from .matrix_column_payload import MatrixColumnPayload
    from .matrix_payload import MatrixPayload
    from .matrix_row_block import MatrixRowBlock
    from .matrix_row_block_group_type import MatrixRowBlockGroupType
    from .matrix_row_payload import MatrixRowPayload
    from .max_characters import MaxCharacters
    from .max_choices import MaxChoices
    from .mention import Mention
    from .min_characters import MinCharacters
    from .min_choices import MinChoices
    from .multi_select_block import MultiSelectBlock
    from .multi_select_block_group_type import MultiSelectBlockGroupType
    from .multi_select_option_block import MultiSelectOptionBlock
    from .multi_select_option_block_group_type import MultiSelectOptionBlockGroupType
    from .multi_select_option_payload import MultiSelectOptionPayload
    from .multiple_choice_block import MultipleChoiceBlock
    from .multiple_choice_block_group_type import MultipleChoiceBlockGroupType
    from .multiple_choice_option_block import MultipleChoiceOptionBlock
    from .multiple_choice_option_block_group_type import MultipleChoiceOptionBlockGroupType
    from .multiple_choice_option_payload import MultipleChoiceOptionPayload
    from .multiple_choice_option_payload_badge_type import MultipleChoiceOptionPayloadBadgeType
    from .name import Name
    from .number_format import NumberFormat
    from .option_color import OptionColor
    from .option_index import OptionIndex
    from .page_break_block import PageBreakBlock
    from .page_break_block_group_type import PageBreakBlockGroupType
    from .page_break_payload import PageBreakPayload
    from .payment_block import PaymentBlock
    from .payment_block_group_type import PaymentBlockGroupType
    from .payment_payload import PaymentPayload
    from .payment_payload_amount import PaymentPayloadAmount
    from .question import Question
    from .question_block import QuestionBlock
    from .question_block_group_type import QuestionBlockGroupType
    from .question_field import QuestionField
    from .question_payload import QuestionPayload
    from .ranking_option_block import RankingOptionBlock
    from .ranking_option_block_group_type import RankingOptionBlockGroupType
    from .ranking_option_payload import RankingOptionPayload
    from .rating_block import RatingBlock
    from .rating_block_group_type import RatingBlockGroupType
    from .rating_payload import RatingPayload
    from .respondent_country_block import RespondentCountryBlock
    from .respondent_country_block_group_type import RespondentCountryBlockGroupType
    from .respondent_country_payload import RespondentCountryPayload
    from .signature_block import SignatureBlock
    from .signature_block_group_type import SignatureBlockGroupType
    from .signature_payload import SignaturePayload
    from .single_conditional import SingleConditional
    from .single_conditional_payload import SingleConditionalPayload
    from .single_conditional_payload_comparison import SingleConditionalPayloadComparison
    from .single_conditional_payload_value import SingleConditionalPayloadValue
    from .text_block import TextBlock
    from .text_block_group_type import TextBlockGroupType
    from .text_payload import TextPayload
    from .textarea_block import TextareaBlock
    from .textarea_block_group_type import TextareaBlockGroupType
    from .textarea_payload import TextareaPayload
    from .thousands_separator import ThousandsSeparator
    from .title_block import TitleBlock
    from .title_block_group_type import TitleBlockGroupType
    from .title_payload import TitlePayload
    from .user import User
    from .user_subscription_plan import UserSubscriptionPlan
    from .utility_uuid import UtilityUuid
    from .wallet_connect_block import WalletConnectBlock
    from .wallet_connect_block_group_type import WalletConnectBlockGroupType
    from .wallet_connect_payload import WalletConnectPayload
    from .workspace import Workspace
    from .workspace_invites_item import WorkspaceInvitesItem
_dynamic_imports: typing.Dict[str, str] = {
    "AllowMultiple": ".allow_multiple",
    "AllowedFiles": ".allowed_files",
    "AllowedFilesApplicationItem": ".allowed_files_application_item",
    "AllowedFilesAudioItem": ".allowed_files_audio_item",
    "AllowedFilesImageItem": ".allowed_files_image_item",
    "AllowedFilesTextItem": ".allowed_files_text_item",
    "AllowedFilesVideoItem": ".allowed_files_video_item",
    "Block": ".block",
    "BlockPayload": ".block_payload",
    "BlockType": ".block_type",
    "BlockUuid": ".block_uuid",
    "Block_CalculatedFields": ".block",
    "Block_Captcha": ".block",
    "Block_Checkbox": ".block",
    "Block_Checkboxes": ".block",
    "Block_ConditionalLogic": ".block",
    "Block_Divider": ".block",
    "Block_Dropdown": ".block",
    "Block_DropdownOption": ".block",
    "Block_Embed": ".block",
    "Block_EmbedAudio": ".block",
    "Block_EmbedVideo": ".block",
    "Block_FileUpload": ".block",
    "Block_FormTitle": ".block",
    "Block_Heading1": ".block",
    "Block_Heading2": ".block",
    "Block_Heading3": ".block",
    "Block_HiddenFields": ".block",
    "Block_Image": ".block",
    "Block_InputDate": ".block",
    "Block_InputEmail": ".block",
    "Block_InputLink": ".block",
    "Block_InputNumber": ".block",
    "Block_InputPhoneNumber": ".block",
    "Block_InputText": ".block",
    "Block_InputTime": ".block",
    "Block_Label": ".block",
    "Block_LinearScale": ".block",
    "Block_Matrix": ".block",
    "Block_MatrixColumn": ".block",
    "Block_MatrixRow": ".block",
    "Block_MultiSelect": ".block",
    "Block_MultiSelectOption": ".block",
    "Block_MultipleChoice": ".block",
    "Block_MultipleChoiceOption": ".block",
    "Block_PageBreak": ".block",
    "Block_Payment": ".block",
    "Block_Question": ".block",
    "Block_RankingOption": ".block",
    "Block_Rating": ".block",
    "Block_RespondentCountry": ".block",
    "Block_Signature": ".block",
    "Block_Text": ".block",
    "Block_Textarea": ".block",
    "Block_Title": ".block",
    "Block_WalletConnect": ".block",
    "Button": ".button",
    "CalculatedField": ".calculated_field",
    "CalculatedFieldType": ".calculated_field_type",
    "CalculatedFieldValue": ".calculated_field_value",
    "CalculatedFieldsBlock": ".calculated_fields_block",
    "CalculatedFieldsBlockGroupType": ".calculated_fields_block_group_type",
    "CalculatedFieldsPayload": ".calculated_fields_payload",
    "CaptchaBlock": ".captcha_block",
    "CaptchaBlockGroupType": ".captcha_block_group_type",
    "CaptchaPayload": ".captcha_payload",
    "CheckboxBlock": ".checkbox_block",
    "CheckboxBlockGroupType": ".checkbox_block_group_type",
    "CheckboxPayload": ".checkbox_payload",
    "CheckboxesBlock": ".checkboxes_block",
    "CheckboxesBlockGroupType": ".checkboxes_block_group_type",
    "ColorCodeOptions": ".color_code_options",
    "ColumnListUuid": ".column_list_uuid",
    "ColumnRatio": ".column_ratio",
    "ColumnUuid": ".column_uuid",
    "Conditional": ".conditional",
    "ConditionalAction": ".conditional_action",
    "ConditionalActionPayload": ".conditional_action_payload",
    "ConditionalActionPayloadCalculate": ".conditional_action_payload_calculate",
    "ConditionalActionPayloadCalculateOperator": ".conditional_action_payload_calculate_operator",
    "ConditionalActionPayloadCalculateValue": ".conditional_action_payload_calculate_value",
    "ConditionalActionPayloadJumpToPage": ".conditional_action_payload_jump_to_page",
    "ConditionalActionType": ".conditional_action_type",
    "ConditionalLogicBlock": ".conditional_logic_block",
    "ConditionalLogicBlockGroupType": ".conditional_logic_block_group_type",
    "ConditionalLogicPayload": ".conditional_logic_payload",
    "ConditionalLogicPayloadLogicalOperator": ".conditional_logic_payload_logical_operator",
    "Conditional_Group": ".conditional",
    "Conditional_Single": ".conditional",
    "Currency": ".currency",
    "DecimalSeparator": ".decimal_separator",
    "DefaultAnswerNumber": ".default_answer_number",
    "DefaultAnswerString": ".default_answer_string",
    "DisableDays": ".disable_days",
    "DividerBlock": ".divider_block",
    "DividerBlockGroupType": ".divider_block_group_type",
    "DividerPayload": ".divider_payload",
    "DropdownBlock": ".dropdown_block",
    "DropdownBlockGroupType": ".dropdown_block_group_type",
    "DropdownOptionBlock": ".dropdown_option_block",
    "DropdownOptionBlockGroupType": ".dropdown_option_block_group_type",
    "DropdownOptionPayload": ".dropdown_option_payload",
    "EmbedAudioBlock": ".embed_audio_block",
    "EmbedAudioBlockGroupType": ".embed_audio_block_group_type",
    "EmbedAudioPayload": ".embed_audio_payload",
    "EmbedBlock": ".embed_block",
    "EmbedBlockGroupType": ".embed_block_group_type",
    "EmbedPayload": ".embed_payload",
    "EmbedPayloadDisplay": ".embed_payload_display",
    "EmbedPayloadHeight": ".embed_payload_height",
    "EmbedPayloadType": ".embed_payload_type",
    "EmbedPayloadWidth": ".embed_payload_width",
    "EmbedProvider": ".embed_provider",
    "EmbedUrl": ".embed_url",
    "EmbedVideoBlock": ".embed_video_block",
    "EmbedVideoBlockGroupType": ".embed_video_block_group_type",
    "EmbedVideoPayload": ".embed_video_payload",
    "EventType": ".event_type",
    "Field": ".field",
    "FieldBlockGroupUuid": ".field_block_group_uuid",
    "FieldQuestionType": ".field_question_type",
    "FieldType": ".field_type",
    "FieldUuid": ".field_uuid",
    "FileUploadBlock": ".file_upload_block",
    "FileUploadBlockGroupType": ".file_upload_block_group_type",
    "FileUploadPayload": ".file_upload_payload",
    "FileUploadPayloadMaxFileSizeUnit": ".file_upload_payload_max_file_size_unit",
    "Form": ".form",
    "FormPaymentsItem": ".form_payments_item",
    "FormSettings": ".form_settings",
    "FormStatus": ".form_status",
    "FormTitleBlock": ".form_title_block",
    "FormTitleBlockGroupType": ".form_title_block_group_type",
    "FormTitlePayload": ".form_title_payload",
    "FormTitlePayloadCoverSettings": ".form_title_payload_cover_settings",
    "GetCurrentUserResponse": ".get_current_user_response",
    "GetFormResponse": ".get_form_response",
    "GroupConditional": ".group_conditional",
    "GroupConditionalPayload": ".group_conditional_payload",
    "GroupConditionalPayloadLogicalOperator": ".group_conditional_payload_logical_operator",
    "GroupUuid": ".group_uuid",
    "HasDefaultAnswer": ".has_default_answer",
    "HasMaxCharacters": ".has_max_characters",
    "HasMaxChoices": ".has_max_choices",
    "HasMinCharacters": ".has_min_characters",
    "HasMinChoices": ".has_min_choices",
    "Heading1Block": ".heading1block",
    "Heading1BlockGroupType": ".heading1block_group_type",
    "Heading1Payload": ".heading1payload",
    "Heading2Block": ".heading2block",
    "Heading2BlockGroupType": ".heading2block_group_type",
    "Heading2Payload": ".heading2payload",
    "Heading3Block": ".heading3block",
    "Heading3BlockGroupType": ".heading3block_group_type",
    "Heading3Payload": ".heading3payload",
    "HiddenField": ".hidden_field",
    "HiddenFieldsBlock": ".hidden_fields_block",
    "HiddenFieldsBlockGroupType": ".hidden_fields_block_group_type",
    "HiddenFieldsPayload": ".hidden_fields_payload",
    "Html": ".html",
    "ImageBlock": ".image_block",
    "ImageBlockGroupType": ".image_block_group_type",
    "ImagePayload": ".image_payload",
    "ImagePayloadImagesItem": ".image_payload_images_item",
    "InputDateBlock": ".input_date_block",
    "InputDateBlockGroupType": ".input_date_block_group_type",
    "InputDatePayload": ".input_date_payload",
    "InputDatePayloadDateRange": ".input_date_payload_date_range",
    "InputDatePayloadFormat": ".input_date_payload_format",
    "InputDatePayloadStartWeekOn": ".input_date_payload_start_week_on",
    "InputEmailBlock": ".input_email_block",
    "InputEmailBlockGroupType": ".input_email_block_group_type",
    "InputEmailPayload": ".input_email_payload",
    "InputLinkBlock": ".input_link_block",
    "InputLinkBlockGroupType": ".input_link_block_group_type",
    "InputLinkPayload": ".input_link_payload",
    "InputNumberBlock": ".input_number_block",
    "InputNumberBlockGroupType": ".input_number_block_group_type",
    "InputNumberPayload": ".input_number_payload",
    "InputPhoneNumberBlock": ".input_phone_number_block",
    "InputPhoneNumberBlockGroupType": ".input_phone_number_block_group_type",
    "InputPhoneNumberPayload": ".input_phone_number_payload",
    "InputTextBlock": ".input_text_block",
    "InputTextBlockGroupType": ".input_text_block_group_type",
    "InputTextPayload": ".input_text_payload",
    "InputTimeBlock": ".input_time_block",
    "InputTimeBlockGroupType": ".input_time_block_group_type",
    "InputTimePayload": ".input_time_payload",
    "Invite": ".invite",
    "IsFirstOption": ".is_first_option",
    "IsFolded": ".is_folded",
    "IsHidden": ".is_hidden",
    "IsLastOption": ".is_last_option",
    "IsRequired": ".is_required",
    "LabelBlock": ".label_block",
    "LabelBlockGroupType": ".label_block_group_type",
    "LabelPayload": ".label_payload",
    "LinearScaleBlock": ".linear_scale_block",
    "LinearScaleBlockGroupType": ".linear_scale_block_group_type",
    "LinearScalePayload": ".linear_scale_payload",
    "ListFormsResponse": ".list_forms_response",
    "ListWorkspacesResponse": ".list_workspaces_response",
    "MatrixBlock": ".matrix_block",
    "MatrixBlockGroupType": ".matrix_block_group_type",
    "MatrixColumnBlock": ".matrix_column_block",
    "MatrixColumnBlockGroupType": ".matrix_column_block_group_type",
    "MatrixColumnPayload": ".matrix_column_payload",
    "MatrixPayload": ".matrix_payload",
    "MatrixRowBlock": ".matrix_row_block",
    "MatrixRowBlockGroupType": ".matrix_row_block_group_type",
    "MatrixRowPayload": ".matrix_row_payload",
    "MaxCharacters": ".max_characters",
    "MaxChoices": ".max_choices",
    "Mention": ".mention",
    "MinCharacters": ".min_characters",
    "MinChoices": ".min_choices",
    "MultiSelectBlock": ".multi_select_block",
    "MultiSelectBlockGroupType": ".multi_select_block_group_type",
    "MultiSelectOptionBlock": ".multi_select_option_block",
    "MultiSelectOptionBlockGroupType": ".multi_select_option_block_group_type",
    "MultiSelectOptionPayload": ".multi_select_option_payload",
    "MultipleChoiceBlock": ".multiple_choice_block",
    "MultipleChoiceBlockGroupType": ".multiple_choice_block_group_type",
    "MultipleChoiceOptionBlock": ".multiple_choice_option_block",
    "MultipleChoiceOptionBlockGroupType": ".multiple_choice_option_block_group_type",
    "MultipleChoiceOptionPayload": ".multiple_choice_option_payload",
    "MultipleChoiceOptionPayloadBadgeType": ".multiple_choice_option_payload_badge_type",
    "Name": ".name",
    "NumberFormat": ".number_format",
    "OptionColor": ".option_color",
    "OptionIndex": ".option_index",
    "PageBreakBlock": ".page_break_block",
    "PageBreakBlockGroupType": ".page_break_block_group_type",
    "PageBreakPayload": ".page_break_payload",
    "PaymentBlock": ".payment_block",
    "PaymentBlockGroupType": ".payment_block_group_type",
    "PaymentPayload": ".payment_payload",
    "PaymentPayloadAmount": ".payment_payload_amount",
    "Question": ".question",
    "QuestionBlock": ".question_block",
    "QuestionBlockGroupType": ".question_block_group_type",
    "QuestionField": ".question_field",
    "QuestionPayload": ".question_payload",
    "RankingOptionBlock": ".ranking_option_block",
    "RankingOptionBlockGroupType": ".ranking_option_block_group_type",
    "RankingOptionPayload": ".ranking_option_payload",
    "RatingBlock": ".rating_block",
    "RatingBlockGroupType": ".rating_block_group_type",
    "RatingPayload": ".rating_payload",
    "RespondentCountryBlock": ".respondent_country_block",
    "RespondentCountryBlockGroupType": ".respondent_country_block_group_type",
    "RespondentCountryPayload": ".respondent_country_payload",
    "SignatureBlock": ".signature_block",
    "SignatureBlockGroupType": ".signature_block_group_type",
    "SignaturePayload": ".signature_payload",
    "SingleConditional": ".single_conditional",
    "SingleConditionalPayload": ".single_conditional_payload",
    "SingleConditionalPayloadComparison": ".single_conditional_payload_comparison",
    "SingleConditionalPayloadValue": ".single_conditional_payload_value",
    "TextBlock": ".text_block",
    "TextBlockGroupType": ".text_block_group_type",
    "TextPayload": ".text_payload",
    "TextareaBlock": ".textarea_block",
    "TextareaBlockGroupType": ".textarea_block_group_type",
    "TextareaPayload": ".textarea_payload",
    "ThousandsSeparator": ".thousands_separator",
    "TitleBlock": ".title_block",
    "TitleBlockGroupType": ".title_block_group_type",
    "TitlePayload": ".title_payload",
    "User": ".user",
    "UserSubscriptionPlan": ".user_subscription_plan",
    "UtilityUuid": ".utility_uuid",
    "WalletConnectBlock": ".wallet_connect_block",
    "WalletConnectBlockGroupType": ".wallet_connect_block_group_type",
    "WalletConnectPayload": ".wallet_connect_payload",
    "Workspace": ".workspace",
    "WorkspaceInvitesItem": ".workspace_invites_item",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AllowMultiple",
    "AllowedFiles",
    "AllowedFilesApplicationItem",
    "AllowedFilesAudioItem",
    "AllowedFilesImageItem",
    "AllowedFilesTextItem",
    "AllowedFilesVideoItem",
    "Block",
    "BlockPayload",
    "BlockType",
    "BlockUuid",
    "Block_CalculatedFields",
    "Block_Captcha",
    "Block_Checkbox",
    "Block_Checkboxes",
    "Block_ConditionalLogic",
    "Block_Divider",
    "Block_Dropdown",
    "Block_DropdownOption",
    "Block_Embed",
    "Block_EmbedAudio",
    "Block_EmbedVideo",
    "Block_FileUpload",
    "Block_FormTitle",
    "Block_Heading1",
    "Block_Heading2",
    "Block_Heading3",
    "Block_HiddenFields",
    "Block_Image",
    "Block_InputDate",
    "Block_InputEmail",
    "Block_InputLink",
    "Block_InputNumber",
    "Block_InputPhoneNumber",
    "Block_InputText",
    "Block_InputTime",
    "Block_Label",
    "Block_LinearScale",
    "Block_Matrix",
    "Block_MatrixColumn",
    "Block_MatrixRow",
    "Block_MultiSelect",
    "Block_MultiSelectOption",
    "Block_MultipleChoice",
    "Block_MultipleChoiceOption",
    "Block_PageBreak",
    "Block_Payment",
    "Block_Question",
    "Block_RankingOption",
    "Block_Rating",
    "Block_RespondentCountry",
    "Block_Signature",
    "Block_Text",
    "Block_Textarea",
    "Block_Title",
    "Block_WalletConnect",
    "Button",
    "CalculatedField",
    "CalculatedFieldType",
    "CalculatedFieldValue",
    "CalculatedFieldsBlock",
    "CalculatedFieldsBlockGroupType",
    "CalculatedFieldsPayload",
    "CaptchaBlock",
    "CaptchaBlockGroupType",
    "CaptchaPayload",
    "CheckboxBlock",
    "CheckboxBlockGroupType",
    "CheckboxPayload",
    "CheckboxesBlock",
    "CheckboxesBlockGroupType",
    "ColorCodeOptions",
    "ColumnListUuid",
    "ColumnRatio",
    "ColumnUuid",
    "Conditional",
    "ConditionalAction",
    "ConditionalActionPayload",
    "ConditionalActionPayloadCalculate",
    "ConditionalActionPayloadCalculateOperator",
    "ConditionalActionPayloadCalculateValue",
    "ConditionalActionPayloadJumpToPage",
    "ConditionalActionType",
    "ConditionalLogicBlock",
    "ConditionalLogicBlockGroupType",
    "ConditionalLogicPayload",
    "ConditionalLogicPayloadLogicalOperator",
    "Conditional_Group",
    "Conditional_Single",
    "Currency",
    "DecimalSeparator",
    "DefaultAnswerNumber",
    "DefaultAnswerString",
    "DisableDays",
    "DividerBlock",
    "DividerBlockGroupType",
    "DividerPayload",
    "DropdownBlock",
    "DropdownBlockGroupType",
    "DropdownOptionBlock",
    "DropdownOptionBlockGroupType",
    "DropdownOptionPayload",
    "EmbedAudioBlock",
    "EmbedAudioBlockGroupType",
    "EmbedAudioPayload",
    "EmbedBlock",
    "EmbedBlockGroupType",
    "EmbedPayload",
    "EmbedPayloadDisplay",
    "EmbedPayloadHeight",
    "EmbedPayloadType",
    "EmbedPayloadWidth",
    "EmbedProvider",
    "EmbedUrl",
    "EmbedVideoBlock",
    "EmbedVideoBlockGroupType",
    "EmbedVideoPayload",
    "EventType",
    "Field",
    "FieldBlockGroupUuid",
    "FieldQuestionType",
    "FieldType",
    "FieldUuid",
    "FileUploadBlock",
    "FileUploadBlockGroupType",
    "FileUploadPayload",
    "FileUploadPayloadMaxFileSizeUnit",
    "Form",
    "FormPaymentsItem",
    "FormSettings",
    "FormStatus",
    "FormTitleBlock",
    "FormTitleBlockGroupType",
    "FormTitlePayload",
    "FormTitlePayloadCoverSettings",
    "GetCurrentUserResponse",
    "GetFormResponse",
    "GroupConditional",
    "GroupConditionalPayload",
    "GroupConditionalPayloadLogicalOperator",
    "GroupUuid",
    "HasDefaultAnswer",
    "HasMaxCharacters",
    "HasMaxChoices",
    "HasMinCharacters",
    "HasMinChoices",
    "Heading1Block",
    "Heading1BlockGroupType",
    "Heading1Payload",
    "Heading2Block",
    "Heading2BlockGroupType",
    "Heading2Payload",
    "Heading3Block",
    "Heading3BlockGroupType",
    "Heading3Payload",
    "HiddenField",
    "HiddenFieldsBlock",
    "HiddenFieldsBlockGroupType",
    "HiddenFieldsPayload",
    "Html",
    "ImageBlock",
    "ImageBlockGroupType",
    "ImagePayload",
    "ImagePayloadImagesItem",
    "InputDateBlock",
    "InputDateBlockGroupType",
    "InputDatePayload",
    "InputDatePayloadDateRange",
    "InputDatePayloadFormat",
    "InputDatePayloadStartWeekOn",
    "InputEmailBlock",
    "InputEmailBlockGroupType",
    "InputEmailPayload",
    "InputLinkBlock",
    "InputLinkBlockGroupType",
    "InputLinkPayload",
    "InputNumberBlock",
    "InputNumberBlockGroupType",
    "InputNumberPayload",
    "InputPhoneNumberBlock",
    "InputPhoneNumberBlockGroupType",
    "InputPhoneNumberPayload",
    "InputTextBlock",
    "InputTextBlockGroupType",
    "InputTextPayload",
    "InputTimeBlock",
    "InputTimeBlockGroupType",
    "InputTimePayload",
    "Invite",
    "IsFirstOption",
    "IsFolded",
    "IsHidden",
    "IsLastOption",
    "IsRequired",
    "LabelBlock",
    "LabelBlockGroupType",
    "LabelPayload",
    "LinearScaleBlock",
    "LinearScaleBlockGroupType",
    "LinearScalePayload",
    "ListFormsResponse",
    "ListWorkspacesResponse",
    "MatrixBlock",
    "MatrixBlockGroupType",
    "MatrixColumnBlock",
    "MatrixColumnBlockGroupType",
    "MatrixColumnPayload",
    "MatrixPayload",
    "MatrixRowBlock",
    "MatrixRowBlockGroupType",
    "MatrixRowPayload",
    "MaxCharacters",
    "MaxChoices",
    "Mention",
    "MinCharacters",
    "MinChoices",
    "MultiSelectBlock",
    "MultiSelectBlockGroupType",
    "MultiSelectOptionBlock",
    "MultiSelectOptionBlockGroupType",
    "MultiSelectOptionPayload",
    "MultipleChoiceBlock",
    "MultipleChoiceBlockGroupType",
    "MultipleChoiceOptionBlock",
    "MultipleChoiceOptionBlockGroupType",
    "MultipleChoiceOptionPayload",
    "MultipleChoiceOptionPayloadBadgeType",
    "Name",
    "NumberFormat",
    "OptionColor",
    "OptionIndex",
    "PageBreakBlock",
    "PageBreakBlockGroupType",
    "PageBreakPayload",
    "PaymentBlock",
    "PaymentBlockGroupType",
    "PaymentPayload",
    "PaymentPayloadAmount",
    "Question",
    "QuestionBlock",
    "QuestionBlockGroupType",
    "QuestionField",
    "QuestionPayload",
    "RankingOptionBlock",
    "RankingOptionBlockGroupType",
    "RankingOptionPayload",
    "RatingBlock",
    "RatingBlockGroupType",
    "RatingPayload",
    "RespondentCountryBlock",
    "RespondentCountryBlockGroupType",
    "RespondentCountryPayload",
    "SignatureBlock",
    "SignatureBlockGroupType",
    "SignaturePayload",
    "SingleConditional",
    "SingleConditionalPayload",
    "SingleConditionalPayloadComparison",
    "SingleConditionalPayloadValue",
    "TextBlock",
    "TextBlockGroupType",
    "TextPayload",
    "TextareaBlock",
    "TextareaBlockGroupType",
    "TextareaPayload",
    "ThousandsSeparator",
    "TitleBlock",
    "TitleBlockGroupType",
    "TitlePayload",
    "User",
    "UserSubscriptionPlan",
    "UtilityUuid",
    "WalletConnectBlock",
    "WalletConnectBlockGroupType",
    "WalletConnectPayload",
    "Workspace",
    "WorkspaceInvitesItem",
]
