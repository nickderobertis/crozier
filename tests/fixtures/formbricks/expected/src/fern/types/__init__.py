



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .condition_group import ConditionGroup
    from .condition_group_conditions_item import ConditionGroupConditionsItem
    from .condition_group_conditions_item_zero import ConditionGroupConditionsItemZero
    from .condition_group_conditions_item_zero_left_operand import (
        ConditionGroupConditionsItemZeroLeftOperand,
        ConditionGroupConditionsItemZeroLeftOperand_Element,
        ConditionGroupConditionsItemZeroLeftOperand_HiddenField,
        ConditionGroupConditionsItemZeroLeftOperand_Variable,
    )
    from .condition_group_conditions_item_zero_left_operand_element import (
        ConditionGroupConditionsItemZeroLeftOperandElement,
    )
    from .condition_group_conditions_item_zero_left_operand_hidden_field import (
        ConditionGroupConditionsItemZeroLeftOperandHiddenField,
    )
    from .condition_group_conditions_item_zero_left_operand_variable import (
        ConditionGroupConditionsItemZeroLeftOperandVariable,
    )
    from .condition_group_conditions_item_zero_operator import ConditionGroupConditionsItemZeroOperator
    from .condition_group_conditions_item_zero_right_operand import (
        ConditionGroupConditionsItemZeroRightOperand,
        ConditionGroupConditionsItemZeroRightOperand_HiddenField,
        ConditionGroupConditionsItemZeroRightOperand_Static,
    )
    from .condition_group_conditions_item_zero_right_operand_hidden_field import (
        ConditionGroupConditionsItemZeroRightOperandHiddenField,
        ConditionGroupConditionsItemZeroRightOperandHiddenField_Element,
        ConditionGroupConditionsItemZeroRightOperandHiddenField_HiddenField,
        ConditionGroupConditionsItemZeroRightOperandHiddenField_Variable,
    )
    from .condition_group_conditions_item_zero_right_operand_hidden_field_element import (
        ConditionGroupConditionsItemZeroRightOperandHiddenFieldElement,
    )
    from .condition_group_conditions_item_zero_right_operand_hidden_field_hidden_field import (
        ConditionGroupConditionsItemZeroRightOperandHiddenFieldHiddenField,
    )
    from .condition_group_conditions_item_zero_right_operand_hidden_field_variable import (
        ConditionGroupConditionsItemZeroRightOperandHiddenFieldVariable,
    )
    from .condition_group_conditions_item_zero_right_operand_static import (
        ConditionGroupConditionsItemZeroRightOperandStatic,
    )
    from .condition_group_conditions_item_zero_right_operand_static_value import (
        ConditionGroupConditionsItemZeroRightOperandStaticValue,
    )
    from .condition_group_connector import ConditionGroupConnector
    from .contact import Contact
    from .contact_attribute import ContactAttribute
    from .contact_attribute_key import ContactAttributeKey
    from .contact_attribute_key_id import ContactAttributeKeyId
    from .contact_attribute_key_type import ContactAttributeKeyType
    from .health import Health
    from .me import Me
    from .me_environments_item import MeEnvironmentsItem
    from .me_environments_item_environment_type import MeEnvironmentsItemEnvironmentType
    from .me_environments_item_permission import MeEnvironmentsItemPermission
    from .me_organization_access import MeOrganizationAccess
    from .me_organization_access_access_control import MeOrganizationAccessAccessControl
    from .me_response import MeResponse
    from .me_response_environments_item import MeResponseEnvironmentsItem
    from .me_response_environments_item_environment_type import MeResponseEnvironmentsItemEnvironmentType
    from .me_response_environments_item_permission import MeResponseEnvironmentsItemPermission
    from .me_response_organization_access import MeResponseOrganizationAccess
    from .me_response_organization_access_access_control import MeResponseOrganizationAccessAccessControl
    from .me_response_workspaces_item import MeResponseWorkspacesItem
    from .me_response_workspaces_item_environment_type import MeResponseWorkspacesItemEnvironmentType
    from .me_response_workspaces_item_permission import MeResponseWorkspacesItemPermission
    from .me_workspaces_item import MeWorkspacesItem
    from .me_workspaces_item_environment_type import MeWorkspacesItemEnvironmentType
    from .me_workspaces_item_permission import MeWorkspacesItemPermission
    from .not_found_error_body import NotFoundErrorBody
    from .organization_id import OrganizationId
    from .response import Response
    from .response_data_value import ResponseDataValue
    from .response_id import ResponseId
    from .response_meta import ResponseMeta
    from .response_meta_user_agent import ResponseMetaUserAgent
    from .response_variables_value import ResponseVariablesValue
    from .role import Role
    from .role_data_item import RoleDataItem
    from .role_data_item_one import RoleDataItemOne
    from .role_data_item_three import RoleDataItemThree
    from .role_data_item_two import RoleDataItemTwo
    from .role_data_item_zero import RoleDataItemZero
    from .survey import Survey
    from .survey_blocks_item import SurveyBlocksItem
    from .survey_blocks_item_elements_item import SurveyBlocksItemElementsItem
    from .survey_blocks_item_elements_item_address_line1 import SurveyBlocksItemElementsItemAddressLine1
    from .survey_blocks_item_elements_item_address_line1address_line1 import (
        SurveyBlocksItemElementsItemAddressLine1AddressLine1,
    )
    from .survey_blocks_item_elements_item_address_line1address_line2 import (
        SurveyBlocksItemElementsItemAddressLine1AddressLine2,
    )
    from .survey_blocks_item_elements_item_address_line1city import SurveyBlocksItemElementsItemAddressLine1City
    from .survey_blocks_item_elements_item_address_line1country import SurveyBlocksItemElementsItemAddressLine1Country
    from .survey_blocks_item_elements_item_address_line1scale import SurveyBlocksItemElementsItemAddressLine1Scale
    from .survey_blocks_item_elements_item_address_line1state import SurveyBlocksItemElementsItemAddressLine1State
    from .survey_blocks_item_elements_item_address_line1type import SurveyBlocksItemElementsItemAddressLine1Type
    from .survey_blocks_item_elements_item_address_line1zip import SurveyBlocksItemElementsItemAddressLine1Zip
    from .survey_blocks_item_elements_item_allow_multi import SurveyBlocksItemElementsItemAllowMulti
    from .survey_blocks_item_elements_item_allow_multi_choices_item import (
        SurveyBlocksItemElementsItemAllowMultiChoicesItem,
    )
    from .survey_blocks_item_elements_item_allow_multi_scale import SurveyBlocksItemElementsItemAllowMultiScale
    from .survey_blocks_item_elements_item_allow_multi_type import SurveyBlocksItemElementsItemAllowMultiType
    from .survey_blocks_item_elements_item_allow_multiple_files import SurveyBlocksItemElementsItemAllowMultipleFiles
    from .survey_blocks_item_elements_item_allow_multiple_files_allowed_file_extensions_item import (
        SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem,
    )
    from .survey_blocks_item_elements_item_allow_multiple_files_scale import (
        SurveyBlocksItemElementsItemAllowMultipleFilesScale,
    )
    from .survey_blocks_item_elements_item_allow_multiple_files_type import (
        SurveyBlocksItemElementsItemAllowMultipleFilesType,
    )
    from .survey_blocks_item_elements_item_button_external import SurveyBlocksItemElementsItemButtonExternal
    from .survey_blocks_item_elements_item_button_external_scale import SurveyBlocksItemElementsItemButtonExternalScale
    from .survey_blocks_item_elements_item_button_external_type import SurveyBlocksItemElementsItemButtonExternalType
    from .survey_blocks_item_elements_item_cal_host import SurveyBlocksItemElementsItemCalHost
    from .survey_blocks_item_elements_item_cal_host_scale import SurveyBlocksItemElementsItemCalHostScale
    from .survey_blocks_item_elements_item_cal_host_type import SurveyBlocksItemElementsItemCalHostType
    from .survey_blocks_item_elements_item_char_limit import SurveyBlocksItemElementsItemCharLimit
    from .survey_blocks_item_elements_item_char_limit_char_limit import SurveyBlocksItemElementsItemCharLimitCharLimit
    from .survey_blocks_item_elements_item_char_limit_input_type import SurveyBlocksItemElementsItemCharLimitInputType
    from .survey_blocks_item_elements_item_char_limit_scale import SurveyBlocksItemElementsItemCharLimitScale
    from .survey_blocks_item_elements_item_char_limit_type import SurveyBlocksItemElementsItemCharLimitType
    from .survey_blocks_item_elements_item_choices import SurveyBlocksItemElementsItemChoices
    from .survey_blocks_item_elements_item_choices_choices_item import SurveyBlocksItemElementsItemChoicesChoicesItem
    from .survey_blocks_item_elements_item_choices_scale import SurveyBlocksItemElementsItemChoicesScale
    from .survey_blocks_item_elements_item_choices_shuffle_option import (
        SurveyBlocksItemElementsItemChoicesShuffleOption,
    )
    from .survey_blocks_item_elements_item_choices_type import SurveyBlocksItemElementsItemChoicesType
    from .survey_blocks_item_elements_item_columns import SurveyBlocksItemElementsItemColumns
    from .survey_blocks_item_elements_item_columns_columns_item import SurveyBlocksItemElementsItemColumnsColumnsItem
    from .survey_blocks_item_elements_item_columns_rows_item import SurveyBlocksItemElementsItemColumnsRowsItem
    from .survey_blocks_item_elements_item_columns_scale import SurveyBlocksItemElementsItemColumnsScale
    from .survey_blocks_item_elements_item_columns_shuffle_option import (
        SurveyBlocksItemElementsItemColumnsShuffleOption,
    )
    from .survey_blocks_item_elements_item_columns_type import SurveyBlocksItemElementsItemColumnsType
    from .survey_blocks_item_elements_item_company import SurveyBlocksItemElementsItemCompany
    from .survey_blocks_item_elements_item_company_company import SurveyBlocksItemElementsItemCompanyCompany
    from .survey_blocks_item_elements_item_company_email import SurveyBlocksItemElementsItemCompanyEmail
    from .survey_blocks_item_elements_item_company_first_name import SurveyBlocksItemElementsItemCompanyFirstName
    from .survey_blocks_item_elements_item_company_last_name import SurveyBlocksItemElementsItemCompanyLastName
    from .survey_blocks_item_elements_item_company_phone import SurveyBlocksItemElementsItemCompanyPhone
    from .survey_blocks_item_elements_item_company_scale import SurveyBlocksItemElementsItemCompanyScale
    from .survey_blocks_item_elements_item_company_type import SurveyBlocksItemElementsItemCompanyType
    from .survey_blocks_item_elements_item_five import SurveyBlocksItemElementsItemFive
    from .survey_blocks_item_elements_item_five_scale import SurveyBlocksItemElementsItemFiveScale
    from .survey_blocks_item_elements_item_five_type import SurveyBlocksItemElementsItemFiveType
    from .survey_blocks_item_elements_item_format import SurveyBlocksItemElementsItemFormat
    from .survey_blocks_item_elements_item_format_format import SurveyBlocksItemElementsItemFormatFormat
    from .survey_blocks_item_elements_item_format_scale import SurveyBlocksItemElementsItemFormatScale
    from .survey_blocks_item_elements_item_format_type import SurveyBlocksItemElementsItemFormatType
    from .survey_blocks_item_elements_item_label import SurveyBlocksItemElementsItemLabel
    from .survey_blocks_item_elements_item_label_scale import SurveyBlocksItemElementsItemLabelScale
    from .survey_blocks_item_elements_item_label_type import SurveyBlocksItemElementsItemLabelType
    from .survey_blocks_item_elements_item_three import SurveyBlocksItemElementsItemThree
    from .survey_blocks_item_elements_item_three_scale import SurveyBlocksItemElementsItemThreeScale
    from .survey_blocks_item_elements_item_three_type import SurveyBlocksItemElementsItemThreeType
    from .survey_blocks_item_elements_item_two import SurveyBlocksItemElementsItemTwo
    from .survey_blocks_item_elements_item_two_choices_item import SurveyBlocksItemElementsItemTwoChoicesItem
    from .survey_blocks_item_elements_item_two_scale import SurveyBlocksItemElementsItemTwoScale
    from .survey_blocks_item_elements_item_two_shuffle_option import SurveyBlocksItemElementsItemTwoShuffleOption
    from .survey_blocks_item_elements_item_two_type import SurveyBlocksItemElementsItemTwoType
    from .survey_blocks_item_elements_item_two_type_one import SurveyBlocksItemElementsItemTwoTypeOne
    from .survey_blocks_item_elements_item_two_type_zero import SurveyBlocksItemElementsItemTwoTypeZero
    from .survey_blocks_item_logic_item import SurveyBlocksItemLogicItem
    from .survey_blocks_item_logic_item_actions_item import (
        SurveyBlocksItemLogicItemActionsItem,
        SurveyBlocksItemLogicItemActionsItem_Calculate,
        SurveyBlocksItemLogicItemActionsItem_JumpToBlock,
        SurveyBlocksItemLogicItemActionsItem_RequireAnswer,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate import SurveyBlocksItemLogicItemActionsItemCalculate
    from .survey_blocks_item_logic_item_actions_item_calculate_one import (
        SurveyBlocksItemLogicItemActionsItemCalculateOne,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_objective import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneObjective,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_operator import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneOperator,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValue,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValue_HiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValue_Static,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Element,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_HiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Variable,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_element import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldElement,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_hidden_field import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldHiddenField,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_variable import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldVariable,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_one_value_static import (
        SurveyBlocksItemLogicItemActionsItemCalculateOneValueStatic,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero import (
        SurveyBlocksItemLogicItemActionsItemCalculateZero,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_objective import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_operator import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValue,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_HiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_Static,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Element,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_HiddenField,
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Variable,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_element import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldElement,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_hidden_field import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldHiddenField,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_variable import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldVariable,
    )
    from .survey_blocks_item_logic_item_actions_item_calculate_zero_value_static import (
        SurveyBlocksItemLogicItemActionsItemCalculateZeroValueStatic,
    )
    from .survey_blocks_item_logic_item_actions_item_jump_to_block import (
        SurveyBlocksItemLogicItemActionsItemJumpToBlock,
    )
    from .survey_blocks_item_logic_item_actions_item_require_answer import (
        SurveyBlocksItemLogicItemActionsItemRequireAnswer,
    )
    from .survey_display_option import SurveyDisplayOption
    from .survey_endings_item import SurveyEndingsItem, SurveyEndingsItem_EndScreen, SurveyEndingsItem_RedirectToUrl
    from .survey_endings_item_end_screen import SurveyEndingsItemEndScreen
    from .survey_endings_item_redirect_to_url import SurveyEndingsItemRedirectToUrl
    from .survey_hidden_fields import SurveyHiddenFields
    from .survey_metadata import SurveyMetadata
    from .survey_recaptcha import SurveyRecaptcha
    from .survey_single_use import SurveySingleUse
    from .survey_status import SurveyStatus
    from .survey_styling import SurveyStyling
    from .survey_styling_background import SurveyStylingBackground
    from .survey_styling_background_bg_type import SurveyStylingBackgroundBgType
    from .survey_styling_brand_color import SurveyStylingBrandColor
    from .survey_styling_card_arrangement import SurveyStylingCardArrangement
    from .survey_styling_card_arrangement_app_surveys import SurveyStylingCardArrangementAppSurveys
    from .survey_styling_card_arrangement_link_surveys import SurveyStylingCardArrangementLinkSurveys
    from .survey_styling_card_background_color import SurveyStylingCardBackgroundColor
    from .survey_styling_card_border_color import SurveyStylingCardBorderColor
    from .survey_styling_highlight_border_color import SurveyStylingHighlightBorderColor
    from .survey_styling_input_border_color import SurveyStylingInputBorderColor
    from .survey_styling_logo import SurveyStylingLogo
    from .survey_survey_closed_message import SurveySurveyClosedMessage
    from .survey_type import SurveyType
    from .survey_variables_item import SurveyVariablesItem, SurveyVariablesItem_Number, SurveyVariablesItem_Text
    from .survey_variables_item_number import SurveyVariablesItemNumber
    from .survey_variables_item_text import SurveyVariablesItemText
    from .survey_welcome_card import SurveyWelcomeCard
    from .survey_workspace_overwrites import SurveyWorkspaceOverwrites
    from .survey_workspace_overwrites_overlay import SurveyWorkspaceOverwritesOverlay
    from .survey_workspace_overwrites_placement import SurveyWorkspaceOverwritesPlacement
    from .team import Team
    from .team_id import TeamId
    from .user import User
    from .user_role import UserRole
    from .webhook import Webhook
    from .webhook_id import WebhookId
    from .webhook_source import WebhookSource
    from .webhook_triggers_item import WebhookTriggersItem
    from .workspace_team import WorkspaceTeam
    from .workspace_team_permission import WorkspaceTeamPermission
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "ConditionGroup": ".condition_group",
    "ConditionGroupConditionsItem": ".condition_group_conditions_item",
    "ConditionGroupConditionsItemZero": ".condition_group_conditions_item_zero",
    "ConditionGroupConditionsItemZeroLeftOperand": ".condition_group_conditions_item_zero_left_operand",
    "ConditionGroupConditionsItemZeroLeftOperandElement": ".condition_group_conditions_item_zero_left_operand_element",
    "ConditionGroupConditionsItemZeroLeftOperandHiddenField": ".condition_group_conditions_item_zero_left_operand_hidden_field",
    "ConditionGroupConditionsItemZeroLeftOperandVariable": ".condition_group_conditions_item_zero_left_operand_variable",
    "ConditionGroupConditionsItemZeroLeftOperand_Element": ".condition_group_conditions_item_zero_left_operand",
    "ConditionGroupConditionsItemZeroLeftOperand_HiddenField": ".condition_group_conditions_item_zero_left_operand",
    "ConditionGroupConditionsItemZeroLeftOperand_Variable": ".condition_group_conditions_item_zero_left_operand",
    "ConditionGroupConditionsItemZeroOperator": ".condition_group_conditions_item_zero_operator",
    "ConditionGroupConditionsItemZeroRightOperand": ".condition_group_conditions_item_zero_right_operand",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField": ".condition_group_conditions_item_zero_right_operand_hidden_field",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldElement": ".condition_group_conditions_item_zero_right_operand_hidden_field_element",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldHiddenField": ".condition_group_conditions_item_zero_right_operand_hidden_field_hidden_field",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldVariable": ".condition_group_conditions_item_zero_right_operand_hidden_field_variable",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_Element": ".condition_group_conditions_item_zero_right_operand_hidden_field",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_HiddenField": ".condition_group_conditions_item_zero_right_operand_hidden_field",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_Variable": ".condition_group_conditions_item_zero_right_operand_hidden_field",
    "ConditionGroupConditionsItemZeroRightOperandStatic": ".condition_group_conditions_item_zero_right_operand_static",
    "ConditionGroupConditionsItemZeroRightOperandStaticValue": ".condition_group_conditions_item_zero_right_operand_static_value",
    "ConditionGroupConditionsItemZeroRightOperand_HiddenField": ".condition_group_conditions_item_zero_right_operand",
    "ConditionGroupConditionsItemZeroRightOperand_Static": ".condition_group_conditions_item_zero_right_operand",
    "ConditionGroupConnector": ".condition_group_connector",
    "Contact": ".contact",
    "ContactAttribute": ".contact_attribute",
    "ContactAttributeKey": ".contact_attribute_key",
    "ContactAttributeKeyId": ".contact_attribute_key_id",
    "ContactAttributeKeyType": ".contact_attribute_key_type",
    "Health": ".health",
    "Me": ".me",
    "MeEnvironmentsItem": ".me_environments_item",
    "MeEnvironmentsItemEnvironmentType": ".me_environments_item_environment_type",
    "MeEnvironmentsItemPermission": ".me_environments_item_permission",
    "MeOrganizationAccess": ".me_organization_access",
    "MeOrganizationAccessAccessControl": ".me_organization_access_access_control",
    "MeResponse": ".me_response",
    "MeResponseEnvironmentsItem": ".me_response_environments_item",
    "MeResponseEnvironmentsItemEnvironmentType": ".me_response_environments_item_environment_type",
    "MeResponseEnvironmentsItemPermission": ".me_response_environments_item_permission",
    "MeResponseOrganizationAccess": ".me_response_organization_access",
    "MeResponseOrganizationAccessAccessControl": ".me_response_organization_access_access_control",
    "MeResponseWorkspacesItem": ".me_response_workspaces_item",
    "MeResponseWorkspacesItemEnvironmentType": ".me_response_workspaces_item_environment_type",
    "MeResponseWorkspacesItemPermission": ".me_response_workspaces_item_permission",
    "MeWorkspacesItem": ".me_workspaces_item",
    "MeWorkspacesItemEnvironmentType": ".me_workspaces_item_environment_type",
    "MeWorkspacesItemPermission": ".me_workspaces_item_permission",
    "NotFoundErrorBody": ".not_found_error_body",
    "OrganizationId": ".organization_id",
    "Response": ".response",
    "ResponseDataValue": ".response_data_value",
    "ResponseId": ".response_id",
    "ResponseMeta": ".response_meta",
    "ResponseMetaUserAgent": ".response_meta_user_agent",
    "ResponseVariablesValue": ".response_variables_value",
    "Role": ".role",
    "RoleDataItem": ".role_data_item",
    "RoleDataItemOne": ".role_data_item_one",
    "RoleDataItemThree": ".role_data_item_three",
    "RoleDataItemTwo": ".role_data_item_two",
    "RoleDataItemZero": ".role_data_item_zero",
    "Survey": ".survey",
    "SurveyBlocksItem": ".survey_blocks_item",
    "SurveyBlocksItemElementsItem": ".survey_blocks_item_elements_item",
    "SurveyBlocksItemElementsItemAddressLine1": ".survey_blocks_item_elements_item_address_line1",
    "SurveyBlocksItemElementsItemAddressLine1AddressLine1": ".survey_blocks_item_elements_item_address_line1address_line1",
    "SurveyBlocksItemElementsItemAddressLine1AddressLine2": ".survey_blocks_item_elements_item_address_line1address_line2",
    "SurveyBlocksItemElementsItemAddressLine1City": ".survey_blocks_item_elements_item_address_line1city",
    "SurveyBlocksItemElementsItemAddressLine1Country": ".survey_blocks_item_elements_item_address_line1country",
    "SurveyBlocksItemElementsItemAddressLine1Scale": ".survey_blocks_item_elements_item_address_line1scale",
    "SurveyBlocksItemElementsItemAddressLine1State": ".survey_blocks_item_elements_item_address_line1state",
    "SurveyBlocksItemElementsItemAddressLine1Type": ".survey_blocks_item_elements_item_address_line1type",
    "SurveyBlocksItemElementsItemAddressLine1Zip": ".survey_blocks_item_elements_item_address_line1zip",
    "SurveyBlocksItemElementsItemAllowMulti": ".survey_blocks_item_elements_item_allow_multi",
    "SurveyBlocksItemElementsItemAllowMultiChoicesItem": ".survey_blocks_item_elements_item_allow_multi_choices_item",
    "SurveyBlocksItemElementsItemAllowMultiScale": ".survey_blocks_item_elements_item_allow_multi_scale",
    "SurveyBlocksItemElementsItemAllowMultiType": ".survey_blocks_item_elements_item_allow_multi_type",
    "SurveyBlocksItemElementsItemAllowMultipleFiles": ".survey_blocks_item_elements_item_allow_multiple_files",
    "SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem": ".survey_blocks_item_elements_item_allow_multiple_files_allowed_file_extensions_item",
    "SurveyBlocksItemElementsItemAllowMultipleFilesScale": ".survey_blocks_item_elements_item_allow_multiple_files_scale",
    "SurveyBlocksItemElementsItemAllowMultipleFilesType": ".survey_blocks_item_elements_item_allow_multiple_files_type",
    "SurveyBlocksItemElementsItemButtonExternal": ".survey_blocks_item_elements_item_button_external",
    "SurveyBlocksItemElementsItemButtonExternalScale": ".survey_blocks_item_elements_item_button_external_scale",
    "SurveyBlocksItemElementsItemButtonExternalType": ".survey_blocks_item_elements_item_button_external_type",
    "SurveyBlocksItemElementsItemCalHost": ".survey_blocks_item_elements_item_cal_host",
    "SurveyBlocksItemElementsItemCalHostScale": ".survey_blocks_item_elements_item_cal_host_scale",
    "SurveyBlocksItemElementsItemCalHostType": ".survey_blocks_item_elements_item_cal_host_type",
    "SurveyBlocksItemElementsItemCharLimit": ".survey_blocks_item_elements_item_char_limit",
    "SurveyBlocksItemElementsItemCharLimitCharLimit": ".survey_blocks_item_elements_item_char_limit_char_limit",
    "SurveyBlocksItemElementsItemCharLimitInputType": ".survey_blocks_item_elements_item_char_limit_input_type",
    "SurveyBlocksItemElementsItemCharLimitScale": ".survey_blocks_item_elements_item_char_limit_scale",
    "SurveyBlocksItemElementsItemCharLimitType": ".survey_blocks_item_elements_item_char_limit_type",
    "SurveyBlocksItemElementsItemChoices": ".survey_blocks_item_elements_item_choices",
    "SurveyBlocksItemElementsItemChoicesChoicesItem": ".survey_blocks_item_elements_item_choices_choices_item",
    "SurveyBlocksItemElementsItemChoicesScale": ".survey_blocks_item_elements_item_choices_scale",
    "SurveyBlocksItemElementsItemChoicesShuffleOption": ".survey_blocks_item_elements_item_choices_shuffle_option",
    "SurveyBlocksItemElementsItemChoicesType": ".survey_blocks_item_elements_item_choices_type",
    "SurveyBlocksItemElementsItemColumns": ".survey_blocks_item_elements_item_columns",
    "SurveyBlocksItemElementsItemColumnsColumnsItem": ".survey_blocks_item_elements_item_columns_columns_item",
    "SurveyBlocksItemElementsItemColumnsRowsItem": ".survey_blocks_item_elements_item_columns_rows_item",
    "SurveyBlocksItemElementsItemColumnsScale": ".survey_blocks_item_elements_item_columns_scale",
    "SurveyBlocksItemElementsItemColumnsShuffleOption": ".survey_blocks_item_elements_item_columns_shuffle_option",
    "SurveyBlocksItemElementsItemColumnsType": ".survey_blocks_item_elements_item_columns_type",
    "SurveyBlocksItemElementsItemCompany": ".survey_blocks_item_elements_item_company",
    "SurveyBlocksItemElementsItemCompanyCompany": ".survey_blocks_item_elements_item_company_company",
    "SurveyBlocksItemElementsItemCompanyEmail": ".survey_blocks_item_elements_item_company_email",
    "SurveyBlocksItemElementsItemCompanyFirstName": ".survey_blocks_item_elements_item_company_first_name",
    "SurveyBlocksItemElementsItemCompanyLastName": ".survey_blocks_item_elements_item_company_last_name",
    "SurveyBlocksItemElementsItemCompanyPhone": ".survey_blocks_item_elements_item_company_phone",
    "SurveyBlocksItemElementsItemCompanyScale": ".survey_blocks_item_elements_item_company_scale",
    "SurveyBlocksItemElementsItemCompanyType": ".survey_blocks_item_elements_item_company_type",
    "SurveyBlocksItemElementsItemFive": ".survey_blocks_item_elements_item_five",
    "SurveyBlocksItemElementsItemFiveScale": ".survey_blocks_item_elements_item_five_scale",
    "SurveyBlocksItemElementsItemFiveType": ".survey_blocks_item_elements_item_five_type",
    "SurveyBlocksItemElementsItemFormat": ".survey_blocks_item_elements_item_format",
    "SurveyBlocksItemElementsItemFormatFormat": ".survey_blocks_item_elements_item_format_format",
    "SurveyBlocksItemElementsItemFormatScale": ".survey_blocks_item_elements_item_format_scale",
    "SurveyBlocksItemElementsItemFormatType": ".survey_blocks_item_elements_item_format_type",
    "SurveyBlocksItemElementsItemLabel": ".survey_blocks_item_elements_item_label",
    "SurveyBlocksItemElementsItemLabelScale": ".survey_blocks_item_elements_item_label_scale",
    "SurveyBlocksItemElementsItemLabelType": ".survey_blocks_item_elements_item_label_type",
    "SurveyBlocksItemElementsItemThree": ".survey_blocks_item_elements_item_three",
    "SurveyBlocksItemElementsItemThreeScale": ".survey_blocks_item_elements_item_three_scale",
    "SurveyBlocksItemElementsItemThreeType": ".survey_blocks_item_elements_item_three_type",
    "SurveyBlocksItemElementsItemTwo": ".survey_blocks_item_elements_item_two",
    "SurveyBlocksItemElementsItemTwoChoicesItem": ".survey_blocks_item_elements_item_two_choices_item",
    "SurveyBlocksItemElementsItemTwoScale": ".survey_blocks_item_elements_item_two_scale",
    "SurveyBlocksItemElementsItemTwoShuffleOption": ".survey_blocks_item_elements_item_two_shuffle_option",
    "SurveyBlocksItemElementsItemTwoType": ".survey_blocks_item_elements_item_two_type",
    "SurveyBlocksItemElementsItemTwoTypeOne": ".survey_blocks_item_elements_item_two_type_one",
    "SurveyBlocksItemElementsItemTwoTypeZero": ".survey_blocks_item_elements_item_two_type_zero",
    "SurveyBlocksItemLogicItem": ".survey_blocks_item_logic_item",
    "SurveyBlocksItemLogicItemActionsItem": ".survey_blocks_item_logic_item_actions_item",
    "SurveyBlocksItemLogicItemActionsItemCalculate": ".survey_blocks_item_logic_item_actions_item_calculate",
    "SurveyBlocksItemLogicItemActionsItemCalculateOne": ".survey_blocks_item_logic_item_actions_item_calculate_one",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneObjective": ".survey_blocks_item_logic_item_actions_item_calculate_one_objective",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneOperator": ".survey_blocks_item_logic_item_actions_item_calculate_one_operator",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue": ".survey_blocks_item_logic_item_actions_item_calculate_one_value",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldElement": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_element",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldHiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldVariable": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field_variable",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Element": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_HiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Variable": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueStatic": ".survey_blocks_item_logic_item_actions_item_calculate_one_value_static",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue_HiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_one_value",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue_Static": ".survey_blocks_item_logic_item_actions_item_calculate_one_value",
    "SurveyBlocksItemLogicItemActionsItemCalculateZero": ".survey_blocks_item_logic_item_actions_item_calculate_zero",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective": ".survey_blocks_item_logic_item_actions_item_calculate_zero_objective",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator": ".survey_blocks_item_logic_item_actions_item_calculate_zero_operator",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldElement": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_element",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldHiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldVariable": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field_variable",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Element": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_HiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Variable": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_hidden_field",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueStatic": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value_static",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_HiddenField": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_Static": ".survey_blocks_item_logic_item_actions_item_calculate_zero_value",
    "SurveyBlocksItemLogicItemActionsItemJumpToBlock": ".survey_blocks_item_logic_item_actions_item_jump_to_block",
    "SurveyBlocksItemLogicItemActionsItemRequireAnswer": ".survey_blocks_item_logic_item_actions_item_require_answer",
    "SurveyBlocksItemLogicItemActionsItem_Calculate": ".survey_blocks_item_logic_item_actions_item",
    "SurveyBlocksItemLogicItemActionsItem_JumpToBlock": ".survey_blocks_item_logic_item_actions_item",
    "SurveyBlocksItemLogicItemActionsItem_RequireAnswer": ".survey_blocks_item_logic_item_actions_item",
    "SurveyDisplayOption": ".survey_display_option",
    "SurveyEndingsItem": ".survey_endings_item",
    "SurveyEndingsItemEndScreen": ".survey_endings_item_end_screen",
    "SurveyEndingsItemRedirectToUrl": ".survey_endings_item_redirect_to_url",
    "SurveyEndingsItem_EndScreen": ".survey_endings_item",
    "SurveyEndingsItem_RedirectToUrl": ".survey_endings_item",
    "SurveyHiddenFields": ".survey_hidden_fields",
    "SurveyMetadata": ".survey_metadata",
    "SurveyRecaptcha": ".survey_recaptcha",
    "SurveySingleUse": ".survey_single_use",
    "SurveyStatus": ".survey_status",
    "SurveyStyling": ".survey_styling",
    "SurveyStylingBackground": ".survey_styling_background",
    "SurveyStylingBackgroundBgType": ".survey_styling_background_bg_type",
    "SurveyStylingBrandColor": ".survey_styling_brand_color",
    "SurveyStylingCardArrangement": ".survey_styling_card_arrangement",
    "SurveyStylingCardArrangementAppSurveys": ".survey_styling_card_arrangement_app_surveys",
    "SurveyStylingCardArrangementLinkSurveys": ".survey_styling_card_arrangement_link_surveys",
    "SurveyStylingCardBackgroundColor": ".survey_styling_card_background_color",
    "SurveyStylingCardBorderColor": ".survey_styling_card_border_color",
    "SurveyStylingHighlightBorderColor": ".survey_styling_highlight_border_color",
    "SurveyStylingInputBorderColor": ".survey_styling_input_border_color",
    "SurveyStylingLogo": ".survey_styling_logo",
    "SurveySurveyClosedMessage": ".survey_survey_closed_message",
    "SurveyType": ".survey_type",
    "SurveyVariablesItem": ".survey_variables_item",
    "SurveyVariablesItemNumber": ".survey_variables_item_number",
    "SurveyVariablesItemText": ".survey_variables_item_text",
    "SurveyVariablesItem_Number": ".survey_variables_item",
    "SurveyVariablesItem_Text": ".survey_variables_item",
    "SurveyWelcomeCard": ".survey_welcome_card",
    "SurveyWorkspaceOverwrites": ".survey_workspace_overwrites",
    "SurveyWorkspaceOverwritesOverlay": ".survey_workspace_overwrites_overlay",
    "SurveyWorkspaceOverwritesPlacement": ".survey_workspace_overwrites_placement",
    "Team": ".team",
    "TeamId": ".team_id",
    "User": ".user",
    "UserRole": ".user_role",
    "Webhook": ".webhook",
    "WebhookId": ".webhook_id",
    "WebhookSource": ".webhook_source",
    "WebhookTriggersItem": ".webhook_triggers_item",
    "WorkspaceTeam": ".workspace_team",
    "WorkspaceTeamPermission": ".workspace_team_permission",
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
    "BadRequestErrorBody",
    "ConditionGroup",
    "ConditionGroupConditionsItem",
    "ConditionGroupConditionsItemZero",
    "ConditionGroupConditionsItemZeroLeftOperand",
    "ConditionGroupConditionsItemZeroLeftOperandElement",
    "ConditionGroupConditionsItemZeroLeftOperandHiddenField",
    "ConditionGroupConditionsItemZeroLeftOperandVariable",
    "ConditionGroupConditionsItemZeroLeftOperand_Element",
    "ConditionGroupConditionsItemZeroLeftOperand_HiddenField",
    "ConditionGroupConditionsItemZeroLeftOperand_Variable",
    "ConditionGroupConditionsItemZeroOperator",
    "ConditionGroupConditionsItemZeroRightOperand",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldElement",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldHiddenField",
    "ConditionGroupConditionsItemZeroRightOperandHiddenFieldVariable",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_Element",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_HiddenField",
    "ConditionGroupConditionsItemZeroRightOperandHiddenField_Variable",
    "ConditionGroupConditionsItemZeroRightOperandStatic",
    "ConditionGroupConditionsItemZeroRightOperandStaticValue",
    "ConditionGroupConditionsItemZeroRightOperand_HiddenField",
    "ConditionGroupConditionsItemZeroRightOperand_Static",
    "ConditionGroupConnector",
    "Contact",
    "ContactAttribute",
    "ContactAttributeKey",
    "ContactAttributeKeyId",
    "ContactAttributeKeyType",
    "Health",
    "Me",
    "MeEnvironmentsItem",
    "MeEnvironmentsItemEnvironmentType",
    "MeEnvironmentsItemPermission",
    "MeOrganizationAccess",
    "MeOrganizationAccessAccessControl",
    "MeResponse",
    "MeResponseEnvironmentsItem",
    "MeResponseEnvironmentsItemEnvironmentType",
    "MeResponseEnvironmentsItemPermission",
    "MeResponseOrganizationAccess",
    "MeResponseOrganizationAccessAccessControl",
    "MeResponseWorkspacesItem",
    "MeResponseWorkspacesItemEnvironmentType",
    "MeResponseWorkspacesItemPermission",
    "MeWorkspacesItem",
    "MeWorkspacesItemEnvironmentType",
    "MeWorkspacesItemPermission",
    "NotFoundErrorBody",
    "OrganizationId",
    "Response",
    "ResponseDataValue",
    "ResponseId",
    "ResponseMeta",
    "ResponseMetaUserAgent",
    "ResponseVariablesValue",
    "Role",
    "RoleDataItem",
    "RoleDataItemOne",
    "RoleDataItemThree",
    "RoleDataItemTwo",
    "RoleDataItemZero",
    "Survey",
    "SurveyBlocksItem",
    "SurveyBlocksItemElementsItem",
    "SurveyBlocksItemElementsItemAddressLine1",
    "SurveyBlocksItemElementsItemAddressLine1AddressLine1",
    "SurveyBlocksItemElementsItemAddressLine1AddressLine2",
    "SurveyBlocksItemElementsItemAddressLine1City",
    "SurveyBlocksItemElementsItemAddressLine1Country",
    "SurveyBlocksItemElementsItemAddressLine1Scale",
    "SurveyBlocksItemElementsItemAddressLine1State",
    "SurveyBlocksItemElementsItemAddressLine1Type",
    "SurveyBlocksItemElementsItemAddressLine1Zip",
    "SurveyBlocksItemElementsItemAllowMulti",
    "SurveyBlocksItemElementsItemAllowMultiChoicesItem",
    "SurveyBlocksItemElementsItemAllowMultiScale",
    "SurveyBlocksItemElementsItemAllowMultiType",
    "SurveyBlocksItemElementsItemAllowMultipleFiles",
    "SurveyBlocksItemElementsItemAllowMultipleFilesAllowedFileExtensionsItem",
    "SurveyBlocksItemElementsItemAllowMultipleFilesScale",
    "SurveyBlocksItemElementsItemAllowMultipleFilesType",
    "SurveyBlocksItemElementsItemButtonExternal",
    "SurveyBlocksItemElementsItemButtonExternalScale",
    "SurveyBlocksItemElementsItemButtonExternalType",
    "SurveyBlocksItemElementsItemCalHost",
    "SurveyBlocksItemElementsItemCalHostScale",
    "SurveyBlocksItemElementsItemCalHostType",
    "SurveyBlocksItemElementsItemCharLimit",
    "SurveyBlocksItemElementsItemCharLimitCharLimit",
    "SurveyBlocksItemElementsItemCharLimitInputType",
    "SurveyBlocksItemElementsItemCharLimitScale",
    "SurveyBlocksItemElementsItemCharLimitType",
    "SurveyBlocksItemElementsItemChoices",
    "SurveyBlocksItemElementsItemChoicesChoicesItem",
    "SurveyBlocksItemElementsItemChoicesScale",
    "SurveyBlocksItemElementsItemChoicesShuffleOption",
    "SurveyBlocksItemElementsItemChoicesType",
    "SurveyBlocksItemElementsItemColumns",
    "SurveyBlocksItemElementsItemColumnsColumnsItem",
    "SurveyBlocksItemElementsItemColumnsRowsItem",
    "SurveyBlocksItemElementsItemColumnsScale",
    "SurveyBlocksItemElementsItemColumnsShuffleOption",
    "SurveyBlocksItemElementsItemColumnsType",
    "SurveyBlocksItemElementsItemCompany",
    "SurveyBlocksItemElementsItemCompanyCompany",
    "SurveyBlocksItemElementsItemCompanyEmail",
    "SurveyBlocksItemElementsItemCompanyFirstName",
    "SurveyBlocksItemElementsItemCompanyLastName",
    "SurveyBlocksItemElementsItemCompanyPhone",
    "SurveyBlocksItemElementsItemCompanyScale",
    "SurveyBlocksItemElementsItemCompanyType",
    "SurveyBlocksItemElementsItemFive",
    "SurveyBlocksItemElementsItemFiveScale",
    "SurveyBlocksItemElementsItemFiveType",
    "SurveyBlocksItemElementsItemFormat",
    "SurveyBlocksItemElementsItemFormatFormat",
    "SurveyBlocksItemElementsItemFormatScale",
    "SurveyBlocksItemElementsItemFormatType",
    "SurveyBlocksItemElementsItemLabel",
    "SurveyBlocksItemElementsItemLabelScale",
    "SurveyBlocksItemElementsItemLabelType",
    "SurveyBlocksItemElementsItemThree",
    "SurveyBlocksItemElementsItemThreeScale",
    "SurveyBlocksItemElementsItemThreeType",
    "SurveyBlocksItemElementsItemTwo",
    "SurveyBlocksItemElementsItemTwoChoicesItem",
    "SurveyBlocksItemElementsItemTwoScale",
    "SurveyBlocksItemElementsItemTwoShuffleOption",
    "SurveyBlocksItemElementsItemTwoType",
    "SurveyBlocksItemElementsItemTwoTypeOne",
    "SurveyBlocksItemElementsItemTwoTypeZero",
    "SurveyBlocksItemLogicItem",
    "SurveyBlocksItemLogicItemActionsItem",
    "SurveyBlocksItemLogicItemActionsItemCalculate",
    "SurveyBlocksItemLogicItemActionsItemCalculateOne",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneObjective",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneOperator",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldElement",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldHiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenFieldVariable",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Element",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_HiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueHiddenField_Variable",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValueStatic",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue_HiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateOneValue_Static",
    "SurveyBlocksItemLogicItemActionsItemCalculateZero",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldElement",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldHiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenFieldVariable",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Element",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_HiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueHiddenField_Variable",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValueStatic",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_HiddenField",
    "SurveyBlocksItemLogicItemActionsItemCalculateZeroValue_Static",
    "SurveyBlocksItemLogicItemActionsItemJumpToBlock",
    "SurveyBlocksItemLogicItemActionsItemRequireAnswer",
    "SurveyBlocksItemLogicItemActionsItem_Calculate",
    "SurveyBlocksItemLogicItemActionsItem_JumpToBlock",
    "SurveyBlocksItemLogicItemActionsItem_RequireAnswer",
    "SurveyDisplayOption",
    "SurveyEndingsItem",
    "SurveyEndingsItemEndScreen",
    "SurveyEndingsItemRedirectToUrl",
    "SurveyEndingsItem_EndScreen",
    "SurveyEndingsItem_RedirectToUrl",
    "SurveyHiddenFields",
    "SurveyMetadata",
    "SurveyRecaptcha",
    "SurveySingleUse",
    "SurveyStatus",
    "SurveyStyling",
    "SurveyStylingBackground",
    "SurveyStylingBackgroundBgType",
    "SurveyStylingBrandColor",
    "SurveyStylingCardArrangement",
    "SurveyStylingCardArrangementAppSurveys",
    "SurveyStylingCardArrangementLinkSurveys",
    "SurveyStylingCardBackgroundColor",
    "SurveyStylingCardBorderColor",
    "SurveyStylingHighlightBorderColor",
    "SurveyStylingInputBorderColor",
    "SurveyStylingLogo",
    "SurveySurveyClosedMessage",
    "SurveyType",
    "SurveyVariablesItem",
    "SurveyVariablesItemNumber",
    "SurveyVariablesItemText",
    "SurveyVariablesItem_Number",
    "SurveyVariablesItem_Text",
    "SurveyWelcomeCard",
    "SurveyWorkspaceOverwrites",
    "SurveyWorkspaceOverwritesOverlay",
    "SurveyWorkspaceOverwritesPlacement",
    "Team",
    "TeamId",
    "User",
    "UserRole",
    "Webhook",
    "WebhookId",
    "WebhookSource",
    "WebhookTriggersItem",
    "WorkspaceTeam",
    "WorkspaceTeamPermission",
]
