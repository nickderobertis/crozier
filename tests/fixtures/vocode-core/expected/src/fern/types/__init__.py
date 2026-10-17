



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_connection_page import AccountConnectionPage
    from .account_connection_page_items_item import (
        AccountConnectionPageItemsItem,
        AccountConnectionPageItemsItem_AccountConnectionOpenai,
        AccountConnectionPageItemsItem_AccountConnectionTwilio,
    )
    from .account_connection_params_request import (
        AccountConnectionParamsRequest,
        AccountConnectionParamsRequest_AccountConnectionOpenai,
        AccountConnectionParamsRequest_AccountConnectionTwilio,
    )
    from .account_connection_response_model import (
        AccountConnectionResponseModel,
        AccountConnectionResponseModel_AccountConnectionOpenai,
        AccountConnectionResponseModel_AccountConnectionTwilio,
    )
    from .account_connection_update_params_request import (
        AccountConnectionUpdateParamsRequest,
        AccountConnectionUpdateParamsRequest_AccountConnectionOpenai,
        AccountConnectionUpdateParamsRequest_AccountConnectionTwilio,
    )
    from .action_page import ActionPage
    from .action_page_items_item import (
        ActionPageItemsItem,
        ActionPageItemsItem_ActionAddToConference,
        ActionPageItemsItem_ActionDtmf,
        ActionPageItemsItem_ActionEndConversation,
        ActionPageItemsItem_ActionExternal,
        ActionPageItemsItem_ActionSetHold,
        ActionPageItemsItem_ActionTransferCall,
    )
    from .action_params_request import (
        ActionParamsRequest,
        ActionParamsRequest_ActionAddToConference,
        ActionParamsRequest_ActionDtmf,
        ActionParamsRequest_ActionEndConversation,
        ActionParamsRequest_ActionExternal,
        ActionParamsRequest_ActionSetHold,
        ActionParamsRequest_ActionTransferCall,
    )
    from .action_response_model import (
        ActionResponseModel,
        ActionResponseModel_ActionAddToConference,
        ActionResponseModel_ActionDtmf,
        ActionResponseModel_ActionEndConversation,
        ActionResponseModel_ActionExternal,
        ActionResponseModel_ActionSetHold,
        ActionResponseModel_ActionTransferCall,
    )
    from .action_update_params_request import (
        ActionUpdateParamsRequest,
        ActionUpdateParamsRequest_ActionAddToConference,
        ActionUpdateParamsRequest_ActionDtmf,
        ActionUpdateParamsRequest_ActionEndConversation,
        ActionUpdateParamsRequest_ActionExternal,
        ActionUpdateParamsRequest_ActionSetHold,
        ActionUpdateParamsRequest_ActionTransferCall,
    )
    from .add_to_conference_action import AddToConferenceAction
    from .add_to_conference_action_action_trigger import (
        AddToConferenceActionActionTrigger,
        AddToConferenceActionActionTrigger_ActionTriggerFunctionCall,
        AddToConferenceActionActionTrigger_ActionTriggerPhraseBased,
    )
    from .add_to_conference_action_params import AddToConferenceActionParams
    from .add_to_conference_action_params_action_trigger import (
        AddToConferenceActionParamsActionTrigger,
        AddToConferenceActionParamsActionTrigger_ActionTriggerFunctionCall,
        AddToConferenceActionParamsActionTrigger_ActionTriggerPhraseBased,
    )
    from .add_to_conference_action_update_params import AddToConferenceActionUpdateParams
    from .add_to_conference_action_update_params_action_trigger import AddToConferenceActionUpdateParamsActionTrigger
    from .add_to_conference_action_update_params_action_trigger_zero import (
        AddToConferenceActionUpdateParamsActionTriggerZero,
        AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall,
        AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased,
    )
    from .add_to_conference_action_update_params_config import AddToConferenceActionUpdateParamsConfig
    from .add_to_conference_config import AddToConferenceConfig
    from .add_to_steering_pool_request import AddToSteeringPoolRequest
    from .agent import Agent
    from .agent_actions_item import (
        AgentActionsItem,
        AgentActionsItem_ActionAddToConference,
        AgentActionsItem_ActionDtmf,
        AgentActionsItem_ActionEndConversation,
        AgentActionsItem_ActionExternal,
        AgentActionsItem_ActionSetHold,
        AgentActionsItem_ActionTransferCall,
    )
    from .agent_deepgram_keywords_value import AgentDeepgramKeywordsValue
    from .agent_endpointing_sensitivity import AgentEndpointingSensitivity
    from .agent_ivr_navigation_mode import AgentIvrNavigationMode
    from .agent_page import AgentPage
    from .agent_params import AgentParams
    from .agent_params_actions_item import AgentParamsActionsItem
    from .agent_params_actions_item_one import (
        AgentParamsActionsItemOne,
        AgentParamsActionsItemOne_ActionAddToConference,
        AgentParamsActionsItemOne_ActionDtmf,
        AgentParamsActionsItemOne_ActionEndConversation,
        AgentParamsActionsItemOne_ActionExternal,
        AgentParamsActionsItemOne_ActionSetHold,
        AgentParamsActionsItemOne_ActionTransferCall,
    )
    from .agent_params_deepgram_keywords_value import AgentParamsDeepgramKeywordsValue
    from .agent_params_endpointing_sensitivity import AgentParamsEndpointingSensitivity
    from .agent_params_ivr_navigation_mode import AgentParamsIvrNavigationMode
    from .agent_params_openai_account_connection import AgentParamsOpenaiAccountConnection
    from .agent_params_prompt import AgentParamsPrompt
    from .agent_params_vector_database import AgentParamsVectorDatabase
    from .agent_params_voice import AgentParamsVoice
    from .agent_params_voice_one import (
        AgentParamsVoiceOne,
        AgentParamsVoiceOne_VoiceAzure,
        AgentParamsVoiceOne_VoiceElevenLabs,
        AgentParamsVoiceOne_VoicePlayHt,
        AgentParamsVoiceOne_VoiceRime,
        AgentParamsVoiceOne_VoiceVocode,
    )
    from .agent_params_webhook import AgentParamsWebhook
    from .agent_update_params import AgentUpdateParams
    from .agent_update_params_actions import AgentUpdateParamsActions
    from .agent_update_params_actions_zero_item import AgentUpdateParamsActionsZeroItem
    from .agent_update_params_actions_zero_item_one import (
        AgentUpdateParamsActionsZeroItemOne,
        AgentUpdateParamsActionsZeroItemOne_ActionAddToConference,
        AgentUpdateParamsActionsZeroItemOne_ActionDtmf,
        AgentUpdateParamsActionsZeroItemOne_ActionEndConversation,
        AgentUpdateParamsActionsZeroItemOne_ActionExternal,
        AgentUpdateParamsActionsZeroItemOne_ActionSetHold,
        AgentUpdateParamsActionsZeroItemOne_ActionTransferCall,
    )
    from .agent_update_params_ask_if_human_present_on_idle import AgentUpdateParamsAskIfHumanPresentOnIdle
    from .agent_update_params_context_endpoint import AgentUpdateParamsContextEndpoint
    from .agent_update_params_conversation_speed import AgentUpdateParamsConversationSpeed
    from .agent_update_params_deepgram_keywords import AgentUpdateParamsDeepgramKeywords
    from .agent_update_params_deepgram_keywords_zero_value import AgentUpdateParamsDeepgramKeywordsZeroValue
    from .agent_update_params_endpointing_sensitivity import AgentUpdateParamsEndpointingSensitivity
    from .agent_update_params_endpointing_sensitivity_zero import AgentUpdateParamsEndpointingSensitivityZero
    from .agent_update_params_idle_time_seconds import AgentUpdateParamsIdleTimeSeconds
    from .agent_update_params_initial_message import AgentUpdateParamsInitialMessage
    from .agent_update_params_initial_message_delay import AgentUpdateParamsInitialMessageDelay
    from .agent_update_params_interrupt_sensitivity import AgentUpdateParamsInterruptSensitivity
    from .agent_update_params_ivr_navigation_mode import AgentUpdateParamsIvrNavigationMode
    from .agent_update_params_ivr_navigation_mode_zero import AgentUpdateParamsIvrNavigationModeZero
    from .agent_update_params_language import AgentUpdateParamsLanguage
    from .agent_update_params_llm_fallback import AgentUpdateParamsLlmFallback
    from .agent_update_params_name import AgentUpdateParamsName
    from .agent_update_params_noise_suppression import AgentUpdateParamsNoiseSuppression
    from .agent_update_params_openai_account_connection import AgentUpdateParamsOpenaiAccountConnection
    from .agent_update_params_openai_model_name_override import AgentUpdateParamsOpenaiModelNameOverride
    from .agent_update_params_prompt import AgentUpdateParamsPrompt
    from .agent_update_params_run_do_not_call_detection import AgentUpdateParamsRunDoNotCallDetection
    from .agent_update_params_vector_database import AgentUpdateParamsVectorDatabase
    from .agent_update_params_voice import AgentUpdateParamsVoice
    from .agent_update_params_voice_one import (
        AgentUpdateParamsVoiceOne,
        AgentUpdateParamsVoiceOne_VoiceAzure,
        AgentUpdateParamsVoiceOne_VoiceElevenLabs,
        AgentUpdateParamsVoiceOne_VoicePlayHt,
        AgentUpdateParamsVoiceOne_VoiceRime,
        AgentUpdateParamsVoiceOne_VoiceVocode,
    )
    from .agent_update_params_webhook import AgentUpdateParamsWebhook
    from .agent_voice import (
        AgentVoice,
        AgentVoice_VoiceAzure,
        AgentVoice_VoiceElevenLabs,
        AgentVoice_VoicePlayHt,
        AgentVoice_VoiceRime,
        AgentVoice_VoiceVocode,
    )
    from .azure_voice import AzureVoice
    from .azure_voice_params import AzureVoiceParams
    from .azure_voice_update_params import AzureVoiceUpdateParams
    from .azure_voice_update_params_pitch import AzureVoiceUpdateParamsPitch
    from .azure_voice_update_params_rate import AzureVoiceUpdateParamsRate
    from .azure_voice_update_params_voice_name import AzureVoiceUpdateParamsVoiceName
    from .call import Call
    from .call_human_detection_result import CallHumanDetectionResult
    from .call_on_no_human_answer import CallOnNoHumanAnswer
    from .call_page import CallPage
    from .call_stage import CallStage
    from .call_stage_outcome import CallStageOutcome
    from .call_status import CallStatus
    from .call_telephony_metadata import (
        CallTelephonyMetadata,
        CallTelephonyMetadata_TelephonyMetadataTwilio,
        CallTelephonyMetadata_TelephonyMetadataVonage,
    )
    from .call_telephony_provider import CallTelephonyProvider
    from .collect_field import CollectField
    from .collect_field_field_type import CollectFieldFieldType
    from .create_call_agent_params import CreateCallAgentParams
    from .create_call_agent_params_actions_item import CreateCallAgentParamsActionsItem
    from .create_call_agent_params_actions_item_one import (
        CreateCallAgentParamsActionsItemOne,
        CreateCallAgentParamsActionsItemOne_ActionAddToConference,
        CreateCallAgentParamsActionsItemOne_ActionDtmf,
        CreateCallAgentParamsActionsItemOne_ActionEndConversation,
        CreateCallAgentParamsActionsItemOne_ActionExternal,
        CreateCallAgentParamsActionsItemOne_ActionSetHold,
        CreateCallAgentParamsActionsItemOne_ActionTransferCall,
    )
    from .create_call_agent_params_deepgram_keywords_value import CreateCallAgentParamsDeepgramKeywordsValue
    from .create_call_agent_params_endpointing_sensitivity import CreateCallAgentParamsEndpointingSensitivity
    from .create_call_agent_params_ivr_navigation_mode import CreateCallAgentParamsIvrNavigationMode
    from .create_call_agent_params_openai_account_connection import CreateCallAgentParamsOpenaiAccountConnection
    from .create_call_agent_params_prompt import CreateCallAgentParamsPrompt
    from .create_call_agent_params_vector_database import CreateCallAgentParamsVectorDatabase
    from .create_call_agent_params_voice import CreateCallAgentParamsVoice
    from .create_call_agent_params_voice_one import (
        CreateCallAgentParamsVoiceOne,
        CreateCallAgentParamsVoiceOne_VoiceAzure,
        CreateCallAgentParamsVoiceOne_VoiceElevenLabs,
        CreateCallAgentParamsVoiceOne_VoicePlayHt,
        CreateCallAgentParamsVoiceOne_VoiceRime,
        CreateCallAgentParamsVoiceOne_VoiceVocode,
    )
    from .create_call_agent_params_webhook import CreateCallAgentParamsWebhook
    from .dtmf_action import DtmfAction
    from .dtmf_action_params import DtmfActionParams
    from .dtmf_action_update_params import DtmfActionUpdateParams
    from .dtmf_action_update_params_action_trigger import DtmfActionUpdateParamsActionTrigger
    from .dtmf_action_update_params_config import DtmfActionUpdateParamsConfig
    from .eleven_labs_voice import ElevenLabsVoice
    from .eleven_labs_voice_params import ElevenLabsVoiceParams
    from .eleven_labs_voice_update_params import ElevenLabsVoiceUpdateParams
    from .eleven_labs_voice_update_params_api_key import ElevenLabsVoiceUpdateParamsApiKey
    from .eleven_labs_voice_update_params_experimental_input_streaming import (
        ElevenLabsVoiceUpdateParamsExperimentalInputStreaming,
    )
    from .eleven_labs_voice_update_params_model_id import ElevenLabsVoiceUpdateParamsModelId
    from .eleven_labs_voice_update_params_optimize_streaming_latency import (
        ElevenLabsVoiceUpdateParamsOptimizeStreamingLatency,
    )
    from .eleven_labs_voice_update_params_similarity_boost import ElevenLabsVoiceUpdateParamsSimilarityBoost
    from .eleven_labs_voice_update_params_stability import ElevenLabsVoiceUpdateParamsStability
    from .eleven_labs_voice_update_params_voice_id import ElevenLabsVoiceUpdateParamsVoiceId
    from .empty_action_config import EmptyActionConfig
    from .end_conversation_action import EndConversationAction
    from .end_conversation_action_action_trigger import (
        EndConversationActionActionTrigger,
        EndConversationActionActionTrigger_ActionTriggerFunctionCall,
        EndConversationActionActionTrigger_ActionTriggerPhraseBased,
    )
    from .end_conversation_action_params import EndConversationActionParams
    from .end_conversation_action_params_action_trigger import (
        EndConversationActionParamsActionTrigger,
        EndConversationActionParamsActionTrigger_ActionTriggerFunctionCall,
        EndConversationActionParamsActionTrigger_ActionTriggerPhraseBased,
    )
    from .end_conversation_action_update_params import EndConversationActionUpdateParams
    from .end_conversation_action_update_params_action_trigger import EndConversationActionUpdateParamsActionTrigger
    from .end_conversation_action_update_params_action_trigger_zero import (
        EndConversationActionUpdateParamsActionTriggerZero,
        EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall,
        EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased,
    )
    from .end_conversation_action_update_params_config import EndConversationActionUpdateParamsConfig
    from .event_type import EventType
    from .external_action import ExternalAction
    from .external_action_config import ExternalActionConfig
    from .external_action_config_processing_mode import ExternalActionConfigProcessingMode
    from .external_action_params import ExternalActionParams
    from .external_action_update_params import ExternalActionUpdateParams
    from .external_action_update_params_action_trigger import ExternalActionUpdateParamsActionTrigger
    from .external_action_update_params_config import ExternalActionUpdateParamsConfig
    from .function_call_action_trigger import FunctionCallActionTrigger
    from .function_call_action_trigger_config import FunctionCallActionTriggerConfig
    from .function_call_action_trigger_type import FunctionCallActionTriggerType
    from .http_method import HttpMethod
    from .http_validation_error import HttpValidationError
    from .internal_llm_fallback import InternalLlmFallback
    from .internal_llm_fallback_provider import InternalLlmFallbackProvider
    from .interrupt_sensitivity import InterruptSensitivity
    from .language import Language
    from .normalized_agent import NormalizedAgent
    from .normalized_agent_deepgram_keywords_value import NormalizedAgentDeepgramKeywordsValue
    from .normalized_agent_endpointing_sensitivity import NormalizedAgentEndpointingSensitivity
    from .normalized_agent_ivr_navigation_mode import NormalizedAgentIvrNavigationMode
    from .normalized_agent_openai_account_connection import NormalizedAgentOpenaiAccountConnection
    from .normalized_agent_prompt import NormalizedAgentPrompt
    from .normalized_agent_vector_database import NormalizedAgentVectorDatabase
    from .normalized_call import NormalizedCall
    from .normalized_call_human_detection_result import NormalizedCallHumanDetectionResult
    from .normalized_call_on_no_human_answer import NormalizedCallOnNoHumanAnswer
    from .normalized_call_stage import NormalizedCallStage
    from .normalized_call_stage_outcome import NormalizedCallStageOutcome
    from .normalized_call_telephony_account_connection import NormalizedCallTelephonyAccountConnection
    from .normalized_call_telephony_metadata import (
        NormalizedCallTelephonyMetadata,
        NormalizedCallTelephonyMetadata_TelephonyMetadataTwilio,
        NormalizedCallTelephonyMetadata_TelephonyMetadataVonage,
    )
    from .normalized_call_telephony_provider import NormalizedCallTelephonyProvider
    from .normalized_phone_number import NormalizedPhoneNumber
    from .normalized_phone_number_telephony_account_connection import NormalizedPhoneNumberTelephonyAccountConnection
    from .normalized_phone_number_telephony_provider import NormalizedPhoneNumberTelephonyProvider
    from .normalized_prompt import NormalizedPrompt
    from .open_ai_account_connection import OpenAiAccountConnection
    from .open_ai_account_connection_params import OpenAiAccountConnectionParams
    from .open_ai_account_connection_type import OpenAiAccountConnectionType
    from .open_ai_account_connection_update_params import OpenAiAccountConnectionUpdateParams
    from .open_ai_account_connection_update_params_credentials import OpenAiAccountConnectionUpdateParamsCredentials
    from .open_ai_credentials import OpenAiCredentials
    from .phone_number import PhoneNumber
    from .phone_number_page import PhoneNumberPage
    from .phone_number_telephony_provider import PhoneNumberTelephonyProvider
    from .phrase_based_action_trigger_config import PhraseBasedActionTriggerConfig
    from .phrase_based_action_trigger_input import PhraseBasedActionTriggerInput
    from .phrase_based_action_trigger_output import PhraseBasedActionTriggerOutput
    from .phrase_trigger import PhraseTrigger
    from .phrase_trigger_conditions_item import PhraseTriggerConditionsItem
    from .pinecone_vector_database import PineconeVectorDatabase
    from .pinecone_vector_database_params import PineconeVectorDatabaseParams
    from .pinecone_vector_database_params_type import PineconeVectorDatabaseParamsType
    from .pinecone_vector_database_type import PineconeVectorDatabaseType
    from .pinecone_vector_database_update_params import PineconeVectorDatabaseUpdateParams
    from .pinecone_vector_database_update_params_api_environment import PineconeVectorDatabaseUpdateParamsApiEnvironment
    from .pinecone_vector_database_update_params_api_key import PineconeVectorDatabaseUpdateParamsApiKey
    from .pinecone_vector_database_update_params_index import PineconeVectorDatabaseUpdateParamsIndex
    from .pinecone_vector_database_update_params_type import PineconeVectorDatabaseUpdateParamsType
    from .plan_type import PlanType
    from .play_ht_voice import PlayHtVoice
    from .play_ht_voice_params import PlayHtVoiceParams
    from .play_ht_voice_params_quality import PlayHtVoiceParamsQuality
    from .play_ht_voice_params_version import PlayHtVoiceParamsVersion
    from .play_ht_voice_quality import PlayHtVoiceQuality
    from .play_ht_voice_update_params import PlayHtVoiceUpdateParams
    from .play_ht_voice_update_params_api_key import PlayHtVoiceUpdateParamsApiKey
    from .play_ht_voice_update_params_api_user_id import PlayHtVoiceUpdateParamsApiUserId
    from .play_ht_voice_update_params_experimental_remove_silence import (
        PlayHtVoiceUpdateParamsExperimentalRemoveSilence,
    )
    from .play_ht_voice_update_params_quality import PlayHtVoiceUpdateParamsQuality
    from .play_ht_voice_update_params_quality_zero import PlayHtVoiceUpdateParamsQualityZero
    from .play_ht_voice_update_params_speed import PlayHtVoiceUpdateParamsSpeed
    from .play_ht_voice_update_params_temperature import PlayHtVoiceUpdateParamsTemperature
    from .play_ht_voice_update_params_text_guidance import PlayHtVoiceUpdateParamsTextGuidance
    from .play_ht_voice_update_params_top_p import PlayHtVoiceUpdateParamsTopP
    from .play_ht_voice_update_params_version import PlayHtVoiceUpdateParamsVersion
    from .play_ht_voice_update_params_version_zero import PlayHtVoiceUpdateParamsVersionZero
    from .play_ht_voice_update_params_voice_guidance import PlayHtVoiceUpdateParamsVoiceGuidance
    from .play_ht_voice_update_params_voice_id import PlayHtVoiceUpdateParamsVoiceId
    from .play_ht_voice_version import PlayHtVoiceVersion
    from .prompt import Prompt
    from .prompt_page import PromptPage
    from .prompt_params import PromptParams
    from .prompt_params_prompt_template import PromptParamsPromptTemplate
    from .prompt_template import PromptTemplate
    from .prompt_update_params import PromptUpdateParams
    from .prompt_update_params_collect_fields import PromptUpdateParamsCollectFields
    from .prompt_update_params_content import PromptUpdateParamsContent
    from .prompt_update_params_context_endpoint import PromptUpdateParamsContextEndpoint
    from .prompt_update_params_prompt_template import PromptUpdateParamsPromptTemplate
    from .rime_voice import RimeVoice
    from .rime_voice_model_id import RimeVoiceModelId
    from .rime_voice_model_id_zero import RimeVoiceModelIdZero
    from .rime_voice_params import RimeVoiceParams
    from .rime_voice_params_model_id import RimeVoiceParamsModelId
    from .rime_voice_params_model_id_zero import RimeVoiceParamsModelIdZero
    from .rime_voice_update_params import RimeVoiceUpdateParams
    from .rime_voice_update_params_model_id import RimeVoiceUpdateParamsModelId
    from .rime_voice_update_params_model_id_zero import RimeVoiceUpdateParamsModelIdZero
    from .rime_voice_update_params_speaker import RimeVoiceUpdateParamsSpeaker
    from .rime_voice_update_params_speed_alpha import RimeVoiceUpdateParamsSpeedAlpha
    from .set_hold_action import SetHoldAction
    from .set_hold_action_action_trigger import (
        SetHoldActionActionTrigger,
        SetHoldActionActionTrigger_ActionTriggerFunctionCall,
        SetHoldActionActionTrigger_ActionTriggerPhraseBased,
    )
    from .set_hold_action_params import SetHoldActionParams
    from .set_hold_action_params_action_trigger import (
        SetHoldActionParamsActionTrigger,
        SetHoldActionParamsActionTrigger_ActionTriggerFunctionCall,
        SetHoldActionParamsActionTrigger_ActionTriggerPhraseBased,
    )
    from .set_hold_action_update_params import SetHoldActionUpdateParams
    from .set_hold_action_update_params_action_trigger import SetHoldActionUpdateParamsActionTrigger
    from .set_hold_action_update_params_action_trigger_zero import (
        SetHoldActionUpdateParamsActionTriggerZero,
        SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall,
        SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased,
    )
    from .set_hold_action_update_params_config import SetHoldActionUpdateParamsConfig
    from .transfer_call_action import TransferCallAction
    from .transfer_call_action_action_trigger import (
        TransferCallActionActionTrigger,
        TransferCallActionActionTrigger_ActionTriggerFunctionCall,
        TransferCallActionActionTrigger_ActionTriggerPhraseBased,
    )
    from .transfer_call_action_params import TransferCallActionParams
    from .transfer_call_action_params_action_trigger import (
        TransferCallActionParamsActionTrigger,
        TransferCallActionParamsActionTrigger_ActionTriggerFunctionCall,
        TransferCallActionParamsActionTrigger_ActionTriggerPhraseBased,
    )
    from .transfer_call_action_update_params import TransferCallActionUpdateParams
    from .transfer_call_action_update_params_action_trigger import TransferCallActionUpdateParamsActionTrigger
    from .transfer_call_action_update_params_action_trigger_zero import (
        TransferCallActionUpdateParamsActionTriggerZero,
        TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall,
        TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased,
    )
    from .transfer_call_action_update_params_config import TransferCallActionUpdateParamsConfig
    from .transfer_call_config import TransferCallConfig
    from .twilio_account_connection import TwilioAccountConnection
    from .twilio_account_connection_params import TwilioAccountConnectionParams
    from .twilio_account_connection_type import TwilioAccountConnectionType
    from .twilio_account_connection_update_params import TwilioAccountConnectionUpdateParams
    from .twilio_account_connection_update_params_credentials import TwilioAccountConnectionUpdateParamsCredentials
    from .twilio_credentials import TwilioCredentials
    from .twilio_telephony_metadata import TwilioTelephonyMetadata
    from .undefined import Undefined
    from .usage import Usage
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .vector_database_page import VectorDatabasePage
    from .vocode_voice import VocodeVoice
    from .vocode_voice_params import VocodeVoiceParams
    from .vocode_voice_params_voice_id import VocodeVoiceParamsVoiceId
    from .vocode_voice_update_params import VocodeVoiceUpdateParams
    from .vocode_voice_update_params_voice_id import VocodeVoiceUpdateParamsVoiceId
    from .vocode_voice_update_params_voice_id_zero import VocodeVoiceUpdateParamsVoiceIdZero
    from .vocode_voice_voice_id import VocodeVoiceVoiceId
    from .voice_page import VoicePage
    from .voice_page_items_item import (
        VoicePageItemsItem,
        VoicePageItemsItem_VoiceAzure,
        VoicePageItemsItem_VoiceElevenLabs,
        VoicePageItemsItem_VoicePlayHt,
        VoicePageItemsItem_VoiceRime,
        VoicePageItemsItem_VoiceVocode,
    )
    from .voice_params_request import (
        VoiceParamsRequest,
        VoiceParamsRequest_VoiceAzure,
        VoiceParamsRequest_VoiceElevenLabs,
        VoiceParamsRequest_VoicePlayHt,
        VoiceParamsRequest_VoiceRime,
        VoiceParamsRequest_VoiceVocode,
    )
    from .voice_response_model import (
        VoiceResponseModel,
        VoiceResponseModel_VoiceAzure,
        VoiceResponseModel_VoiceElevenLabs,
        VoiceResponseModel_VoicePlayHt,
        VoiceResponseModel_VoiceRime,
        VoiceResponseModel_VoiceVocode,
    )
    from .voice_update_params_request import (
        VoiceUpdateParamsRequest,
        VoiceUpdateParamsRequest_VoiceAzure,
        VoiceUpdateParamsRequest_VoiceElevenLabs,
        VoiceUpdateParamsRequest_VoicePlayHt,
        VoiceUpdateParamsRequest_VoiceRime,
        VoiceUpdateParamsRequest_VoiceVocode,
    )
    from .vonage_telephony_metadata import VonageTelephonyMetadata
    from .webhook import Webhook
    from .webhook_page import WebhookPage
    from .webhook_params import WebhookParams
    from .webhook_update_params import WebhookUpdateParams
    from .webhook_update_params_method import WebhookUpdateParamsMethod
    from .webhook_update_params_subscriptions import WebhookUpdateParamsSubscriptions
    from .webhook_update_params_url import WebhookUpdateParamsUrl
