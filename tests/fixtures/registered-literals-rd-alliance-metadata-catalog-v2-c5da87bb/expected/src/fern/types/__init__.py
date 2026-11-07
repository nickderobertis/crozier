



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .creator import Creator
    from .data_type import DataType
    from .date_range import DateRange
    from .endorsement import Endorsement
    from .endorsement_related_entities_item import EndorsementRelatedEntitiesItem
    from .endorsement_related_entities_item_data import EndorsementRelatedEntitiesItemData
    from .endorsement_related_entities_item_role import EndorsementRelatedEntitiesItemRole
    from .endorsement_valid import EndorsementValid
    from .identifier import Identifier
    from .inv_relation import InvRelation
    from .location import Location
    from .mapping import Mapping
    from .mapping_related_entities_item import MappingRelatedEntitiesItem
    from .mapping_related_entities_item_data import MappingRelatedEntitiesItemData
    from .mapping_related_entities_item_role import MappingRelatedEntitiesItemRole
    from .mapping_versions_item import MappingVersionsItem
    from .metadata_scheme import MetadataScheme
    from .metadata_scheme_related_entities_item import MetadataSchemeRelatedEntitiesItem
    from .metadata_scheme_related_entities_item_data import MetadataSchemeRelatedEntitiesItemData
    from .metadata_scheme_related_entities_item_role import MetadataSchemeRelatedEntitiesItemRole
    from .metadata_scheme_versions_item import MetadataSchemeVersionsItem
    from .metadata_scheme_versions_item_samples_item import MetadataSchemeVersionsItemSamplesItem
    from .metadata_scheme_versions_item_valid import MetadataSchemeVersionsItemValid
    from .mscid import Mscid
    from .namespace import Namespace
    from .organization import Organization
    from .organization_related_entities_item import OrganizationRelatedEntitiesItem
    from .organization_related_entities_item_data import OrganizationRelatedEntitiesItemData
    from .organization_related_entities_item_role import OrganizationRelatedEntitiesItemRole
    from .page import Page
    from .patch_inv_relation import PatchInvRelation
    from .patch_inv_relation_item import PatchInvRelationItem
    from .patch_inv_relation_item_one import PatchInvRelationItemOne
    from .patch_inv_relation_item_one_op import PatchInvRelationItemOneOp
    from .patch_inv_relation_item_zero import PatchInvRelationItemZero
    from .patch_inv_relation_item_zero_op import PatchInvRelationItemZeroOp
    from .patch_inv_relation_item_zero_path import PatchInvRelationItemZeroPath
    from .patch_relation import PatchRelation
    from .patch_relation_item import PatchRelationItem
    from .patch_relation_item_one import PatchRelationItemOne
    from .patch_relation_item_one_op import PatchRelationItemOneOp
    from .patch_relation_item_zero import PatchRelationItemZero
    from .patch_relation_item_zero_op import PatchRelationItemZeroOp
    from .patch_relation_item_zero_path import PatchRelationItemZeroPath
    from .qa import Qa
    from .qa_meta import QaMeta
    from .qa_meta_conformance import QaMetaConformance
    from .relation import Relation
    from .response import Response
    from .response_item_data_type import ResponseItemDataType
    from .response_item_endorsement import ResponseItemEndorsement
    from .response_item_inv_relation import ResponseItemInvRelation
    from .response_item_mapping import ResponseItemMapping
    from .response_item_metadata_scheme import ResponseItemMetadataScheme
    from .response_item_organization import ResponseItemOrganization
    from .response_item_relation import ResponseItemRelation
    from .response_item_thesaurus_concept import ResponseItemThesaurusConcept
    from .response_item_thesaurus_concept_scheme import ResponseItemThesaurusConceptScheme
    from .response_item_tool import ResponseItemTool
    from .response_item_vocabulary_term import ResponseItemVocabularyTerm
    from .response_page_data_type import ResponsePageDataType
    from .response_page_data_type_data import ResponsePageDataTypeData
    from .response_page_endorsement import ResponsePageEndorsement
    from .response_page_endorsement_data import ResponsePageEndorsementData
    from .response_page_inv_relation import ResponsePageInvRelation
    from .response_page_inv_relation_data import ResponsePageInvRelationData
    from .response_page_mapping import ResponsePageMapping
    from .response_page_mapping_data import ResponsePageMappingData
    from .response_page_metadata_scheme import ResponsePageMetadataScheme
    from .response_page_metadata_scheme_data import ResponsePageMetadataSchemeData
    from .response_page_organization import ResponsePageOrganization
    from .response_page_organization_data import ResponsePageOrganizationData
    from .response_page_relation import ResponsePageRelation
    from .response_page_relation_data import ResponsePageRelationData
    from .response_page_thesaurus_concept import ResponsePageThesaurusConcept
    from .response_page_thesaurus_concept_data import ResponsePageThesaurusConceptData
    from .response_page_tool import ResponsePageTool
    from .response_page_tool_data import ResponsePageToolData
    from .response_page_vocabulary_term import ResponsePageVocabularyTerm
    from .response_page_vocabulary_term_data import ResponsePageVocabularyTermData
    from .response_password import ResponsePassword
    from .response_success_data_type import ResponseSuccessDataType
    from .response_success_endorsement import ResponseSuccessEndorsement
    from .response_success_inv_relation import ResponseSuccessInvRelation
    from .response_success_mapping import ResponseSuccessMapping
    from .response_success_metadata_scheme import ResponseSuccessMetadataScheme
    from .response_success_organization import ResponseSuccessOrganization
    from .response_success_relation import ResponseSuccessRelation
    from .response_success_tool import ResponseSuccessTool
    from .response_success_vocabulary_term import ResponseSuccessVocabularyTerm
    from .slug import Slug
    from .submission_response_failure import SubmissionResponseFailure
    from .submission_response_failure_error import SubmissionResponseFailureError
    from .submission_response_failure_error_errors_item import SubmissionResponseFailureErrorErrorsItem
    from .thesaurus_base import ThesaurusBase
    from .thesaurus_base_context import ThesaurusBaseContext
    from .thesaurus_base_skos_pref_label_item import ThesaurusBaseSkosPrefLabelItem
    from .thesaurus_concept import ThesaurusConcept
    from .thesaurus_concept_broader import ThesaurusConceptBroader
    from .thesaurus_concept_broader_skos_broader_item import ThesaurusConceptBroaderSkosBroaderItem
    from .thesaurus_concept_broader_skos_top_concept_of_item import ThesaurusConceptBroaderSkosTopConceptOfItem
    from .thesaurus_concept_narrower import ThesaurusConceptNarrower
    from .thesaurus_concept_narrower_skos_narrower_item import ThesaurusConceptNarrowerSkosNarrowerItem
    from .thesaurus_concept_scheme import ThesaurusConceptScheme
    from .thesaurus_concept_scheme_skos_has_top_concept_item import ThesaurusConceptSchemeSkosHasTopConceptItem
    from .tool import Tool
    from .tool_related_entities_item import ToolRelatedEntitiesItem
    from .tool_related_entities_item_data import ToolRelatedEntitiesItemData
    from .tool_related_entities_item_role import ToolRelatedEntitiesItemRole
    from .tool_versions_item import ToolVersionsItem
    from .uri import Uri
    from .vocabulary_term import VocabularyTerm
    from .vocabulary_term_applies_item import VocabularyTermAppliesItem
    from .vocabulary_term_new import VocabularyTermNew
    from .vocabulary_term_old import VocabularyTermOld
