



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .applications_api_usage import ApplicationsApiUsage
    from .applications_application import ApplicationsApplication
    from .applications_application_developer import ApplicationsApplicationDeveloper
    from .applications_application_scopes import ApplicationsApplicationScopes
    from .applications_application_status import ApplicationsApplicationStatus
    from .applications_datapoint import ApplicationsDatapoint
    from .applications_developer_role import ApplicationsDeveloperRole
    from .applications_series import ApplicationsSeries
    from .bungie_credential_type import BungieCredentialType
    from .bungie_membership_type import BungieMembershipType
    from .bungie_membership_type_array import BungieMembershipTypeArray
    from .common_models_core_setting import CommonModelsCoreSetting
    from .common_models_core_settings_configuration import CommonModelsCoreSettingsConfiguration
    from .common_models_core_system import CommonModelsCoreSystem
    from .common_models_destiny2core_settings import CommonModelsDestiny2CoreSettings
    from .components_component_privacy_setting import ComponentsComponentPrivacySetting
    from .components_component_response import ComponentsComponentResponse
    from .config_clan_banner_clan_banner_decal import ConfigClanBannerClanBannerDecal
    from .config_clan_banner_clan_banner_source import ConfigClanBannerClanBannerSource
    from .config_group_theme import ConfigGroupTheme
    from .config_user_theme import ConfigUserTheme
    from .content_comment_summary import ContentCommentSummary
    from .content_content_item_public_contract import ContentContentItemPublicContract
    from .content_content_representation import ContentContentRepresentation
    from .content_models_content_preview import ContentModelsContentPreview
    from .content_models_content_property_data_type_enum import ContentModelsContentPropertyDataTypeEnum
    from .content_models_content_type_default_value import ContentModelsContentTypeDefaultValue
    from .content_models_content_type_description import ContentModelsContentTypeDescription
    from .content_models_content_type_property import ContentModelsContentTypeProperty
    from .content_models_content_type_property_section import ContentModelsContentTypePropertySection
    from .content_models_tag_metadata_definition import ContentModelsTagMetadataDefinition
    from .content_models_tag_metadata_item import ContentModelsTagMetadataItem
    from .content_news_article_rss_item import ContentNewsArticleRssItem
    from .content_news_article_rss_response import ContentNewsArticleRssResponse
    from .dates_date_range import DatesDateRange
    from .destiny_activities_destiny_public_activity_status import DestinyActivitiesDestinyPublicActivityStatus
    from .destiny_activity_graph_node_highlight_type import DestinyActivityGraphNodeHighlightType
    from .destiny_advanced_awa_authorization_result import DestinyAdvancedAwaAuthorizationResult
    from .destiny_advanced_awa_initialize_response import DestinyAdvancedAwaInitializeResponse
    from .destiny_advanced_awa_permission_requested import DestinyAdvancedAwaPermissionRequested
    from .destiny_advanced_awa_response_reason import DestinyAdvancedAwaResponseReason
    from .destiny_advanced_awa_type import DestinyAdvancedAwaType
    from .destiny_advanced_awa_user_response import DestinyAdvancedAwaUserResponse
    from .destiny_advanced_awa_user_selection import DestinyAdvancedAwaUserSelection
    from .destiny_artifacts_destiny_artifact_character_scoped import DestinyArtifactsDestinyArtifactCharacterScoped
    from .destiny_artifacts_destiny_artifact_profile_scoped import DestinyArtifactsDestinyArtifactProfileScoped
    from .destiny_artifacts_destiny_artifact_tier import DestinyArtifactsDestinyArtifactTier
    from .destiny_artifacts_destiny_artifact_tier_item import DestinyArtifactsDestinyArtifactTierItem
    from .destiny_base_item_component_set_ofint32 import DestinyBaseItemComponentSetOfint32
    from .destiny_base_item_component_set_ofint64 import DestinyBaseItemComponentSetOfint64
    from .destiny_base_item_component_set_ofuint32 import DestinyBaseItemComponentSetOfuint32
    from .destiny_bucket_category import DestinyBucketCategory
    from .destiny_bucket_scope import DestinyBucketScope
    from .destiny_challenges_destiny_challenge_status import DestinyChallengesDestinyChallengeStatus
    from .destiny_character_destiny_character_customization import DestinyCharacterDestinyCharacterCustomization
    from .destiny_character_destiny_character_peer_view import DestinyCharacterDestinyCharacterPeerView
    from .destiny_character_destiny_item_peer_view import DestinyCharacterDestinyItemPeerView
    from .destiny_components_collectibles_destiny_collectible_component import (
        DestinyComponentsCollectiblesDestinyCollectibleComponent,
    )
    from .destiny_components_collectibles_destiny_collectibles_component import (
        DestinyComponentsCollectiblesDestinyCollectiblesComponent,
    )
    from .destiny_components_collectibles_destiny_profile_collectibles_component import (
        DestinyComponentsCollectiblesDestinyProfileCollectiblesComponent,
    )
    from .destiny_components_craftables_destiny_craftable_component import (
        DestinyComponentsCraftablesDestinyCraftableComponent,
    )
    from .destiny_components_craftables_destiny_craftable_socket_component import (
        DestinyComponentsCraftablesDestinyCraftableSocketComponent,
    )
    from .destiny_components_craftables_destiny_craftable_socket_plug_component import (
        DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent,
    )
    from .destiny_components_craftables_destiny_craftables_component import (
        DestinyComponentsCraftablesDestinyCraftablesComponent,
    )
    from .destiny_components_inventory_destiny_currencies_component import (
        DestinyComponentsInventoryDestinyCurrenciesComponent,
    )
    from .destiny_components_inventory_destiny_platform_silver_component import (
        DestinyComponentsInventoryDestinyPlatformSilverComponent,
    )
    from .destiny_components_items_destiny_item_plug_component import DestinyComponentsItemsDestinyItemPlugComponent
    from .destiny_components_items_destiny_item_plug_objectives_component import (
        DestinyComponentsItemsDestinyItemPlugObjectivesComponent,
    )
    from .destiny_components_items_destiny_item_reusable_plugs_component import (
        DestinyComponentsItemsDestinyItemReusablePlugsComponent,
    )
    from .destiny_components_kiosks_destiny_kiosk_item import DestinyComponentsKiosksDestinyKioskItem
    from .destiny_components_kiosks_destiny_kiosks_component import DestinyComponentsKiosksDestinyKiosksComponent
    from .destiny_components_loadouts_destiny_loadout_component import DestinyComponentsLoadoutsDestinyLoadoutComponent
    from .destiny_components_loadouts_destiny_loadout_item_component import (
        DestinyComponentsLoadoutsDestinyLoadoutItemComponent,
    )
    from .destiny_components_loadouts_destiny_loadouts_component import (
        DestinyComponentsLoadoutsDestinyLoadoutsComponent,
    )
    from .destiny_components_metrics_destiny_metric_component import DestinyComponentsMetricsDestinyMetricComponent
    from .destiny_components_metrics_destiny_metrics_component import DestinyComponentsMetricsDestinyMetricsComponent
    from .destiny_components_plug_sets_destiny_plug_sets_component import (
        DestinyComponentsPlugSetsDestinyPlugSetsComponent,
    )
    from .destiny_components_presentation_destiny_presentation_node_component import (
        DestinyComponentsPresentationDestinyPresentationNodeComponent,
    )
    from .destiny_components_presentation_destiny_presentation_nodes_component import (
        DestinyComponentsPresentationDestinyPresentationNodesComponent,
    )
    from .destiny_components_profiles_destiny_profile_progression_component import (
        DestinyComponentsProfilesDestinyProfileProgressionComponent,
    )
    from .destiny_components_profiles_destiny_profile_transitory_component import (
        DestinyComponentsProfilesDestinyProfileTransitoryComponent,
    )
    from .destiny_components_profiles_destiny_profile_transitory_current_activity import (
        DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity,
    )
    from .destiny_components_profiles_destiny_profile_transitory_joinability import (
        DestinyComponentsProfilesDestinyProfileTransitoryJoinability,
    )
    from .destiny_components_profiles_destiny_profile_transitory_party_member import (
        DestinyComponentsProfilesDestinyProfileTransitoryPartyMember,
    )
    from .destiny_components_profiles_destiny_profile_transitory_tracking_entry import (
        DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry,
    )
    from .destiny_components_records_destiny_character_records_component import (
        DestinyComponentsRecordsDestinyCharacterRecordsComponent,
    )
    from .destiny_components_records_destiny_profile_records_component import (
        DestinyComponentsRecordsDestinyProfileRecordsComponent,
    )
    from .destiny_components_records_destiny_record_component import DestinyComponentsRecordsDestinyRecordComponent
    from .destiny_components_records_destiny_records_component import DestinyComponentsRecordsDestinyRecordsComponent
    from .destiny_components_social_destiny_social_commendations_component import (
        DestinyComponentsSocialDestinySocialCommendationsComponent,
    )
    from .destiny_components_string_variables_destiny_string_variables_component import (
        DestinyComponentsStringVariablesDestinyStringVariablesComponent,
    )
    from .destiny_components_vendors_destiny_public_vendor_component import (
        DestinyComponentsVendorsDestinyPublicVendorComponent,
    )
    from .destiny_components_vendors_destiny_public_vendor_sale_item_component import (
        DestinyComponentsVendorsDestinyPublicVendorSaleItemComponent,
    )
    from .destiny_components_vendors_destiny_vendor_base_component import (
        DestinyComponentsVendorsDestinyVendorBaseComponent,
    )
    from .destiny_components_vendors_destiny_vendor_group import DestinyComponentsVendorsDestinyVendorGroup
    from .destiny_components_vendors_destiny_vendor_group_component import (
        DestinyComponentsVendorsDestinyVendorGroupComponent,
    )
    from .destiny_components_vendors_destiny_vendor_sale_item_base_component import (
        DestinyComponentsVendorsDestinyVendorSaleItemBaseComponent,
    )
    from .destiny_config_destiny_manifest import DestinyConfigDestinyManifest
    from .destiny_config_gear_asset_data_base_definition import DestinyConfigGearAssetDataBaseDefinition
    from .destiny_config_image_pyramid_entry import DestinyConfigImagePyramidEntry
    from .destiny_constants_destiny_environment_location_mapping import (
        DestinyConstantsDestinyEnvironmentLocationMapping,
    )
    from .destiny_damage_type import DestinyDamageType
    from .destiny_definitions_activity_modifiers_destiny_activity_modifier_definition import (
        DestinyDefinitionsActivityModifiersDestinyActivityModifierDefinition,
    )
    from .destiny_definitions_animations_destiny_animation_reference import (
        DestinyDefinitionsAnimationsDestinyAnimationReference,
    )
    from .destiny_definitions_artifacts_destiny_artifact_definition import (
        DestinyDefinitionsArtifactsDestinyArtifactDefinition,
    )
    from .destiny_definitions_artifacts_destiny_artifact_tier_definition import (
        DestinyDefinitionsArtifactsDestinyArtifactTierDefinition,
    )
    from .destiny_definitions_artifacts_destiny_artifact_tier_item_definition import (
        DestinyDefinitionsArtifactsDestinyArtifactTierItemDefinition,
    )
    from .destiny_definitions_breaker_types_destiny_breaker_type_definition import (
        DestinyDefinitionsBreakerTypesDestinyBreakerTypeDefinition,
    )
    from .destiny_definitions_checklists_destiny_checklist_definition import (
        DestinyDefinitionsChecklistsDestinyChecklistDefinition,
    )
    from .destiny_definitions_checklists_destiny_checklist_entry_definition import (
        DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition,
    )
    from .destiny_definitions_collectibles_destiny_collectible_acquisition_block import (
        DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock,
    )
    from .destiny_definitions_collectibles_destiny_collectible_definition import (
        DestinyDefinitionsCollectiblesDestinyCollectibleDefinition,
    )
    from .destiny_definitions_collectibles_destiny_collectible_state_block import (
        DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock,
    )
    from .destiny_definitions_common_destiny_display_properties_definition import (
        DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
    )
    from .destiny_definitions_common_destiny_icon_sequence_definition import (
        DestinyDefinitionsCommonDestinyIconSequenceDefinition,
    )
    from .destiny_definitions_common_destiny_position_definition import (
        DestinyDefinitionsCommonDestinyPositionDefinition,
    )
    from .destiny_definitions_destiny_activity_challenge_definition import (
        DestinyDefinitionsDestinyActivityChallengeDefinition,
    )
    from .destiny_definitions_destiny_activity_definition import DestinyDefinitionsDestinyActivityDefinition
    from .destiny_definitions_destiny_activity_graph_list_entry_definition import (
        DestinyDefinitionsDestinyActivityGraphListEntryDefinition,
    )
    from .destiny_definitions_destiny_activity_guided_block_definition import (
        DestinyDefinitionsDestinyActivityGuidedBlockDefinition,
    )
    from .destiny_definitions_destiny_activity_insertion_point_definition import (
        DestinyDefinitionsDestinyActivityInsertionPointDefinition,
    )
    from .destiny_definitions_destiny_activity_loadout_requirement import (
        DestinyDefinitionsDestinyActivityLoadoutRequirement,
    )
    from .destiny_definitions_destiny_activity_loadout_requirement_set import (
        DestinyDefinitionsDestinyActivityLoadoutRequirementSet,
    )
    from .destiny_definitions_destiny_activity_matchmaking_block_definition import (
        DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition,
    )
    from .destiny_definitions_destiny_activity_mode_definition import DestinyDefinitionsDestinyActivityModeDefinition
    from .destiny_definitions_destiny_activity_modifier_reference_definition import (
        DestinyDefinitionsDestinyActivityModifierReferenceDefinition,
    )
    from .destiny_definitions_destiny_activity_playlist_item_definition import (
        DestinyDefinitionsDestinyActivityPlaylistItemDefinition,
    )
    from .destiny_definitions_destiny_activity_reward_definition import (
        DestinyDefinitionsDestinyActivityRewardDefinition,
    )
    from .destiny_definitions_destiny_activity_type_definition import DestinyDefinitionsDestinyActivityTypeDefinition
    from .destiny_definitions_destiny_activity_unlock_string_definition import (
        DestinyDefinitionsDestinyActivityUnlockStringDefinition,
    )
    from .destiny_definitions_destiny_arrangement_region_filter_definition import (
        DestinyDefinitionsDestinyArrangementRegionFilterDefinition,
    )
    from .destiny_definitions_destiny_art_dye_reference import DestinyDefinitionsDestinyArtDyeReference
    from .destiny_definitions_destiny_bubble_definition import DestinyDefinitionsDestinyBubbleDefinition
    from .destiny_definitions_destiny_class_definition import DestinyDefinitionsDestinyClassDefinition
    from .destiny_definitions_destiny_damage_type_definition import DestinyDefinitionsDestinyDamageTypeDefinition
    from .destiny_definitions_destiny_definition import DestinyDefinitionsDestinyDefinition
    from .destiny_definitions_destiny_destination_bubble_setting_definition import (
        DestinyDefinitionsDestinyDestinationBubbleSettingDefinition,
    )
    from .destiny_definitions_destiny_destination_definition import DestinyDefinitionsDestinyDestinationDefinition
    from .destiny_definitions_destiny_display_category_definition import (
        DestinyDefinitionsDestinyDisplayCategoryDefinition,
    )
    from .destiny_definitions_destiny_entity_search_result import DestinyDefinitionsDestinyEntitySearchResult
    from .destiny_definitions_destiny_entity_search_result_item import DestinyDefinitionsDestinyEntitySearchResultItem
    from .destiny_definitions_destiny_equipment_slot_definition import DestinyDefinitionsDestinyEquipmentSlotDefinition
    from .destiny_definitions_destiny_equipping_block_definition import (
        DestinyDefinitionsDestinyEquippingBlockDefinition,
    )
    from .destiny_definitions_destiny_faction_definition import DestinyDefinitionsDestinyFactionDefinition
    from .destiny_definitions_destiny_faction_vendor_definition import DestinyDefinitionsDestinyFactionVendorDefinition
    from .destiny_definitions_destiny_gear_art_arrangement_reference import (
        DestinyDefinitionsDestinyGearArtArrangementReference,
    )
    from .destiny_definitions_destiny_gender_definition import DestinyDefinitionsDestinyGenderDefinition
    from .destiny_definitions_destiny_inventory_bucket_definition import (
        DestinyDefinitionsDestinyInventoryBucketDefinition,
    )
    from .destiny_definitions_destiny_inventory_item_definition import DestinyDefinitionsDestinyInventoryItemDefinition
    from .destiny_definitions_destiny_inventory_item_stat_definition import (
        DestinyDefinitionsDestinyInventoryItemStatDefinition,
    )
    from .destiny_definitions_destiny_item_action_block_definition import (
        DestinyDefinitionsDestinyItemActionBlockDefinition,
    )
    from .destiny_definitions_destiny_item_action_required_item_definition import (
        DestinyDefinitionsDestinyItemActionRequiredItemDefinition,
    )
    from .destiny_definitions_destiny_item_category_definition import DestinyDefinitionsDestinyItemCategoryDefinition
    from .destiny_definitions_destiny_item_crafting_block_bonus_plug_definition import (
        DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition,
    )
    from .destiny_definitions_destiny_item_crafting_block_definition import (
        DestinyDefinitionsDestinyItemCraftingBlockDefinition,
    )
    from .destiny_definitions_destiny_item_creation_entry_level_definition import (
        DestinyDefinitionsDestinyItemCreationEntryLevelDefinition,
    )
    from .destiny_definitions_destiny_item_gearset_block_definition import (
        DestinyDefinitionsDestinyItemGearsetBlockDefinition,
    )
    from .destiny_definitions_destiny_item_intrinsic_socket_entry_definition import (
        DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition,
    )
    from .destiny_definitions_destiny_item_inventory_block_definition import (
        DestinyDefinitionsDestinyItemInventoryBlockDefinition,
    )
    from .destiny_definitions_destiny_item_investment_stat_definition import (
        DestinyDefinitionsDestinyItemInvestmentStatDefinition,
    )
    from .destiny_definitions_destiny_item_metric_block_definition import (
        DestinyDefinitionsDestinyItemMetricBlockDefinition,
    )
    from .destiny_definitions_destiny_item_objective_block_definition import (
        DestinyDefinitionsDestinyItemObjectiveBlockDefinition,
    )
    from .destiny_definitions_destiny_item_perk_entry_definition import DestinyDefinitionsDestinyItemPerkEntryDefinition
    from .destiny_definitions_destiny_item_preview_block_definition import (
        DestinyDefinitionsDestinyItemPreviewBlockDefinition,
    )
    from .destiny_definitions_destiny_item_quality_block_definition import (
        DestinyDefinitionsDestinyItemQualityBlockDefinition,
    )
    from .destiny_definitions_destiny_item_sack_block_definition import DestinyDefinitionsDestinyItemSackBlockDefinition
    from .destiny_definitions_destiny_item_set_block_definition import DestinyDefinitionsDestinyItemSetBlockDefinition
    from .destiny_definitions_destiny_item_set_block_entry_definition import (
        DestinyDefinitionsDestinyItemSetBlockEntryDefinition,
    )
    from .destiny_definitions_destiny_item_socket_block_definition import (
        DestinyDefinitionsDestinyItemSocketBlockDefinition,
    )
    from .destiny_definitions_destiny_item_socket_category_definition import (
        DestinyDefinitionsDestinyItemSocketCategoryDefinition,
    )
    from .destiny_definitions_destiny_item_socket_entry_definition import (
        DestinyDefinitionsDestinyItemSocketEntryDefinition,
    )
    from .destiny_definitions_destiny_item_socket_entry_plug_item_definition import (
        DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition,
    )
    from .destiny_definitions_destiny_item_socket_entry_plug_item_randomized_definition import (
        DestinyDefinitionsDestinyItemSocketEntryPlugItemRandomizedDefinition,
    )
    from .destiny_definitions_destiny_item_source_block_definition import (
        DestinyDefinitionsDestinyItemSourceBlockDefinition,
    )
    from .destiny_definitions_destiny_item_stat_block_definition import DestinyDefinitionsDestinyItemStatBlockDefinition
    from .destiny_definitions_destiny_item_summary_block_definition import (
        DestinyDefinitionsDestinyItemSummaryBlockDefinition,
    )
    from .destiny_definitions_destiny_item_talent_grid_block_definition import (
        DestinyDefinitionsDestinyItemTalentGridBlockDefinition,
    )
    from .destiny_definitions_destiny_item_tooltip_notification import DestinyDefinitionsDestinyItemTooltipNotification
    from .destiny_definitions_destiny_item_translation_block_definition import (
        DestinyDefinitionsDestinyItemTranslationBlockDefinition,
    )
    from .destiny_definitions_destiny_item_value_block_definition import (
        DestinyDefinitionsDestinyItemValueBlockDefinition,
    )
    from .destiny_definitions_destiny_item_vendor_source_reference import (
        DestinyDefinitionsDestinyItemVendorSourceReference,
    )
    from .destiny_definitions_destiny_item_version_definition import DestinyDefinitionsDestinyItemVersionDefinition
    from .destiny_definitions_destiny_location_definition import DestinyDefinitionsDestinyLocationDefinition
    from .destiny_definitions_destiny_location_release_definition import (
        DestinyDefinitionsDestinyLocationReleaseDefinition,
    )
    from .destiny_definitions_destiny_material_requirement import DestinyDefinitionsDestinyMaterialRequirement
    from .destiny_definitions_destiny_material_requirement_set_definition import (
        DestinyDefinitionsDestinyMaterialRequirementSetDefinition,
    )
    from .destiny_definitions_destiny_medal_tier_definition import DestinyDefinitionsDestinyMedalTierDefinition
    from .destiny_definitions_destiny_node_activation_requirement import (
        DestinyDefinitionsDestinyNodeActivationRequirement,
    )
    from .destiny_definitions_destiny_node_socket_replace_response import (
        DestinyDefinitionsDestinyNodeSocketReplaceResponse,
    )
    from .destiny_definitions_destiny_node_step_definition import DestinyDefinitionsDestinyNodeStepDefinition
    from .destiny_definitions_destiny_objective_definition import DestinyDefinitionsDestinyObjectiveDefinition
    from .destiny_definitions_destiny_objective_display_properties import (
        DestinyDefinitionsDestinyObjectiveDisplayProperties,
    )
    from .destiny_definitions_destiny_objective_perk_entry_definition import (
        DestinyDefinitionsDestinyObjectivePerkEntryDefinition,
    )
    from .destiny_definitions_destiny_objective_stat_entry_definition import (
        DestinyDefinitionsDestinyObjectiveStatEntryDefinition,
    )
    from .destiny_definitions_destiny_place_definition import DestinyDefinitionsDestinyPlaceDefinition
    from .destiny_definitions_destiny_plug_item_crafting_requirements import (
        DestinyDefinitionsDestinyPlugItemCraftingRequirements,
    )
    from .destiny_definitions_destiny_plug_item_crafting_unlock_requirement import (
        DestinyDefinitionsDestinyPlugItemCraftingUnlockRequirement,
    )
    from .destiny_definitions_destiny_progression_definition import DestinyDefinitionsDestinyProgressionDefinition
    from .destiny_definitions_destiny_progression_display_properties_definition import (
        DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition,
    )
    from .destiny_definitions_destiny_progression_mapping_definition import (
        DestinyDefinitionsDestinyProgressionMappingDefinition,
    )
    from .destiny_definitions_destiny_progression_reward_definition import (
        DestinyDefinitionsDestinyProgressionRewardDefinition,
    )
    from .destiny_definitions_destiny_progression_reward_item_quantity import (
        DestinyDefinitionsDestinyProgressionRewardItemQuantity,
    )
    from .destiny_definitions_destiny_progression_step_definition import (
        DestinyDefinitionsDestinyProgressionStepDefinition,
    )
    from .destiny_definitions_destiny_race_definition import DestinyDefinitionsDestinyRaceDefinition
    from .destiny_definitions_destiny_reward_source_category import DestinyDefinitionsDestinyRewardSourceCategory
    from .destiny_definitions_destiny_reward_source_definition import DestinyDefinitionsDestinyRewardSourceDefinition
    from .destiny_definitions_destiny_sandbox_pattern_definition import (
        DestinyDefinitionsDestinySandboxPatternDefinition,
    )
    from .destiny_definitions_destiny_sandbox_perk_definition import DestinyDefinitionsDestinySandboxPerkDefinition
    from .destiny_definitions_destiny_stat_definition import DestinyDefinitionsDestinyStatDefinition
    from .destiny_definitions_destiny_stat_display_definition import DestinyDefinitionsDestinyStatDisplayDefinition
    from .destiny_definitions_destiny_stat_group_definition import DestinyDefinitionsDestinyStatGroupDefinition
    from .destiny_definitions_destiny_stat_override_definition import DestinyDefinitionsDestinyStatOverrideDefinition
    from .destiny_definitions_destiny_talent_exclusive_group import DestinyDefinitionsDestinyTalentExclusiveGroup
    from .destiny_definitions_destiny_talent_grid_definition import DestinyDefinitionsDestinyTalentGridDefinition
    from .destiny_definitions_destiny_talent_node_category import DestinyDefinitionsDestinyTalentNodeCategory
    from .destiny_definitions_destiny_talent_node_definition import DestinyDefinitionsDestinyTalentNodeDefinition
    from .destiny_definitions_destiny_talent_node_exclusive_set_definition import (
        DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition,
    )
    from .destiny_definitions_destiny_talent_node_step_damage_types import (
        DestinyDefinitionsDestinyTalentNodeStepDamageTypes,
    )
    from .destiny_definitions_destiny_talent_node_step_groups import DestinyDefinitionsDestinyTalentNodeStepGroups
    from .destiny_definitions_destiny_talent_node_step_guardian_attributes import (
        DestinyDefinitionsDestinyTalentNodeStepGuardianAttributes,
    )
    from .destiny_definitions_destiny_talent_node_step_impact_effects import (
        DestinyDefinitionsDestinyTalentNodeStepImpactEffects,
    )
    from .destiny_definitions_destiny_talent_node_step_light_abilities import (
        DestinyDefinitionsDestinyTalentNodeStepLightAbilities,
    )
    from .destiny_definitions_destiny_talent_node_step_weapon_performances import (
        DestinyDefinitionsDestinyTalentNodeStepWeaponPerformances,
    )
    from .destiny_definitions_destiny_unlock_definition import DestinyDefinitionsDestinyUnlockDefinition
    from .destiny_definitions_destiny_unlock_expression_definition import (
        DestinyDefinitionsDestinyUnlockExpressionDefinition,
    )
    from .destiny_definitions_destiny_unlock_value_definition import DestinyDefinitionsDestinyUnlockValueDefinition
    from .destiny_definitions_destiny_vendor_accepted_item_definition import (
        DestinyDefinitionsDestinyVendorAcceptedItemDefinition,
    )
    from .destiny_definitions_destiny_vendor_action_definition import DestinyDefinitionsDestinyVendorActionDefinition
    from .destiny_definitions_destiny_vendor_category_entry_definition import (
        DestinyDefinitionsDestinyVendorCategoryEntryDefinition,
    )
    from .destiny_definitions_destiny_vendor_category_overlay_definition import (
        DestinyDefinitionsDestinyVendorCategoryOverlayDefinition,
    )
    from .destiny_definitions_destiny_vendor_definition import DestinyDefinitionsDestinyVendorDefinition
    from .destiny_definitions_destiny_vendor_display_properties_definition import (
        DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition,
    )
    from .destiny_definitions_destiny_vendor_group_definition import DestinyDefinitionsDestinyVendorGroupDefinition
    from .destiny_definitions_destiny_vendor_group_reference import DestinyDefinitionsDestinyVendorGroupReference
    from .destiny_definitions_destiny_vendor_interaction_definition import (
        DestinyDefinitionsDestinyVendorInteractionDefinition,
    )
    from .destiny_definitions_destiny_vendor_interaction_reply_definition import (
        DestinyDefinitionsDestinyVendorInteractionReplyDefinition,
    )
    from .destiny_definitions_destiny_vendor_interaction_sack_entry_definition import (
        DestinyDefinitionsDestinyVendorInteractionSackEntryDefinition,
    )
    from .destiny_definitions_destiny_vendor_inventory_flyout_bucket_definition import (
        DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition,
    )
    from .destiny_definitions_destiny_vendor_inventory_flyout_definition import (
        DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition,
    )
    from .destiny_definitions_destiny_vendor_item_definition import DestinyDefinitionsDestinyVendorItemDefinition
    from .destiny_definitions_destiny_vendor_item_quantity import DestinyDefinitionsDestinyVendorItemQuantity
    from .destiny_definitions_destiny_vendor_item_socket_override import (
        DestinyDefinitionsDestinyVendorItemSocketOverride,
    )
    from .destiny_definitions_destiny_vendor_requirement_display_entry_definition import (
        DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition,
    )
    from .destiny_definitions_destiny_vendor_sale_item_action_block_definition import (
        DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition,
    )
    from .destiny_definitions_destiny_vendor_service_definition import DestinyDefinitionsDestinyVendorServiceDefinition
    from .destiny_definitions_director_destiny_activity_graph_art_element_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_connection_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_display_objective_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_display_progression_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_node_activity_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_node_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_node_featuring_state_definition import (
        DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition,
    )
    from .destiny_definitions_director_destiny_activity_graph_node_state_entry import (
        DestinyDefinitionsDirectorDestinyActivityGraphNodeStateEntry,
    )
    from .destiny_definitions_director_destiny_linked_graph_definition import (
        DestinyDefinitionsDirectorDestinyLinkedGraphDefinition,
    )
    from .destiny_definitions_director_destiny_linked_graph_entry_definition import (
        DestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition,
    )
    from .destiny_definitions_energy_types_destiny_energy_type_definition import (
        DestinyDefinitionsEnergyTypesDestinyEnergyTypeDefinition,
    )
    from .destiny_definitions_guardian_ranks_destiny_guardian_rank_constants_definition import (
        DestinyDefinitionsGuardianRanksDestinyGuardianRankConstantsDefinition,
    )
    from .destiny_definitions_guardian_ranks_destiny_guardian_rank_definition import (
        DestinyDefinitionsGuardianRanksDestinyGuardianRankDefinition,
    )
    from .destiny_definitions_guardian_ranks_destiny_guardian_rank_icon_backgrounds_definition import (
        DestinyDefinitionsGuardianRanksDestinyGuardianRankIconBackgroundsDefinition,
    )
    from .destiny_definitions_items_destiny_derived_item_category_definition import (
        DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition,
    )
    from .destiny_definitions_items_destiny_derived_item_definition import (
        DestinyDefinitionsItemsDestinyDerivedItemDefinition,
    )
    from .destiny_definitions_items_destiny_energy_capacity_entry import (
        DestinyDefinitionsItemsDestinyEnergyCapacityEntry,
    )
    from .destiny_definitions_items_destiny_energy_cost_entry import DestinyDefinitionsItemsDestinyEnergyCostEntry
    from .destiny_definitions_items_destiny_item_plug_definition import DestinyDefinitionsItemsDestinyItemPlugDefinition
    from .destiny_definitions_items_destiny_item_tier_type_definition import (
        DestinyDefinitionsItemsDestinyItemTierTypeDefinition,
    )
    from .destiny_definitions_items_destiny_item_tier_type_infusion_block import (
        DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock,
    )
    from .destiny_definitions_items_destiny_parent_item_override import DestinyDefinitionsItemsDestinyParentItemOverride
    from .destiny_definitions_items_destiny_plug_rule_definition import DestinyDefinitionsItemsDestinyPlugRuleDefinition
    from .destiny_definitions_loadouts_destiny_loadout_color_definition import (
        DestinyDefinitionsLoadoutsDestinyLoadoutColorDefinition,
    )
    from .destiny_definitions_loadouts_destiny_loadout_constants_definition import (
        DestinyDefinitionsLoadoutsDestinyLoadoutConstantsDefinition,
    )
    from .destiny_definitions_loadouts_destiny_loadout_icon_definition import (
        DestinyDefinitionsLoadoutsDestinyLoadoutIconDefinition,
    )
    from .destiny_definitions_loadouts_destiny_loadout_name_definition import (
        DestinyDefinitionsLoadoutsDestinyLoadoutNameDefinition,
    )
    from .destiny_definitions_lore_destiny_lore_definition import DestinyDefinitionsLoreDestinyLoreDefinition
    from .destiny_definitions_metrics_destiny_metric_definition import DestinyDefinitionsMetricsDestinyMetricDefinition
    from .destiny_definitions_milestones_destiny_milestone_activity_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_activity_variant_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_challenge_activity_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_challenge_activity_graph_node_entry import (
        DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityGraphNodeEntry,
    )
    from .destiny_definitions_milestones_destiny_milestone_challenge_activity_phase import (
        DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase,
    )
    from .destiny_definitions_milestones_destiny_milestone_challenge_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_display_preference import (
        DestinyDefinitionsMilestonesDestinyMilestoneDisplayPreference,
    )
    from .destiny_definitions_milestones_destiny_milestone_quest_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_quest_reward_item import (
        DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem,
    )
    from .destiny_definitions_milestones_destiny_milestone_quest_rewards_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_reward_category_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_reward_entry_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_type import DestinyDefinitionsMilestonesDestinyMilestoneType
    from .destiny_definitions_milestones_destiny_milestone_value_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneValueDefinition,
    )
    from .destiny_definitions_milestones_destiny_milestone_vendor_definition import (
        DestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition,
    )
    from .destiny_definitions_power_caps_destiny_power_cap_definition import (
        DestinyDefinitionsPowerCapsDestinyPowerCapDefinition,
    )
    from .destiny_definitions_presentation_destiny_presentation_child_block import (
        DestinyDefinitionsPresentationDestinyPresentationChildBlock,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_base_definition import (
        DestinyDefinitionsPresentationDestinyPresentationNodeBaseDefinition,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_child_entry import (
        DestinyDefinitionsPresentationDestinyPresentationNodeChildEntry,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_child_entry_base import (
        DestinyDefinitionsPresentationDestinyPresentationNodeChildEntryBase,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_children_block import (
        DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_collectible_child_entry import (
        DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_craftable_child_entry import (
        DestinyDefinitionsPresentationDestinyPresentationNodeCraftableChildEntry,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_definition import (
        DestinyDefinitionsPresentationDestinyPresentationNodeDefinition,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_metric_child_entry import (
        DestinyDefinitionsPresentationDestinyPresentationNodeMetricChildEntry,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_record_child_entry import (
        DestinyDefinitionsPresentationDestinyPresentationNodeRecordChildEntry,
    )
    from .destiny_definitions_presentation_destiny_presentation_node_requirements_block import (
        DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock,
    )
    from .destiny_definitions_presentation_destiny_scored_presentation_node_base_definition import (
        DestinyDefinitionsPresentationDestinyScoredPresentationNodeBaseDefinition,
    )
    from .destiny_definitions_progression_destiny_progression_level_requirement_definition import (
        DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition,
    )
    from .destiny_definitions_records_destiny_record_completion_block import (
        DestinyDefinitionsRecordsDestinyRecordCompletionBlock,
    )
    from .destiny_definitions_records_destiny_record_definition import DestinyDefinitionsRecordsDestinyRecordDefinition
    from .destiny_definitions_records_destiny_record_expiration_block import (
        DestinyDefinitionsRecordsDestinyRecordExpirationBlock,
    )
    from .destiny_definitions_records_destiny_record_interval_block import (
        DestinyDefinitionsRecordsDestinyRecordIntervalBlock,
    )
    from .destiny_definitions_records_destiny_record_interval_objective import (
        DestinyDefinitionsRecordsDestinyRecordIntervalObjective,
    )
    from .destiny_definitions_records_destiny_record_interval_rewards import (
        DestinyDefinitionsRecordsDestinyRecordIntervalRewards,
    )
    from .destiny_definitions_records_destiny_record_title_block import DestinyDefinitionsRecordsDestinyRecordTitleBlock
    from .destiny_definitions_records_schema_record_state_block import DestinyDefinitionsRecordsSchemaRecordStateBlock
    from .destiny_definitions_reporting_destiny_report_reason_category_definition import (
        DestinyDefinitionsReportingDestinyReportReasonCategoryDefinition,
    )
    from .destiny_definitions_reporting_destiny_report_reason_definition import (
        DestinyDefinitionsReportingDestinyReportReasonDefinition,
    )
    from .destiny_definitions_seasons_destiny_event_card_definition import (
        DestinyDefinitionsSeasonsDestinyEventCardDefinition,
    )
    from .destiny_definitions_seasons_destiny_event_card_images import DestinyDefinitionsSeasonsDestinyEventCardImages
    from .destiny_definitions_seasons_destiny_season_definition import DestinyDefinitionsSeasonsDestinySeasonDefinition
    from .destiny_definitions_seasons_destiny_season_pass_definition import (
        DestinyDefinitionsSeasonsDestinySeasonPassDefinition,
    )
    from .destiny_definitions_seasons_destiny_season_preview_definition import (
        DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition,
    )
    from .destiny_definitions_seasons_destiny_season_preview_image_definition import (
        DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition,
    )
    from .destiny_definitions_social_destiny_social_commendation_definition import (
        DestinyDefinitionsSocialDestinySocialCommendationDefinition,
    )
    from .destiny_definitions_social_destiny_social_commendation_node_definition import (
        DestinyDefinitionsSocialDestinySocialCommendationNodeDefinition,
    )
    from .destiny_definitions_sockets_destiny_insert_plug_action_definition import (
        DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition,
    )
    from .destiny_definitions_sockets_destiny_plug_set_definition import (
        DestinyDefinitionsSocketsDestinyPlugSetDefinition,
    )
    from .destiny_definitions_sockets_destiny_plug_whitelist_entry_definition import (
        DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition,
    )
    from .destiny_definitions_sockets_destiny_socket_category_definition import (
        DestinyDefinitionsSocketsDestinySocketCategoryDefinition,
    )
    from .destiny_definitions_sockets_destiny_socket_type_definition import (
        DestinyDefinitionsSocketsDestinySocketTypeDefinition,
    )
    from .destiny_definitions_sockets_destiny_socket_type_scalar_material_requirement_entry import (
        DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry,
    )
    from .destiny_definitions_sources_destiny_item_source_definition import (
        DestinyDefinitionsSourcesDestinyItemSourceDefinition,
    )
    from .destiny_definitions_traits_destiny_trait_definition import DestinyDefinitionsTraitsDestinyTraitDefinition
    from .destiny_definitions_vendors_destiny_vendor_location_definition import (
        DestinyDefinitionsVendorsDestinyVendorLocationDefinition,
    )
    from .destiny_destiny_activity import DestinyDestinyActivity
    from .destiny_destiny_activity_difficulty_tier import DestinyDestinyActivityDifficultyTier
    from .destiny_destiny_activity_mode_category import DestinyDestinyActivityModeCategory
    from .destiny_destiny_activity_nav_point_type import DestinyDestinyActivityNavPointType
    from .destiny_destiny_ammunition_type import DestinyDestinyAmmunitionType
    from .destiny_destiny_breaker_type import DestinyDestinyBreakerType
    from .destiny_destiny_class import DestinyDestinyClass
    from .destiny_destiny_collectible_state import DestinyDestinyCollectibleState
    from .destiny_destiny_component_type import DestinyDestinyComponentType
    from .destiny_destiny_energy_type import DestinyDestinyEnergyType
    from .destiny_destiny_equip_item_result import DestinyDestinyEquipItemResult
    from .destiny_destiny_equip_item_results import DestinyDestinyEquipItemResults
    from .destiny_destiny_game_privacy_setting import DestinyDestinyGamePrivacySetting
    from .destiny_destiny_game_versions import DestinyDestinyGameVersions
    from .destiny_destiny_gating_scope import DestinyDestinyGatingScope
    from .destiny_destiny_gender import DestinyDestinyGender
    from .destiny_destiny_graph_node_state import DestinyDestinyGraphNodeState
    from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity
    from .destiny_destiny_item_sort_type import DestinyDestinyItemSortType
    from .destiny_destiny_item_sub_type import DestinyDestinyItemSubType
    from .destiny_destiny_item_type import DestinyDestinyItemType
    from .destiny_destiny_join_closed_reasons import DestinyDestinyJoinClosedReasons
    from .destiny_destiny_objective_grant_style import DestinyDestinyObjectiveGrantStyle
    from .destiny_destiny_objective_ui_style import DestinyDestinyObjectiveUiStyle
    from .destiny_destiny_party_member_states import DestinyDestinyPartyMemberStates
    from .destiny_destiny_presentation_display_style import DestinyDestinyPresentationDisplayStyle
    from .destiny_destiny_presentation_node_state import DestinyDestinyPresentationNodeState
    from .destiny_destiny_presentation_node_type import DestinyDestinyPresentationNodeType
    from .destiny_destiny_presentation_screen_style import DestinyDestinyPresentationScreenStyle
    from .destiny_destiny_progression import DestinyDestinyProgression
    from .destiny_destiny_progression_reset_entry import DestinyDestinyProgressionResetEntry
    from .destiny_destiny_progression_reward_item_acquisition_behavior import (
        DestinyDestinyProgressionRewardItemAcquisitionBehavior,
    )
    from .destiny_destiny_progression_reward_item_state import DestinyDestinyProgressionRewardItemState
    from .destiny_destiny_progression_scope import DestinyDestinyProgressionScope
    from .destiny_destiny_progression_step_display_effect import DestinyDestinyProgressionStepDisplayEffect
    from .destiny_destiny_race import DestinyDestinyRace
    from .destiny_destiny_record_state import DestinyDestinyRecordState
    from .destiny_destiny_record_toast_style import DestinyDestinyRecordToastStyle
    from .destiny_destiny_record_value_style import DestinyDestinyRecordValueStyle
    from .destiny_destiny_scope import DestinyDestinyScope
    from .destiny_destiny_socket_category_style import DestinyDestinySocketCategoryStyle
    from .destiny_destiny_socket_visibility import DestinyDestinySocketVisibility
    from .destiny_destiny_stat import DestinyDestinyStat
    from .destiny_destiny_stat_aggregation_type import DestinyDestinyStatAggregationType
    from .destiny_destiny_stat_category import DestinyDestinyStatCategory
    from .destiny_destiny_talent_node import DestinyDestinyTalentNode
    from .destiny_destiny_talent_node_stat_block import DestinyDestinyTalentNodeStatBlock
    from .destiny_destiny_talent_node_state import DestinyDestinyTalentNodeState
    from .destiny_destiny_unlock_status import DestinyDestinyUnlockStatus
    from .destiny_destiny_unlock_value_ui_style import DestinyDestinyUnlockValueUiStyle
    from .destiny_destiny_vendor_filter import DestinyDestinyVendorFilter
    from .destiny_destiny_vendor_interaction_reward_selection import DestinyDestinyVendorInteractionRewardSelection
    from .destiny_destiny_vendor_item_refund_policy import DestinyDestinyVendorItemRefundPolicy
    from .destiny_destiny_vendor_item_state import DestinyDestinyVendorItemState
    from .destiny_destiny_vendor_progression_type import DestinyDestinyVendorProgressionType
    from .destiny_destiny_vendor_reply_type import DestinyDestinyVendorReplyType
    from .destiny_dye_reference import DestinyDyeReference
    from .destiny_entities_characters_destiny_character_activities_component import (
        DestinyEntitiesCharactersDestinyCharacterActivitiesComponent,
    )
    from .destiny_entities_characters_destiny_character_component import (
        DestinyEntitiesCharactersDestinyCharacterComponent,
    )
    from .destiny_entities_characters_destiny_character_progression_component import (
        DestinyEntitiesCharactersDestinyCharacterProgressionComponent,
    )
    from .destiny_entities_characters_destiny_character_render_component import (
        DestinyEntitiesCharactersDestinyCharacterRenderComponent,
    )
    from .destiny_entities_inventory_destiny_inventory_component import (
        DestinyEntitiesInventoryDestinyInventoryComponent,
    )
    from .destiny_entities_items_destiny_item_component import DestinyEntitiesItemsDestinyItemComponent
    from .destiny_entities_items_destiny_item_instance_component import DestinyEntitiesItemsDestinyItemInstanceComponent
    from .destiny_entities_items_destiny_item_instance_energy import DestinyEntitiesItemsDestinyItemInstanceEnergy
    from .destiny_entities_items_destiny_item_objectives_component import (
        DestinyEntitiesItemsDestinyItemObjectivesComponent,
    )
    from .destiny_entities_items_destiny_item_perks_component import DestinyEntitiesItemsDestinyItemPerksComponent
    from .destiny_entities_items_destiny_item_render_component import DestinyEntitiesItemsDestinyItemRenderComponent
    from .destiny_entities_items_destiny_item_socket_state import DestinyEntitiesItemsDestinyItemSocketState
    from .destiny_entities_items_destiny_item_sockets_component import DestinyEntitiesItemsDestinyItemSocketsComponent
    from .destiny_entities_items_destiny_item_stats_component import DestinyEntitiesItemsDestinyItemStatsComponent
    from .destiny_entities_items_destiny_item_talent_grid_component import (
        DestinyEntitiesItemsDestinyItemTalentGridComponent,
    )
    from .destiny_entities_profiles_destiny_profile_component import DestinyEntitiesProfilesDestinyProfileComponent
    from .destiny_entities_profiles_destiny_vendor_receipts_component import (
        DestinyEntitiesProfilesDestinyVendorReceiptsComponent,
    )
    from .destiny_entities_vendors_destiny_vendor_categories_component import (
        DestinyEntitiesVendorsDestinyVendorCategoriesComponent,
    )
    from .destiny_entities_vendors_destiny_vendor_category import DestinyEntitiesVendorsDestinyVendorCategory
    from .destiny_entities_vendors_destiny_vendor_component import DestinyEntitiesVendorsDestinyVendorComponent
    from .destiny_entities_vendors_destiny_vendor_sale_item_component import (
        DestinyEntitiesVendorsDestinyVendorSaleItemComponent,
    )
    from .destiny_equip_failure_reason import DestinyEquipFailureReason
    from .destiny_equipping_item_block_attributes import DestinyEquippingItemBlockAttributes
    from .destiny_historical_stats_definitions_destiny_activity_mode_type import (
        DestinyHistoricalStatsDefinitionsDestinyActivityModeType,
    )
    from .destiny_historical_stats_definitions_destiny_activity_mode_type_array import (
        DestinyHistoricalStatsDefinitionsDestinyActivityModeTypeArray,
    )
    from .destiny_historical_stats_definitions_destiny_historical_stats_definition import (
        DestinyHistoricalStatsDefinitionsDestinyHistoricalStatsDefinition,
    )
    from .destiny_historical_stats_definitions_destiny_stats_category_type import (
        DestinyHistoricalStatsDefinitionsDestinyStatsCategoryType,
    )
    from .destiny_historical_stats_definitions_destiny_stats_group_type import (
        DestinyHistoricalStatsDefinitionsDestinyStatsGroupType,
    )
    from .destiny_historical_stats_definitions_destiny_stats_merge_method import (
        DestinyHistoricalStatsDefinitionsDestinyStatsMergeMethod,
    )
    from .destiny_historical_stats_definitions_period_type import DestinyHistoricalStatsDefinitionsPeriodType
    from .destiny_historical_stats_definitions_period_type_array import DestinyHistoricalStatsDefinitionsPeriodTypeArray
    from .destiny_historical_stats_definitions_unit_type import DestinyHistoricalStatsDefinitionsUnitType
    from .destiny_historical_stats_destiny_activity_history_results import (
        DestinyHistoricalStatsDestinyActivityHistoryResults,
    )
    from .destiny_historical_stats_destiny_aggregate_activity_results import (
        DestinyHistoricalStatsDestinyAggregateActivityResults,
    )
    from .destiny_historical_stats_destiny_aggregate_activity_stats import (
        DestinyHistoricalStatsDestinyAggregateActivityStats,
    )
    from .destiny_historical_stats_destiny_clan_aggregate_stat import DestinyHistoricalStatsDestinyClanAggregateStat
    from .destiny_historical_stats_destiny_historical_stats_account_result import (
        DestinyHistoricalStatsDestinyHistoricalStatsAccountResult,
    )
    from .destiny_historical_stats_destiny_historical_stats_activity import (
        DestinyHistoricalStatsDestinyHistoricalStatsActivity,
    )
    from .destiny_historical_stats_destiny_historical_stats_by_period import (
        DestinyHistoricalStatsDestinyHistoricalStatsByPeriod,
    )
    from .destiny_historical_stats_destiny_historical_stats_per_character import (
        DestinyHistoricalStatsDestinyHistoricalStatsPerCharacter,
    )
    from .destiny_historical_stats_destiny_historical_stats_period_group import (
        DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup,
    )
    from .destiny_historical_stats_destiny_historical_stats_results import (
        DestinyHistoricalStatsDestinyHistoricalStatsResults,
    )
    from .destiny_historical_stats_destiny_historical_stats_value import (
        DestinyHistoricalStatsDestinyHistoricalStatsValue,
    )
    from .destiny_historical_stats_destiny_historical_stats_value_pair import (
        DestinyHistoricalStatsDestinyHistoricalStatsValuePair,
    )
    from .destiny_historical_stats_destiny_historical_stats_with_merged import (
        DestinyHistoricalStatsDestinyHistoricalStatsWithMerged,
    )
    from .destiny_historical_stats_destiny_historical_weapon_stats import (
        DestinyHistoricalStatsDestinyHistoricalWeaponStats,
    )
    from .destiny_historical_stats_destiny_historical_weapon_stats_data import (
        DestinyHistoricalStatsDestinyHistoricalWeaponStatsData,
    )
    from .destiny_historical_stats_destiny_leaderboard import DestinyHistoricalStatsDestinyLeaderboard
    from .destiny_historical_stats_destiny_leaderboard_entry import DestinyHistoricalStatsDestinyLeaderboardEntry
    from .destiny_historical_stats_destiny_leaderboard_results import DestinyHistoricalStatsDestinyLeaderboardResults
    from .destiny_historical_stats_destiny_player import DestinyHistoricalStatsDestinyPlayer
    from .destiny_historical_stats_destiny_post_game_carnage_report_data import (
        DestinyHistoricalStatsDestinyPostGameCarnageReportData,
    )
    from .destiny_historical_stats_destiny_post_game_carnage_report_entry import (
        DestinyHistoricalStatsDestinyPostGameCarnageReportEntry,
    )
    from .destiny_historical_stats_destiny_post_game_carnage_report_extended_data import (
        DestinyHistoricalStatsDestinyPostGameCarnageReportExtendedData,
    )
    from .destiny_historical_stats_destiny_post_game_carnage_report_team_entry import (
        DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry,
    )
    from .destiny_item_bind_status import DestinyItemBindStatus
    from .destiny_item_component_set_ofint32 import DestinyItemComponentSetOfint32
    from .destiny_item_component_set_ofint64 import DestinyItemComponentSetOfint64
    from .destiny_item_component_set_ofuint32 import DestinyItemComponentSetOfuint32
    from .destiny_item_location import DestinyItemLocation
    from .destiny_item_perk_visibility import DestinyItemPerkVisibility
    from .destiny_item_state import DestinyItemState
    from .destiny_milestones_destiny_milestone import DestinyMilestonesDestinyMilestone
    from .destiny_milestones_destiny_milestone_activity import DestinyMilestonesDestinyMilestoneActivity
    from .destiny_milestones_destiny_milestone_activity_completion_status import (
        DestinyMilestonesDestinyMilestoneActivityCompletionStatus,
    )
    from .destiny_milestones_destiny_milestone_activity_phase import DestinyMilestonesDestinyMilestoneActivityPhase
    from .destiny_milestones_destiny_milestone_activity_variant import DestinyMilestonesDestinyMilestoneActivityVariant
    from .destiny_milestones_destiny_milestone_challenge_activity import (
        DestinyMilestonesDestinyMilestoneChallengeActivity,
    )
    from .destiny_milestones_destiny_milestone_content import DestinyMilestonesDestinyMilestoneContent
    from .destiny_milestones_destiny_milestone_content_item_category import (
        DestinyMilestonesDestinyMilestoneContentItemCategory,
    )
    from .destiny_milestones_destiny_milestone_quest import DestinyMilestonesDestinyMilestoneQuest
    from .destiny_milestones_destiny_milestone_reward_category import DestinyMilestonesDestinyMilestoneRewardCategory
    from .destiny_milestones_destiny_milestone_reward_entry import DestinyMilestonesDestinyMilestoneRewardEntry
    from .destiny_milestones_destiny_milestone_vendor import DestinyMilestonesDestinyMilestoneVendor
    from .destiny_milestones_destiny_public_milestone import DestinyMilestonesDestinyPublicMilestone
    from .destiny_milestones_destiny_public_milestone_activity import DestinyMilestonesDestinyPublicMilestoneActivity
    from .destiny_milestones_destiny_public_milestone_activity_variant import (
        DestinyMilestonesDestinyPublicMilestoneActivityVariant,
    )
    from .destiny_milestones_destiny_public_milestone_challenge import DestinyMilestonesDestinyPublicMilestoneChallenge
    from .destiny_milestones_destiny_public_milestone_challenge_activity import (
        DestinyMilestonesDestinyPublicMilestoneChallengeActivity,
    )
    from .destiny_milestones_destiny_public_milestone_quest import DestinyMilestonesDestinyPublicMilestoneQuest
    from .destiny_milestones_destiny_public_milestone_vendor import DestinyMilestonesDestinyPublicMilestoneVendor
    from .destiny_misc_destiny_color import DestinyMiscDestinyColor
    from .destiny_perks_destiny_perk_reference import DestinyPerksDestinyPerkReference
    from .destiny_plug_availability_mode import DestinyPlugAvailabilityMode
    from .destiny_plug_ui_styles import DestinyPlugUiStyles
    from .destiny_progression_destiny_faction_progression import DestinyProgressionDestinyFactionProgression
    from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress
    from .destiny_quests_destiny_quest_status import DestinyQuestsDestinyQuestStatus
    from .destiny_reporting_requests_destiny_report_offense_pgcr_request import (
        DestinyReportingRequestsDestinyReportOffensePgcrRequest,
    )
    from .destiny_requests_actions_destiny_action_request import DestinyRequestsActionsDestinyActionRequest
    from .destiny_requests_actions_destiny_character_action_request import (
        DestinyRequestsActionsDestinyCharacterActionRequest,
    )
    from .destiny_requests_actions_destiny_insert_plugs_action_request import (
        DestinyRequestsActionsDestinyInsertPlugsActionRequest,
    )
    from .destiny_requests_actions_destiny_insert_plugs_free_action_request import (
        DestinyRequestsActionsDestinyInsertPlugsFreeActionRequest,
    )
    from .destiny_requests_actions_destiny_insert_plugs_request_entry import (
        DestinyRequestsActionsDestinyInsertPlugsRequestEntry,
    )
    from .destiny_requests_actions_destiny_item_action_request import DestinyRequestsActionsDestinyItemActionRequest
    from .destiny_requests_actions_destiny_item_set_action_request import (
        DestinyRequestsActionsDestinyItemSetActionRequest,
    )
    from .destiny_requests_actions_destiny_item_state_request import DestinyRequestsActionsDestinyItemStateRequest
    from .destiny_requests_actions_destiny_loadout_action_request import (
        DestinyRequestsActionsDestinyLoadoutActionRequest,
    )
    from .destiny_requests_actions_destiny_loadout_update_action_request import (
        DestinyRequestsActionsDestinyLoadoutUpdateActionRequest,
    )
    from .destiny_requests_actions_destiny_postmaster_transfer_request import (
        DestinyRequestsActionsDestinyPostmasterTransferRequest,
    )
    from .destiny_requests_actions_destiny_socket_array_type import DestinyRequestsActionsDestinySocketArrayType
    from .destiny_requests_destiny_item_transfer_request import DestinyRequestsDestinyItemTransferRequest
    from .destiny_responses_destiny_character_response import DestinyResponsesDestinyCharacterResponse
    from .destiny_responses_destiny_collectible_node_detail_response import (
        DestinyResponsesDestinyCollectibleNodeDetailResponse,
    )
    from .destiny_responses_destiny_error_profile import DestinyResponsesDestinyErrorProfile
    from .destiny_responses_destiny_item_change_response import DestinyResponsesDestinyItemChangeResponse
    from .destiny_responses_destiny_item_response import DestinyResponsesDestinyItemResponse
    from .destiny_responses_destiny_linked_profiles_response import DestinyResponsesDestinyLinkedProfilesResponse
    from .destiny_responses_destiny_profile_response import DestinyResponsesDestinyProfileResponse
    from .destiny_responses_destiny_profile_user_info_card import DestinyResponsesDestinyProfileUserInfoCard
    from .destiny_responses_destiny_public_vendors_response import DestinyResponsesDestinyPublicVendorsResponse
    from .destiny_responses_destiny_vendor_response import DestinyResponsesDestinyVendorResponse
    from .destiny_responses_destiny_vendors_response import DestinyResponsesDestinyVendorsResponse
    from .destiny_responses_inventory_changed_response import DestinyResponsesInventoryChangedResponse
    from .destiny_responses_personal_destiny_vendor_sale_item_set_component import (
        DestinyResponsesPersonalDestinyVendorSaleItemSetComponent,
    )
    from .destiny_responses_public_destiny_vendor_sale_item_set_component import (
        DestinyResponsesPublicDestinyVendorSaleItemSetComponent,
    )
    from .destiny_socket_plug_sources import DestinySocketPlugSources
    from .destiny_socket_type_action_type import DestinySocketTypeActionType
    from .destiny_sockets_destiny_item_plug import DestinySocketsDestinyItemPlug
    from .destiny_sockets_destiny_item_plug_base import DestinySocketsDestinyItemPlugBase
    from .destiny_special_item_type import DestinySpecialItemType
    from .destiny_tier_type import DestinyTierType
    from .destiny_transfer_statuses import DestinyTransferStatuses
    from .destiny_vendor_display_category_sort_order import DestinyVendorDisplayCategorySortOrder
    from .destiny_vendor_interaction_type import DestinyVendorInteractionType
    from .destiny_vendor_item_status import DestinyVendorItemStatus
    from .destiny_vendor_sale_item_set_component_of_destiny_public_vendor_sale_item_component import (
        DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent,
    )
    from .destiny_vendor_sale_item_set_component_of_destiny_vendor_sale_item_component import (
        DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent,
    )
    from .destiny_vendors_destiny_vendor_receipt import DestinyVendorsDestinyVendorReceipt
    from .dictionary_component_response_ofint32and_destiny_item_instance_component import (
        DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_objectives_component import (
        DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_perks_component import (
        DictionaryComponentResponseOfint32AndDestinyItemPerksComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_plug_objectives_component import (
        DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_render_component import (
        DictionaryComponentResponseOfint32AndDestinyItemRenderComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_reusable_plugs_component import (
        DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_sockets_component import (
        DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_stats_component import (
        DictionaryComponentResponseOfint32AndDestinyItemStatsComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_item_talent_grid_component import (
        DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent,
    )
    from .dictionary_component_response_ofint32and_destiny_vendor_sale_item_component import (
        DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_character_activities_component import (
        DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_character_component import (
        DictionaryComponentResponseOfint64AndDestinyCharacterComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_character_progression_component import (
        DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_character_records_component import (
        DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_character_render_component import (
        DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_collectibles_component import (
        DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_craftables_component import (
        DictionaryComponentResponseOfint64AndDestinyCraftablesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_currencies_component import (
        DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_inventory_component import (
        DictionaryComponentResponseOfint64AndDestinyInventoryComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_instance_component import (
        DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_objectives_component import (
        DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_perks_component import (
        DictionaryComponentResponseOfint64AndDestinyItemPerksComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_plug_objectives_component import (
        DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_render_component import (
        DictionaryComponentResponseOfint64AndDestinyItemRenderComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_reusable_plugs_component import (
        DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_sockets_component import (
        DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_stats_component import (
        DictionaryComponentResponseOfint64AndDestinyItemStatsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_item_talent_grid_component import (
        DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_kiosks_component import (
        DictionaryComponentResponseOfint64AndDestinyKiosksComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_loadouts_component import (
        DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_plug_sets_component import (
        DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_presentation_nodes_component import (
        DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent,
    )
    from .dictionary_component_response_ofint64and_destiny_string_variables_component import (
        DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_instance_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_objectives_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_perks_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_plug_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_plug_objectives_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_render_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_reusable_plugs_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_sockets_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_stats_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_item_talent_grid_component import (
        DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_public_vendor_component import (
        DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_vendor_categories_component import (
        DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent,
    )
    from .dictionary_component_response_ofuint32and_destiny_vendor_component import (
        DictionaryComponentResponseOfuint32AndDestinyVendorComponent,
    )
    from .dictionary_component_response_ofuint32and_personal_destiny_vendor_sale_item_set_component import (
        DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent,
    )
    from .dictionary_component_response_ofuint32and_public_destiny_vendor_sale_item_set_component import (
        DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent,
    )
    from .entities_entity_action_result import EntitiesEntityActionResult
    from .exceptions_platform_error_codes import ExceptionsPlatformErrorCodes
    from .fireteam_fireteam_date_range import FireteamFireteamDateRange
    from .fireteam_fireteam_member import FireteamFireteamMember
    from .fireteam_fireteam_platform import FireteamFireteamPlatform
    from .fireteam_fireteam_platform_invite_result import FireteamFireteamPlatformInviteResult
    from .fireteam_fireteam_public_search_option import FireteamFireteamPublicSearchOption
    from .fireteam_fireteam_response import FireteamFireteamResponse
    from .fireteam_fireteam_slot_search import FireteamFireteamSlotSearch
    from .fireteam_fireteam_summary import FireteamFireteamSummary
    from .fireteam_fireteam_user_info_card import FireteamFireteamUserInfoCard
    from .forum_community_content_sort_mode import ForumCommunityContentSortMode
    from .forum_forum_media_type import ForumForumMediaType
    from .forum_forum_post_popularity import ForumForumPostPopularity
    from .forum_forum_post_sort_enum import ForumForumPostSortEnum
    from .forum_forum_recruitment_detail import ForumForumRecruitmentDetail
    from .forum_forum_recruitment_intensity_label import ForumForumRecruitmentIntensityLabel
    from .forum_forum_recruitment_tone_label import ForumForumRecruitmentToneLabel
    from .forum_forum_topics_category_filters_enum import ForumForumTopicsCategoryFiltersEnum
    from .forum_forum_topics_quick_date_enum import ForumForumTopicsQuickDateEnum
    from .forum_forum_topics_sort_enum import ForumForumTopicsSortEnum
    from .forum_poll_response import ForumPollResponse
    from .forum_poll_result import ForumPollResult
    from .forum_post_response import ForumPostResponse
    from .forum_post_search_response import ForumPostSearchResponse
    from .forums_forum_flags_enum import ForumsForumFlagsEnum
    from .forums_forum_post_category_enums import ForumsForumPostCategoryEnums
    from .global_alert import GlobalAlert
    from .global_alert_level import GlobalAlertLevel
    from .global_alert_type import GlobalAlertType
    from .groups_v2capabilities import GroupsV2Capabilities
    from .groups_v2chat_security_setting import GroupsV2ChatSecuritySetting
    from .groups_v2clan_banner import GroupsV2ClanBanner
    from .groups_v2get_groups_for_member_response import GroupsV2GetGroupsForMemberResponse
    from .groups_v2group_alliance_status import GroupsV2GroupAllianceStatus
    from .groups_v2group_application_list_request import GroupsV2GroupApplicationListRequest
    from .groups_v2group_application_request import GroupsV2GroupApplicationRequest
    from .groups_v2group_application_resolve_state import GroupsV2GroupApplicationResolveState
    from .groups_v2group_application_response import GroupsV2GroupApplicationResponse
    from .groups_v2group_ban import GroupsV2GroupBan
    from .groups_v2group_ban_request import GroupsV2GroupBanRequest
    from .groups_v2group_date_range import GroupsV2GroupDateRange
    from .groups_v2group_edit_action import GroupsV2GroupEditAction
    from .groups_v2group_features import GroupsV2GroupFeatures
    from .groups_v2group_homepage import GroupsV2GroupHomepage
    from .groups_v2group_member import GroupsV2GroupMember
    from .groups_v2group_member_application import GroupsV2GroupMemberApplication
    from .groups_v2group_member_count_filter import GroupsV2GroupMemberCountFilter
    from .groups_v2group_member_leave_result import GroupsV2GroupMemberLeaveResult
    from .groups_v2group_membership import GroupsV2GroupMembership
    from .groups_v2group_membership_base import GroupsV2GroupMembershipBase
    from .groups_v2group_membership_search_response import GroupsV2GroupMembershipSearchResponse
    from .groups_v2group_name_search_request import GroupsV2GroupNameSearchRequest
    from .groups_v2group_optional_conversation import GroupsV2GroupOptionalConversation
    from .groups_v2group_optional_conversation_add_request import GroupsV2GroupOptionalConversationAddRequest
    from .groups_v2group_optional_conversation_edit_request import GroupsV2GroupOptionalConversationEditRequest
    from .groups_v2group_options_edit_action import GroupsV2GroupOptionsEditAction
    from .groups_v2group_post_publicity import GroupsV2GroupPostPublicity
    from .groups_v2group_potential_member import GroupsV2GroupPotentialMember
    from .groups_v2group_potential_member_status import GroupsV2GroupPotentialMemberStatus
    from .groups_v2group_potential_membership import GroupsV2GroupPotentialMembership
    from .groups_v2group_potential_membership_search_response import GroupsV2GroupPotentialMembershipSearchResponse
    from .groups_v2group_query import GroupsV2GroupQuery
    from .groups_v2group_response import GroupsV2GroupResponse
    from .groups_v2group_search_response import GroupsV2GroupSearchResponse
    from .groups_v2group_sort_by import GroupsV2GroupSortBy
    from .groups_v2group_type import GroupsV2GroupType
    from .groups_v2group_user_base import GroupsV2GroupUserBase
    from .groups_v2group_user_info_card import GroupsV2GroupUserInfoCard
    from .groups_v2group_v2 import GroupsV2GroupV2
    from .groups_v2group_v2card import GroupsV2GroupV2Card
    from .groups_v2group_v2clan_info import GroupsV2GroupV2ClanInfo
    from .groups_v2group_v2clan_info_and_investment import GroupsV2GroupV2ClanInfoAndInvestment
    from .groups_v2groups_for_member_filter import GroupsV2GroupsForMemberFilter
    from .groups_v2host_guided_games_permission_level import GroupsV2HostGuidedGamesPermissionLevel
    from .groups_v2membership_option import GroupsV2MembershipOption
    from .groups_v2runtime_group_member_type import GroupsV2RuntimeGroupMemberType
    from .ignores_ignore_length import IgnoresIgnoreLength
    from .ignores_ignore_response import IgnoresIgnoreResponse
    from .ignores_ignore_status import IgnoresIgnoreStatus
    from .interpolation_interpolation_point import InterpolationInterpolationPoint
    from .interpolation_interpolation_point_float import InterpolationInterpolationPointFloat
    from .links_hyperlink_reference import LinksHyperlinkReference
    from .oauth_scope import OauthScope
    from .queries_paged_query import QueriesPagedQuery
    from .queries_search_result import QueriesSearchResult
    from .schema1 import Schema1
    from .schema10 import Schema10
    from .schema100 import Schema100
    from .schema101 import Schema101
    from .schema102 import Schema102
    from .schema103 import Schema103
    from .schema104 import Schema104
    from .schema105 import Schema105
    from .schema106 import Schema106
    from .schema107 import Schema107
    from .schema108 import Schema108
    from .schema109 import Schema109
    from .schema11 import Schema11
    from .schema110 import Schema110
    from .schema111 import Schema111
    from .schema112 import Schema112
    from .schema113 import Schema113
    from .schema114 import Schema114
    from .schema115 import Schema115
    from .schema116 import Schema116
    from .schema117 import Schema117
    from .schema118 import Schema118
    from .schema12 import Schema12
    from .schema13 import Schema13
    from .schema14 import Schema14
    from .schema15 import Schema15
    from .schema16 import Schema16
    from .schema17 import Schema17
    from .schema18 import Schema18
    from .schema19 import Schema19
    from .schema2 import Schema2
    from .schema20 import Schema20
    from .schema21 import Schema21
    from .schema22 import Schema22
    from .schema23 import Schema23
    from .schema24 import Schema24
    from .schema25 import Schema25
    from .schema26 import Schema26
    from .schema27 import Schema27
    from .schema28 import Schema28
    from .schema29 import Schema29
    from .schema3 import Schema3
    from .schema30 import Schema30
    from .schema31 import Schema31
    from .schema32 import Schema32
    from .schema33 import Schema33
    from .schema34 import Schema34
    from .schema35 import Schema35
    from .schema36 import Schema36
    from .schema37 import Schema37
    from .schema38 import Schema38
    from .schema39 import Schema39
    from .schema4 import Schema4
    from .schema40 import Schema40
    from .schema41 import Schema41
    from .schema42 import Schema42
    from .schema43 import Schema43
    from .schema44 import Schema44
    from .schema45 import Schema45
    from .schema46 import Schema46
    from .schema47 import Schema47
    from .schema48 import Schema48
    from .schema49 import Schema49
    from .schema5 import Schema5
    from .schema50 import Schema50
    from .schema51 import Schema51
    from .schema52 import Schema52
    from .schema53 import Schema53
    from .schema54 import Schema54
    from .schema55 import Schema55
    from .schema56 import Schema56
    from .schema57 import Schema57
    from .schema58 import Schema58
    from .schema59 import Schema59
    from .schema6 import Schema6
    from .schema60 import Schema60
    from .schema61 import Schema61
    from .schema62 import Schema62
    from .schema63 import Schema63
    from .schema64 import Schema64
    from .schema65 import Schema65
    from .schema66 import Schema66
    from .schema67 import Schema67
    from .schema68 import Schema68
    from .schema69 import Schema69
    from .schema7 import Schema7
    from .schema70 import Schema70
    from .schema71 import Schema71
    from .schema72 import Schema72
    from .schema73 import Schema73
    from .schema74 import Schema74
    from .schema75 import Schema75
    from .schema76 import Schema76
    from .schema77 import Schema77
    from .schema78 import Schema78
    from .schema79 import Schema79
    from .schema8 import Schema8
    from .schema80 import Schema80
    from .schema81 import Schema81
    from .schema82 import Schema82
    from .schema83 import Schema83
    from .schema84 import Schema84
    from .schema85 import Schema85
    from .schema86 import Schema86
    from .schema87 import Schema87
    from .schema88 import Schema88
    from .schema89 import Schema89
    from .schema9 import Schema9
    from .schema90 import Schema90
    from .schema91 import Schema91
    from .schema92 import Schema92
    from .schema93 import Schema93
    from .schema94 import Schema94
    from .schema95 import Schema95
    from .schema96 import Schema96
    from .schema97 import Schema97
    from .schema98 import Schema98
    from .schema99 import Schema99
    from .search_result_of_content_item_public_contract import SearchResultOfContentItemPublicContract
    from .search_result_of_destiny_entity_search_result_item import SearchResultOfDestinyEntitySearchResultItem
    from .search_result_of_fireteam_response import SearchResultOfFireteamResponse
    from .search_result_of_fireteam_summary import SearchResultOfFireteamSummary
    from .search_result_of_group_ban import SearchResultOfGroupBan
    from .search_result_of_group_member import SearchResultOfGroupMember
    from .search_result_of_group_member_application import SearchResultOfGroupMemberApplication
    from .search_result_of_group_membership import SearchResultOfGroupMembership
    from .search_result_of_group_potential_membership import SearchResultOfGroupPotentialMembership
    from .search_result_of_group_v2card import SearchResultOfGroupV2Card
    from .search_result_of_post_response import SearchResultOfPostResponse
    from .search_result_of_trending_entry import SearchResultOfTrendingEntry
    from .single_component_response_of_destiny_character_activities_component import (
        SingleComponentResponseOfDestinyCharacterActivitiesComponent,
    )
    from .single_component_response_of_destiny_character_component import (
        SingleComponentResponseOfDestinyCharacterComponent,
    )
    from .single_component_response_of_destiny_character_progression_component import (
        SingleComponentResponseOfDestinyCharacterProgressionComponent,
    )
    from .single_component_response_of_destiny_character_records_component import (
        SingleComponentResponseOfDestinyCharacterRecordsComponent,
    )
    from .single_component_response_of_destiny_character_render_component import (
        SingleComponentResponseOfDestinyCharacterRenderComponent,
    )
    from .single_component_response_of_destiny_collectibles_component import (
        SingleComponentResponseOfDestinyCollectiblesComponent,
    )
    from .single_component_response_of_destiny_currencies_component import (
        SingleComponentResponseOfDestinyCurrenciesComponent,
    )
    from .single_component_response_of_destiny_inventory_component import (
        SingleComponentResponseOfDestinyInventoryComponent,
    )
    from .single_component_response_of_destiny_item_component import SingleComponentResponseOfDestinyItemComponent
    from .single_component_response_of_destiny_item_instance_component import (
        SingleComponentResponseOfDestinyItemInstanceComponent,
    )
    from .single_component_response_of_destiny_item_objectives_component import (
        SingleComponentResponseOfDestinyItemObjectivesComponent,
    )
    from .single_component_response_of_destiny_item_perks_component import (
        SingleComponentResponseOfDestinyItemPerksComponent,
    )
    from .single_component_response_of_destiny_item_plug_objectives_component import (
        SingleComponentResponseOfDestinyItemPlugObjectivesComponent,
    )
    from .single_component_response_of_destiny_item_render_component import (
        SingleComponentResponseOfDestinyItemRenderComponent,
    )
    from .single_component_response_of_destiny_item_reusable_plugs_component import (
        SingleComponentResponseOfDestinyItemReusablePlugsComponent,
    )
    from .single_component_response_of_destiny_item_sockets_component import (
        SingleComponentResponseOfDestinyItemSocketsComponent,
    )
    from .single_component_response_of_destiny_item_stats_component import (
        SingleComponentResponseOfDestinyItemStatsComponent,
    )
    from .single_component_response_of_destiny_item_talent_grid_component import (
        SingleComponentResponseOfDestinyItemTalentGridComponent,
    )
    from .single_component_response_of_destiny_kiosks_component import SingleComponentResponseOfDestinyKiosksComponent
    from .single_component_response_of_destiny_loadouts_component import (
        SingleComponentResponseOfDestinyLoadoutsComponent,
    )
    from .single_component_response_of_destiny_metrics_component import SingleComponentResponseOfDestinyMetricsComponent
    from .single_component_response_of_destiny_platform_silver_component import (
        SingleComponentResponseOfDestinyPlatformSilverComponent,
    )
    from .single_component_response_of_destiny_plug_sets_component import (
        SingleComponentResponseOfDestinyPlugSetsComponent,
    )
    from .single_component_response_of_destiny_presentation_nodes_component import (
        SingleComponentResponseOfDestinyPresentationNodesComponent,
    )
    from .single_component_response_of_destiny_profile_collectibles_component import (
        SingleComponentResponseOfDestinyProfileCollectiblesComponent,
    )
    from .single_component_response_of_destiny_profile_component import SingleComponentResponseOfDestinyProfileComponent
    from .single_component_response_of_destiny_profile_progression_component import (
        SingleComponentResponseOfDestinyProfileProgressionComponent,
    )
    from .single_component_response_of_destiny_profile_records_component import (
        SingleComponentResponseOfDestinyProfileRecordsComponent,
    )
    from .single_component_response_of_destiny_profile_transitory_component import (
        SingleComponentResponseOfDestinyProfileTransitoryComponent,
    )
    from .single_component_response_of_destiny_social_commendations_component import (
        SingleComponentResponseOfDestinySocialCommendationsComponent,
    )
    from .single_component_response_of_destiny_string_variables_component import (
        SingleComponentResponseOfDestinyStringVariablesComponent,
    )
    from .single_component_response_of_destiny_vendor_categories_component import (
        SingleComponentResponseOfDestinyVendorCategoriesComponent,
    )
    from .single_component_response_of_destiny_vendor_component import SingleComponentResponseOfDestinyVendorComponent
    from .single_component_response_of_destiny_vendor_group_component import (
        SingleComponentResponseOfDestinyVendorGroupComponent,
    )
    from .single_component_response_of_destiny_vendor_receipts_component import (
        SingleComponentResponseOfDestinyVendorReceiptsComponent,
    )
    from .social_friends_bungie_friend import SocialFriendsBungieFriend
    from .social_friends_bungie_friend_list_response import SocialFriendsBungieFriendListResponse
    from .social_friends_bungie_friend_request_list_response import SocialFriendsBungieFriendRequestListResponse
    from .social_friends_friend_relationship_state import SocialFriendsFriendRelationshipState
    from .social_friends_platform_friend import SocialFriendsPlatformFriend
    from .social_friends_platform_friend_response import SocialFriendsPlatformFriendResponse
    from .social_friends_platform_friend_type import SocialFriendsPlatformFriendType
    from .social_friends_presence_online_state_flags import SocialFriendsPresenceOnlineStateFlags
    from .social_friends_presence_status import SocialFriendsPresenceStatus
    from .stream_info import StreamInfo
    from .streaming_drop_state_enum import StreamingDropStateEnum
    from .tags_models_contracts_tag_response import TagsModelsContractsTagResponse
    from .tokens_bungie_reward_display import TokensBungieRewardDisplay
    from .tokens_collectible_definitions import TokensCollectibleDefinitions
    from .tokens_partner_offer_claim_request import TokensPartnerOfferClaimRequest
    from .tokens_partner_offer_history_response import TokensPartnerOfferHistoryResponse
    from .tokens_partner_offer_sku_history_response import TokensPartnerOfferSkuHistoryResponse
    from .tokens_partner_reward_history_response import TokensPartnerRewardHistoryResponse
    from .tokens_reward_availability_model import TokensRewardAvailabilityModel
    from .tokens_reward_display_properties import TokensRewardDisplayProperties
    from .tokens_twitch_drop_history_response import TokensTwitchDropHistoryResponse
    from .tokens_user_reward_availability_model import TokensUserRewardAvailabilityModel
    from .trending_trending_categories import TrendingTrendingCategories
    from .trending_trending_category import TrendingTrendingCategory
    from .trending_trending_detail import TrendingTrendingDetail
    from .trending_trending_entry import TrendingTrendingEntry
    from .trending_trending_entry_community_creation import TrendingTrendingEntryCommunityCreation
    from .trending_trending_entry_destiny_activity import TrendingTrendingEntryDestinyActivity
    from .trending_trending_entry_destiny_item import TrendingTrendingEntryDestinyItem
    from .trending_trending_entry_destiny_ritual import TrendingTrendingEntryDestinyRitual
    from .trending_trending_entry_news import TrendingTrendingEntryNews
    from .trending_trending_entry_support_article import TrendingTrendingEntrySupportArticle
    from .trending_trending_entry_type import TrendingTrendingEntryType
    from .user_cross_save_user_membership import UserCrossSaveUserMembership
    from .user_e_mail_setting_localization import UserEMailSettingLocalization
    from .user_e_mail_setting_subscription_localization import UserEMailSettingSubscriptionLocalization
    from .user_email_opt_in_definition import UserEmailOptInDefinition
    from .user_email_settings import UserEmailSettings
    from .user_email_subscription_definition import UserEmailSubscriptionDefinition
    from .user_email_view_definition import UserEmailViewDefinition
    from .user_email_view_definition_setting import UserEmailViewDefinitionSetting
    from .user_exact_search_request import UserExactSearchRequest
    from .user_general_user import UserGeneralUser
    from .user_hard_linked_user_membership import UserHardLinkedUserMembership
    from .user_models_get_credential_types_for_account_response import UserModelsGetCredentialTypesForAccountResponse
    from .user_opt_in_flags import UserOptInFlags
    from .user_user_info_card import UserUserInfoCard
    from .user_user_membership import UserUserMembership
    from .user_user_membership_data import UserUserMembershipData
    from .user_user_search_prefix_request import UserUserSearchPrefixRequest
    from .user_user_search_response import UserUserSearchResponse
    from .user_user_search_response_detail import UserUserSearchResponseDetail
    from .user_user_to_user_context import UserUserToUserContext
_dynamic_imports: typing.Dict[str, str] = {
    "ApplicationsApiUsage": ".applications_api_usage",
    "ApplicationsApplication": ".applications_application",
    "ApplicationsApplicationDeveloper": ".applications_application_developer",
    "ApplicationsApplicationScopes": ".applications_application_scopes",
    "ApplicationsApplicationStatus": ".applications_application_status",
    "ApplicationsDatapoint": ".applications_datapoint",
    "ApplicationsDeveloperRole": ".applications_developer_role",
    "ApplicationsSeries": ".applications_series",
    "BungieCredentialType": ".bungie_credential_type",
    "BungieMembershipType": ".bungie_membership_type",
    "BungieMembershipTypeArray": ".bungie_membership_type_array",
    "CommonModelsCoreSetting": ".common_models_core_setting",
    "CommonModelsCoreSettingsConfiguration": ".common_models_core_settings_configuration",
    "CommonModelsCoreSystem": ".common_models_core_system",
    "CommonModelsDestiny2CoreSettings": ".common_models_destiny2core_settings",
    "ComponentsComponentPrivacySetting": ".components_component_privacy_setting",
    "ComponentsComponentResponse": ".components_component_response",
    "ConfigClanBannerClanBannerDecal": ".config_clan_banner_clan_banner_decal",
    "ConfigClanBannerClanBannerSource": ".config_clan_banner_clan_banner_source",
    "ConfigGroupTheme": ".config_group_theme",
    "ConfigUserTheme": ".config_user_theme",
    "ContentCommentSummary": ".content_comment_summary",
    "ContentContentItemPublicContract": ".content_content_item_public_contract",
    "ContentContentRepresentation": ".content_content_representation",
    "ContentModelsContentPreview": ".content_models_content_preview",
    "ContentModelsContentPropertyDataTypeEnum": ".content_models_content_property_data_type_enum",
    "ContentModelsContentTypeDefaultValue": ".content_models_content_type_default_value",
    "ContentModelsContentTypeDescription": ".content_models_content_type_description",
    "ContentModelsContentTypeProperty": ".content_models_content_type_property",
    "ContentModelsContentTypePropertySection": ".content_models_content_type_property_section",
    "ContentModelsTagMetadataDefinition": ".content_models_tag_metadata_definition",
    "ContentModelsTagMetadataItem": ".content_models_tag_metadata_item",
    "ContentNewsArticleRssItem": ".content_news_article_rss_item",
    "ContentNewsArticleRssResponse": ".content_news_article_rss_response",
    "DatesDateRange": ".dates_date_range",
    "DestinyActivitiesDestinyPublicActivityStatus": ".destiny_activities_destiny_public_activity_status",
    "DestinyActivityGraphNodeHighlightType": ".destiny_activity_graph_node_highlight_type",
    "DestinyAdvancedAwaAuthorizationResult": ".destiny_advanced_awa_authorization_result",
    "DestinyAdvancedAwaInitializeResponse": ".destiny_advanced_awa_initialize_response",
    "DestinyAdvancedAwaPermissionRequested": ".destiny_advanced_awa_permission_requested",
    "DestinyAdvancedAwaResponseReason": ".destiny_advanced_awa_response_reason",
    "DestinyAdvancedAwaType": ".destiny_advanced_awa_type",
    "DestinyAdvancedAwaUserResponse": ".destiny_advanced_awa_user_response",
    "DestinyAdvancedAwaUserSelection": ".destiny_advanced_awa_user_selection",
    "DestinyArtifactsDestinyArtifactCharacterScoped": ".destiny_artifacts_destiny_artifact_character_scoped",
    "DestinyArtifactsDestinyArtifactProfileScoped": ".destiny_artifacts_destiny_artifact_profile_scoped",
    "DestinyArtifactsDestinyArtifactTier": ".destiny_artifacts_destiny_artifact_tier",
    "DestinyArtifactsDestinyArtifactTierItem": ".destiny_artifacts_destiny_artifact_tier_item",
    "DestinyBaseItemComponentSetOfint32": ".destiny_base_item_component_set_ofint32",
    "DestinyBaseItemComponentSetOfint64": ".destiny_base_item_component_set_ofint64",
    "DestinyBaseItemComponentSetOfuint32": ".destiny_base_item_component_set_ofuint32",
    "DestinyBucketCategory": ".destiny_bucket_category",
    "DestinyBucketScope": ".destiny_bucket_scope",
    "DestinyChallengesDestinyChallengeStatus": ".destiny_challenges_destiny_challenge_status",
    "DestinyCharacterDestinyCharacterCustomization": ".destiny_character_destiny_character_customization",
    "DestinyCharacterDestinyCharacterPeerView": ".destiny_character_destiny_character_peer_view",
    "DestinyCharacterDestinyItemPeerView": ".destiny_character_destiny_item_peer_view",
    "DestinyComponentsCollectiblesDestinyCollectibleComponent": ".destiny_components_collectibles_destiny_collectible_component",
    "DestinyComponentsCollectiblesDestinyCollectiblesComponent": ".destiny_components_collectibles_destiny_collectibles_component",
    "DestinyComponentsCollectiblesDestinyProfileCollectiblesComponent": ".destiny_components_collectibles_destiny_profile_collectibles_component",
    "DestinyComponentsCraftablesDestinyCraftableComponent": ".destiny_components_craftables_destiny_craftable_component",
    "DestinyComponentsCraftablesDestinyCraftableSocketComponent": ".destiny_components_craftables_destiny_craftable_socket_component",
    "DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent": ".destiny_components_craftables_destiny_craftable_socket_plug_component",
    "DestinyComponentsCraftablesDestinyCraftablesComponent": ".destiny_components_craftables_destiny_craftables_component",
    "DestinyComponentsInventoryDestinyCurrenciesComponent": ".destiny_components_inventory_destiny_currencies_component",
    "DestinyComponentsInventoryDestinyPlatformSilverComponent": ".destiny_components_inventory_destiny_platform_silver_component",
    "DestinyComponentsItemsDestinyItemPlugComponent": ".destiny_components_items_destiny_item_plug_component",
    "DestinyComponentsItemsDestinyItemPlugObjectivesComponent": ".destiny_components_items_destiny_item_plug_objectives_component",
    "DestinyComponentsItemsDestinyItemReusablePlugsComponent": ".destiny_components_items_destiny_item_reusable_plugs_component",
    "DestinyComponentsKiosksDestinyKioskItem": ".destiny_components_kiosks_destiny_kiosk_item",
    "DestinyComponentsKiosksDestinyKiosksComponent": ".destiny_components_kiosks_destiny_kiosks_component",
    "DestinyComponentsLoadoutsDestinyLoadoutComponent": ".destiny_components_loadouts_destiny_loadout_component",
    "DestinyComponentsLoadoutsDestinyLoadoutItemComponent": ".destiny_components_loadouts_destiny_loadout_item_component",
    "DestinyComponentsLoadoutsDestinyLoadoutsComponent": ".destiny_components_loadouts_destiny_loadouts_component",
    "DestinyComponentsMetricsDestinyMetricComponent": ".destiny_components_metrics_destiny_metric_component",
    "DestinyComponentsMetricsDestinyMetricsComponent": ".destiny_components_metrics_destiny_metrics_component",
    "DestinyComponentsPlugSetsDestinyPlugSetsComponent": ".destiny_components_plug_sets_destiny_plug_sets_component",
    "DestinyComponentsPresentationDestinyPresentationNodeComponent": ".destiny_components_presentation_destiny_presentation_node_component",
    "DestinyComponentsPresentationDestinyPresentationNodesComponent": ".destiny_components_presentation_destiny_presentation_nodes_component",
    "DestinyComponentsProfilesDestinyProfileProgressionComponent": ".destiny_components_profiles_destiny_profile_progression_component",
    "DestinyComponentsProfilesDestinyProfileTransitoryComponent": ".destiny_components_profiles_destiny_profile_transitory_component",
    "DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity": ".destiny_components_profiles_destiny_profile_transitory_current_activity",
    "DestinyComponentsProfilesDestinyProfileTransitoryJoinability": ".destiny_components_profiles_destiny_profile_transitory_joinability",
    "DestinyComponentsProfilesDestinyProfileTransitoryPartyMember": ".destiny_components_profiles_destiny_profile_transitory_party_member",
    "DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry": ".destiny_components_profiles_destiny_profile_transitory_tracking_entry",
    "DestinyComponentsRecordsDestinyCharacterRecordsComponent": ".destiny_components_records_destiny_character_records_component",
    "DestinyComponentsRecordsDestinyProfileRecordsComponent": ".destiny_components_records_destiny_profile_records_component",
    "DestinyComponentsRecordsDestinyRecordComponent": ".destiny_components_records_destiny_record_component",
    "DestinyComponentsRecordsDestinyRecordsComponent": ".destiny_components_records_destiny_records_component",
    "DestinyComponentsSocialDestinySocialCommendationsComponent": ".destiny_components_social_destiny_social_commendations_component",
    "DestinyComponentsStringVariablesDestinyStringVariablesComponent": ".destiny_components_string_variables_destiny_string_variables_component",
    "DestinyComponentsVendorsDestinyPublicVendorComponent": ".destiny_components_vendors_destiny_public_vendor_component",
    "DestinyComponentsVendorsDestinyPublicVendorSaleItemComponent": ".destiny_components_vendors_destiny_public_vendor_sale_item_component",
    "DestinyComponentsVendorsDestinyVendorBaseComponent": ".destiny_components_vendors_destiny_vendor_base_component",
    "DestinyComponentsVendorsDestinyVendorGroup": ".destiny_components_vendors_destiny_vendor_group",
    "DestinyComponentsVendorsDestinyVendorGroupComponent": ".destiny_components_vendors_destiny_vendor_group_component",
    "DestinyComponentsVendorsDestinyVendorSaleItemBaseComponent": ".destiny_components_vendors_destiny_vendor_sale_item_base_component",
    "DestinyConfigDestinyManifest": ".destiny_config_destiny_manifest",
    "DestinyConfigGearAssetDataBaseDefinition": ".destiny_config_gear_asset_data_base_definition",
    "DestinyConfigImagePyramidEntry": ".destiny_config_image_pyramid_entry",
    "DestinyConstantsDestinyEnvironmentLocationMapping": ".destiny_constants_destiny_environment_location_mapping",
    "DestinyDamageType": ".destiny_damage_type",
    "DestinyDefinitionsActivityModifiersDestinyActivityModifierDefinition": ".destiny_definitions_activity_modifiers_destiny_activity_modifier_definition",
    "DestinyDefinitionsAnimationsDestinyAnimationReference": ".destiny_definitions_animations_destiny_animation_reference",
    "DestinyDefinitionsArtifactsDestinyArtifactDefinition": ".destiny_definitions_artifacts_destiny_artifact_definition",
    "DestinyDefinitionsArtifactsDestinyArtifactTierDefinition": ".destiny_definitions_artifacts_destiny_artifact_tier_definition",
    "DestinyDefinitionsArtifactsDestinyArtifactTierItemDefinition": ".destiny_definitions_artifacts_destiny_artifact_tier_item_definition",
    "DestinyDefinitionsBreakerTypesDestinyBreakerTypeDefinition": ".destiny_definitions_breaker_types_destiny_breaker_type_definition",
    "DestinyDefinitionsChecklistsDestinyChecklistDefinition": ".destiny_definitions_checklists_destiny_checklist_definition",
    "DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition": ".destiny_definitions_checklists_destiny_checklist_entry_definition",
    "DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock": ".destiny_definitions_collectibles_destiny_collectible_acquisition_block",
    "DestinyDefinitionsCollectiblesDestinyCollectibleDefinition": ".destiny_definitions_collectibles_destiny_collectible_definition",
    "DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock": ".destiny_definitions_collectibles_destiny_collectible_state_block",
    "DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition": ".destiny_definitions_common_destiny_display_properties_definition",
    "DestinyDefinitionsCommonDestinyIconSequenceDefinition": ".destiny_definitions_common_destiny_icon_sequence_definition",
    "DestinyDefinitionsCommonDestinyPositionDefinition": ".destiny_definitions_common_destiny_position_definition",
    "DestinyDefinitionsDestinyActivityChallengeDefinition": ".destiny_definitions_destiny_activity_challenge_definition",
    "DestinyDefinitionsDestinyActivityDefinition": ".destiny_definitions_destiny_activity_definition",
    "DestinyDefinitionsDestinyActivityGraphListEntryDefinition": ".destiny_definitions_destiny_activity_graph_list_entry_definition",
    "DestinyDefinitionsDestinyActivityGuidedBlockDefinition": ".destiny_definitions_destiny_activity_guided_block_definition",
    "DestinyDefinitionsDestinyActivityInsertionPointDefinition": ".destiny_definitions_destiny_activity_insertion_point_definition",
    "DestinyDefinitionsDestinyActivityLoadoutRequirement": ".destiny_definitions_destiny_activity_loadout_requirement",
    "DestinyDefinitionsDestinyActivityLoadoutRequirementSet": ".destiny_definitions_destiny_activity_loadout_requirement_set",
    "DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition": ".destiny_definitions_destiny_activity_matchmaking_block_definition",
    "DestinyDefinitionsDestinyActivityModeDefinition": ".destiny_definitions_destiny_activity_mode_definition",
    "DestinyDefinitionsDestinyActivityModifierReferenceDefinition": ".destiny_definitions_destiny_activity_modifier_reference_definition",
    "DestinyDefinitionsDestinyActivityPlaylistItemDefinition": ".destiny_definitions_destiny_activity_playlist_item_definition",
    "DestinyDefinitionsDestinyActivityRewardDefinition": ".destiny_definitions_destiny_activity_reward_definition",
    "DestinyDefinitionsDestinyActivityTypeDefinition": ".destiny_definitions_destiny_activity_type_definition",
    "DestinyDefinitionsDestinyActivityUnlockStringDefinition": ".destiny_definitions_destiny_activity_unlock_string_definition",
    "DestinyDefinitionsDestinyArrangementRegionFilterDefinition": ".destiny_definitions_destiny_arrangement_region_filter_definition",
    "DestinyDefinitionsDestinyArtDyeReference": ".destiny_definitions_destiny_art_dye_reference",
    "DestinyDefinitionsDestinyBubbleDefinition": ".destiny_definitions_destiny_bubble_definition",
    "DestinyDefinitionsDestinyClassDefinition": ".destiny_definitions_destiny_class_definition",
    "DestinyDefinitionsDestinyDamageTypeDefinition": ".destiny_definitions_destiny_damage_type_definition",
    "DestinyDefinitionsDestinyDefinition": ".destiny_definitions_destiny_definition",
    "DestinyDefinitionsDestinyDestinationBubbleSettingDefinition": ".destiny_definitions_destiny_destination_bubble_setting_definition",
    "DestinyDefinitionsDestinyDestinationDefinition": ".destiny_definitions_destiny_destination_definition",
    "DestinyDefinitionsDestinyDisplayCategoryDefinition": ".destiny_definitions_destiny_display_category_definition",
    "DestinyDefinitionsDestinyEntitySearchResult": ".destiny_definitions_destiny_entity_search_result",
    "DestinyDefinitionsDestinyEntitySearchResultItem": ".destiny_definitions_destiny_entity_search_result_item",
    "DestinyDefinitionsDestinyEquipmentSlotDefinition": ".destiny_definitions_destiny_equipment_slot_definition",
    "DestinyDefinitionsDestinyEquippingBlockDefinition": ".destiny_definitions_destiny_equipping_block_definition",
    "DestinyDefinitionsDestinyFactionDefinition": ".destiny_definitions_destiny_faction_definition",
    "DestinyDefinitionsDestinyFactionVendorDefinition": ".destiny_definitions_destiny_faction_vendor_definition",
    "DestinyDefinitionsDestinyGearArtArrangementReference": ".destiny_definitions_destiny_gear_art_arrangement_reference",
    "DestinyDefinitionsDestinyGenderDefinition": ".destiny_definitions_destiny_gender_definition",
    "DestinyDefinitionsDestinyInventoryBucketDefinition": ".destiny_definitions_destiny_inventory_bucket_definition",
    "DestinyDefinitionsDestinyInventoryItemDefinition": ".destiny_definitions_destiny_inventory_item_definition",
    "DestinyDefinitionsDestinyInventoryItemStatDefinition": ".destiny_definitions_destiny_inventory_item_stat_definition",
    "DestinyDefinitionsDestinyItemActionBlockDefinition": ".destiny_definitions_destiny_item_action_block_definition",
    "DestinyDefinitionsDestinyItemActionRequiredItemDefinition": ".destiny_definitions_destiny_item_action_required_item_definition",
    "DestinyDefinitionsDestinyItemCategoryDefinition": ".destiny_definitions_destiny_item_category_definition",
    "DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition": ".destiny_definitions_destiny_item_crafting_block_bonus_plug_definition",
    "DestinyDefinitionsDestinyItemCraftingBlockDefinition": ".destiny_definitions_destiny_item_crafting_block_definition",
    "DestinyDefinitionsDestinyItemCreationEntryLevelDefinition": ".destiny_definitions_destiny_item_creation_entry_level_definition",
    "DestinyDefinitionsDestinyItemGearsetBlockDefinition": ".destiny_definitions_destiny_item_gearset_block_definition",
    "DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition": ".destiny_definitions_destiny_item_intrinsic_socket_entry_definition",
    "DestinyDefinitionsDestinyItemInventoryBlockDefinition": ".destiny_definitions_destiny_item_inventory_block_definition",
    "DestinyDefinitionsDestinyItemInvestmentStatDefinition": ".destiny_definitions_destiny_item_investment_stat_definition",
    "DestinyDefinitionsDestinyItemMetricBlockDefinition": ".destiny_definitions_destiny_item_metric_block_definition",
    "DestinyDefinitionsDestinyItemObjectiveBlockDefinition": ".destiny_definitions_destiny_item_objective_block_definition",
    "DestinyDefinitionsDestinyItemPerkEntryDefinition": ".destiny_definitions_destiny_item_perk_entry_definition",
    "DestinyDefinitionsDestinyItemPreviewBlockDefinition": ".destiny_definitions_destiny_item_preview_block_definition",
    "DestinyDefinitionsDestinyItemQualityBlockDefinition": ".destiny_definitions_destiny_item_quality_block_definition",
    "DestinyDefinitionsDestinyItemSackBlockDefinition": ".destiny_definitions_destiny_item_sack_block_definition",
    "DestinyDefinitionsDestinyItemSetBlockDefinition": ".destiny_definitions_destiny_item_set_block_definition",
    "DestinyDefinitionsDestinyItemSetBlockEntryDefinition": ".destiny_definitions_destiny_item_set_block_entry_definition",
    "DestinyDefinitionsDestinyItemSocketBlockDefinition": ".destiny_definitions_destiny_item_socket_block_definition",
    "DestinyDefinitionsDestinyItemSocketCategoryDefinition": ".destiny_definitions_destiny_item_socket_category_definition",
    "DestinyDefinitionsDestinyItemSocketEntryDefinition": ".destiny_definitions_destiny_item_socket_entry_definition",
    "DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition": ".destiny_definitions_destiny_item_socket_entry_plug_item_definition",
    "DestinyDefinitionsDestinyItemSocketEntryPlugItemRandomizedDefinition": ".destiny_definitions_destiny_item_socket_entry_plug_item_randomized_definition",
    "DestinyDefinitionsDestinyItemSourceBlockDefinition": ".destiny_definitions_destiny_item_source_block_definition",
    "DestinyDefinitionsDestinyItemStatBlockDefinition": ".destiny_definitions_destiny_item_stat_block_definition",
    "DestinyDefinitionsDestinyItemSummaryBlockDefinition": ".destiny_definitions_destiny_item_summary_block_definition",
    "DestinyDefinitionsDestinyItemTalentGridBlockDefinition": ".destiny_definitions_destiny_item_talent_grid_block_definition",
    "DestinyDefinitionsDestinyItemTooltipNotification": ".destiny_definitions_destiny_item_tooltip_notification",
    "DestinyDefinitionsDestinyItemTranslationBlockDefinition": ".destiny_definitions_destiny_item_translation_block_definition",
    "DestinyDefinitionsDestinyItemValueBlockDefinition": ".destiny_definitions_destiny_item_value_block_definition",
    "DestinyDefinitionsDestinyItemVendorSourceReference": ".destiny_definitions_destiny_item_vendor_source_reference",
    "DestinyDefinitionsDestinyItemVersionDefinition": ".destiny_definitions_destiny_item_version_definition",
    "DestinyDefinitionsDestinyLocationDefinition": ".destiny_definitions_destiny_location_definition",
    "DestinyDefinitionsDestinyLocationReleaseDefinition": ".destiny_definitions_destiny_location_release_definition",
    "DestinyDefinitionsDestinyMaterialRequirement": ".destiny_definitions_destiny_material_requirement",
    "DestinyDefinitionsDestinyMaterialRequirementSetDefinition": ".destiny_definitions_destiny_material_requirement_set_definition",
    "DestinyDefinitionsDestinyMedalTierDefinition": ".destiny_definitions_destiny_medal_tier_definition",
    "DestinyDefinitionsDestinyNodeActivationRequirement": ".destiny_definitions_destiny_node_activation_requirement",
    "DestinyDefinitionsDestinyNodeSocketReplaceResponse": ".destiny_definitions_destiny_node_socket_replace_response",
    "DestinyDefinitionsDestinyNodeStepDefinition": ".destiny_definitions_destiny_node_step_definition",
    "DestinyDefinitionsDestinyObjectiveDefinition": ".destiny_definitions_destiny_objective_definition",
    "DestinyDefinitionsDestinyObjectiveDisplayProperties": ".destiny_definitions_destiny_objective_display_properties",
    "DestinyDefinitionsDestinyObjectivePerkEntryDefinition": ".destiny_definitions_destiny_objective_perk_entry_definition",
    "DestinyDefinitionsDestinyObjectiveStatEntryDefinition": ".destiny_definitions_destiny_objective_stat_entry_definition",
    "DestinyDefinitionsDestinyPlaceDefinition": ".destiny_definitions_destiny_place_definition",
    "DestinyDefinitionsDestinyPlugItemCraftingRequirements": ".destiny_definitions_destiny_plug_item_crafting_requirements",
    "DestinyDefinitionsDestinyPlugItemCraftingUnlockRequirement": ".destiny_definitions_destiny_plug_item_crafting_unlock_requirement",
    "DestinyDefinitionsDestinyProgressionDefinition": ".destiny_definitions_destiny_progression_definition",
    "DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition": ".destiny_definitions_destiny_progression_display_properties_definition",
    "DestinyDefinitionsDestinyProgressionMappingDefinition": ".destiny_definitions_destiny_progression_mapping_definition",
    "DestinyDefinitionsDestinyProgressionRewardDefinition": ".destiny_definitions_destiny_progression_reward_definition",
    "DestinyDefinitionsDestinyProgressionRewardItemQuantity": ".destiny_definitions_destiny_progression_reward_item_quantity",
    "DestinyDefinitionsDestinyProgressionStepDefinition": ".destiny_definitions_destiny_progression_step_definition",
    "DestinyDefinitionsDestinyRaceDefinition": ".destiny_definitions_destiny_race_definition",
    "DestinyDefinitionsDestinyRewardSourceCategory": ".destiny_definitions_destiny_reward_source_category",
    "DestinyDefinitionsDestinyRewardSourceDefinition": ".destiny_definitions_destiny_reward_source_definition",
    "DestinyDefinitionsDestinySandboxPatternDefinition": ".destiny_definitions_destiny_sandbox_pattern_definition",
    "DestinyDefinitionsDestinySandboxPerkDefinition": ".destiny_definitions_destiny_sandbox_perk_definition",
    "DestinyDefinitionsDestinyStatDefinition": ".destiny_definitions_destiny_stat_definition",
    "DestinyDefinitionsDestinyStatDisplayDefinition": ".destiny_definitions_destiny_stat_display_definition",
    "DestinyDefinitionsDestinyStatGroupDefinition": ".destiny_definitions_destiny_stat_group_definition",
    "DestinyDefinitionsDestinyStatOverrideDefinition": ".destiny_definitions_destiny_stat_override_definition",
    "DestinyDefinitionsDestinyTalentExclusiveGroup": ".destiny_definitions_destiny_talent_exclusive_group",
    "DestinyDefinitionsDestinyTalentGridDefinition": ".destiny_definitions_destiny_talent_grid_definition",
    "DestinyDefinitionsDestinyTalentNodeCategory": ".destiny_definitions_destiny_talent_node_category",
    "DestinyDefinitionsDestinyTalentNodeDefinition": ".destiny_definitions_destiny_talent_node_definition",
    "DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition": ".destiny_definitions_destiny_talent_node_exclusive_set_definition",
    "DestinyDefinitionsDestinyTalentNodeStepDamageTypes": ".destiny_definitions_destiny_talent_node_step_damage_types",
    "DestinyDefinitionsDestinyTalentNodeStepGroups": ".destiny_definitions_destiny_talent_node_step_groups",
    "DestinyDefinitionsDestinyTalentNodeStepGuardianAttributes": ".destiny_definitions_destiny_talent_node_step_guardian_attributes",
    "DestinyDefinitionsDestinyTalentNodeStepImpactEffects": ".destiny_definitions_destiny_talent_node_step_impact_effects",
    "DestinyDefinitionsDestinyTalentNodeStepLightAbilities": ".destiny_definitions_destiny_talent_node_step_light_abilities",
    "DestinyDefinitionsDestinyTalentNodeStepWeaponPerformances": ".destiny_definitions_destiny_talent_node_step_weapon_performances",
    "DestinyDefinitionsDestinyUnlockDefinition": ".destiny_definitions_destiny_unlock_definition",
    "DestinyDefinitionsDestinyUnlockExpressionDefinition": ".destiny_definitions_destiny_unlock_expression_definition",
    "DestinyDefinitionsDestinyUnlockValueDefinition": ".destiny_definitions_destiny_unlock_value_definition",
    "DestinyDefinitionsDestinyVendorAcceptedItemDefinition": ".destiny_definitions_destiny_vendor_accepted_item_definition",
    "DestinyDefinitionsDestinyVendorActionDefinition": ".destiny_definitions_destiny_vendor_action_definition",
    "DestinyDefinitionsDestinyVendorCategoryEntryDefinition": ".destiny_definitions_destiny_vendor_category_entry_definition",
    "DestinyDefinitionsDestinyVendorCategoryOverlayDefinition": ".destiny_definitions_destiny_vendor_category_overlay_definition",
    "DestinyDefinitionsDestinyVendorDefinition": ".destiny_definitions_destiny_vendor_definition",
    "DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition": ".destiny_definitions_destiny_vendor_display_properties_definition",
    "DestinyDefinitionsDestinyVendorGroupDefinition": ".destiny_definitions_destiny_vendor_group_definition",
    "DestinyDefinitionsDestinyVendorGroupReference": ".destiny_definitions_destiny_vendor_group_reference",
    "DestinyDefinitionsDestinyVendorInteractionDefinition": ".destiny_definitions_destiny_vendor_interaction_definition",
    "DestinyDefinitionsDestinyVendorInteractionReplyDefinition": ".destiny_definitions_destiny_vendor_interaction_reply_definition",
    "DestinyDefinitionsDestinyVendorInteractionSackEntryDefinition": ".destiny_definitions_destiny_vendor_interaction_sack_entry_definition",
    "DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition": ".destiny_definitions_destiny_vendor_inventory_flyout_bucket_definition",
    "DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition": ".destiny_definitions_destiny_vendor_inventory_flyout_definition",
    "DestinyDefinitionsDestinyVendorItemDefinition": ".destiny_definitions_destiny_vendor_item_definition",
    "DestinyDefinitionsDestinyVendorItemQuantity": ".destiny_definitions_destiny_vendor_item_quantity",
    "DestinyDefinitionsDestinyVendorItemSocketOverride": ".destiny_definitions_destiny_vendor_item_socket_override",
    "DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition": ".destiny_definitions_destiny_vendor_requirement_display_entry_definition",
    "DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition": ".destiny_definitions_destiny_vendor_sale_item_action_block_definition",
    "DestinyDefinitionsDestinyVendorServiceDefinition": ".destiny_definitions_destiny_vendor_service_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition": ".destiny_definitions_director_destiny_activity_graph_art_element_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition": ".destiny_definitions_director_destiny_activity_graph_connection_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDefinition": ".destiny_definitions_director_destiny_activity_graph_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition": ".destiny_definitions_director_destiny_activity_graph_display_objective_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition": ".destiny_definitions_director_destiny_activity_graph_display_progression_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition": ".destiny_definitions_director_destiny_activity_graph_node_activity_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition": ".destiny_definitions_director_destiny_activity_graph_node_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition": ".destiny_definitions_director_destiny_activity_graph_node_featuring_state_definition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeStateEntry": ".destiny_definitions_director_destiny_activity_graph_node_state_entry",
    "DestinyDefinitionsDirectorDestinyLinkedGraphDefinition": ".destiny_definitions_director_destiny_linked_graph_definition",
    "DestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition": ".destiny_definitions_director_destiny_linked_graph_entry_definition",
    "DestinyDefinitionsEnergyTypesDestinyEnergyTypeDefinition": ".destiny_definitions_energy_types_destiny_energy_type_definition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankConstantsDefinition": ".destiny_definitions_guardian_ranks_destiny_guardian_rank_constants_definition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankDefinition": ".destiny_definitions_guardian_ranks_destiny_guardian_rank_definition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankIconBackgroundsDefinition": ".destiny_definitions_guardian_ranks_destiny_guardian_rank_icon_backgrounds_definition",
    "DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition": ".destiny_definitions_items_destiny_derived_item_category_definition",
    "DestinyDefinitionsItemsDestinyDerivedItemDefinition": ".destiny_definitions_items_destiny_derived_item_definition",
    "DestinyDefinitionsItemsDestinyEnergyCapacityEntry": ".destiny_definitions_items_destiny_energy_capacity_entry",
    "DestinyDefinitionsItemsDestinyEnergyCostEntry": ".destiny_definitions_items_destiny_energy_cost_entry",
    "DestinyDefinitionsItemsDestinyItemPlugDefinition": ".destiny_definitions_items_destiny_item_plug_definition",
    "DestinyDefinitionsItemsDestinyItemTierTypeDefinition": ".destiny_definitions_items_destiny_item_tier_type_definition",
    "DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock": ".destiny_definitions_items_destiny_item_tier_type_infusion_block",
    "DestinyDefinitionsItemsDestinyParentItemOverride": ".destiny_definitions_items_destiny_parent_item_override",
    "DestinyDefinitionsItemsDestinyPlugRuleDefinition": ".destiny_definitions_items_destiny_plug_rule_definition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutColorDefinition": ".destiny_definitions_loadouts_destiny_loadout_color_definition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutConstantsDefinition": ".destiny_definitions_loadouts_destiny_loadout_constants_definition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutIconDefinition": ".destiny_definitions_loadouts_destiny_loadout_icon_definition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutNameDefinition": ".destiny_definitions_loadouts_destiny_loadout_name_definition",
    "DestinyDefinitionsLoreDestinyLoreDefinition": ".destiny_definitions_lore_destiny_lore_definition",
    "DestinyDefinitionsMetricsDestinyMetricDefinition": ".destiny_definitions_metrics_destiny_metric_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition": ".destiny_definitions_milestones_destiny_milestone_activity_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition": ".destiny_definitions_milestones_destiny_milestone_activity_variant_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityDefinition": ".destiny_definitions_milestones_destiny_milestone_challenge_activity_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityGraphNodeEntry": ".destiny_definitions_milestones_destiny_milestone_challenge_activity_graph_node_entry",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase": ".destiny_definitions_milestones_destiny_milestone_challenge_activity_phase",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition": ".destiny_definitions_milestones_destiny_milestone_challenge_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneDefinition": ".destiny_definitions_milestones_destiny_milestone_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneDisplayPreference": ".destiny_definitions_milestones_destiny_milestone_display_preference",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition": ".destiny_definitions_milestones_destiny_milestone_quest_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem": ".destiny_definitions_milestones_destiny_milestone_quest_reward_item",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition": ".destiny_definitions_milestones_destiny_milestone_quest_rewards_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition": ".destiny_definitions_milestones_destiny_milestone_reward_category_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition": ".destiny_definitions_milestones_destiny_milestone_reward_entry_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneType": ".destiny_definitions_milestones_destiny_milestone_type",
    "DestinyDefinitionsMilestonesDestinyMilestoneValueDefinition": ".destiny_definitions_milestones_destiny_milestone_value_definition",
    "DestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition": ".destiny_definitions_milestones_destiny_milestone_vendor_definition",
    "DestinyDefinitionsPowerCapsDestinyPowerCapDefinition": ".destiny_definitions_power_caps_destiny_power_cap_definition",
    "DestinyDefinitionsPresentationDestinyPresentationChildBlock": ".destiny_definitions_presentation_destiny_presentation_child_block",
    "DestinyDefinitionsPresentationDestinyPresentationNodeBaseDefinition": ".destiny_definitions_presentation_destiny_presentation_node_base_definition",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildEntry": ".destiny_definitions_presentation_destiny_presentation_node_child_entry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildEntryBase": ".destiny_definitions_presentation_destiny_presentation_node_child_entry_base",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock": ".destiny_definitions_presentation_destiny_presentation_node_children_block",
    "DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry": ".destiny_definitions_presentation_destiny_presentation_node_collectible_child_entry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeCraftableChildEntry": ".destiny_definitions_presentation_destiny_presentation_node_craftable_child_entry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeDefinition": ".destiny_definitions_presentation_destiny_presentation_node_definition",
    "DestinyDefinitionsPresentationDestinyPresentationNodeMetricChildEntry": ".destiny_definitions_presentation_destiny_presentation_node_metric_child_entry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeRecordChildEntry": ".destiny_definitions_presentation_destiny_presentation_node_record_child_entry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock": ".destiny_definitions_presentation_destiny_presentation_node_requirements_block",
    "DestinyDefinitionsPresentationDestinyScoredPresentationNodeBaseDefinition": ".destiny_definitions_presentation_destiny_scored_presentation_node_base_definition",
    "DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition": ".destiny_definitions_progression_destiny_progression_level_requirement_definition",
    "DestinyDefinitionsRecordsDestinyRecordCompletionBlock": ".destiny_definitions_records_destiny_record_completion_block",
    "DestinyDefinitionsRecordsDestinyRecordDefinition": ".destiny_definitions_records_destiny_record_definition",
    "DestinyDefinitionsRecordsDestinyRecordExpirationBlock": ".destiny_definitions_records_destiny_record_expiration_block",
    "DestinyDefinitionsRecordsDestinyRecordIntervalBlock": ".destiny_definitions_records_destiny_record_interval_block",
    "DestinyDefinitionsRecordsDestinyRecordIntervalObjective": ".destiny_definitions_records_destiny_record_interval_objective",
    "DestinyDefinitionsRecordsDestinyRecordIntervalRewards": ".destiny_definitions_records_destiny_record_interval_rewards",
    "DestinyDefinitionsRecordsDestinyRecordTitleBlock": ".destiny_definitions_records_destiny_record_title_block",
    "DestinyDefinitionsRecordsSchemaRecordStateBlock": ".destiny_definitions_records_schema_record_state_block",
    "DestinyDefinitionsReportingDestinyReportReasonCategoryDefinition": ".destiny_definitions_reporting_destiny_report_reason_category_definition",
    "DestinyDefinitionsReportingDestinyReportReasonDefinition": ".destiny_definitions_reporting_destiny_report_reason_definition",
    "DestinyDefinitionsSeasonsDestinyEventCardDefinition": ".destiny_definitions_seasons_destiny_event_card_definition",
    "DestinyDefinitionsSeasonsDestinyEventCardImages": ".destiny_definitions_seasons_destiny_event_card_images",
    "DestinyDefinitionsSeasonsDestinySeasonDefinition": ".destiny_definitions_seasons_destiny_season_definition",
    "DestinyDefinitionsSeasonsDestinySeasonPassDefinition": ".destiny_definitions_seasons_destiny_season_pass_definition",
    "DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition": ".destiny_definitions_seasons_destiny_season_preview_definition",
    "DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition": ".destiny_definitions_seasons_destiny_season_preview_image_definition",
    "DestinyDefinitionsSocialDestinySocialCommendationDefinition": ".destiny_definitions_social_destiny_social_commendation_definition",
    "DestinyDefinitionsSocialDestinySocialCommendationNodeDefinition": ".destiny_definitions_social_destiny_social_commendation_node_definition",
    "DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition": ".destiny_definitions_sockets_destiny_insert_plug_action_definition",
    "DestinyDefinitionsSocketsDestinyPlugSetDefinition": ".destiny_definitions_sockets_destiny_plug_set_definition",
    "DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition": ".destiny_definitions_sockets_destiny_plug_whitelist_entry_definition",
    "DestinyDefinitionsSocketsDestinySocketCategoryDefinition": ".destiny_definitions_sockets_destiny_socket_category_definition",
    "DestinyDefinitionsSocketsDestinySocketTypeDefinition": ".destiny_definitions_sockets_destiny_socket_type_definition",
    "DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry": ".destiny_definitions_sockets_destiny_socket_type_scalar_material_requirement_entry",
    "DestinyDefinitionsSourcesDestinyItemSourceDefinition": ".destiny_definitions_sources_destiny_item_source_definition",
    "DestinyDefinitionsTraitsDestinyTraitDefinition": ".destiny_definitions_traits_destiny_trait_definition",
    "DestinyDefinitionsVendorsDestinyVendorLocationDefinition": ".destiny_definitions_vendors_destiny_vendor_location_definition",
    "DestinyDestinyActivity": ".destiny_destiny_activity",
    "DestinyDestinyActivityDifficultyTier": ".destiny_destiny_activity_difficulty_tier",
    "DestinyDestinyActivityModeCategory": ".destiny_destiny_activity_mode_category",
    "DestinyDestinyActivityNavPointType": ".destiny_destiny_activity_nav_point_type",
    "DestinyDestinyAmmunitionType": ".destiny_destiny_ammunition_type",
    "DestinyDestinyBreakerType": ".destiny_destiny_breaker_type",
    "DestinyDestinyClass": ".destiny_destiny_class",
    "DestinyDestinyCollectibleState": ".destiny_destiny_collectible_state",
    "DestinyDestinyComponentType": ".destiny_destiny_component_type",
    "DestinyDestinyEnergyType": ".destiny_destiny_energy_type",
    "DestinyDestinyEquipItemResult": ".destiny_destiny_equip_item_result",
    "DestinyDestinyEquipItemResults": ".destiny_destiny_equip_item_results",
    "DestinyDestinyGamePrivacySetting": ".destiny_destiny_game_privacy_setting",
    "DestinyDestinyGameVersions": ".destiny_destiny_game_versions",
    "DestinyDestinyGatingScope": ".destiny_destiny_gating_scope",
    "DestinyDestinyGender": ".destiny_destiny_gender",
    "DestinyDestinyGraphNodeState": ".destiny_destiny_graph_node_state",
    "DestinyDestinyItemQuantity": ".destiny_destiny_item_quantity",
    "DestinyDestinyItemSortType": ".destiny_destiny_item_sort_type",
    "DestinyDestinyItemSubType": ".destiny_destiny_item_sub_type",
    "DestinyDestinyItemType": ".destiny_destiny_item_type",
    "DestinyDestinyJoinClosedReasons": ".destiny_destiny_join_closed_reasons",
    "DestinyDestinyObjectiveGrantStyle": ".destiny_destiny_objective_grant_style",
    "DestinyDestinyObjectiveUiStyle": ".destiny_destiny_objective_ui_style",
    "DestinyDestinyPartyMemberStates": ".destiny_destiny_party_member_states",
    "DestinyDestinyPresentationDisplayStyle": ".destiny_destiny_presentation_display_style",
    "DestinyDestinyPresentationNodeState": ".destiny_destiny_presentation_node_state",
    "DestinyDestinyPresentationNodeType": ".destiny_destiny_presentation_node_type",
    "DestinyDestinyPresentationScreenStyle": ".destiny_destiny_presentation_screen_style",
    "DestinyDestinyProgression": ".destiny_destiny_progression",
    "DestinyDestinyProgressionResetEntry": ".destiny_destiny_progression_reset_entry",
    "DestinyDestinyProgressionRewardItemAcquisitionBehavior": ".destiny_destiny_progression_reward_item_acquisition_behavior",
    "DestinyDestinyProgressionRewardItemState": ".destiny_destiny_progression_reward_item_state",
    "DestinyDestinyProgressionScope": ".destiny_destiny_progression_scope",
    "DestinyDestinyProgressionStepDisplayEffect": ".destiny_destiny_progression_step_display_effect",
    "DestinyDestinyRace": ".destiny_destiny_race",
    "DestinyDestinyRecordState": ".destiny_destiny_record_state",
    "DestinyDestinyRecordToastStyle": ".destiny_destiny_record_toast_style",
    "DestinyDestinyRecordValueStyle": ".destiny_destiny_record_value_style",
    "DestinyDestinyScope": ".destiny_destiny_scope",
    "DestinyDestinySocketCategoryStyle": ".destiny_destiny_socket_category_style",
    "DestinyDestinySocketVisibility": ".destiny_destiny_socket_visibility",
    "DestinyDestinyStat": ".destiny_destiny_stat",
    "DestinyDestinyStatAggregationType": ".destiny_destiny_stat_aggregation_type",
    "DestinyDestinyStatCategory": ".destiny_destiny_stat_category",
    "DestinyDestinyTalentNode": ".destiny_destiny_talent_node",
    "DestinyDestinyTalentNodeStatBlock": ".destiny_destiny_talent_node_stat_block",
    "DestinyDestinyTalentNodeState": ".destiny_destiny_talent_node_state",
    "DestinyDestinyUnlockStatus": ".destiny_destiny_unlock_status",
    "DestinyDestinyUnlockValueUiStyle": ".destiny_destiny_unlock_value_ui_style",
    "DestinyDestinyVendorFilter": ".destiny_destiny_vendor_filter",
    "DestinyDestinyVendorInteractionRewardSelection": ".destiny_destiny_vendor_interaction_reward_selection",
    "DestinyDestinyVendorItemRefundPolicy": ".destiny_destiny_vendor_item_refund_policy",
    "DestinyDestinyVendorItemState": ".destiny_destiny_vendor_item_state",
    "DestinyDestinyVendorProgressionType": ".destiny_destiny_vendor_progression_type",
    "DestinyDestinyVendorReplyType": ".destiny_destiny_vendor_reply_type",
    "DestinyDyeReference": ".destiny_dye_reference",
    "DestinyEntitiesCharactersDestinyCharacterActivitiesComponent": ".destiny_entities_characters_destiny_character_activities_component",
    "DestinyEntitiesCharactersDestinyCharacterComponent": ".destiny_entities_characters_destiny_character_component",
    "DestinyEntitiesCharactersDestinyCharacterProgressionComponent": ".destiny_entities_characters_destiny_character_progression_component",
    "DestinyEntitiesCharactersDestinyCharacterRenderComponent": ".destiny_entities_characters_destiny_character_render_component",
    "DestinyEntitiesInventoryDestinyInventoryComponent": ".destiny_entities_inventory_destiny_inventory_component",
    "DestinyEntitiesItemsDestinyItemComponent": ".destiny_entities_items_destiny_item_component",
    "DestinyEntitiesItemsDestinyItemInstanceComponent": ".destiny_entities_items_destiny_item_instance_component",
    "DestinyEntitiesItemsDestinyItemInstanceEnergy": ".destiny_entities_items_destiny_item_instance_energy",
    "DestinyEntitiesItemsDestinyItemObjectivesComponent": ".destiny_entities_items_destiny_item_objectives_component",
    "DestinyEntitiesItemsDestinyItemPerksComponent": ".destiny_entities_items_destiny_item_perks_component",
    "DestinyEntitiesItemsDestinyItemRenderComponent": ".destiny_entities_items_destiny_item_render_component",
    "DestinyEntitiesItemsDestinyItemSocketState": ".destiny_entities_items_destiny_item_socket_state",
    "DestinyEntitiesItemsDestinyItemSocketsComponent": ".destiny_entities_items_destiny_item_sockets_component",
    "DestinyEntitiesItemsDestinyItemStatsComponent": ".destiny_entities_items_destiny_item_stats_component",
    "DestinyEntitiesItemsDestinyItemTalentGridComponent": ".destiny_entities_items_destiny_item_talent_grid_component",
    "DestinyEntitiesProfilesDestinyProfileComponent": ".destiny_entities_profiles_destiny_profile_component",
    "DestinyEntitiesProfilesDestinyVendorReceiptsComponent": ".destiny_entities_profiles_destiny_vendor_receipts_component",
    "DestinyEntitiesVendorsDestinyVendorCategoriesComponent": ".destiny_entities_vendors_destiny_vendor_categories_component",
    "DestinyEntitiesVendorsDestinyVendorCategory": ".destiny_entities_vendors_destiny_vendor_category",
    "DestinyEntitiesVendorsDestinyVendorComponent": ".destiny_entities_vendors_destiny_vendor_component",
    "DestinyEntitiesVendorsDestinyVendorSaleItemComponent": ".destiny_entities_vendors_destiny_vendor_sale_item_component",
    "DestinyEquipFailureReason": ".destiny_equip_failure_reason",
    "DestinyEquippingItemBlockAttributes": ".destiny_equipping_item_block_attributes",
    "DestinyHistoricalStatsDefinitionsDestinyActivityModeType": ".destiny_historical_stats_definitions_destiny_activity_mode_type",
    "DestinyHistoricalStatsDefinitionsDestinyActivityModeTypeArray": ".destiny_historical_stats_definitions_destiny_activity_mode_type_array",
    "DestinyHistoricalStatsDefinitionsDestinyHistoricalStatsDefinition": ".destiny_historical_stats_definitions_destiny_historical_stats_definition",
    "DestinyHistoricalStatsDefinitionsDestinyStatsCategoryType": ".destiny_historical_stats_definitions_destiny_stats_category_type",
    "DestinyHistoricalStatsDefinitionsDestinyStatsGroupType": ".destiny_historical_stats_definitions_destiny_stats_group_type",
    "DestinyHistoricalStatsDefinitionsDestinyStatsMergeMethod": ".destiny_historical_stats_definitions_destiny_stats_merge_method",
    "DestinyHistoricalStatsDefinitionsPeriodType": ".destiny_historical_stats_definitions_period_type",
    "DestinyHistoricalStatsDefinitionsPeriodTypeArray": ".destiny_historical_stats_definitions_period_type_array",
    "DestinyHistoricalStatsDefinitionsUnitType": ".destiny_historical_stats_definitions_unit_type",
    "DestinyHistoricalStatsDestinyActivityHistoryResults": ".destiny_historical_stats_destiny_activity_history_results",
    "DestinyHistoricalStatsDestinyAggregateActivityResults": ".destiny_historical_stats_destiny_aggregate_activity_results",
    "DestinyHistoricalStatsDestinyAggregateActivityStats": ".destiny_historical_stats_destiny_aggregate_activity_stats",
    "DestinyHistoricalStatsDestinyClanAggregateStat": ".destiny_historical_stats_destiny_clan_aggregate_stat",
    "DestinyHistoricalStatsDestinyHistoricalStatsAccountResult": ".destiny_historical_stats_destiny_historical_stats_account_result",
    "DestinyHistoricalStatsDestinyHistoricalStatsActivity": ".destiny_historical_stats_destiny_historical_stats_activity",
    "DestinyHistoricalStatsDestinyHistoricalStatsByPeriod": ".destiny_historical_stats_destiny_historical_stats_by_period",
    "DestinyHistoricalStatsDestinyHistoricalStatsPerCharacter": ".destiny_historical_stats_destiny_historical_stats_per_character",
    "DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup": ".destiny_historical_stats_destiny_historical_stats_period_group",
    "DestinyHistoricalStatsDestinyHistoricalStatsResults": ".destiny_historical_stats_destiny_historical_stats_results",
    "DestinyHistoricalStatsDestinyHistoricalStatsValue": ".destiny_historical_stats_destiny_historical_stats_value",
    "DestinyHistoricalStatsDestinyHistoricalStatsValuePair": ".destiny_historical_stats_destiny_historical_stats_value_pair",
    "DestinyHistoricalStatsDestinyHistoricalStatsWithMerged": ".destiny_historical_stats_destiny_historical_stats_with_merged",
    "DestinyHistoricalStatsDestinyHistoricalWeaponStats": ".destiny_historical_stats_destiny_historical_weapon_stats",
    "DestinyHistoricalStatsDestinyHistoricalWeaponStatsData": ".destiny_historical_stats_destiny_historical_weapon_stats_data",
    "DestinyHistoricalStatsDestinyLeaderboard": ".destiny_historical_stats_destiny_leaderboard",
    "DestinyHistoricalStatsDestinyLeaderboardEntry": ".destiny_historical_stats_destiny_leaderboard_entry",
    "DestinyHistoricalStatsDestinyLeaderboardResults": ".destiny_historical_stats_destiny_leaderboard_results",
    "DestinyHistoricalStatsDestinyPlayer": ".destiny_historical_stats_destiny_player",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportData": ".destiny_historical_stats_destiny_post_game_carnage_report_data",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportEntry": ".destiny_historical_stats_destiny_post_game_carnage_report_entry",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportExtendedData": ".destiny_historical_stats_destiny_post_game_carnage_report_extended_data",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry": ".destiny_historical_stats_destiny_post_game_carnage_report_team_entry",
    "DestinyItemBindStatus": ".destiny_item_bind_status",
    "DestinyItemComponentSetOfint32": ".destiny_item_component_set_ofint32",
    "DestinyItemComponentSetOfint64": ".destiny_item_component_set_ofint64",
    "DestinyItemComponentSetOfuint32": ".destiny_item_component_set_ofuint32",
    "DestinyItemLocation": ".destiny_item_location",
    "DestinyItemPerkVisibility": ".destiny_item_perk_visibility",
    "DestinyItemState": ".destiny_item_state",
    "DestinyMilestonesDestinyMilestone": ".destiny_milestones_destiny_milestone",
    "DestinyMilestonesDestinyMilestoneActivity": ".destiny_milestones_destiny_milestone_activity",
    "DestinyMilestonesDestinyMilestoneActivityCompletionStatus": ".destiny_milestones_destiny_milestone_activity_completion_status",
    "DestinyMilestonesDestinyMilestoneActivityPhase": ".destiny_milestones_destiny_milestone_activity_phase",
    "DestinyMilestonesDestinyMilestoneActivityVariant": ".destiny_milestones_destiny_milestone_activity_variant",
    "DestinyMilestonesDestinyMilestoneChallengeActivity": ".destiny_milestones_destiny_milestone_challenge_activity",
    "DestinyMilestonesDestinyMilestoneContent": ".destiny_milestones_destiny_milestone_content",
    "DestinyMilestonesDestinyMilestoneContentItemCategory": ".destiny_milestones_destiny_milestone_content_item_category",
    "DestinyMilestonesDestinyMilestoneQuest": ".destiny_milestones_destiny_milestone_quest",
    "DestinyMilestonesDestinyMilestoneRewardCategory": ".destiny_milestones_destiny_milestone_reward_category",
    "DestinyMilestonesDestinyMilestoneRewardEntry": ".destiny_milestones_destiny_milestone_reward_entry",
    "DestinyMilestonesDestinyMilestoneVendor": ".destiny_milestones_destiny_milestone_vendor",
    "DestinyMilestonesDestinyPublicMilestone": ".destiny_milestones_destiny_public_milestone",
    "DestinyMilestonesDestinyPublicMilestoneActivity": ".destiny_milestones_destiny_public_milestone_activity",
    "DestinyMilestonesDestinyPublicMilestoneActivityVariant": ".destiny_milestones_destiny_public_milestone_activity_variant",
    "DestinyMilestonesDestinyPublicMilestoneChallenge": ".destiny_milestones_destiny_public_milestone_challenge",
    "DestinyMilestonesDestinyPublicMilestoneChallengeActivity": ".destiny_milestones_destiny_public_milestone_challenge_activity",
    "DestinyMilestonesDestinyPublicMilestoneQuest": ".destiny_milestones_destiny_public_milestone_quest",
    "DestinyMilestonesDestinyPublicMilestoneVendor": ".destiny_milestones_destiny_public_milestone_vendor",
    "DestinyMiscDestinyColor": ".destiny_misc_destiny_color",
    "DestinyPerksDestinyPerkReference": ".destiny_perks_destiny_perk_reference",
    "DestinyPlugAvailabilityMode": ".destiny_plug_availability_mode",
    "DestinyPlugUiStyles": ".destiny_plug_ui_styles",
    "DestinyProgressionDestinyFactionProgression": ".destiny_progression_destiny_faction_progression",
    "DestinyQuestsDestinyObjectiveProgress": ".destiny_quests_destiny_objective_progress",
    "DestinyQuestsDestinyQuestStatus": ".destiny_quests_destiny_quest_status",
    "DestinyReportingRequestsDestinyReportOffensePgcrRequest": ".destiny_reporting_requests_destiny_report_offense_pgcr_request",
    "DestinyRequestsActionsDestinyActionRequest": ".destiny_requests_actions_destiny_action_request",
    "DestinyRequestsActionsDestinyCharacterActionRequest": ".destiny_requests_actions_destiny_character_action_request",
    "DestinyRequestsActionsDestinyInsertPlugsActionRequest": ".destiny_requests_actions_destiny_insert_plugs_action_request",
    "DestinyRequestsActionsDestinyInsertPlugsFreeActionRequest": ".destiny_requests_actions_destiny_insert_plugs_free_action_request",
    "DestinyRequestsActionsDestinyInsertPlugsRequestEntry": ".destiny_requests_actions_destiny_insert_plugs_request_entry",
    "DestinyRequestsActionsDestinyItemActionRequest": ".destiny_requests_actions_destiny_item_action_request",
    "DestinyRequestsActionsDestinyItemSetActionRequest": ".destiny_requests_actions_destiny_item_set_action_request",
    "DestinyRequestsActionsDestinyItemStateRequest": ".destiny_requests_actions_destiny_item_state_request",
    "DestinyRequestsActionsDestinyLoadoutActionRequest": ".destiny_requests_actions_destiny_loadout_action_request",
    "DestinyRequestsActionsDestinyLoadoutUpdateActionRequest": ".destiny_requests_actions_destiny_loadout_update_action_request",
    "DestinyRequestsActionsDestinyPostmasterTransferRequest": ".destiny_requests_actions_destiny_postmaster_transfer_request",
    "DestinyRequestsActionsDestinySocketArrayType": ".destiny_requests_actions_destiny_socket_array_type",
    "DestinyRequestsDestinyItemTransferRequest": ".destiny_requests_destiny_item_transfer_request",
    "DestinyResponsesDestinyCharacterResponse": ".destiny_responses_destiny_character_response",
    "DestinyResponsesDestinyCollectibleNodeDetailResponse": ".destiny_responses_destiny_collectible_node_detail_response",
    "DestinyResponsesDestinyErrorProfile": ".destiny_responses_destiny_error_profile",
    "DestinyResponsesDestinyItemChangeResponse": ".destiny_responses_destiny_item_change_response",
    "DestinyResponsesDestinyItemResponse": ".destiny_responses_destiny_item_response",
    "DestinyResponsesDestinyLinkedProfilesResponse": ".destiny_responses_destiny_linked_profiles_response",
    "DestinyResponsesDestinyProfileResponse": ".destiny_responses_destiny_profile_response",
    "DestinyResponsesDestinyProfileUserInfoCard": ".destiny_responses_destiny_profile_user_info_card",
    "DestinyResponsesDestinyPublicVendorsResponse": ".destiny_responses_destiny_public_vendors_response",
    "DestinyResponsesDestinyVendorResponse": ".destiny_responses_destiny_vendor_response",
    "DestinyResponsesDestinyVendorsResponse": ".destiny_responses_destiny_vendors_response",
    "DestinyResponsesInventoryChangedResponse": ".destiny_responses_inventory_changed_response",
    "DestinyResponsesPersonalDestinyVendorSaleItemSetComponent": ".destiny_responses_personal_destiny_vendor_sale_item_set_component",
    "DestinyResponsesPublicDestinyVendorSaleItemSetComponent": ".destiny_responses_public_destiny_vendor_sale_item_set_component",
    "DestinySocketPlugSources": ".destiny_socket_plug_sources",
    "DestinySocketTypeActionType": ".destiny_socket_type_action_type",
    "DestinySocketsDestinyItemPlug": ".destiny_sockets_destiny_item_plug",
    "DestinySocketsDestinyItemPlugBase": ".destiny_sockets_destiny_item_plug_base",
    "DestinySpecialItemType": ".destiny_special_item_type",
    "DestinyTierType": ".destiny_tier_type",
    "DestinyTransferStatuses": ".destiny_transfer_statuses",
    "DestinyVendorDisplayCategorySortOrder": ".destiny_vendor_display_category_sort_order",
    "DestinyVendorInteractionType": ".destiny_vendor_interaction_type",
    "DestinyVendorItemStatus": ".destiny_vendor_item_status",
    "DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent": ".destiny_vendor_sale_item_set_component_of_destiny_public_vendor_sale_item_component",
    "DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent": ".destiny_vendor_sale_item_set_component_of_destiny_vendor_sale_item_component",
    "DestinyVendorsDestinyVendorReceipt": ".destiny_vendors_destiny_vendor_receipt",
    "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent": ".dictionary_component_response_ofint32and_destiny_item_instance_component",
    "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent": ".dictionary_component_response_ofint32and_destiny_item_objectives_component",
    "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent": ".dictionary_component_response_ofint32and_destiny_item_perks_component",
    "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent": ".dictionary_component_response_ofint32and_destiny_item_plug_objectives_component",
    "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent": ".dictionary_component_response_ofint32and_destiny_item_render_component",
    "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent": ".dictionary_component_response_ofint32and_destiny_item_reusable_plugs_component",
    "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent": ".dictionary_component_response_ofint32and_destiny_item_sockets_component",
    "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent": ".dictionary_component_response_ofint32and_destiny_item_stats_component",
    "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent": ".dictionary_component_response_ofint32and_destiny_item_talent_grid_component",
    "DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent": ".dictionary_component_response_ofint32and_destiny_vendor_sale_item_component",
    "DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent": ".dictionary_component_response_ofint64and_destiny_character_activities_component",
    "DictionaryComponentResponseOfint64AndDestinyCharacterComponent": ".dictionary_component_response_ofint64and_destiny_character_component",
    "DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent": ".dictionary_component_response_ofint64and_destiny_character_progression_component",
    "DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent": ".dictionary_component_response_ofint64and_destiny_character_records_component",
    "DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent": ".dictionary_component_response_ofint64and_destiny_character_render_component",
    "DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent": ".dictionary_component_response_ofint64and_destiny_collectibles_component",
    "DictionaryComponentResponseOfint64AndDestinyCraftablesComponent": ".dictionary_component_response_ofint64and_destiny_craftables_component",
    "DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent": ".dictionary_component_response_ofint64and_destiny_currencies_component",
    "DictionaryComponentResponseOfint64AndDestinyInventoryComponent": ".dictionary_component_response_ofint64and_destiny_inventory_component",
    "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent": ".dictionary_component_response_ofint64and_destiny_item_instance_component",
    "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent": ".dictionary_component_response_ofint64and_destiny_item_objectives_component",
    "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent": ".dictionary_component_response_ofint64and_destiny_item_perks_component",
    "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent": ".dictionary_component_response_ofint64and_destiny_item_plug_objectives_component",
    "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent": ".dictionary_component_response_ofint64and_destiny_item_render_component",
    "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent": ".dictionary_component_response_ofint64and_destiny_item_reusable_plugs_component",
    "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent": ".dictionary_component_response_ofint64and_destiny_item_sockets_component",
    "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent": ".dictionary_component_response_ofint64and_destiny_item_stats_component",
    "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent": ".dictionary_component_response_ofint64and_destiny_item_talent_grid_component",
    "DictionaryComponentResponseOfint64AndDestinyKiosksComponent": ".dictionary_component_response_ofint64and_destiny_kiosks_component",
    "DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent": ".dictionary_component_response_ofint64and_destiny_loadouts_component",
    "DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent": ".dictionary_component_response_ofint64and_destiny_plug_sets_component",
    "DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent": ".dictionary_component_response_ofint64and_destiny_presentation_nodes_component",
    "DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent": ".dictionary_component_response_ofint64and_destiny_string_variables_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent": ".dictionary_component_response_ofuint32and_destiny_item_instance_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent": ".dictionary_component_response_ofuint32and_destiny_item_objectives_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent": ".dictionary_component_response_ofuint32and_destiny_item_perks_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent": ".dictionary_component_response_ofuint32and_destiny_item_plug_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent": ".dictionary_component_response_ofuint32and_destiny_item_plug_objectives_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent": ".dictionary_component_response_ofuint32and_destiny_item_render_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent": ".dictionary_component_response_ofuint32and_destiny_item_reusable_plugs_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent": ".dictionary_component_response_ofuint32and_destiny_item_sockets_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent": ".dictionary_component_response_ofuint32and_destiny_item_stats_component",
    "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent": ".dictionary_component_response_ofuint32and_destiny_item_talent_grid_component",
    "DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent": ".dictionary_component_response_ofuint32and_destiny_public_vendor_component",
    "DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent": ".dictionary_component_response_ofuint32and_destiny_vendor_categories_component",
    "DictionaryComponentResponseOfuint32AndDestinyVendorComponent": ".dictionary_component_response_ofuint32and_destiny_vendor_component",
    "DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent": ".dictionary_component_response_ofuint32and_personal_destiny_vendor_sale_item_set_component",
    "DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent": ".dictionary_component_response_ofuint32and_public_destiny_vendor_sale_item_set_component",
    "EntitiesEntityActionResult": ".entities_entity_action_result",
    "ExceptionsPlatformErrorCodes": ".exceptions_platform_error_codes",
    "FireteamFireteamDateRange": ".fireteam_fireteam_date_range",
    "FireteamFireteamMember": ".fireteam_fireteam_member",
    "FireteamFireteamPlatform": ".fireteam_fireteam_platform",
    "FireteamFireteamPlatformInviteResult": ".fireteam_fireteam_platform_invite_result",
    "FireteamFireteamPublicSearchOption": ".fireteam_fireteam_public_search_option",
    "FireteamFireteamResponse": ".fireteam_fireteam_response",
    "FireteamFireteamSlotSearch": ".fireteam_fireteam_slot_search",
    "FireteamFireteamSummary": ".fireteam_fireteam_summary",
    "FireteamFireteamUserInfoCard": ".fireteam_fireteam_user_info_card",
    "ForumCommunityContentSortMode": ".forum_community_content_sort_mode",
    "ForumForumMediaType": ".forum_forum_media_type",
    "ForumForumPostPopularity": ".forum_forum_post_popularity",
    "ForumForumPostSortEnum": ".forum_forum_post_sort_enum",
    "ForumForumRecruitmentDetail": ".forum_forum_recruitment_detail",
    "ForumForumRecruitmentIntensityLabel": ".forum_forum_recruitment_intensity_label",
    "ForumForumRecruitmentToneLabel": ".forum_forum_recruitment_tone_label",
    "ForumForumTopicsCategoryFiltersEnum": ".forum_forum_topics_category_filters_enum",
    "ForumForumTopicsQuickDateEnum": ".forum_forum_topics_quick_date_enum",
    "ForumForumTopicsSortEnum": ".forum_forum_topics_sort_enum",
    "ForumPollResponse": ".forum_poll_response",
    "ForumPollResult": ".forum_poll_result",
    "ForumPostResponse": ".forum_post_response",
    "ForumPostSearchResponse": ".forum_post_search_response",
    "ForumsForumFlagsEnum": ".forums_forum_flags_enum",
    "ForumsForumPostCategoryEnums": ".forums_forum_post_category_enums",
    "GlobalAlert": ".global_alert",
    "GlobalAlertLevel": ".global_alert_level",
    "GlobalAlertType": ".global_alert_type",
    "GroupsV2Capabilities": ".groups_v2capabilities",
    "GroupsV2ChatSecuritySetting": ".groups_v2chat_security_setting",
    "GroupsV2ClanBanner": ".groups_v2clan_banner",
    "GroupsV2GetGroupsForMemberResponse": ".groups_v2get_groups_for_member_response",
    "GroupsV2GroupAllianceStatus": ".groups_v2group_alliance_status",
    "GroupsV2GroupApplicationListRequest": ".groups_v2group_application_list_request",
    "GroupsV2GroupApplicationRequest": ".groups_v2group_application_request",
    "GroupsV2GroupApplicationResolveState": ".groups_v2group_application_resolve_state",
    "GroupsV2GroupApplicationResponse": ".groups_v2group_application_response",
    "GroupsV2GroupBan": ".groups_v2group_ban",
    "GroupsV2GroupBanRequest": ".groups_v2group_ban_request",
    "GroupsV2GroupDateRange": ".groups_v2group_date_range",
    "GroupsV2GroupEditAction": ".groups_v2group_edit_action",
    "GroupsV2GroupFeatures": ".groups_v2group_features",
    "GroupsV2GroupHomepage": ".groups_v2group_homepage",
    "GroupsV2GroupMember": ".groups_v2group_member",
    "GroupsV2GroupMemberApplication": ".groups_v2group_member_application",
    "GroupsV2GroupMemberCountFilter": ".groups_v2group_member_count_filter",
    "GroupsV2GroupMemberLeaveResult": ".groups_v2group_member_leave_result",
    "GroupsV2GroupMembership": ".groups_v2group_membership",
    "GroupsV2GroupMembershipBase": ".groups_v2group_membership_base",
    "GroupsV2GroupMembershipSearchResponse": ".groups_v2group_membership_search_response",
    "GroupsV2GroupNameSearchRequest": ".groups_v2group_name_search_request",
    "GroupsV2GroupOptionalConversation": ".groups_v2group_optional_conversation",
    "GroupsV2GroupOptionalConversationAddRequest": ".groups_v2group_optional_conversation_add_request",
    "GroupsV2GroupOptionalConversationEditRequest": ".groups_v2group_optional_conversation_edit_request",
    "GroupsV2GroupOptionsEditAction": ".groups_v2group_options_edit_action",
    "GroupsV2GroupPostPublicity": ".groups_v2group_post_publicity",
    "GroupsV2GroupPotentialMember": ".groups_v2group_potential_member",
    "GroupsV2GroupPotentialMemberStatus": ".groups_v2group_potential_member_status",
    "GroupsV2GroupPotentialMembership": ".groups_v2group_potential_membership",
    "GroupsV2GroupPotentialMembershipSearchResponse": ".groups_v2group_potential_membership_search_response",
    "GroupsV2GroupQuery": ".groups_v2group_query",
    "GroupsV2GroupResponse": ".groups_v2group_response",
    "GroupsV2GroupSearchResponse": ".groups_v2group_search_response",
    "GroupsV2GroupSortBy": ".groups_v2group_sort_by",
    "GroupsV2GroupType": ".groups_v2group_type",
    "GroupsV2GroupUserBase": ".groups_v2group_user_base",
    "GroupsV2GroupUserInfoCard": ".groups_v2group_user_info_card",
    "GroupsV2GroupV2": ".groups_v2group_v2",
    "GroupsV2GroupV2Card": ".groups_v2group_v2card",
    "GroupsV2GroupV2ClanInfo": ".groups_v2group_v2clan_info",
    "GroupsV2GroupV2ClanInfoAndInvestment": ".groups_v2group_v2clan_info_and_investment",
    "GroupsV2GroupsForMemberFilter": ".groups_v2groups_for_member_filter",
    "GroupsV2HostGuidedGamesPermissionLevel": ".groups_v2host_guided_games_permission_level",
    "GroupsV2MembershipOption": ".groups_v2membership_option",
    "GroupsV2RuntimeGroupMemberType": ".groups_v2runtime_group_member_type",
    "IgnoresIgnoreLength": ".ignores_ignore_length",
    "IgnoresIgnoreResponse": ".ignores_ignore_response",
    "IgnoresIgnoreStatus": ".ignores_ignore_status",
    "InterpolationInterpolationPoint": ".interpolation_interpolation_point",
    "InterpolationInterpolationPointFloat": ".interpolation_interpolation_point_float",
    "LinksHyperlinkReference": ".links_hyperlink_reference",
    "OauthScope": ".oauth_scope",
    "QueriesPagedQuery": ".queries_paged_query",
    "QueriesSearchResult": ".queries_search_result",
    "Schema1": ".schema1",
    "Schema10": ".schema10",
    "Schema100": ".schema100",
    "Schema101": ".schema101",
    "Schema102": ".schema102",
    "Schema103": ".schema103",
    "Schema104": ".schema104",
    "Schema105": ".schema105",
    "Schema106": ".schema106",
    "Schema107": ".schema107",
    "Schema108": ".schema108",
    "Schema109": ".schema109",
    "Schema11": ".schema11",
    "Schema110": ".schema110",
    "Schema111": ".schema111",
    "Schema112": ".schema112",
    "Schema113": ".schema113",
    "Schema114": ".schema114",
    "Schema115": ".schema115",
    "Schema116": ".schema116",
    "Schema117": ".schema117",
    "Schema118": ".schema118",
    "Schema12": ".schema12",
    "Schema13": ".schema13",
    "Schema14": ".schema14",
    "Schema15": ".schema15",
    "Schema16": ".schema16",
    "Schema17": ".schema17",
    "Schema18": ".schema18",
    "Schema19": ".schema19",
    "Schema2": ".schema2",
    "Schema20": ".schema20",
    "Schema21": ".schema21",
    "Schema22": ".schema22",
    "Schema23": ".schema23",
    "Schema24": ".schema24",
    "Schema25": ".schema25",
    "Schema26": ".schema26",
    "Schema27": ".schema27",
    "Schema28": ".schema28",
    "Schema29": ".schema29",
    "Schema3": ".schema3",
    "Schema30": ".schema30",
    "Schema31": ".schema31",
    "Schema32": ".schema32",
    "Schema33": ".schema33",
    "Schema34": ".schema34",
    "Schema35": ".schema35",
    "Schema36": ".schema36",
    "Schema37": ".schema37",
    "Schema38": ".schema38",
    "Schema39": ".schema39",
    "Schema4": ".schema4",
    "Schema40": ".schema40",
    "Schema41": ".schema41",
    "Schema42": ".schema42",
    "Schema43": ".schema43",
    "Schema44": ".schema44",
    "Schema45": ".schema45",
    "Schema46": ".schema46",
    "Schema47": ".schema47",
    "Schema48": ".schema48",
    "Schema49": ".schema49",
    "Schema5": ".schema5",
    "Schema50": ".schema50",
    "Schema51": ".schema51",
    "Schema52": ".schema52",
    "Schema53": ".schema53",
    "Schema54": ".schema54",
    "Schema55": ".schema55",
    "Schema56": ".schema56",
    "Schema57": ".schema57",
    "Schema58": ".schema58",
    "Schema59": ".schema59",
    "Schema6": ".schema6",
    "Schema60": ".schema60",
    "Schema61": ".schema61",
    "Schema62": ".schema62",
    "Schema63": ".schema63",
    "Schema64": ".schema64",
    "Schema65": ".schema65",
    "Schema66": ".schema66",
    "Schema67": ".schema67",
    "Schema68": ".schema68",
    "Schema69": ".schema69",
    "Schema7": ".schema7",
    "Schema70": ".schema70",
    "Schema71": ".schema71",
    "Schema72": ".schema72",
    "Schema73": ".schema73",
    "Schema74": ".schema74",
    "Schema75": ".schema75",
    "Schema76": ".schema76",
    "Schema77": ".schema77",
    "Schema78": ".schema78",
    "Schema79": ".schema79",
    "Schema8": ".schema8",
    "Schema80": ".schema80",
    "Schema81": ".schema81",
    "Schema82": ".schema82",
    "Schema83": ".schema83",
    "Schema84": ".schema84",
    "Schema85": ".schema85",
    "Schema86": ".schema86",
    "Schema87": ".schema87",
    "Schema88": ".schema88",
    "Schema89": ".schema89",
    "Schema9": ".schema9",
    "Schema90": ".schema90",
    "Schema91": ".schema91",
    "Schema92": ".schema92",
    "Schema93": ".schema93",
    "Schema94": ".schema94",
    "Schema95": ".schema95",
    "Schema96": ".schema96",
    "Schema97": ".schema97",
    "Schema98": ".schema98",
    "Schema99": ".schema99",
    "SearchResultOfContentItemPublicContract": ".search_result_of_content_item_public_contract",
    "SearchResultOfDestinyEntitySearchResultItem": ".search_result_of_destiny_entity_search_result_item",
    "SearchResultOfFireteamResponse": ".search_result_of_fireteam_response",
    "SearchResultOfFireteamSummary": ".search_result_of_fireteam_summary",
    "SearchResultOfGroupBan": ".search_result_of_group_ban",
    "SearchResultOfGroupMember": ".search_result_of_group_member",
    "SearchResultOfGroupMemberApplication": ".search_result_of_group_member_application",
    "SearchResultOfGroupMembership": ".search_result_of_group_membership",
    "SearchResultOfGroupPotentialMembership": ".search_result_of_group_potential_membership",
    "SearchResultOfGroupV2Card": ".search_result_of_group_v2card",
    "SearchResultOfPostResponse": ".search_result_of_post_response",
    "SearchResultOfTrendingEntry": ".search_result_of_trending_entry",
    "SingleComponentResponseOfDestinyCharacterActivitiesComponent": ".single_component_response_of_destiny_character_activities_component",
    "SingleComponentResponseOfDestinyCharacterComponent": ".single_component_response_of_destiny_character_component",
    "SingleComponentResponseOfDestinyCharacterProgressionComponent": ".single_component_response_of_destiny_character_progression_component",
    "SingleComponentResponseOfDestinyCharacterRecordsComponent": ".single_component_response_of_destiny_character_records_component",
    "SingleComponentResponseOfDestinyCharacterRenderComponent": ".single_component_response_of_destiny_character_render_component",
    "SingleComponentResponseOfDestinyCollectiblesComponent": ".single_component_response_of_destiny_collectibles_component",
    "SingleComponentResponseOfDestinyCurrenciesComponent": ".single_component_response_of_destiny_currencies_component",
    "SingleComponentResponseOfDestinyInventoryComponent": ".single_component_response_of_destiny_inventory_component",
    "SingleComponentResponseOfDestinyItemComponent": ".single_component_response_of_destiny_item_component",
    "SingleComponentResponseOfDestinyItemInstanceComponent": ".single_component_response_of_destiny_item_instance_component",
    "SingleComponentResponseOfDestinyItemObjectivesComponent": ".single_component_response_of_destiny_item_objectives_component",
    "SingleComponentResponseOfDestinyItemPerksComponent": ".single_component_response_of_destiny_item_perks_component",
    "SingleComponentResponseOfDestinyItemPlugObjectivesComponent": ".single_component_response_of_destiny_item_plug_objectives_component",
    "SingleComponentResponseOfDestinyItemRenderComponent": ".single_component_response_of_destiny_item_render_component",
    "SingleComponentResponseOfDestinyItemReusablePlugsComponent": ".single_component_response_of_destiny_item_reusable_plugs_component",
    "SingleComponentResponseOfDestinyItemSocketsComponent": ".single_component_response_of_destiny_item_sockets_component",
    "SingleComponentResponseOfDestinyItemStatsComponent": ".single_component_response_of_destiny_item_stats_component",
    "SingleComponentResponseOfDestinyItemTalentGridComponent": ".single_component_response_of_destiny_item_talent_grid_component",
    "SingleComponentResponseOfDestinyKiosksComponent": ".single_component_response_of_destiny_kiosks_component",
    "SingleComponentResponseOfDestinyLoadoutsComponent": ".single_component_response_of_destiny_loadouts_component",
    "SingleComponentResponseOfDestinyMetricsComponent": ".single_component_response_of_destiny_metrics_component",
    "SingleComponentResponseOfDestinyPlatformSilverComponent": ".single_component_response_of_destiny_platform_silver_component",
    "SingleComponentResponseOfDestinyPlugSetsComponent": ".single_component_response_of_destiny_plug_sets_component",
    "SingleComponentResponseOfDestinyPresentationNodesComponent": ".single_component_response_of_destiny_presentation_nodes_component",
    "SingleComponentResponseOfDestinyProfileCollectiblesComponent": ".single_component_response_of_destiny_profile_collectibles_component",
    "SingleComponentResponseOfDestinyProfileComponent": ".single_component_response_of_destiny_profile_component",
    "SingleComponentResponseOfDestinyProfileProgressionComponent": ".single_component_response_of_destiny_profile_progression_component",
    "SingleComponentResponseOfDestinyProfileRecordsComponent": ".single_component_response_of_destiny_profile_records_component",
    "SingleComponentResponseOfDestinyProfileTransitoryComponent": ".single_component_response_of_destiny_profile_transitory_component",
    "SingleComponentResponseOfDestinySocialCommendationsComponent": ".single_component_response_of_destiny_social_commendations_component",
    "SingleComponentResponseOfDestinyStringVariablesComponent": ".single_component_response_of_destiny_string_variables_component",
    "SingleComponentResponseOfDestinyVendorCategoriesComponent": ".single_component_response_of_destiny_vendor_categories_component",
    "SingleComponentResponseOfDestinyVendorComponent": ".single_component_response_of_destiny_vendor_component",
    "SingleComponentResponseOfDestinyVendorGroupComponent": ".single_component_response_of_destiny_vendor_group_component",
    "SingleComponentResponseOfDestinyVendorReceiptsComponent": ".single_component_response_of_destiny_vendor_receipts_component",
    "SocialFriendsBungieFriend": ".social_friends_bungie_friend",
    "SocialFriendsBungieFriendListResponse": ".social_friends_bungie_friend_list_response",
    "SocialFriendsBungieFriendRequestListResponse": ".social_friends_bungie_friend_request_list_response",
    "SocialFriendsFriendRelationshipState": ".social_friends_friend_relationship_state",
    "SocialFriendsPlatformFriend": ".social_friends_platform_friend",
    "SocialFriendsPlatformFriendResponse": ".social_friends_platform_friend_response",
    "SocialFriendsPlatformFriendType": ".social_friends_platform_friend_type",
    "SocialFriendsPresenceOnlineStateFlags": ".social_friends_presence_online_state_flags",
    "SocialFriendsPresenceStatus": ".social_friends_presence_status",
    "StreamInfo": ".stream_info",
    "StreamingDropStateEnum": ".streaming_drop_state_enum",
    "TagsModelsContractsTagResponse": ".tags_models_contracts_tag_response",
    "TokensBungieRewardDisplay": ".tokens_bungie_reward_display",
    "TokensCollectibleDefinitions": ".tokens_collectible_definitions",
    "TokensPartnerOfferClaimRequest": ".tokens_partner_offer_claim_request",
    "TokensPartnerOfferHistoryResponse": ".tokens_partner_offer_history_response",
    "TokensPartnerOfferSkuHistoryResponse": ".tokens_partner_offer_sku_history_response",
    "TokensPartnerRewardHistoryResponse": ".tokens_partner_reward_history_response",
    "TokensRewardAvailabilityModel": ".tokens_reward_availability_model",
    "TokensRewardDisplayProperties": ".tokens_reward_display_properties",
    "TokensTwitchDropHistoryResponse": ".tokens_twitch_drop_history_response",
    "TokensUserRewardAvailabilityModel": ".tokens_user_reward_availability_model",
    "TrendingTrendingCategories": ".trending_trending_categories",
    "TrendingTrendingCategory": ".trending_trending_category",
    "TrendingTrendingDetail": ".trending_trending_detail",
    "TrendingTrendingEntry": ".trending_trending_entry",
    "TrendingTrendingEntryCommunityCreation": ".trending_trending_entry_community_creation",
    "TrendingTrendingEntryDestinyActivity": ".trending_trending_entry_destiny_activity",
    "TrendingTrendingEntryDestinyItem": ".trending_trending_entry_destiny_item",
    "TrendingTrendingEntryDestinyRitual": ".trending_trending_entry_destiny_ritual",
    "TrendingTrendingEntryNews": ".trending_trending_entry_news",
    "TrendingTrendingEntrySupportArticle": ".trending_trending_entry_support_article",
    "TrendingTrendingEntryType": ".trending_trending_entry_type",
    "UserCrossSaveUserMembership": ".user_cross_save_user_membership",
    "UserEMailSettingLocalization": ".user_e_mail_setting_localization",
    "UserEMailSettingSubscriptionLocalization": ".user_e_mail_setting_subscription_localization",
    "UserEmailOptInDefinition": ".user_email_opt_in_definition",
    "UserEmailSettings": ".user_email_settings",
    "UserEmailSubscriptionDefinition": ".user_email_subscription_definition",
    "UserEmailViewDefinition": ".user_email_view_definition",
    "UserEmailViewDefinitionSetting": ".user_email_view_definition_setting",
    "UserExactSearchRequest": ".user_exact_search_request",
    "UserGeneralUser": ".user_general_user",
    "UserHardLinkedUserMembership": ".user_hard_linked_user_membership",
    "UserModelsGetCredentialTypesForAccountResponse": ".user_models_get_credential_types_for_account_response",
    "UserOptInFlags": ".user_opt_in_flags",
    "UserUserInfoCard": ".user_user_info_card",
    "UserUserMembership": ".user_user_membership",
    "UserUserMembershipData": ".user_user_membership_data",
    "UserUserSearchPrefixRequest": ".user_user_search_prefix_request",
    "UserUserSearchResponse": ".user_user_search_response",
    "UserUserSearchResponseDetail": ".user_user_search_response_detail",
    "UserUserToUserContext": ".user_user_to_user_context",
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
    "ApplicationsApiUsage",
    "ApplicationsApplication",
    "ApplicationsApplicationDeveloper",
    "ApplicationsApplicationScopes",
    "ApplicationsApplicationStatus",
    "ApplicationsDatapoint",
    "ApplicationsDeveloperRole",
    "ApplicationsSeries",
    "BungieCredentialType",
    "BungieMembershipType",
    "BungieMembershipTypeArray",
    "CommonModelsCoreSetting",
    "CommonModelsCoreSettingsConfiguration",
    "CommonModelsCoreSystem",
    "CommonModelsDestiny2CoreSettings",
    "ComponentsComponentPrivacySetting",
    "ComponentsComponentResponse",
    "ConfigClanBannerClanBannerDecal",
    "ConfigClanBannerClanBannerSource",
    "ConfigGroupTheme",
    "ConfigUserTheme",
    "ContentCommentSummary",
    "ContentContentItemPublicContract",
    "ContentContentRepresentation",
    "ContentModelsContentPreview",
    "ContentModelsContentPropertyDataTypeEnum",
    "ContentModelsContentTypeDefaultValue",
    "ContentModelsContentTypeDescription",
    "ContentModelsContentTypeProperty",
    "ContentModelsContentTypePropertySection",
    "ContentModelsTagMetadataDefinition",
    "ContentModelsTagMetadataItem",
    "ContentNewsArticleRssItem",
    "ContentNewsArticleRssResponse",
    "DatesDateRange",
    "DestinyActivitiesDestinyPublicActivityStatus",
    "DestinyActivityGraphNodeHighlightType",
    "DestinyAdvancedAwaAuthorizationResult",
    "DestinyAdvancedAwaInitializeResponse",
    "DestinyAdvancedAwaPermissionRequested",
    "DestinyAdvancedAwaResponseReason",
    "DestinyAdvancedAwaType",
    "DestinyAdvancedAwaUserResponse",
    "DestinyAdvancedAwaUserSelection",
    "DestinyArtifactsDestinyArtifactCharacterScoped",
    "DestinyArtifactsDestinyArtifactProfileScoped",
    "DestinyArtifactsDestinyArtifactTier",
    "DestinyArtifactsDestinyArtifactTierItem",
    "DestinyBaseItemComponentSetOfint32",
    "DestinyBaseItemComponentSetOfint64",
    "DestinyBaseItemComponentSetOfuint32",
    "DestinyBucketCategory",
    "DestinyBucketScope",
    "DestinyChallengesDestinyChallengeStatus",
    "DestinyCharacterDestinyCharacterCustomization",
    "DestinyCharacterDestinyCharacterPeerView",
    "DestinyCharacterDestinyItemPeerView",
    "DestinyComponentsCollectiblesDestinyCollectibleComponent",
    "DestinyComponentsCollectiblesDestinyCollectiblesComponent",
    "DestinyComponentsCollectiblesDestinyProfileCollectiblesComponent",
    "DestinyComponentsCraftablesDestinyCraftableComponent",
    "DestinyComponentsCraftablesDestinyCraftableSocketComponent",
    "DestinyComponentsCraftablesDestinyCraftableSocketPlugComponent",
    "DestinyComponentsCraftablesDestinyCraftablesComponent",
    "DestinyComponentsInventoryDestinyCurrenciesComponent",
    "DestinyComponentsInventoryDestinyPlatformSilverComponent",
    "DestinyComponentsItemsDestinyItemPlugComponent",
    "DestinyComponentsItemsDestinyItemPlugObjectivesComponent",
    "DestinyComponentsItemsDestinyItemReusablePlugsComponent",
    "DestinyComponentsKiosksDestinyKioskItem",
    "DestinyComponentsKiosksDestinyKiosksComponent",
    "DestinyComponentsLoadoutsDestinyLoadoutComponent",
    "DestinyComponentsLoadoutsDestinyLoadoutItemComponent",
    "DestinyComponentsLoadoutsDestinyLoadoutsComponent",
    "DestinyComponentsMetricsDestinyMetricComponent",
    "DestinyComponentsMetricsDestinyMetricsComponent",
    "DestinyComponentsPlugSetsDestinyPlugSetsComponent",
    "DestinyComponentsPresentationDestinyPresentationNodeComponent",
    "DestinyComponentsPresentationDestinyPresentationNodesComponent",
    "DestinyComponentsProfilesDestinyProfileProgressionComponent",
    "DestinyComponentsProfilesDestinyProfileTransitoryComponent",
    "DestinyComponentsProfilesDestinyProfileTransitoryCurrentActivity",
    "DestinyComponentsProfilesDestinyProfileTransitoryJoinability",
    "DestinyComponentsProfilesDestinyProfileTransitoryPartyMember",
    "DestinyComponentsProfilesDestinyProfileTransitoryTrackingEntry",
    "DestinyComponentsRecordsDestinyCharacterRecordsComponent",
    "DestinyComponentsRecordsDestinyProfileRecordsComponent",
    "DestinyComponentsRecordsDestinyRecordComponent",
    "DestinyComponentsRecordsDestinyRecordsComponent",
    "DestinyComponentsSocialDestinySocialCommendationsComponent",
    "DestinyComponentsStringVariablesDestinyStringVariablesComponent",
    "DestinyComponentsVendorsDestinyPublicVendorComponent",
    "DestinyComponentsVendorsDestinyPublicVendorSaleItemComponent",
    "DestinyComponentsVendorsDestinyVendorBaseComponent",
    "DestinyComponentsVendorsDestinyVendorGroup",
    "DestinyComponentsVendorsDestinyVendorGroupComponent",
    "DestinyComponentsVendorsDestinyVendorSaleItemBaseComponent",
    "DestinyConfigDestinyManifest",
    "DestinyConfigGearAssetDataBaseDefinition",
    "DestinyConfigImagePyramidEntry",
    "DestinyConstantsDestinyEnvironmentLocationMapping",
    "DestinyDamageType",
    "DestinyDefinitionsActivityModifiersDestinyActivityModifierDefinition",
    "DestinyDefinitionsAnimationsDestinyAnimationReference",
    "DestinyDefinitionsArtifactsDestinyArtifactDefinition",
    "DestinyDefinitionsArtifactsDestinyArtifactTierDefinition",
    "DestinyDefinitionsArtifactsDestinyArtifactTierItemDefinition",
    "DestinyDefinitionsBreakerTypesDestinyBreakerTypeDefinition",
    "DestinyDefinitionsChecklistsDestinyChecklistDefinition",
    "DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition",
    "DestinyDefinitionsCollectiblesDestinyCollectibleAcquisitionBlock",
    "DestinyDefinitionsCollectiblesDestinyCollectibleDefinition",
    "DestinyDefinitionsCollectiblesDestinyCollectibleStateBlock",
    "DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition",
    "DestinyDefinitionsCommonDestinyIconSequenceDefinition",
    "DestinyDefinitionsCommonDestinyPositionDefinition",
    "DestinyDefinitionsDestinyActivityChallengeDefinition",
    "DestinyDefinitionsDestinyActivityDefinition",
    "DestinyDefinitionsDestinyActivityGraphListEntryDefinition",
    "DestinyDefinitionsDestinyActivityGuidedBlockDefinition",
    "DestinyDefinitionsDestinyActivityInsertionPointDefinition",
    "DestinyDefinitionsDestinyActivityLoadoutRequirement",
    "DestinyDefinitionsDestinyActivityLoadoutRequirementSet",
    "DestinyDefinitionsDestinyActivityMatchmakingBlockDefinition",
    "DestinyDefinitionsDestinyActivityModeDefinition",
    "DestinyDefinitionsDestinyActivityModifierReferenceDefinition",
    "DestinyDefinitionsDestinyActivityPlaylistItemDefinition",
    "DestinyDefinitionsDestinyActivityRewardDefinition",
    "DestinyDefinitionsDestinyActivityTypeDefinition",
    "DestinyDefinitionsDestinyActivityUnlockStringDefinition",
    "DestinyDefinitionsDestinyArrangementRegionFilterDefinition",
    "DestinyDefinitionsDestinyArtDyeReference",
    "DestinyDefinitionsDestinyBubbleDefinition",
    "DestinyDefinitionsDestinyClassDefinition",
    "DestinyDefinitionsDestinyDamageTypeDefinition",
    "DestinyDefinitionsDestinyDefinition",
    "DestinyDefinitionsDestinyDestinationBubbleSettingDefinition",
    "DestinyDefinitionsDestinyDestinationDefinition",
    "DestinyDefinitionsDestinyDisplayCategoryDefinition",
    "DestinyDefinitionsDestinyEntitySearchResult",
    "DestinyDefinitionsDestinyEntitySearchResultItem",
    "DestinyDefinitionsDestinyEquipmentSlotDefinition",
    "DestinyDefinitionsDestinyEquippingBlockDefinition",
    "DestinyDefinitionsDestinyFactionDefinition",
    "DestinyDefinitionsDestinyFactionVendorDefinition",
    "DestinyDefinitionsDestinyGearArtArrangementReference",
    "DestinyDefinitionsDestinyGenderDefinition",
    "DestinyDefinitionsDestinyInventoryBucketDefinition",
    "DestinyDefinitionsDestinyInventoryItemDefinition",
    "DestinyDefinitionsDestinyInventoryItemStatDefinition",
    "DestinyDefinitionsDestinyItemActionBlockDefinition",
    "DestinyDefinitionsDestinyItemActionRequiredItemDefinition",
    "DestinyDefinitionsDestinyItemCategoryDefinition",
    "DestinyDefinitionsDestinyItemCraftingBlockBonusPlugDefinition",
    "DestinyDefinitionsDestinyItemCraftingBlockDefinition",
    "DestinyDefinitionsDestinyItemCreationEntryLevelDefinition",
    "DestinyDefinitionsDestinyItemGearsetBlockDefinition",
    "DestinyDefinitionsDestinyItemIntrinsicSocketEntryDefinition",
    "DestinyDefinitionsDestinyItemInventoryBlockDefinition",
    "DestinyDefinitionsDestinyItemInvestmentStatDefinition",
    "DestinyDefinitionsDestinyItemMetricBlockDefinition",
    "DestinyDefinitionsDestinyItemObjectiveBlockDefinition",
    "DestinyDefinitionsDestinyItemPerkEntryDefinition",
    "DestinyDefinitionsDestinyItemPreviewBlockDefinition",
    "DestinyDefinitionsDestinyItemQualityBlockDefinition",
    "DestinyDefinitionsDestinyItemSackBlockDefinition",
    "DestinyDefinitionsDestinyItemSetBlockDefinition",
    "DestinyDefinitionsDestinyItemSetBlockEntryDefinition",
    "DestinyDefinitionsDestinyItemSocketBlockDefinition",
    "DestinyDefinitionsDestinyItemSocketCategoryDefinition",
    "DestinyDefinitionsDestinyItemSocketEntryDefinition",
    "DestinyDefinitionsDestinyItemSocketEntryPlugItemDefinition",
    "DestinyDefinitionsDestinyItemSocketEntryPlugItemRandomizedDefinition",
    "DestinyDefinitionsDestinyItemSourceBlockDefinition",
    "DestinyDefinitionsDestinyItemStatBlockDefinition",
    "DestinyDefinitionsDestinyItemSummaryBlockDefinition",
    "DestinyDefinitionsDestinyItemTalentGridBlockDefinition",
    "DestinyDefinitionsDestinyItemTooltipNotification",
    "DestinyDefinitionsDestinyItemTranslationBlockDefinition",
    "DestinyDefinitionsDestinyItemValueBlockDefinition",
    "DestinyDefinitionsDestinyItemVendorSourceReference",
    "DestinyDefinitionsDestinyItemVersionDefinition",
    "DestinyDefinitionsDestinyLocationDefinition",
    "DestinyDefinitionsDestinyLocationReleaseDefinition",
    "DestinyDefinitionsDestinyMaterialRequirement",
    "DestinyDefinitionsDestinyMaterialRequirementSetDefinition",
    "DestinyDefinitionsDestinyMedalTierDefinition",
    "DestinyDefinitionsDestinyNodeActivationRequirement",
    "DestinyDefinitionsDestinyNodeSocketReplaceResponse",
    "DestinyDefinitionsDestinyNodeStepDefinition",
    "DestinyDefinitionsDestinyObjectiveDefinition",
    "DestinyDefinitionsDestinyObjectiveDisplayProperties",
    "DestinyDefinitionsDestinyObjectivePerkEntryDefinition",
    "DestinyDefinitionsDestinyObjectiveStatEntryDefinition",
    "DestinyDefinitionsDestinyPlaceDefinition",
    "DestinyDefinitionsDestinyPlugItemCraftingRequirements",
    "DestinyDefinitionsDestinyPlugItemCraftingUnlockRequirement",
    "DestinyDefinitionsDestinyProgressionDefinition",
    "DestinyDefinitionsDestinyProgressionDisplayPropertiesDefinition",
    "DestinyDefinitionsDestinyProgressionMappingDefinition",
    "DestinyDefinitionsDestinyProgressionRewardDefinition",
    "DestinyDefinitionsDestinyProgressionRewardItemQuantity",
    "DestinyDefinitionsDestinyProgressionStepDefinition",
    "DestinyDefinitionsDestinyRaceDefinition",
    "DestinyDefinitionsDestinyRewardSourceCategory",
    "DestinyDefinitionsDestinyRewardSourceDefinition",
    "DestinyDefinitionsDestinySandboxPatternDefinition",
    "DestinyDefinitionsDestinySandboxPerkDefinition",
    "DestinyDefinitionsDestinyStatDefinition",
    "DestinyDefinitionsDestinyStatDisplayDefinition",
    "DestinyDefinitionsDestinyStatGroupDefinition",
    "DestinyDefinitionsDestinyStatOverrideDefinition",
    "DestinyDefinitionsDestinyTalentExclusiveGroup",
    "DestinyDefinitionsDestinyTalentGridDefinition",
    "DestinyDefinitionsDestinyTalentNodeCategory",
    "DestinyDefinitionsDestinyTalentNodeDefinition",
    "DestinyDefinitionsDestinyTalentNodeExclusiveSetDefinition",
    "DestinyDefinitionsDestinyTalentNodeStepDamageTypes",
    "DestinyDefinitionsDestinyTalentNodeStepGroups",
    "DestinyDefinitionsDestinyTalentNodeStepGuardianAttributes",
    "DestinyDefinitionsDestinyTalentNodeStepImpactEffects",
    "DestinyDefinitionsDestinyTalentNodeStepLightAbilities",
    "DestinyDefinitionsDestinyTalentNodeStepWeaponPerformances",
    "DestinyDefinitionsDestinyUnlockDefinition",
    "DestinyDefinitionsDestinyUnlockExpressionDefinition",
    "DestinyDefinitionsDestinyUnlockValueDefinition",
    "DestinyDefinitionsDestinyVendorAcceptedItemDefinition",
    "DestinyDefinitionsDestinyVendorActionDefinition",
    "DestinyDefinitionsDestinyVendorCategoryEntryDefinition",
    "DestinyDefinitionsDestinyVendorCategoryOverlayDefinition",
    "DestinyDefinitionsDestinyVendorDefinition",
    "DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition",
    "DestinyDefinitionsDestinyVendorGroupDefinition",
    "DestinyDefinitionsDestinyVendorGroupReference",
    "DestinyDefinitionsDestinyVendorInteractionDefinition",
    "DestinyDefinitionsDestinyVendorInteractionReplyDefinition",
    "DestinyDefinitionsDestinyVendorInteractionSackEntryDefinition",
    "DestinyDefinitionsDestinyVendorInventoryFlyoutBucketDefinition",
    "DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition",
    "DestinyDefinitionsDestinyVendorItemDefinition",
    "DestinyDefinitionsDestinyVendorItemQuantity",
    "DestinyDefinitionsDestinyVendorItemSocketOverride",
    "DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition",
    "DestinyDefinitionsDestinyVendorSaleItemActionBlockDefinition",
    "DestinyDefinitionsDestinyVendorServiceDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition",
    "DestinyDefinitionsDirectorDestinyActivityGraphNodeStateEntry",
    "DestinyDefinitionsDirectorDestinyLinkedGraphDefinition",
    "DestinyDefinitionsDirectorDestinyLinkedGraphEntryDefinition",
    "DestinyDefinitionsEnergyTypesDestinyEnergyTypeDefinition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankConstantsDefinition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankDefinition",
    "DestinyDefinitionsGuardianRanksDestinyGuardianRankIconBackgroundsDefinition",
    "DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition",
    "DestinyDefinitionsItemsDestinyDerivedItemDefinition",
    "DestinyDefinitionsItemsDestinyEnergyCapacityEntry",
    "DestinyDefinitionsItemsDestinyEnergyCostEntry",
    "DestinyDefinitionsItemsDestinyItemPlugDefinition",
    "DestinyDefinitionsItemsDestinyItemTierTypeDefinition",
    "DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock",
    "DestinyDefinitionsItemsDestinyParentItemOverride",
    "DestinyDefinitionsItemsDestinyPlugRuleDefinition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutColorDefinition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutConstantsDefinition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutIconDefinition",
    "DestinyDefinitionsLoadoutsDestinyLoadoutNameDefinition",
    "DestinyDefinitionsLoreDestinyLoreDefinition",
    "DestinyDefinitionsMetricsDestinyMetricDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneActivityVariantDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityGraphNodeEntry",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase",
    "DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneDisplayPreference",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem",
    "DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneType",
    "DestinyDefinitionsMilestonesDestinyMilestoneValueDefinition",
    "DestinyDefinitionsMilestonesDestinyMilestoneVendorDefinition",
    "DestinyDefinitionsPowerCapsDestinyPowerCapDefinition",
    "DestinyDefinitionsPresentationDestinyPresentationChildBlock",
    "DestinyDefinitionsPresentationDestinyPresentationNodeBaseDefinition",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildEntry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildEntryBase",
    "DestinyDefinitionsPresentationDestinyPresentationNodeChildrenBlock",
    "DestinyDefinitionsPresentationDestinyPresentationNodeCollectibleChildEntry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeCraftableChildEntry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeDefinition",
    "DestinyDefinitionsPresentationDestinyPresentationNodeMetricChildEntry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeRecordChildEntry",
    "DestinyDefinitionsPresentationDestinyPresentationNodeRequirementsBlock",
    "DestinyDefinitionsPresentationDestinyScoredPresentationNodeBaseDefinition",
    "DestinyDefinitionsProgressionDestinyProgressionLevelRequirementDefinition",
    "DestinyDefinitionsRecordsDestinyRecordCompletionBlock",
    "DestinyDefinitionsRecordsDestinyRecordDefinition",
    "DestinyDefinitionsRecordsDestinyRecordExpirationBlock",
    "DestinyDefinitionsRecordsDestinyRecordIntervalBlock",
    "DestinyDefinitionsRecordsDestinyRecordIntervalObjective",
    "DestinyDefinitionsRecordsDestinyRecordIntervalRewards",
    "DestinyDefinitionsRecordsDestinyRecordTitleBlock",
    "DestinyDefinitionsRecordsSchemaRecordStateBlock",
    "DestinyDefinitionsReportingDestinyReportReasonCategoryDefinition",
    "DestinyDefinitionsReportingDestinyReportReasonDefinition",
    "DestinyDefinitionsSeasonsDestinyEventCardDefinition",
    "DestinyDefinitionsSeasonsDestinyEventCardImages",
    "DestinyDefinitionsSeasonsDestinySeasonDefinition",
    "DestinyDefinitionsSeasonsDestinySeasonPassDefinition",
    "DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition",
    "DestinyDefinitionsSeasonsDestinySeasonPreviewImageDefinition",
    "DestinyDefinitionsSocialDestinySocialCommendationDefinition",
    "DestinyDefinitionsSocialDestinySocialCommendationNodeDefinition",
    "DestinyDefinitionsSocketsDestinyInsertPlugActionDefinition",
    "DestinyDefinitionsSocketsDestinyPlugSetDefinition",
    "DestinyDefinitionsSocketsDestinyPlugWhitelistEntryDefinition",
    "DestinyDefinitionsSocketsDestinySocketCategoryDefinition",
    "DestinyDefinitionsSocketsDestinySocketTypeDefinition",
    "DestinyDefinitionsSocketsDestinySocketTypeScalarMaterialRequirementEntry",
    "DestinyDefinitionsSourcesDestinyItemSourceDefinition",
    "DestinyDefinitionsTraitsDestinyTraitDefinition",
    "DestinyDefinitionsVendorsDestinyVendorLocationDefinition",
    "DestinyDestinyActivity",
    "DestinyDestinyActivityDifficultyTier",
    "DestinyDestinyActivityModeCategory",
    "DestinyDestinyActivityNavPointType",
    "DestinyDestinyAmmunitionType",
    "DestinyDestinyBreakerType",
    "DestinyDestinyClass",
    "DestinyDestinyCollectibleState",
    "DestinyDestinyComponentType",
    "DestinyDestinyEnergyType",
    "DestinyDestinyEquipItemResult",
    "DestinyDestinyEquipItemResults",
    "DestinyDestinyGamePrivacySetting",
    "DestinyDestinyGameVersions",
    "DestinyDestinyGatingScope",
    "DestinyDestinyGender",
    "DestinyDestinyGraphNodeState",
    "DestinyDestinyItemQuantity",
    "DestinyDestinyItemSortType",
    "DestinyDestinyItemSubType",
    "DestinyDestinyItemType",
    "DestinyDestinyJoinClosedReasons",
    "DestinyDestinyObjectiveGrantStyle",
    "DestinyDestinyObjectiveUiStyle",
    "DestinyDestinyPartyMemberStates",
    "DestinyDestinyPresentationDisplayStyle",
    "DestinyDestinyPresentationNodeState",
    "DestinyDestinyPresentationNodeType",
    "DestinyDestinyPresentationScreenStyle",
    "DestinyDestinyProgression",
    "DestinyDestinyProgressionResetEntry",
    "DestinyDestinyProgressionRewardItemAcquisitionBehavior",
    "DestinyDestinyProgressionRewardItemState",
    "DestinyDestinyProgressionScope",
    "DestinyDestinyProgressionStepDisplayEffect",
    "DestinyDestinyRace",
    "DestinyDestinyRecordState",
    "DestinyDestinyRecordToastStyle",
    "DestinyDestinyRecordValueStyle",
    "DestinyDestinyScope",
    "DestinyDestinySocketCategoryStyle",
    "DestinyDestinySocketVisibility",
    "DestinyDestinyStat",
    "DestinyDestinyStatAggregationType",
    "DestinyDestinyStatCategory",
    "DestinyDestinyTalentNode",
    "DestinyDestinyTalentNodeStatBlock",
    "DestinyDestinyTalentNodeState",
    "DestinyDestinyUnlockStatus",
    "DestinyDestinyUnlockValueUiStyle",
    "DestinyDestinyVendorFilter",
    "DestinyDestinyVendorInteractionRewardSelection",
    "DestinyDestinyVendorItemRefundPolicy",
    "DestinyDestinyVendorItemState",
    "DestinyDestinyVendorProgressionType",
    "DestinyDestinyVendorReplyType",
    "DestinyDyeReference",
    "DestinyEntitiesCharactersDestinyCharacterActivitiesComponent",
    "DestinyEntitiesCharactersDestinyCharacterComponent",
    "DestinyEntitiesCharactersDestinyCharacterProgressionComponent",
    "DestinyEntitiesCharactersDestinyCharacterRenderComponent",
    "DestinyEntitiesInventoryDestinyInventoryComponent",
    "DestinyEntitiesItemsDestinyItemComponent",
    "DestinyEntitiesItemsDestinyItemInstanceComponent",
    "DestinyEntitiesItemsDestinyItemInstanceEnergy",
    "DestinyEntitiesItemsDestinyItemObjectivesComponent",
    "DestinyEntitiesItemsDestinyItemPerksComponent",
    "DestinyEntitiesItemsDestinyItemRenderComponent",
    "DestinyEntitiesItemsDestinyItemSocketState",
    "DestinyEntitiesItemsDestinyItemSocketsComponent",
    "DestinyEntitiesItemsDestinyItemStatsComponent",
    "DestinyEntitiesItemsDestinyItemTalentGridComponent",
    "DestinyEntitiesProfilesDestinyProfileComponent",
    "DestinyEntitiesProfilesDestinyVendorReceiptsComponent",
    "DestinyEntitiesVendorsDestinyVendorCategoriesComponent",
    "DestinyEntitiesVendorsDestinyVendorCategory",
    "DestinyEntitiesVendorsDestinyVendorComponent",
    "DestinyEntitiesVendorsDestinyVendorSaleItemComponent",
    "DestinyEquipFailureReason",
    "DestinyEquippingItemBlockAttributes",
    "DestinyHistoricalStatsDefinitionsDestinyActivityModeType",
    "DestinyHistoricalStatsDefinitionsDestinyActivityModeTypeArray",
    "DestinyHistoricalStatsDefinitionsDestinyHistoricalStatsDefinition",
    "DestinyHistoricalStatsDefinitionsDestinyStatsCategoryType",
    "DestinyHistoricalStatsDefinitionsDestinyStatsGroupType",
    "DestinyHistoricalStatsDefinitionsDestinyStatsMergeMethod",
    "DestinyHistoricalStatsDefinitionsPeriodType",
    "DestinyHistoricalStatsDefinitionsPeriodTypeArray",
    "DestinyHistoricalStatsDefinitionsUnitType",
    "DestinyHistoricalStatsDestinyActivityHistoryResults",
    "DestinyHistoricalStatsDestinyAggregateActivityResults",
    "DestinyHistoricalStatsDestinyAggregateActivityStats",
    "DestinyHistoricalStatsDestinyClanAggregateStat",
    "DestinyHistoricalStatsDestinyHistoricalStatsAccountResult",
    "DestinyHistoricalStatsDestinyHistoricalStatsActivity",
    "DestinyHistoricalStatsDestinyHistoricalStatsByPeriod",
    "DestinyHistoricalStatsDestinyHistoricalStatsPerCharacter",
    "DestinyHistoricalStatsDestinyHistoricalStatsPeriodGroup",
    "DestinyHistoricalStatsDestinyHistoricalStatsResults",
    "DestinyHistoricalStatsDestinyHistoricalStatsValue",
    "DestinyHistoricalStatsDestinyHistoricalStatsValuePair",
    "DestinyHistoricalStatsDestinyHistoricalStatsWithMerged",
    "DestinyHistoricalStatsDestinyHistoricalWeaponStats",
    "DestinyHistoricalStatsDestinyHistoricalWeaponStatsData",
    "DestinyHistoricalStatsDestinyLeaderboard",
    "DestinyHistoricalStatsDestinyLeaderboardEntry",
    "DestinyHistoricalStatsDestinyLeaderboardResults",
    "DestinyHistoricalStatsDestinyPlayer",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportData",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportEntry",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportExtendedData",
    "DestinyHistoricalStatsDestinyPostGameCarnageReportTeamEntry",
    "DestinyItemBindStatus",
    "DestinyItemComponentSetOfint32",
    "DestinyItemComponentSetOfint64",
    "DestinyItemComponentSetOfuint32",
    "DestinyItemLocation",
    "DestinyItemPerkVisibility",
    "DestinyItemState",
    "DestinyMilestonesDestinyMilestone",
    "DestinyMilestonesDestinyMilestoneActivity",
    "DestinyMilestonesDestinyMilestoneActivityCompletionStatus",
    "DestinyMilestonesDestinyMilestoneActivityPhase",
    "DestinyMilestonesDestinyMilestoneActivityVariant",
    "DestinyMilestonesDestinyMilestoneChallengeActivity",
    "DestinyMilestonesDestinyMilestoneContent",
    "DestinyMilestonesDestinyMilestoneContentItemCategory",
    "DestinyMilestonesDestinyMilestoneQuest",
    "DestinyMilestonesDestinyMilestoneRewardCategory",
    "DestinyMilestonesDestinyMilestoneRewardEntry",
    "DestinyMilestonesDestinyMilestoneVendor",
    "DestinyMilestonesDestinyPublicMilestone",
    "DestinyMilestonesDestinyPublicMilestoneActivity",
    "DestinyMilestonesDestinyPublicMilestoneActivityVariant",
    "DestinyMilestonesDestinyPublicMilestoneChallenge",
    "DestinyMilestonesDestinyPublicMilestoneChallengeActivity",
    "DestinyMilestonesDestinyPublicMilestoneQuest",
    "DestinyMilestonesDestinyPublicMilestoneVendor",
    "DestinyMiscDestinyColor",
    "DestinyPerksDestinyPerkReference",
    "DestinyPlugAvailabilityMode",
    "DestinyPlugUiStyles",
    "DestinyProgressionDestinyFactionProgression",
    "DestinyQuestsDestinyObjectiveProgress",
    "DestinyQuestsDestinyQuestStatus",
    "DestinyReportingRequestsDestinyReportOffensePgcrRequest",
    "DestinyRequestsActionsDestinyActionRequest",
    "DestinyRequestsActionsDestinyCharacterActionRequest",
    "DestinyRequestsActionsDestinyInsertPlugsActionRequest",
    "DestinyRequestsActionsDestinyInsertPlugsFreeActionRequest",
    "DestinyRequestsActionsDestinyInsertPlugsRequestEntry",
    "DestinyRequestsActionsDestinyItemActionRequest",
    "DestinyRequestsActionsDestinyItemSetActionRequest",
    "DestinyRequestsActionsDestinyItemStateRequest",
    "DestinyRequestsActionsDestinyLoadoutActionRequest",
    "DestinyRequestsActionsDestinyLoadoutUpdateActionRequest",
    "DestinyRequestsActionsDestinyPostmasterTransferRequest",
    "DestinyRequestsActionsDestinySocketArrayType",
    "DestinyRequestsDestinyItemTransferRequest",
    "DestinyResponsesDestinyCharacterResponse",
    "DestinyResponsesDestinyCollectibleNodeDetailResponse",
    "DestinyResponsesDestinyErrorProfile",
    "DestinyResponsesDestinyItemChangeResponse",
    "DestinyResponsesDestinyItemResponse",
    "DestinyResponsesDestinyLinkedProfilesResponse",
    "DestinyResponsesDestinyProfileResponse",
    "DestinyResponsesDestinyProfileUserInfoCard",
    "DestinyResponsesDestinyPublicVendorsResponse",
    "DestinyResponsesDestinyVendorResponse",
    "DestinyResponsesDestinyVendorsResponse",
    "DestinyResponsesInventoryChangedResponse",
    "DestinyResponsesPersonalDestinyVendorSaleItemSetComponent",
    "DestinyResponsesPublicDestinyVendorSaleItemSetComponent",
    "DestinySocketPlugSources",
    "DestinySocketTypeActionType",
    "DestinySocketsDestinyItemPlug",
    "DestinySocketsDestinyItemPlugBase",
    "DestinySpecialItemType",
    "DestinyTierType",
    "DestinyTransferStatuses",
    "DestinyVendorDisplayCategorySortOrder",
    "DestinyVendorInteractionType",
    "DestinyVendorItemStatus",
    "DestinyVendorSaleItemSetComponentOfDestinyPublicVendorSaleItemComponent",
    "DestinyVendorSaleItemSetComponentOfDestinyVendorSaleItemComponent",
    "DestinyVendorsDestinyVendorReceipt",
    "DictionaryComponentResponseOfint32AndDestinyItemInstanceComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemObjectivesComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemPerksComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemPlugObjectivesComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemRenderComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemReusablePlugsComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemSocketsComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemStatsComponent",
    "DictionaryComponentResponseOfint32AndDestinyItemTalentGridComponent",
    "DictionaryComponentResponseOfint32AndDestinyVendorSaleItemComponent",
    "DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent",
    "DictionaryComponentResponseOfint64AndDestinyCharacterComponent",
    "DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent",
    "DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent",
    "DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent",
    "DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent",
    "DictionaryComponentResponseOfint64AndDestinyCraftablesComponent",
    "DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent",
    "DictionaryComponentResponseOfint64AndDestinyInventoryComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemInstanceComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemObjectivesComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemPerksComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemPlugObjectivesComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemRenderComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemReusablePlugsComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemSocketsComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemStatsComponent",
    "DictionaryComponentResponseOfint64AndDestinyItemTalentGridComponent",
    "DictionaryComponentResponseOfint64AndDestinyKiosksComponent",
    "DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent",
    "DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent",
    "DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent",
    "DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemInstanceComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemObjectivesComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemPerksComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemPlugComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemPlugObjectivesComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemRenderComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemReusablePlugsComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemSocketsComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemStatsComponent",
    "DictionaryComponentResponseOfuint32AndDestinyItemTalentGridComponent",
    "DictionaryComponentResponseOfuint32AndDestinyPublicVendorComponent",
    "DictionaryComponentResponseOfuint32AndDestinyVendorCategoriesComponent",
    "DictionaryComponentResponseOfuint32AndDestinyVendorComponent",
    "DictionaryComponentResponseOfuint32AndPersonalDestinyVendorSaleItemSetComponent",
    "DictionaryComponentResponseOfuint32AndPublicDestinyVendorSaleItemSetComponent",
    "EntitiesEntityActionResult",
    "ExceptionsPlatformErrorCodes",
    "FireteamFireteamDateRange",
    "FireteamFireteamMember",
    "FireteamFireteamPlatform",
    "FireteamFireteamPlatformInviteResult",
    "FireteamFireteamPublicSearchOption",
    "FireteamFireteamResponse",
    "FireteamFireteamSlotSearch",
    "FireteamFireteamSummary",
    "FireteamFireteamUserInfoCard",
    "ForumCommunityContentSortMode",
    "ForumForumMediaType",
    "ForumForumPostPopularity",
    "ForumForumPostSortEnum",
    "ForumForumRecruitmentDetail",
    "ForumForumRecruitmentIntensityLabel",
    "ForumForumRecruitmentToneLabel",
    "ForumForumTopicsCategoryFiltersEnum",
    "ForumForumTopicsQuickDateEnum",
    "ForumForumTopicsSortEnum",
    "ForumPollResponse",
    "ForumPollResult",
    "ForumPostResponse",
    "ForumPostSearchResponse",
    "ForumsForumFlagsEnum",
    "ForumsForumPostCategoryEnums",
    "GlobalAlert",
    "GlobalAlertLevel",
    "GlobalAlertType",
    "GroupsV2Capabilities",
    "GroupsV2ChatSecuritySetting",
    "GroupsV2ClanBanner",
    "GroupsV2GetGroupsForMemberResponse",
    "GroupsV2GroupAllianceStatus",
    "GroupsV2GroupApplicationListRequest",
    "GroupsV2GroupApplicationRequest",
    "GroupsV2GroupApplicationResolveState",
    "GroupsV2GroupApplicationResponse",
    "GroupsV2GroupBan",
    "GroupsV2GroupBanRequest",
    "GroupsV2GroupDateRange",
    "GroupsV2GroupEditAction",
    "GroupsV2GroupFeatures",
    "GroupsV2GroupHomepage",
    "GroupsV2GroupMember",
    "GroupsV2GroupMemberApplication",
    "GroupsV2GroupMemberCountFilter",
    "GroupsV2GroupMemberLeaveResult",
    "GroupsV2GroupMembership",
    "GroupsV2GroupMembershipBase",
    "GroupsV2GroupMembershipSearchResponse",
    "GroupsV2GroupNameSearchRequest",
    "GroupsV2GroupOptionalConversation",
    "GroupsV2GroupOptionalConversationAddRequest",
    "GroupsV2GroupOptionalConversationEditRequest",
    "GroupsV2GroupOptionsEditAction",
    "GroupsV2GroupPostPublicity",
    "GroupsV2GroupPotentialMember",
    "GroupsV2GroupPotentialMemberStatus",
    "GroupsV2GroupPotentialMembership",
    "GroupsV2GroupPotentialMembershipSearchResponse",
    "GroupsV2GroupQuery",
    "GroupsV2GroupResponse",
    "GroupsV2GroupSearchResponse",
    "GroupsV2GroupSortBy",
    "GroupsV2GroupType",
    "GroupsV2GroupUserBase",
    "GroupsV2GroupUserInfoCard",
    "GroupsV2GroupV2",
    "GroupsV2GroupV2Card",
    "GroupsV2GroupV2ClanInfo",
    "GroupsV2GroupV2ClanInfoAndInvestment",
    "GroupsV2GroupsForMemberFilter",
    "GroupsV2HostGuidedGamesPermissionLevel",
    "GroupsV2MembershipOption",
    "GroupsV2RuntimeGroupMemberType",
    "IgnoresIgnoreLength",
    "IgnoresIgnoreResponse",
    "IgnoresIgnoreStatus",
    "InterpolationInterpolationPoint",
    "InterpolationInterpolationPointFloat",
    "LinksHyperlinkReference",
    "OauthScope",
    "QueriesPagedQuery",
    "QueriesSearchResult",
    "Schema1",
    "Schema10",
    "Schema100",
    "Schema101",
    "Schema102",
    "Schema103",
    "Schema104",
    "Schema105",
    "Schema106",
    "Schema107",
    "Schema108",
    "Schema109",
    "Schema11",
    "Schema110",
    "Schema111",
    "Schema112",
    "Schema113",
    "Schema114",
    "Schema115",
    "Schema116",
    "Schema117",
    "Schema118",
    "Schema12",
    "Schema13",
    "Schema14",
    "Schema15",
    "Schema16",
    "Schema17",
    "Schema18",
    "Schema19",
    "Schema2",
    "Schema20",
    "Schema21",
    "Schema22",
    "Schema23",
    "Schema24",
    "Schema25",
    "Schema26",
    "Schema27",
    "Schema28",
    "Schema29",
    "Schema3",
    "Schema30",
    "Schema31",
    "Schema32",
    "Schema33",
    "Schema34",
    "Schema35",
    "Schema36",
    "Schema37",
    "Schema38",
    "Schema39",
    "Schema4",
    "Schema40",
    "Schema41",
    "Schema42",
    "Schema43",
    "Schema44",
    "Schema45",
    "Schema46",
    "Schema47",
    "Schema48",
    "Schema49",
    "Schema5",
    "Schema50",
    "Schema51",
    "Schema52",
    "Schema53",
    "Schema54",
    "Schema55",
    "Schema56",
    "Schema57",
    "Schema58",
    "Schema59",
    "Schema6",
    "Schema60",
    "Schema61",
    "Schema62",
    "Schema63",
    "Schema64",
    "Schema65",
    "Schema66",
    "Schema67",
    "Schema68",
    "Schema69",
    "Schema7",
    "Schema70",
    "Schema71",
    "Schema72",
    "Schema73",
    "Schema74",
    "Schema75",
    "Schema76",
    "Schema77",
    "Schema78",
    "Schema79",
    "Schema8",
    "Schema80",
    "Schema81",
    "Schema82",
    "Schema83",
    "Schema84",
    "Schema85",
    "Schema86",
    "Schema87",
    "Schema88",
    "Schema89",
    "Schema9",
    "Schema90",
    "Schema91",
    "Schema92",
    "Schema93",
    "Schema94",
    "Schema95",
    "Schema96",
    "Schema97",
    "Schema98",
    "Schema99",
    "SearchResultOfContentItemPublicContract",
    "SearchResultOfDestinyEntitySearchResultItem",
    "SearchResultOfFireteamResponse",
    "SearchResultOfFireteamSummary",
    "SearchResultOfGroupBan",
    "SearchResultOfGroupMember",
    "SearchResultOfGroupMemberApplication",
    "SearchResultOfGroupMembership",
    "SearchResultOfGroupPotentialMembership",
    "SearchResultOfGroupV2Card",
    "SearchResultOfPostResponse",
    "SearchResultOfTrendingEntry",
    "SingleComponentResponseOfDestinyCharacterActivitiesComponent",
    "SingleComponentResponseOfDestinyCharacterComponent",
    "SingleComponentResponseOfDestinyCharacterProgressionComponent",
    "SingleComponentResponseOfDestinyCharacterRecordsComponent",
    "SingleComponentResponseOfDestinyCharacterRenderComponent",
    "SingleComponentResponseOfDestinyCollectiblesComponent",
    "SingleComponentResponseOfDestinyCurrenciesComponent",
    "SingleComponentResponseOfDestinyInventoryComponent",
    "SingleComponentResponseOfDestinyItemComponent",
    "SingleComponentResponseOfDestinyItemInstanceComponent",
    "SingleComponentResponseOfDestinyItemObjectivesComponent",
    "SingleComponentResponseOfDestinyItemPerksComponent",
    "SingleComponentResponseOfDestinyItemPlugObjectivesComponent",
    "SingleComponentResponseOfDestinyItemRenderComponent",
    "SingleComponentResponseOfDestinyItemReusablePlugsComponent",
    "SingleComponentResponseOfDestinyItemSocketsComponent",
    "SingleComponentResponseOfDestinyItemStatsComponent",
    "SingleComponentResponseOfDestinyItemTalentGridComponent",
    "SingleComponentResponseOfDestinyKiosksComponent",
    "SingleComponentResponseOfDestinyLoadoutsComponent",
    "SingleComponentResponseOfDestinyMetricsComponent",
    "SingleComponentResponseOfDestinyPlatformSilverComponent",
    "SingleComponentResponseOfDestinyPlugSetsComponent",
    "SingleComponentResponseOfDestinyPresentationNodesComponent",
    "SingleComponentResponseOfDestinyProfileCollectiblesComponent",
    "SingleComponentResponseOfDestinyProfileComponent",
    "SingleComponentResponseOfDestinyProfileProgressionComponent",
    "SingleComponentResponseOfDestinyProfileRecordsComponent",
    "SingleComponentResponseOfDestinyProfileTransitoryComponent",
    "SingleComponentResponseOfDestinySocialCommendationsComponent",
    "SingleComponentResponseOfDestinyStringVariablesComponent",
    "SingleComponentResponseOfDestinyVendorCategoriesComponent",
    "SingleComponentResponseOfDestinyVendorComponent",
    "SingleComponentResponseOfDestinyVendorGroupComponent",
    "SingleComponentResponseOfDestinyVendorReceiptsComponent",
    "SocialFriendsBungieFriend",
    "SocialFriendsBungieFriendListResponse",
    "SocialFriendsBungieFriendRequestListResponse",
    "SocialFriendsFriendRelationshipState",
    "SocialFriendsPlatformFriend",
    "SocialFriendsPlatformFriendResponse",
    "SocialFriendsPlatformFriendType",
    "SocialFriendsPresenceOnlineStateFlags",
    "SocialFriendsPresenceStatus",
    "StreamInfo",
    "StreamingDropStateEnum",
    "TagsModelsContractsTagResponse",
    "TokensBungieRewardDisplay",
    "TokensCollectibleDefinitions",
    "TokensPartnerOfferClaimRequest",
    "TokensPartnerOfferHistoryResponse",
    "TokensPartnerOfferSkuHistoryResponse",
    "TokensPartnerRewardHistoryResponse",
    "TokensRewardAvailabilityModel",
    "TokensRewardDisplayProperties",
    "TokensTwitchDropHistoryResponse",
    "TokensUserRewardAvailabilityModel",
    "TrendingTrendingCategories",
    "TrendingTrendingCategory",
    "TrendingTrendingDetail",
    "TrendingTrendingEntry",
    "TrendingTrendingEntryCommunityCreation",
    "TrendingTrendingEntryDestinyActivity",
    "TrendingTrendingEntryDestinyItem",
    "TrendingTrendingEntryDestinyRitual",
    "TrendingTrendingEntryNews",
    "TrendingTrendingEntrySupportArticle",
    "TrendingTrendingEntryType",
    "UserCrossSaveUserMembership",
    "UserEMailSettingLocalization",
    "UserEMailSettingSubscriptionLocalization",
    "UserEmailOptInDefinition",
    "UserEmailSettings",
    "UserEmailSubscriptionDefinition",
    "UserEmailViewDefinition",
    "UserEmailViewDefinitionSetting",
    "UserExactSearchRequest",
    "UserGeneralUser",
    "UserHardLinkedUserMembership",
    "UserModelsGetCredentialTypesForAccountResponse",
    "UserOptInFlags",
    "UserUserInfoCard",
    "UserUserMembership",
    "UserUserMembershipData",
    "UserUserSearchPrefixRequest",
    "UserUserSearchResponse",
    "UserUserSearchResponseDetail",
    "UserUserToUserContext",
]