_dynamic_imports: typing.Dict[str, str] = {
    "AccountConnectionPage": ".account_connection_page",
    "AccountConnectionPageItemsItem": ".account_connection_page_items_item",
    "AccountConnectionPageItemsItem_AccountConnectionOpenai": ".account_connection_page_items_item",
    "AccountConnectionPageItemsItem_AccountConnectionTwilio": ".account_connection_page_items_item",
    "AccountConnectionParamsRequest": ".account_connection_params_request",
    "AccountConnectionParamsRequest_AccountConnectionOpenai": ".account_connection_params_request",
    "AccountConnectionParamsRequest_AccountConnectionTwilio": ".account_connection_params_request",
    "AccountConnectionResponseModel": ".account_connection_response_model",
    "AccountConnectionResponseModel_AccountConnectionOpenai": ".account_connection_response_model",
    "AccountConnectionResponseModel_AccountConnectionTwilio": ".account_connection_response_model",
    "AccountConnectionUpdateParamsRequest": ".account_connection_update_params_request",
    "AccountConnectionUpdateParamsRequest_AccountConnectionOpenai": ".account_connection_update_params_request",
    "AccountConnectionUpdateParamsRequest_AccountConnectionTwilio": ".account_connection_update_params_request",
    "ActionPage": ".action_page",
    "ActionPageItemsItem": ".action_page_items_item",
    "ActionPageItemsItem_ActionAddToConference": ".action_page_items_item",
    "ActionPageItemsItem_ActionDtmf": ".action_page_items_item",
    "ActionPageItemsItem_ActionEndConversation": ".action_page_items_item",
    "ActionPageItemsItem_ActionExternal": ".action_page_items_item",
    "ActionPageItemsItem_ActionSetHold": ".action_page_items_item",
    "ActionPageItemsItem_ActionTransferCall": ".action_page_items_item",
    "ActionParamsRequest": ".action_params_request",
    "ActionParamsRequest_ActionAddToConference": ".action_params_request",
    "ActionParamsRequest_ActionDtmf": ".action_params_request",
    "ActionParamsRequest_ActionEndConversation": ".action_params_request",
    "ActionParamsRequest_ActionExternal": ".action_params_request",
    "ActionParamsRequest_ActionSetHold": ".action_params_request",
    "ActionParamsRequest_ActionTransferCall": ".action_params_request",
    "ActionResponseModel": ".action_response_model",
    "ActionResponseModel_ActionAddToConference": ".action_response_model",
    "ActionResponseModel_ActionDtmf": ".action_response_model",
    "ActionResponseModel_ActionEndConversation": ".action_response_model",
    "ActionResponseModel_ActionExternal": ".action_response_model",
    "ActionResponseModel_ActionSetHold": ".action_response_model",
    "ActionResponseModel_ActionTransferCall": ".action_response_model",
    "ActionUpdateParamsRequest": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionAddToConference": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionDtmf": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionEndConversation": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionExternal": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionSetHold": ".action_update_params_request",
    "ActionUpdateParamsRequest_ActionTransferCall": ".action_update_params_request",
    "AddToConferenceAction": ".add_to_conference_action",
    "AddToConferenceActionActionTrigger": ".add_to_conference_action_action_trigger",
    "AddToConferenceActionActionTrigger_ActionTriggerFunctionCall": ".add_to_conference_action_action_trigger",
    "AddToConferenceActionActionTrigger_ActionTriggerPhraseBased": ".add_to_conference_action_action_trigger",
    "AddToConferenceActionParams": ".add_to_conference_action_params",
    "AddToConferenceActionParamsActionTrigger": ".add_to_conference_action_params_action_trigger",
    "AddToConferenceActionParamsActionTrigger_ActionTriggerFunctionCall": ".add_to_conference_action_params_action_trigger",
    "AddToConferenceActionParamsActionTrigger_ActionTriggerPhraseBased": ".add_to_conference_action_params_action_trigger",
    "AddToConferenceActionUpdateParams": ".add_to_conference_action_update_params",
    "AddToConferenceActionUpdateParamsActionTrigger": ".add_to_conference_action_update_params_action_trigger",
    "AddToConferenceActionUpdateParamsActionTriggerZero": ".add_to_conference_action_update_params_action_trigger_zero",
    "AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall": ".add_to_conference_action_update_params_action_trigger_zero",
    "AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased": ".add_to_conference_action_update_params_action_trigger_zero",
    "AddToConferenceActionUpdateParamsConfig": ".add_to_conference_action_update_params_config",
    "AddToConferenceConfig": ".add_to_conference_config",
    "AddToSteeringPoolRequest": ".add_to_steering_pool_request",
    "Agent": ".agent",
    "AgentActionsItem": ".agent_actions_item",
    "AgentActionsItem_ActionAddToConference": ".agent_actions_item",
    "AgentActionsItem_ActionDtmf": ".agent_actions_item",
    "AgentActionsItem_ActionEndConversation": ".agent_actions_item",
    "AgentActionsItem_ActionExternal": ".agent_actions_item",
    "AgentActionsItem_ActionSetHold": ".agent_actions_item",
    "AgentActionsItem_ActionTransferCall": ".agent_actions_item",
    "AgentDeepgramKeywordsValue": ".agent_deepgram_keywords_value",
    "AgentEndpointingSensitivity": ".agent_endpointing_sensitivity",
    "AgentIvrNavigationMode": ".agent_ivr_navigation_mode",
    "AgentPage": ".agent_page",
    "AgentParams": ".agent_params",
    "AgentParamsActionsItem": ".agent_params_actions_item",
    "AgentParamsActionsItemOne": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionAddToConference": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionDtmf": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionEndConversation": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionExternal": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionSetHold": ".agent_params_actions_item_one",
    "AgentParamsActionsItemOne_ActionTransferCall": ".agent_params_actions_item_one",
    "AgentParamsDeepgramKeywordsValue": ".agent_params_deepgram_keywords_value",
    "AgentParamsEndpointingSensitivity": ".agent_params_endpointing_sensitivity",
    "AgentParamsIvrNavigationMode": ".agent_params_ivr_navigation_mode",
    "AgentParamsOpenaiAccountConnection": ".agent_params_openai_account_connection",
    "AgentParamsPrompt": ".agent_params_prompt",
    "AgentParamsVectorDatabase": ".agent_params_vector_database",
    "AgentParamsVoice": ".agent_params_voice",
    "AgentParamsVoiceOne": ".agent_params_voice_one",
    "AgentParamsVoiceOne_VoiceAzure": ".agent_params_voice_one",
    "AgentParamsVoiceOne_VoiceElevenLabs": ".agent_params_voice_one",
    "AgentParamsVoiceOne_VoicePlayHt": ".agent_params_voice_one",
    "AgentParamsVoiceOne_VoiceRime": ".agent_params_voice_one",
    "AgentParamsVoiceOne_VoiceVocode": ".agent_params_voice_one",
    "AgentParamsWebhook": ".agent_params_webhook",
    "AgentUpdateParams": ".agent_update_params",
    "AgentUpdateParamsActions": ".agent_update_params_actions",
    "AgentUpdateParamsActionsZeroItem": ".agent_update_params_actions_zero_item",
    "AgentUpdateParamsActionsZeroItemOne": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionAddToConference": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionDtmf": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionEndConversation": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionExternal": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionSetHold": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsActionsZeroItemOne_ActionTransferCall": ".agent_update_params_actions_zero_item_one",
    "AgentUpdateParamsAskIfHumanPresentOnIdle": ".agent_update_params_ask_if_human_present_on_idle",
    "AgentUpdateParamsContextEndpoint": ".agent_update_params_context_endpoint",
    "AgentUpdateParamsConversationSpeed": ".agent_update_params_conversation_speed",
    "AgentUpdateParamsDeepgramKeywords": ".agent_update_params_deepgram_keywords",
    "AgentUpdateParamsDeepgramKeywordsZeroValue": ".agent_update_params_deepgram_keywords_zero_value",
    "AgentUpdateParamsEndpointingSensitivity": ".agent_update_params_endpointing_sensitivity",
    "AgentUpdateParamsEndpointingSensitivityZero": ".agent_update_params_endpointing_sensitivity_zero",
    "AgentUpdateParamsIdleTimeSeconds": ".agent_update_params_idle_time_seconds",
    "AgentUpdateParamsInitialMessage": ".agent_update_params_initial_message",
    "AgentUpdateParamsInitialMessageDelay": ".agent_update_params_initial_message_delay",
    "AgentUpdateParamsInterruptSensitivity": ".agent_update_params_interrupt_sensitivity",
    "AgentUpdateParamsIvrNavigationMode": ".agent_update_params_ivr_navigation_mode",
    "AgentUpdateParamsIvrNavigationModeZero": ".agent_update_params_ivr_navigation_mode_zero",
    "AgentUpdateParamsLanguage": ".agent_update_params_language",
    "AgentUpdateParamsLlmFallback": ".agent_update_params_llm_fallback",
    "AgentUpdateParamsName": ".agent_update_params_name",
    "AgentUpdateParamsNoiseSuppression": ".agent_update_params_noise_suppression",
    "AgentUpdateParamsOpenaiAccountConnection": ".agent_update_params_openai_account_connection",
    "AgentUpdateParamsOpenaiModelNameOverride": ".agent_update_params_openai_model_name_override",
    "AgentUpdateParamsPrompt": ".agent_update_params_prompt",
    "AgentUpdateParamsRunDoNotCallDetection": ".agent_update_params_run_do_not_call_detection",
    "AgentUpdateParamsVectorDatabase": ".agent_update_params_vector_database",
    "AgentUpdateParamsVoice": ".agent_update_params_voice",
    "AgentUpdateParamsVoiceOne": ".agent_update_params_voice_one",
    "AgentUpdateParamsVoiceOne_VoiceAzure": ".agent_update_params_voice_one",
    "AgentUpdateParamsVoiceOne_VoiceElevenLabs": ".agent_update_params_voice_one",
    "AgentUpdateParamsVoiceOne_VoicePlayHt": ".agent_update_params_voice_one",
    "AgentUpdateParamsVoiceOne_VoiceRime": ".agent_update_params_voice_one",
    "AgentUpdateParamsVoiceOne_VoiceVocode": ".agent_update_params_voice_one",
    "AgentUpdateParamsWebhook": ".agent_update_params_webhook",
    "AgentVoice": ".agent_voice",
    "AgentVoice_VoiceAzure": ".agent_voice",
    "AgentVoice_VoiceElevenLabs": ".agent_voice",
    "AgentVoice_VoicePlayHt": ".agent_voice",
    "AgentVoice_VoiceRime": ".agent_voice",
    "AgentVoice_VoiceVocode": ".agent_voice",
    "AzureVoice": ".azure_voice",
    "AzureVoiceParams": ".azure_voice_params",
    "AzureVoiceUpdateParams": ".azure_voice_update_params",
    "AzureVoiceUpdateParamsPitch": ".azure_voice_update_params_pitch",
    "AzureVoiceUpdateParamsRate": ".azure_voice_update_params_rate",
    "AzureVoiceUpdateParamsVoiceName": ".azure_voice_update_params_voice_name",
    "Call": ".call",
    "CallHumanDetectionResult": ".call_human_detection_result",
    "CallOnNoHumanAnswer": ".call_on_no_human_answer",
    "CallPage": ".call_page",
    "CallStage": ".call_stage",
    "CallStageOutcome": ".call_stage_outcome",
    "CallStatus": ".call_status",
    "CallTelephonyMetadata": ".call_telephony_metadata",
    "CallTelephonyMetadata_TelephonyMetadataTwilio": ".call_telephony_metadata",
    "CallTelephonyMetadata_TelephonyMetadataVonage": ".call_telephony_metadata",
    "CallTelephonyProvider": ".call_telephony_provider",
    "CollectField": ".collect_field",
    "CollectFieldFieldType": ".collect_field_field_type",
    "CreateCallAgentParams": ".create_call_agent_params",
    "CreateCallAgentParamsActionsItem": ".create_call_agent_params_actions_item",
    "CreateCallAgentParamsActionsItemOne": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionAddToConference": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionDtmf": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionEndConversation": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionExternal": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionSetHold": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsActionsItemOne_ActionTransferCall": ".create_call_agent_params_actions_item_one",
    "CreateCallAgentParamsDeepgramKeywordsValue": ".create_call_agent_params_deepgram_keywords_value",
    "CreateCallAgentParamsEndpointingSensitivity": ".create_call_agent_params_endpointing_sensitivity",
    "CreateCallAgentParamsIvrNavigationMode": ".create_call_agent_params_ivr_navigation_mode",
    "CreateCallAgentParamsOpenaiAccountConnection": ".create_call_agent_params_openai_account_connection",
    "CreateCallAgentParamsPrompt": ".create_call_agent_params_prompt",
    "CreateCallAgentParamsVectorDatabase": ".create_call_agent_params_vector_database",
    "CreateCallAgentParamsVoice": ".create_call_agent_params_voice",
    "CreateCallAgentParamsVoiceOne": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsVoiceOne_VoiceAzure": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsVoiceOne_VoiceElevenLabs": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsVoiceOne_VoicePlayHt": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsVoiceOne_VoiceRime": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsVoiceOne_VoiceVocode": ".create_call_agent_params_voice_one",
    "CreateCallAgentParamsWebhook": ".create_call_agent_params_webhook",
    "DtmfAction": ".dtmf_action",
    "DtmfActionParams": ".dtmf_action_params",
    "DtmfActionUpdateParams": ".dtmf_action_update_params",
    "DtmfActionUpdateParamsActionTrigger": ".dtmf_action_update_params_action_trigger",
    "DtmfActionUpdateParamsConfig": ".dtmf_action_update_params_config",
    "ElevenLabsVoice": ".eleven_labs_voice",
    "ElevenLabsVoiceParams": ".eleven_labs_voice_params",
    "ElevenLabsVoiceUpdateParams": ".eleven_labs_voice_update_params",
    "ElevenLabsVoiceUpdateParamsApiKey": ".eleven_labs_voice_update_params_api_key",
    "ElevenLabsVoiceUpdateParamsExperimentalInputStreaming": ".eleven_labs_voice_update_params_experimental_input_streaming",
    "ElevenLabsVoiceUpdateParamsModelId": ".eleven_labs_voice_update_params_model_id",
    "ElevenLabsVoiceUpdateParamsOptimizeStreamingLatency": ".eleven_labs_voice_update_params_optimize_streaming_latency",
    "ElevenLabsVoiceUpdateParamsSimilarityBoost": ".eleven_labs_voice_update_params_similarity_boost",
    "ElevenLabsVoiceUpdateParamsStability": ".eleven_labs_voice_update_params_stability",
    "ElevenLabsVoiceUpdateParamsVoiceId": ".eleven_labs_voice_update_params_voice_id",
    "EmptyActionConfig": ".empty_action_config",
    "EndConversationAction": ".end_conversation_action",
    "EndConversationActionActionTrigger": ".end_conversation_action_action_trigger",
    "EndConversationActionActionTrigger_ActionTriggerFunctionCall": ".end_conversation_action_action_trigger",
    "EndConversationActionActionTrigger_ActionTriggerPhraseBased": ".end_conversation_action_action_trigger",
    "EndConversationActionParams": ".end_conversation_action_params",
    "EndConversationActionParamsActionTrigger": ".end_conversation_action_params_action_trigger",
    "EndConversationActionParamsActionTrigger_ActionTriggerFunctionCall": ".end_conversation_action_params_action_trigger",
    "EndConversationActionParamsActionTrigger_ActionTriggerPhraseBased": ".end_conversation_action_params_action_trigger",
    "EndConversationActionUpdateParams": ".end_conversation_action_update_params",
    "EndConversationActionUpdateParamsActionTrigger": ".end_conversation_action_update_params_action_trigger",
    "EndConversationActionUpdateParamsActionTriggerZero": ".end_conversation_action_update_params_action_trigger_zero",
    "EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall": ".end_conversation_action_update_params_action_trigger_zero",
    "EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased": ".end_conversation_action_update_params_action_trigger_zero",
    "EndConversationActionUpdateParamsConfig": ".end_conversation_action_update_params_config",
    "EventType": ".event_type",
    "ExternalAction": ".external_action",
    "ExternalActionConfig": ".external_action_config",
    "ExternalActionConfigProcessingMode": ".external_action_config_processing_mode",
    "ExternalActionParams": ".external_action_params",
    "ExternalActionUpdateParams": ".external_action_update_params",
    "ExternalActionUpdateParamsActionTrigger": ".external_action_update_params_action_trigger",
    "ExternalActionUpdateParamsConfig": ".external_action_update_params_config",
    "FunctionCallActionTrigger": ".function_call_action_trigger",
    "FunctionCallActionTriggerConfig": ".function_call_action_trigger_config",
    "FunctionCallActionTriggerType": ".function_call_action_trigger_type",
    "HttpMethod": ".http_method",
    "HttpValidationError": ".http_validation_error",
    "InternalLlmFallback": ".internal_llm_fallback",
    "InternalLlmFallbackProvider": ".internal_llm_fallback_provider",
    "InterruptSensitivity": ".interrupt_sensitivity",
    "Language": ".language",
    "NormalizedAgent": ".normalized_agent",
    "NormalizedAgentDeepgramKeywordsValue": ".normalized_agent_deepgram_keywords_value",
    "NormalizedAgentEndpointingSensitivity": ".normalized_agent_endpointing_sensitivity",
    "NormalizedAgentIvrNavigationMode": ".normalized_agent_ivr_navigation_mode",
    "NormalizedAgentOpenaiAccountConnection": ".normalized_agent_openai_account_connection",
    "NormalizedAgentPrompt": ".normalized_agent_prompt",
    "NormalizedAgentVectorDatabase": ".normalized_agent_vector_database",
    "NormalizedCall": ".normalized_call",
    "NormalizedCallHumanDetectionResult": ".normalized_call_human_detection_result",
    "NormalizedCallOnNoHumanAnswer": ".normalized_call_on_no_human_answer",
    "NormalizedCallStage": ".normalized_call_stage",
    "NormalizedCallStageOutcome": ".normalized_call_stage_outcome",
    "NormalizedCallTelephonyAccountConnection": ".normalized_call_telephony_account_connection",
    "NormalizedCallTelephonyMetadata": ".normalized_call_telephony_metadata",
    "NormalizedCallTelephonyMetadata_TelephonyMetadataTwilio": ".normalized_call_telephony_metadata",
    "NormalizedCallTelephonyMetadata_TelephonyMetadataVonage": ".normalized_call_telephony_metadata",
    "NormalizedCallTelephonyProvider": ".normalized_call_telephony_provider",
    "NormalizedPhoneNumber": ".normalized_phone_number",
    "NormalizedPhoneNumberTelephonyAccountConnection": ".normalized_phone_number_telephony_account_connection",
    "NormalizedPhoneNumberTelephonyProvider": ".normalized_phone_number_telephony_provider",
    "NormalizedPrompt": ".normalized_prompt",
    "OpenAiAccountConnection": ".open_ai_account_connection",
    "OpenAiAccountConnectionParams": ".open_ai_account_connection_params",
    "OpenAiAccountConnectionType": ".open_ai_account_connection_type",
    "OpenAiAccountConnectionUpdateParams": ".open_ai_account_connection_update_params",
    "OpenAiAccountConnectionUpdateParamsCredentials": ".open_ai_account_connection_update_params_credentials",
    "OpenAiCredentials": ".open_ai_credentials",
    "PhoneNumber": ".phone_number",
    "PhoneNumberPage": ".phone_number_page",
    "PhoneNumberTelephonyProvider": ".phone_number_telephony_provider",
    "PhraseBasedActionTriggerConfig": ".phrase_based_action_trigger_config",
    "PhraseBasedActionTriggerInput": ".phrase_based_action_trigger_input",
    "PhraseBasedActionTriggerOutput": ".phrase_based_action_trigger_output",
    "PhraseTrigger": ".phrase_trigger",
    "PhraseTriggerConditionsItem": ".phrase_trigger_conditions_item",
    "PineconeVectorDatabase": ".pinecone_vector_database",
    "PineconeVectorDatabaseParams": ".pinecone_vector_database_params",
    "PineconeVectorDatabaseParamsType": ".pinecone_vector_database_params_type",
    "PineconeVectorDatabaseType": ".pinecone_vector_database_type",
    "PineconeVectorDatabaseUpdateParams": ".pinecone_vector_database_update_params",
    "PineconeVectorDatabaseUpdateParamsApiEnvironment": ".pinecone_vector_database_update_params_api_environment",
    "PineconeVectorDatabaseUpdateParamsApiKey": ".pinecone_vector_database_update_params_api_key",
    "PineconeVectorDatabaseUpdateParamsIndex": ".pinecone_vector_database_update_params_index",
    "PineconeVectorDatabaseUpdateParamsType": ".pinecone_vector_database_update_params_type",
    "PlanType": ".plan_type",
    "PlayHtVoice": ".play_ht_voice",
    "PlayHtVoiceParams": ".play_ht_voice_params",
    "PlayHtVoiceParamsQuality": ".play_ht_voice_params_quality",
    "PlayHtVoiceParamsVersion": ".play_ht_voice_params_version",
    "PlayHtVoiceQuality": ".play_ht_voice_quality",
    "PlayHtVoiceUpdateParams": ".play_ht_voice_update_params",
    "PlayHtVoiceUpdateParamsApiKey": ".play_ht_voice_update_params_api_key",
    "PlayHtVoiceUpdateParamsApiUserId": ".play_ht_voice_update_params_api_user_id",
    "PlayHtVoiceUpdateParamsExperimentalRemoveSilence": ".play_ht_voice_update_params_experimental_remove_silence",
    "PlayHtVoiceUpdateParamsQuality": ".play_ht_voice_update_params_quality",
    "PlayHtVoiceUpdateParamsQualityZero": ".play_ht_voice_update_params_quality_zero",
    "PlayHtVoiceUpdateParamsSpeed": ".play_ht_voice_update_params_speed",
    "PlayHtVoiceUpdateParamsTemperature": ".play_ht_voice_update_params_temperature",
    "PlayHtVoiceUpdateParamsTextGuidance": ".play_ht_voice_update_params_text_guidance",
    "PlayHtVoiceUpdateParamsTopP": ".play_ht_voice_update_params_top_p",
    "PlayHtVoiceUpdateParamsVersion": ".play_ht_voice_update_params_version",
    "PlayHtVoiceUpdateParamsVersionZero": ".play_ht_voice_update_params_version_zero",
    "PlayHtVoiceUpdateParamsVoiceGuidance": ".play_ht_voice_update_params_voice_guidance",
    "PlayHtVoiceUpdateParamsVoiceId": ".play_ht_voice_update_params_voice_id",
    "PlayHtVoiceVersion": ".play_ht_voice_version",
    "Prompt": ".prompt",
    "PromptPage": ".prompt_page",
    "PromptParams": ".prompt_params",
    "PromptParamsPromptTemplate": ".prompt_params_prompt_template",
    "PromptTemplate": ".prompt_template",
    "PromptUpdateParams": ".prompt_update_params",
    "PromptUpdateParamsCollectFields": ".prompt_update_params_collect_fields",
    "PromptUpdateParamsContent": ".prompt_update_params_content",
    "PromptUpdateParamsContextEndpoint": ".prompt_update_params_context_endpoint",
    "PromptUpdateParamsPromptTemplate": ".prompt_update_params_prompt_template",
    "RimeVoice": ".rime_voice",
    "RimeVoiceModelId": ".rime_voice_model_id",
    "RimeVoiceModelIdZero": ".rime_voice_model_id_zero",
    "RimeVoiceParams": ".rime_voice_params",
    "RimeVoiceParamsModelId": ".rime_voice_params_model_id",
    "RimeVoiceParamsModelIdZero": ".rime_voice_params_model_id_zero",
    "RimeVoiceUpdateParams": ".rime_voice_update_params",
    "RimeVoiceUpdateParamsModelId": ".rime_voice_update_params_model_id",
    "RimeVoiceUpdateParamsModelIdZero": ".rime_voice_update_params_model_id_zero",
    "RimeVoiceUpdateParamsSpeaker": ".rime_voice_update_params_speaker",
    "RimeVoiceUpdateParamsSpeedAlpha": ".rime_voice_update_params_speed_alpha",
    "SetHoldAction": ".set_hold_action",
    "SetHoldActionActionTrigger": ".set_hold_action_action_trigger",
    "SetHoldActionActionTrigger_ActionTriggerFunctionCall": ".set_hold_action_action_trigger",
    "SetHoldActionActionTrigger_ActionTriggerPhraseBased": ".set_hold_action_action_trigger",
    "SetHoldActionParams": ".set_hold_action_params",
    "SetHoldActionParamsActionTrigger": ".set_hold_action_params_action_trigger",
    "SetHoldActionParamsActionTrigger_ActionTriggerFunctionCall": ".set_hold_action_params_action_trigger",
    "SetHoldActionParamsActionTrigger_ActionTriggerPhraseBased": ".set_hold_action_params_action_trigger",
    "SetHoldActionUpdateParams": ".set_hold_action_update_params",
    "SetHoldActionUpdateParamsActionTrigger": ".set_hold_action_update_params_action_trigger",
    "SetHoldActionUpdateParamsActionTriggerZero": ".set_hold_action_update_params_action_trigger_zero",
    "SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall": ".set_hold_action_update_params_action_trigger_zero",
    "SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased": ".set_hold_action_update_params_action_trigger_zero",
    "SetHoldActionUpdateParamsConfig": ".set_hold_action_update_params_config",
    "TransferCallAction": ".transfer_call_action",
    "TransferCallActionActionTrigger": ".transfer_call_action_action_trigger",
    "TransferCallActionActionTrigger_ActionTriggerFunctionCall": ".transfer_call_action_action_trigger",
    "TransferCallActionActionTrigger_ActionTriggerPhraseBased": ".transfer_call_action_action_trigger",
    "TransferCallActionParams": ".transfer_call_action_params",
    "TransferCallActionParamsActionTrigger": ".transfer_call_action_params_action_trigger",
    "TransferCallActionParamsActionTrigger_ActionTriggerFunctionCall": ".transfer_call_action_params_action_trigger",
    "TransferCallActionParamsActionTrigger_ActionTriggerPhraseBased": ".transfer_call_action_params_action_trigger",
    "TransferCallActionUpdateParams": ".transfer_call_action_update_params",
    "TransferCallActionUpdateParamsActionTrigger": ".transfer_call_action_update_params_action_trigger",
    "TransferCallActionUpdateParamsActionTriggerZero": ".transfer_call_action_update_params_action_trigger_zero",
    "TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall": ".transfer_call_action_update_params_action_trigger_zero",
    "TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased": ".transfer_call_action_update_params_action_trigger_zero",
    "TransferCallActionUpdateParamsConfig": ".transfer_call_action_update_params_config",
    "TransferCallConfig": ".transfer_call_config",
    "TwilioAccountConnection": ".twilio_account_connection",
    "TwilioAccountConnectionParams": ".twilio_account_connection_params",
    "TwilioAccountConnectionType": ".twilio_account_connection_type",
    "TwilioAccountConnectionUpdateParams": ".twilio_account_connection_update_params",
    "TwilioAccountConnectionUpdateParamsCredentials": ".twilio_account_connection_update_params_credentials",
    "TwilioCredentials": ".twilio_credentials",
    "TwilioTelephonyMetadata": ".twilio_telephony_metadata",
    "Undefined": ".undefined",
    "Usage": ".usage",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VectorDatabasePage": ".vector_database_page",
    "VocodeVoice": ".vocode_voice",
    "VocodeVoiceParams": ".vocode_voice_params",
    "VocodeVoiceParamsVoiceId": ".vocode_voice_params_voice_id",
    "VocodeVoiceUpdateParams": ".vocode_voice_update_params",
    "VocodeVoiceUpdateParamsVoiceId": ".vocode_voice_update_params_voice_id",
    "VocodeVoiceUpdateParamsVoiceIdZero": ".vocode_voice_update_params_voice_id_zero",
    "VocodeVoiceVoiceId": ".vocode_voice_voice_id",
    "VoicePage": ".voice_page",
    "VoicePageItemsItem": ".voice_page_items_item",
    "VoicePageItemsItem_VoiceAzure": ".voice_page_items_item",
    "VoicePageItemsItem_VoiceElevenLabs": ".voice_page_items_item",
    "VoicePageItemsItem_VoicePlayHt": ".voice_page_items_item",
    "VoicePageItemsItem_VoiceRime": ".voice_page_items_item",
    "VoicePageItemsItem_VoiceVocode": ".voice_page_items_item",
    "VoiceParamsRequest": ".voice_params_request",
    "VoiceParamsRequest_VoiceAzure": ".voice_params_request",
    "VoiceParamsRequest_VoiceElevenLabs": ".voice_params_request",
    "VoiceParamsRequest_VoicePlayHt": ".voice_params_request",
    "VoiceParamsRequest_VoiceRime": ".voice_params_request",
    "VoiceParamsRequest_VoiceVocode": ".voice_params_request",
    "VoiceResponseModel": ".voice_response_model",
    "VoiceResponseModel_VoiceAzure": ".voice_response_model",
    "VoiceResponseModel_VoiceElevenLabs": ".voice_response_model",
    "VoiceResponseModel_VoicePlayHt": ".voice_response_model",
    "VoiceResponseModel_VoiceRime": ".voice_response_model",
    "VoiceResponseModel_VoiceVocode": ".voice_response_model",
    "VoiceUpdateParamsRequest": ".voice_update_params_request",
    "VoiceUpdateParamsRequest_VoiceAzure": ".voice_update_params_request",
    "VoiceUpdateParamsRequest_VoiceElevenLabs": ".voice_update_params_request",
    "VoiceUpdateParamsRequest_VoicePlayHt": ".voice_update_params_request",
    "VoiceUpdateParamsRequest_VoiceRime": ".voice_update_params_request",
    "VoiceUpdateParamsRequest_VoiceVocode": ".voice_update_params_request",
    "VonageTelephonyMetadata": ".vonage_telephony_metadata",
    "Webhook": ".webhook",
    "WebhookPage": ".webhook_page",
    "WebhookParams": ".webhook_params",
    "WebhookUpdateParams": ".webhook_update_params",
    "WebhookUpdateParamsMethod": ".webhook_update_params_method",
    "WebhookUpdateParamsSubscriptions": ".webhook_update_params_subscriptions",
    "WebhookUpdateParamsUrl": ".webhook_update_params_url",
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
    "AccountConnectionPage",
    "AccountConnectionPageItemsItem",
    "AccountConnectionPageItemsItem_AccountConnectionOpenai",
    "AccountConnectionPageItemsItem_AccountConnectionTwilio",
    "AccountConnectionParamsRequest",
    "AccountConnectionParamsRequest_AccountConnectionOpenai",
    "AccountConnectionParamsRequest_AccountConnectionTwilio",
    "AccountConnectionResponseModel",
    "AccountConnectionResponseModel_AccountConnectionOpenai",
    "AccountConnectionResponseModel_AccountConnectionTwilio",
    "AccountConnectionUpdateParamsRequest",
    "AccountConnectionUpdateParamsRequest_AccountConnectionOpenai",
    "AccountConnectionUpdateParamsRequest_AccountConnectionTwilio",
    "ActionPage",
    "ActionPageItemsItem",
    "ActionPageItemsItem_ActionAddToConference",
    "ActionPageItemsItem_ActionDtmf",
    "ActionPageItemsItem_ActionEndConversation",
    "ActionPageItemsItem_ActionExternal",
    "ActionPageItemsItem_ActionSetHold",
    "ActionPageItemsItem_ActionTransferCall",
    "ActionParamsRequest",
    "ActionParamsRequest_ActionAddToConference",
    "ActionParamsRequest_ActionDtmf",
    "ActionParamsRequest_ActionEndConversation",
    "ActionParamsRequest_ActionExternal",
    "ActionParamsRequest_ActionSetHold",
    "ActionParamsRequest_ActionTransferCall",
    "ActionResponseModel",
    "ActionResponseModel_ActionAddToConference",
    "ActionResponseModel_ActionDtmf",
    "ActionResponseModel_ActionEndConversation",
    "ActionResponseModel_ActionExternal",
    "ActionResponseModel_ActionSetHold",
    "ActionResponseModel_ActionTransferCall",
    "ActionUpdateParamsRequest",
    "ActionUpdateParamsRequest_ActionAddToConference",
    "ActionUpdateParamsRequest_ActionDtmf",
    "ActionUpdateParamsRequest_ActionEndConversation",
    "ActionUpdateParamsRequest_ActionExternal",
    "ActionUpdateParamsRequest_ActionSetHold",
    "ActionUpdateParamsRequest_ActionTransferCall",
    "AddToConferenceAction",
    "AddToConferenceActionActionTrigger",
    "AddToConferenceActionActionTrigger_ActionTriggerFunctionCall",
    "AddToConferenceActionActionTrigger_ActionTriggerPhraseBased",
    "AddToConferenceActionParams",
    "AddToConferenceActionParamsActionTrigger",
    "AddToConferenceActionParamsActionTrigger_ActionTriggerFunctionCall",
    "AddToConferenceActionParamsActionTrigger_ActionTriggerPhraseBased",
    "AddToConferenceActionUpdateParams",
    "AddToConferenceActionUpdateParamsActionTrigger",
    "AddToConferenceActionUpdateParamsActionTriggerZero",
    "AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall",
    "AddToConferenceActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased",
    "AddToConferenceActionUpdateParamsConfig",
    "AddToConferenceConfig",
    "AddToSteeringPoolRequest",
    "Agent",
    "AgentActionsItem",
    "AgentActionsItem_ActionAddToConference",
    "AgentActionsItem_ActionDtmf",
    "AgentActionsItem_ActionEndConversation",
    "AgentActionsItem_ActionExternal",
    "AgentActionsItem_ActionSetHold",
    "AgentActionsItem_ActionTransferCall",
    "AgentDeepgramKeywordsValue",
    "AgentEndpointingSensitivity",
    "AgentIvrNavigationMode",
    "AgentPage",
    "AgentParams",
    "AgentParamsActionsItem",
    "AgentParamsActionsItemOne",
    "AgentParamsActionsItemOne_ActionAddToConference",
    "AgentParamsActionsItemOne_ActionDtmf",
    "AgentParamsActionsItemOne_ActionEndConversation",
    "AgentParamsActionsItemOne_ActionExternal",
    "AgentParamsActionsItemOne_ActionSetHold",
    "AgentParamsActionsItemOne_ActionTransferCall",
    "AgentParamsDeepgramKeywordsValue",
    "AgentParamsEndpointingSensitivity",
    "AgentParamsIvrNavigationMode",
    "AgentParamsOpenaiAccountConnection",
    "AgentParamsPrompt",
    "AgentParamsVectorDatabase",
    "AgentParamsVoice",
    "AgentParamsVoiceOne",
    "AgentParamsVoiceOne_VoiceAzure",
    "AgentParamsVoiceOne_VoiceElevenLabs",
    "AgentParamsVoiceOne_VoicePlayHt",
    "AgentParamsVoiceOne_VoiceRime",
    "AgentParamsVoiceOne_VoiceVocode",
    "AgentParamsWebhook",
    "AgentUpdateParams",
    "AgentUpdateParamsActions",
    "AgentUpdateParamsActionsZeroItem",
    "AgentUpdateParamsActionsZeroItemOne",
    "AgentUpdateParamsActionsZeroItemOne_ActionAddToConference",
    "AgentUpdateParamsActionsZeroItemOne_ActionDtmf",
    "AgentUpdateParamsActionsZeroItemOne_ActionEndConversation",
    "AgentUpdateParamsActionsZeroItemOne_ActionExternal",
    "AgentUpdateParamsActionsZeroItemOne_ActionSetHold",
    "AgentUpdateParamsActionsZeroItemOne_ActionTransferCall",
    "AgentUpdateParamsAskIfHumanPresentOnIdle",
    "AgentUpdateParamsContextEndpoint",
    "AgentUpdateParamsConversationSpeed",
    "AgentUpdateParamsDeepgramKeywords",
    "AgentUpdateParamsDeepgramKeywordsZeroValue",
    "AgentUpdateParamsEndpointingSensitivity",
    "AgentUpdateParamsEndpointingSensitivityZero",
    "AgentUpdateParamsIdleTimeSeconds",
    "AgentUpdateParamsInitialMessage",
    "AgentUpdateParamsInitialMessageDelay",
    "AgentUpdateParamsInterruptSensitivity",
    "AgentUpdateParamsIvrNavigationMode",
    "AgentUpdateParamsIvrNavigationModeZero",
    "AgentUpdateParamsLanguage",
    "AgentUpdateParamsLlmFallback",
    "AgentUpdateParamsName",
    "AgentUpdateParamsNoiseSuppression",
    "AgentUpdateParamsOpenaiAccountConnection",
    "AgentUpdateParamsOpenaiModelNameOverride",
    "AgentUpdateParamsPrompt",
    "AgentUpdateParamsRunDoNotCallDetection",
    "AgentUpdateParamsVectorDatabase",
    "AgentUpdateParamsVoice",
    "AgentUpdateParamsVoiceOne",
    "AgentUpdateParamsVoiceOne_VoiceAzure",
    "AgentUpdateParamsVoiceOne_VoiceElevenLabs",
    "AgentUpdateParamsVoiceOne_VoicePlayHt",
    "AgentUpdateParamsVoiceOne_VoiceRime",
    "AgentUpdateParamsVoiceOne_VoiceVocode",
    "AgentUpdateParamsWebhook",
    "AgentVoice",
    "AgentVoice_VoiceAzure",
    "AgentVoice_VoiceElevenLabs",
    "AgentVoice_VoicePlayHt",
    "AgentVoice_VoiceRime",
    "AgentVoice_VoiceVocode",
    "AzureVoice",
    "AzureVoiceParams",
    "AzureVoiceUpdateParams",
    "AzureVoiceUpdateParamsPitch",
    "AzureVoiceUpdateParamsRate",
    "AzureVoiceUpdateParamsVoiceName",
    "Call",
    "CallHumanDetectionResult",
    "CallOnNoHumanAnswer",
    "CallPage",
    "CallStage",
    "CallStageOutcome",
    "CallStatus",
    "CallTelephonyMetadata",
    "CallTelephonyMetadata_TelephonyMetadataTwilio",
    "CallTelephonyMetadata_TelephonyMetadataVonage",
    "CallTelephonyProvider",
    "CollectField",
    "CollectFieldFieldType",
    "CreateCallAgentParams",
    "CreateCallAgentParamsActionsItem",
    "CreateCallAgentParamsActionsItemOne",
    "CreateCallAgentParamsActionsItemOne_ActionAddToConference",
    "CreateCallAgentParamsActionsItemOne_ActionDtmf",
    "CreateCallAgentParamsActionsItemOne_ActionEndConversation",
    "CreateCallAgentParamsActionsItemOne_ActionExternal",
    "CreateCallAgentParamsActionsItemOne_ActionSetHold",
    "CreateCallAgentParamsActionsItemOne_ActionTransferCall",
    "CreateCallAgentParamsDeepgramKeywordsValue",
    "CreateCallAgentParamsEndpointingSensitivity",
    "CreateCallAgentParamsIvrNavigationMode",
    "CreateCallAgentParamsOpenaiAccountConnection",
    "CreateCallAgentParamsPrompt",
    "CreateCallAgentParamsVectorDatabase",
    "CreateCallAgentParamsVoice",
    "CreateCallAgentParamsVoiceOne",
    "CreateCallAgentParamsVoiceOne_VoiceAzure",
    "CreateCallAgentParamsVoiceOne_VoiceElevenLabs",
    "CreateCallAgentParamsVoiceOne_VoicePlayHt",
    "CreateCallAgentParamsVoiceOne_VoiceRime",
    "CreateCallAgentParamsVoiceOne_VoiceVocode",
    "CreateCallAgentParamsWebhook",
    "DtmfAction",
    "DtmfActionParams",
    "DtmfActionUpdateParams",
    "DtmfActionUpdateParamsActionTrigger",
    "DtmfActionUpdateParamsConfig",
    "ElevenLabsVoice",
    "ElevenLabsVoiceParams",
    "ElevenLabsVoiceUpdateParams",
    "ElevenLabsVoiceUpdateParamsApiKey",
    "ElevenLabsVoiceUpdateParamsExperimentalInputStreaming",
    "ElevenLabsVoiceUpdateParamsModelId",
    "ElevenLabsVoiceUpdateParamsOptimizeStreamingLatency",
    "ElevenLabsVoiceUpdateParamsSimilarityBoost",
    "ElevenLabsVoiceUpdateParamsStability",
    "ElevenLabsVoiceUpdateParamsVoiceId",
    "EmptyActionConfig",
    "EndConversationAction",
    "EndConversationActionActionTrigger",
    "EndConversationActionActionTrigger_ActionTriggerFunctionCall",
    "EndConversationActionActionTrigger_ActionTriggerPhraseBased",
    "EndConversationActionParams",
    "EndConversationActionParamsActionTrigger",
    "EndConversationActionParamsActionTrigger_ActionTriggerFunctionCall",
    "EndConversationActionParamsActionTrigger_ActionTriggerPhraseBased",
    "EndConversationActionUpdateParams",
    "EndConversationActionUpdateParamsActionTrigger",
    "EndConversationActionUpdateParamsActionTriggerZero",
    "EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall",
    "EndConversationActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased",
    "EndConversationActionUpdateParamsConfig",
    "EventType",
    "ExternalAction",
    "ExternalActionConfig",
    "ExternalActionConfigProcessingMode",
    "ExternalActionParams",
    "ExternalActionUpdateParams",
    "ExternalActionUpdateParamsActionTrigger",
    "ExternalActionUpdateParamsConfig",
    "FunctionCallActionTrigger",
    "FunctionCallActionTriggerConfig",
    "FunctionCallActionTriggerType",
    "HttpMethod",
    "HttpValidationError",
    "InternalLlmFallback",
    "InternalLlmFallbackProvider",
    "InterruptSensitivity",
    "Language",
    "NormalizedAgent",
    "NormalizedAgentDeepgramKeywordsValue",
    "NormalizedAgentEndpointingSensitivity",
    "NormalizedAgentIvrNavigationMode",
    "NormalizedAgentOpenaiAccountConnection",
    "NormalizedAgentPrompt",
    "NormalizedAgentVectorDatabase",
    "NormalizedCall",
    "NormalizedCallHumanDetectionResult",
    "NormalizedCallOnNoHumanAnswer",
    "NormalizedCallStage",
    "NormalizedCallStageOutcome",
    "NormalizedCallTelephonyAccountConnection",
    "NormalizedCallTelephonyMetadata",
    "NormalizedCallTelephonyMetadata_TelephonyMetadataTwilio",
    "NormalizedCallTelephonyMetadata_TelephonyMetadataVonage",
    "NormalizedCallTelephonyProvider",
    "NormalizedPhoneNumber",
    "NormalizedPhoneNumberTelephonyAccountConnection",
    "NormalizedPhoneNumberTelephonyProvider",
    "NormalizedPrompt",
    "OpenAiAccountConnection",
    "OpenAiAccountConnectionParams",
    "OpenAiAccountConnectionType",
    "OpenAiAccountConnectionUpdateParams",
    "OpenAiAccountConnectionUpdateParamsCredentials",
    "OpenAiCredentials",
    "PhoneNumber",
    "PhoneNumberPage",
    "PhoneNumberTelephonyProvider",
    "PhraseBasedActionTriggerConfig",
    "PhraseBasedActionTriggerInput",
    "PhraseBasedActionTriggerOutput",
    "PhraseTrigger",
    "PhraseTriggerConditionsItem",
    "PineconeVectorDatabase",
    "PineconeVectorDatabaseParams",
    "PineconeVectorDatabaseParamsType",
    "PineconeVectorDatabaseType",
    "PineconeVectorDatabaseUpdateParams",
    "PineconeVectorDatabaseUpdateParamsApiEnvironment",
    "PineconeVectorDatabaseUpdateParamsApiKey",
    "PineconeVectorDatabaseUpdateParamsIndex",
    "PineconeVectorDatabaseUpdateParamsType",
    "PlanType",
    "PlayHtVoice",
    "PlayHtVoiceParams",
    "PlayHtVoiceParamsQuality",
    "PlayHtVoiceParamsVersion",
    "PlayHtVoiceQuality",
    "PlayHtVoiceUpdateParams",
    "PlayHtVoiceUpdateParamsApiKey",
    "PlayHtVoiceUpdateParamsApiUserId",
    "PlayHtVoiceUpdateParamsExperimentalRemoveSilence",
    "PlayHtVoiceUpdateParamsQuality",
    "PlayHtVoiceUpdateParamsQualityZero",
    "PlayHtVoiceUpdateParamsSpeed",
    "PlayHtVoiceUpdateParamsTemperature",
    "PlayHtVoiceUpdateParamsTextGuidance",
    "PlayHtVoiceUpdateParamsTopP",
    "PlayHtVoiceUpdateParamsVersion",
    "PlayHtVoiceUpdateParamsVersionZero",
    "PlayHtVoiceUpdateParamsVoiceGuidance",
    "PlayHtVoiceUpdateParamsVoiceId",
    "PlayHtVoiceVersion",
    "Prompt",
    "PromptPage",
    "PromptParams",
    "PromptParamsPromptTemplate",
    "PromptTemplate",
    "PromptUpdateParams",
    "PromptUpdateParamsCollectFields",
    "PromptUpdateParamsContent",
    "PromptUpdateParamsContextEndpoint",
    "PromptUpdateParamsPromptTemplate",
    "RimeVoice",
    "RimeVoiceModelId",
    "RimeVoiceModelIdZero",
    "RimeVoiceParams",
    "RimeVoiceParamsModelId",
    "RimeVoiceParamsModelIdZero",
    "RimeVoiceUpdateParams",
    "RimeVoiceUpdateParamsModelId",
    "RimeVoiceUpdateParamsModelIdZero",
    "RimeVoiceUpdateParamsSpeaker",
    "RimeVoiceUpdateParamsSpeedAlpha",
    "SetHoldAction",
    "SetHoldActionActionTrigger",
    "SetHoldActionActionTrigger_ActionTriggerFunctionCall",
    "SetHoldActionActionTrigger_ActionTriggerPhraseBased",
    "SetHoldActionParams",
    "SetHoldActionParamsActionTrigger",
    "SetHoldActionParamsActionTrigger_ActionTriggerFunctionCall",
    "SetHoldActionParamsActionTrigger_ActionTriggerPhraseBased",
    "SetHoldActionUpdateParams",
    "SetHoldActionUpdateParamsActionTrigger",
    "SetHoldActionUpdateParamsActionTriggerZero",
    "SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall",
    "SetHoldActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased",
    "SetHoldActionUpdateParamsConfig",
    "TransferCallAction",
    "TransferCallActionActionTrigger",
    "TransferCallActionActionTrigger_ActionTriggerFunctionCall",
    "TransferCallActionActionTrigger_ActionTriggerPhraseBased",
    "TransferCallActionParams",
    "TransferCallActionParamsActionTrigger",
    "TransferCallActionParamsActionTrigger_ActionTriggerFunctionCall",
    "TransferCallActionParamsActionTrigger_ActionTriggerPhraseBased",
    "TransferCallActionUpdateParams",
    "TransferCallActionUpdateParamsActionTrigger",
    "TransferCallActionUpdateParamsActionTriggerZero",
    "TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerFunctionCall",
    "TransferCallActionUpdateParamsActionTriggerZero_ActionTriggerPhraseBased",
    "TransferCallActionUpdateParamsConfig",
    "TransferCallConfig",
    "TwilioAccountConnection",
    "TwilioAccountConnectionParams",
    "TwilioAccountConnectionType",
    "TwilioAccountConnectionUpdateParams",
    "TwilioAccountConnectionUpdateParamsCredentials",
    "TwilioCredentials",
    "TwilioTelephonyMetadata",
    "Undefined",
    "Usage",
    "ValidationError",
    "ValidationErrorLocItem",
    "VectorDatabasePage",
    "VocodeVoice",
    "VocodeVoiceParams",
    "VocodeVoiceParamsVoiceId",
    "VocodeVoiceUpdateParams",
    "VocodeVoiceUpdateParamsVoiceId",
    "VocodeVoiceUpdateParamsVoiceIdZero",
    "VocodeVoiceVoiceId",
    "VoicePage",
    "VoicePageItemsItem",
    "VoicePageItemsItem_VoiceAzure",
    "VoicePageItemsItem_VoiceElevenLabs",
    "VoicePageItemsItem_VoicePlayHt",
    "VoicePageItemsItem_VoiceRime",
    "VoicePageItemsItem_VoiceVocode",
    "VoiceParamsRequest",
    "VoiceParamsRequest_VoiceAzure",
    "VoiceParamsRequest_VoiceElevenLabs",
    "VoiceParamsRequest_VoicePlayHt",
    "VoiceParamsRequest_VoiceRime",
    "VoiceParamsRequest_VoiceVocode",
    "VoiceResponseModel",
    "VoiceResponseModel_VoiceAzure",
    "VoiceResponseModel_VoiceElevenLabs",
    "VoiceResponseModel_VoicePlayHt",
    "VoiceResponseModel_VoiceRime",
    "VoiceResponseModel_VoiceVocode",
    "VoiceUpdateParamsRequest",
    "VoiceUpdateParamsRequest_VoiceAzure",
    "VoiceUpdateParamsRequest_VoiceElevenLabs",
    "VoiceUpdateParamsRequest_VoicePlayHt",
    "VoiceUpdateParamsRequest_VoiceRime",
    "VoiceUpdateParamsRequest_VoiceVocode",
    "VonageTelephonyMetadata",
    "Webhook",
    "WebhookPage",
    "WebhookParams",
    "WebhookUpdateParams",
    "WebhookUpdateParamsMethod",
    "WebhookUpdateParamsSubscriptions",
    "WebhookUpdateParamsUrl",
]