_dynamic_imports: typing.Dict[str, str] = {
    "Creator": ".creator",
    "DataType": ".data_type",
    "DateRange": ".date_range",
    "Endorsement": ".endorsement",
    "EndorsementRelatedEntitiesItem": ".endorsement_related_entities_item",
    "EndorsementRelatedEntitiesItemData": ".endorsement_related_entities_item_data",
    "EndorsementRelatedEntitiesItemRole": ".endorsement_related_entities_item_role",
    "EndorsementValid": ".endorsement_valid",
    "Identifier": ".identifier",
    "InvRelation": ".inv_relation",
    "Location": ".location",
    "Mapping": ".mapping",
    "MappingRelatedEntitiesItem": ".mapping_related_entities_item",
    "MappingRelatedEntitiesItemData": ".mapping_related_entities_item_data",
    "MappingRelatedEntitiesItemRole": ".mapping_related_entities_item_role",
    "MappingVersionsItem": ".mapping_versions_item",
    "MetadataScheme": ".metadata_scheme",
    "MetadataSchemeRelatedEntitiesItem": ".metadata_scheme_related_entities_item",
    "MetadataSchemeRelatedEntitiesItemData": ".metadata_scheme_related_entities_item_data",
    "MetadataSchemeRelatedEntitiesItemRole": ".metadata_scheme_related_entities_item_role",
    "MetadataSchemeVersionsItem": ".metadata_scheme_versions_item",
    "MetadataSchemeVersionsItemSamplesItem": ".metadata_scheme_versions_item_samples_item",
    "MetadataSchemeVersionsItemValid": ".metadata_scheme_versions_item_valid",
    "Mscid": ".mscid",
    "Namespace": ".namespace",
    "Organization": ".organization",
    "OrganizationRelatedEntitiesItem": ".organization_related_entities_item",
    "OrganizationRelatedEntitiesItemData": ".organization_related_entities_item_data",
    "OrganizationRelatedEntitiesItemRole": ".organization_related_entities_item_role",
    "Page": ".page",
    "PatchInvRelation": ".patch_inv_relation",
    "PatchInvRelationItem": ".patch_inv_relation_item",
    "PatchInvRelationItemOne": ".patch_inv_relation_item_one",
    "PatchInvRelationItemOneOp": ".patch_inv_relation_item_one_op",
    "PatchInvRelationItemZero": ".patch_inv_relation_item_zero",
    "PatchInvRelationItemZeroOp": ".patch_inv_relation_item_zero_op",
    "PatchInvRelationItemZeroPath": ".patch_inv_relation_item_zero_path",
    "PatchRelation": ".patch_relation",
    "PatchRelationItem": ".patch_relation_item",
    "PatchRelationItemOne": ".patch_relation_item_one",
    "PatchRelationItemOneOp": ".patch_relation_item_one_op",
    "PatchRelationItemZero": ".patch_relation_item_zero",
    "PatchRelationItemZeroOp": ".patch_relation_item_zero_op",
    "PatchRelationItemZeroPath": ".patch_relation_item_zero_path",
    "Qa": ".qa",
    "QaMeta": ".qa_meta",
    "QaMetaConformance": ".qa_meta_conformance",
    "Relation": ".relation",
    "Response": ".response",
    "ResponseItemDataType": ".response_item_data_type",
    "ResponseItemEndorsement": ".response_item_endorsement",
    "ResponseItemInvRelation": ".response_item_inv_relation",
    "ResponseItemMapping": ".response_item_mapping",
    "ResponseItemMetadataScheme": ".response_item_metadata_scheme",
    "ResponseItemOrganization": ".response_item_organization",
    "ResponseItemRelation": ".response_item_relation",
    "ResponseItemThesaurusConcept": ".response_item_thesaurus_concept",
    "ResponseItemThesaurusConceptScheme": ".response_item_thesaurus_concept_scheme",
    "ResponseItemTool": ".response_item_tool",
    "ResponseItemVocabularyTerm": ".response_item_vocabulary_term",
    "ResponsePageDataType": ".response_page_data_type",
    "ResponsePageDataTypeData": ".response_page_data_type_data",
    "ResponsePageEndorsement": ".response_page_endorsement",
    "ResponsePageEndorsementData": ".response_page_endorsement_data",
    "ResponsePageInvRelation": ".response_page_inv_relation",
    "ResponsePageInvRelationData": ".response_page_inv_relation_data",
    "ResponsePageMapping": ".response_page_mapping",
    "ResponsePageMappingData": ".response_page_mapping_data",
    "ResponsePageMetadataScheme": ".response_page_metadata_scheme",
    "ResponsePageMetadataSchemeData": ".response_page_metadata_scheme_data",
    "ResponsePageOrganization": ".response_page_organization",
    "ResponsePageOrganizationData": ".response_page_organization_data",
    "ResponsePageRelation": ".response_page_relation",
    "ResponsePageRelationData": ".response_page_relation_data",
    "ResponsePageThesaurusConcept": ".response_page_thesaurus_concept",
    "ResponsePageThesaurusConceptData": ".response_page_thesaurus_concept_data",
    "ResponsePageTool": ".response_page_tool",
    "ResponsePageToolData": ".response_page_tool_data",
    "ResponsePageVocabularyTerm": ".response_page_vocabulary_term",
    "ResponsePageVocabularyTermData": ".response_page_vocabulary_term_data",
    "ResponsePassword": ".response_password",
    "ResponseSuccessDataType": ".response_success_data_type",
    "ResponseSuccessEndorsement": ".response_success_endorsement",
    "ResponseSuccessInvRelation": ".response_success_inv_relation",
    "ResponseSuccessMapping": ".response_success_mapping",
    "ResponseSuccessMetadataScheme": ".response_success_metadata_scheme",
    "ResponseSuccessOrganization": ".response_success_organization",
    "ResponseSuccessRelation": ".response_success_relation",
    "ResponseSuccessTool": ".response_success_tool",
    "ResponseSuccessVocabularyTerm": ".response_success_vocabulary_term",
    "Slug": ".slug",
    "SubmissionResponseFailure": ".submission_response_failure",
    "SubmissionResponseFailureError": ".submission_response_failure_error",
    "SubmissionResponseFailureErrorErrorsItem": ".submission_response_failure_error_errors_item",
    "ThesaurusBase": ".thesaurus_base",
    "ThesaurusBaseContext": ".thesaurus_base_context",
    "ThesaurusBaseSkosPrefLabelItem": ".thesaurus_base_skos_pref_label_item",
    "ThesaurusConcept": ".thesaurus_concept",
    "ThesaurusConceptBroader": ".thesaurus_concept_broader",
    "ThesaurusConceptBroaderSkosBroaderItem": ".thesaurus_concept_broader_skos_broader_item",
    "ThesaurusConceptBroaderSkosTopConceptOfItem": ".thesaurus_concept_broader_skos_top_concept_of_item",
    "ThesaurusConceptNarrower": ".thesaurus_concept_narrower",
    "ThesaurusConceptNarrowerSkosNarrowerItem": ".thesaurus_concept_narrower_skos_narrower_item",
    "ThesaurusConceptScheme": ".thesaurus_concept_scheme",
    "ThesaurusConceptSchemeSkosHasTopConceptItem": ".thesaurus_concept_scheme_skos_has_top_concept_item",
    "Tool": ".tool",
    "ToolRelatedEntitiesItem": ".tool_related_entities_item",
    "ToolRelatedEntitiesItemData": ".tool_related_entities_item_data",
    "ToolRelatedEntitiesItemRole": ".tool_related_entities_item_role",
    "ToolVersionsItem": ".tool_versions_item",
    "Uri": ".uri",
    "VocabularyTerm": ".vocabulary_term",
    "VocabularyTermAppliesItem": ".vocabulary_term_applies_item",
    "VocabularyTermNew": ".vocabulary_term_new",
    "VocabularyTermOld": ".vocabulary_term_old",
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
    "Creator",
    "DataType",
    "DateRange",
    "Endorsement",
    "EndorsementRelatedEntitiesItem",
    "EndorsementRelatedEntitiesItemData",
    "EndorsementRelatedEntitiesItemRole",
    "EndorsementValid",
    "Identifier",
    "InvRelation",
    "Location",
    "Mapping",
    "MappingRelatedEntitiesItem",
    "MappingRelatedEntitiesItemData",
    "MappingRelatedEntitiesItemRole",
    "MappingVersionsItem",
    "MetadataScheme",
    "MetadataSchemeRelatedEntitiesItem",
    "MetadataSchemeRelatedEntitiesItemData",
    "MetadataSchemeRelatedEntitiesItemRole",
    "MetadataSchemeVersionsItem",
    "MetadataSchemeVersionsItemSamplesItem",
    "MetadataSchemeVersionsItemValid",
    "Mscid",
    "Namespace",
    "Organization",
    "OrganizationRelatedEntitiesItem",
    "OrganizationRelatedEntitiesItemData",
    "OrganizationRelatedEntitiesItemRole",
    "Page",
    "PatchInvRelation",
    "PatchInvRelationItem",
    "PatchInvRelationItemOne",
    "PatchInvRelationItemOneOp",
    "PatchInvRelationItemZero",
    "PatchInvRelationItemZeroOp",
    "PatchInvRelationItemZeroPath",
    "PatchRelation",
    "PatchRelationItem",
    "PatchRelationItemOne",
    "PatchRelationItemOneOp",
    "PatchRelationItemZero",
    "PatchRelationItemZeroOp",
    "PatchRelationItemZeroPath",
    "Qa",
    "QaMeta",
    "QaMetaConformance",
    "Relation",
    "Response",
    "ResponseItemDataType",
    "ResponseItemEndorsement",
    "ResponseItemInvRelation",
    "ResponseItemMapping",
    "ResponseItemMetadataScheme",
    "ResponseItemOrganization",
    "ResponseItemRelation",
    "ResponseItemThesaurusConcept",
    "ResponseItemThesaurusConceptScheme",
    "ResponseItemTool",
    "ResponseItemVocabularyTerm",
    "ResponsePageDataType",
    "ResponsePageDataTypeData",
    "ResponsePageEndorsement",
    "ResponsePageEndorsementData",
    "ResponsePageInvRelation",
    "ResponsePageInvRelationData",
    "ResponsePageMapping",
    "ResponsePageMappingData",
    "ResponsePageMetadataScheme",
    "ResponsePageMetadataSchemeData",
    "ResponsePageOrganization",
    "ResponsePageOrganizationData",
    "ResponsePageRelation",
    "ResponsePageRelationData",
    "ResponsePageThesaurusConcept",
    "ResponsePageThesaurusConceptData",
    "ResponsePageTool",
    "ResponsePageToolData",
    "ResponsePageVocabularyTerm",
    "ResponsePageVocabularyTermData",
    "ResponsePassword",
    "ResponseSuccessDataType",
    "ResponseSuccessEndorsement",
    "ResponseSuccessInvRelation",
    "ResponseSuccessMapping",
    "ResponseSuccessMetadataScheme",
    "ResponseSuccessOrganization",
    "ResponseSuccessRelation",
    "ResponseSuccessTool",
    "ResponseSuccessVocabularyTerm",
    "Slug",
    "SubmissionResponseFailure",
    "SubmissionResponseFailureError",
    "SubmissionResponseFailureErrorErrorsItem",
    "ThesaurusBase",
    "ThesaurusBaseContext",
    "ThesaurusBaseSkosPrefLabelItem",
    "ThesaurusConcept",
    "ThesaurusConceptBroader",
    "ThesaurusConceptBroaderSkosBroaderItem",
    "ThesaurusConceptBroaderSkosTopConceptOfItem",
    "ThesaurusConceptNarrower",
    "ThesaurusConceptNarrowerSkosNarrowerItem",
    "ThesaurusConceptScheme",
    "ThesaurusConceptSchemeSkosHasTopConceptItem",
    "Tool",
    "ToolRelatedEntitiesItem",
    "ToolRelatedEntitiesItemData",
    "ToolRelatedEntitiesItemRole",
    "ToolVersionsItem",
    "Uri",
    "VocabularyTerm",
    "VocabularyTermAppliesItem",
    "VocabularyTermNew",
    "VocabularyTermOld",
]
