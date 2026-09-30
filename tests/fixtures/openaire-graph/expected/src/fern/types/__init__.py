



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_right import AccessRight
    from .access_right_open_access_route import AccessRightOpenAccessRoute
    from .affiliation import Affiliation
    from .alternate_identifier import AlternateIdentifier
    from .apc import Apc
    from .api_organization import ApiOrganization
    from .api_person import ApiPerson
    from .api_project import ApiProject
    from .api_result import ApiResult
    from .api_result_open_access_color import ApiResultOpenAccessColor
    from .author import Author
    from .author_pid import AuthorPid
    from .author_pid_scheme_value import AuthorPidSchemeValue
    from .best_access_right import BestAccessRight
    from .bip_indicators import BipIndicators
    from .category import Category
    from .cf_hb_key_value import CfHbKeyValue
    from .code_label import CodeLabel
    from .community_instance import CommunityInstance
    from .concept import Concept
    from .container import Container
    from .context import Context
    from .country import Country
    from .data_source_search_response import DataSourceSearchResponse
    from .datasource import Datasource
    from .datasource_pid import DatasourcePid
    from .datasource_scheme_value import DatasourceSchemeValue
    from .entity import Entity
    from .error_response import ErrorResponse
    from .funder import Funder
    from .fundings import Fundings
    from .geo_location import GeoLocation
    from .granted import Granted
    from .graph_result import GraphResult
    from .graph_result_open_access_color import GraphResultOpenAccessColor
    from .identifier import Identifier
    from .indicator import Indicator
    from .instance import Instance
    from .language import Language
    from .measure import Measure
    from .node import Node
    from .organization_pid import OrganizationPid
    from .organization_search_response import OrganizationSearchResponse
    from .person_topic import PersonTopic
    from .programme import Programme
    from .project import Project
    from .project_pid import ProjectPid
    from .project_search_response import ProjectSearchResponse
    from .provenance import Provenance
    from .rel_type import RelType
    from .relation import Relation
    from .research_products_search_response import ResearchProductsSearchResponse
    from .research_products_search_response_v2 import ResearchProductsSearchResponseV2
    from .result_country import ResultCountry
    from .result_pid import ResultPid
    from .search_header import SearchHeader
    from .search_header_debug import SearchHeaderDebug
    from .search_response import SearchResponse
    from .search_response_relation import SearchResponseRelation
    from .skg_if_json_ld_response import SkgIfJsonLdResponse
    from .skg_if_next_page import SkgIfNextPage
    from .skg_if_part_of import SkgIfPartOf
    from .skg_if_prev_page import SkgIfPrevPage
    from .skg_if_response_meta import SkgIfResponseMeta
    from .solr_query_params import SolrQueryParams
    from .sort_clause import SortClause
    from .sort_clause_order import SortClauseOrder
    from .subject import Subject
    from .subject_scheme_value import SubjectSchemeValue
    from .usage_counts import UsageCounts
    from .xml_child_result import XmlChildResult
    from .xml_children import XmlChildren
    from .xml_classification import XmlClassification
    from .xml_classified_value import XmlClassifiedValue
    from .xml_collected_from import XmlCollectedFrom
    from .xml_context import XmlContext
    from .xml_contract_type import XmlContractType
    from .xml_country import XmlCountry
    from .xml_creator import XmlCreator
    from .xml_data_info import XmlDataInfo
    from .xml_entity import XmlEntity
    from .xml_funder import XmlFunder
    from .xml_funding_level import XmlFundingLevel
    from .xml_funding_level_parent import XmlFundingLevelParent
    from .xml_funding_tree import XmlFundingTree
    from .xml_header import XmlHeader
    from .xml_instance import XmlInstance
    from .xml_journal_element import XmlJournalElement
    from .xml_measure import XmlMeasure
    from .xml_metadata import XmlMetadata
    from .xml_pid import XmlPid
    from .xml_project import XmlProject
    from .xml_provenance_action import XmlProvenanceAction
    from .xml_publication_result import XmlPublicationResult
    from .xml_rel import XmlRel
    from .xml_rel_to import XmlRelTo
    from .xml_rels import XmlRels
    from .xml_response import XmlResponse
    from .xml_result import XmlResult
    from .xml_result_header import XmlResultHeader
    from .xml_results import XmlResults
    from .xml_subject import XmlSubject
    from .xml_web_resource import XmlWebResource
_dynamic_imports: typing.Dict[str, str] = {
    "AccessRight": ".access_right",
    "AccessRightOpenAccessRoute": ".access_right_open_access_route",
    "Affiliation": ".affiliation",
    "AlternateIdentifier": ".alternate_identifier",
    "Apc": ".apc",
    "ApiOrganization": ".api_organization",
    "ApiPerson": ".api_person",
    "ApiProject": ".api_project",
    "ApiResult": ".api_result",
    "ApiResultOpenAccessColor": ".api_result_open_access_color",
    "Author": ".author",
    "AuthorPid": ".author_pid",
    "AuthorPidSchemeValue": ".author_pid_scheme_value",
    "BestAccessRight": ".best_access_right",
    "BipIndicators": ".bip_indicators",
    "Category": ".category",
    "CfHbKeyValue": ".cf_hb_key_value",
    "CodeLabel": ".code_label",
    "CommunityInstance": ".community_instance",
    "Concept": ".concept",
    "Container": ".container",
    "Context": ".context",
    "Country": ".country",
    "DataSourceSearchResponse": ".data_source_search_response",
    "Datasource": ".datasource",
    "DatasourcePid": ".datasource_pid",
    "DatasourceSchemeValue": ".datasource_scheme_value",
    "Entity": ".entity",
    "ErrorResponse": ".error_response",
    "Funder": ".funder",
    "Fundings": ".fundings",
    "GeoLocation": ".geo_location",
    "Granted": ".granted",
    "GraphResult": ".graph_result",
    "GraphResultOpenAccessColor": ".graph_result_open_access_color",
    "Identifier": ".identifier",
    "Indicator": ".indicator",
    "Instance": ".instance",
    "Language": ".language",
    "Measure": ".measure",
    "Node": ".node",
    "OrganizationPid": ".organization_pid",
    "OrganizationSearchResponse": ".organization_search_response",
    "PersonTopic": ".person_topic",
    "Programme": ".programme",
    "Project": ".project",
    "ProjectPid": ".project_pid",
    "ProjectSearchResponse": ".project_search_response",
    "Provenance": ".provenance",
    "RelType": ".rel_type",
    "Relation": ".relation",
    "ResearchProductsSearchResponse": ".research_products_search_response",
    "ResearchProductsSearchResponseV2": ".research_products_search_response_v2",
    "ResultCountry": ".result_country",
    "ResultPid": ".result_pid",
    "SearchHeader": ".search_header",
    "SearchHeaderDebug": ".search_header_debug",
    "SearchResponse": ".search_response",
    "SearchResponseRelation": ".search_response_relation",
    "SkgIfJsonLdResponse": ".skg_if_json_ld_response",
    "SkgIfNextPage": ".skg_if_next_page",
    "SkgIfPartOf": ".skg_if_part_of",
    "SkgIfPrevPage": ".skg_if_prev_page",
    "SkgIfResponseMeta": ".skg_if_response_meta",
    "SolrQueryParams": ".solr_query_params",
    "SortClause": ".sort_clause",
    "SortClauseOrder": ".sort_clause_order",
    "Subject": ".subject",
    "SubjectSchemeValue": ".subject_scheme_value",
    "UsageCounts": ".usage_counts",
    "XmlChildResult": ".xml_child_result",
    "XmlChildren": ".xml_children",
    "XmlClassification": ".xml_classification",
    "XmlClassifiedValue": ".xml_classified_value",
    "XmlCollectedFrom": ".xml_collected_from",
    "XmlContext": ".xml_context",
    "XmlContractType": ".xml_contract_type",
    "XmlCountry": ".xml_country",
    "XmlCreator": ".xml_creator",
    "XmlDataInfo": ".xml_data_info",
    "XmlEntity": ".xml_entity",
    "XmlFunder": ".xml_funder",
    "XmlFundingLevel": ".xml_funding_level",
    "XmlFundingLevelParent": ".xml_funding_level_parent",
    "XmlFundingTree": ".xml_funding_tree",
    "XmlHeader": ".xml_header",
    "XmlInstance": ".xml_instance",
    "XmlJournalElement": ".xml_journal_element",
    "XmlMeasure": ".xml_measure",
    "XmlMetadata": ".xml_metadata",
    "XmlPid": ".xml_pid",
    "XmlProject": ".xml_project",
    "XmlProvenanceAction": ".xml_provenance_action",
    "XmlPublicationResult": ".xml_publication_result",
    "XmlRel": ".xml_rel",
    "XmlRelTo": ".xml_rel_to",
    "XmlRels": ".xml_rels",
    "XmlResponse": ".xml_response",
    "XmlResult": ".xml_result",
    "XmlResultHeader": ".xml_result_header",
    "XmlResults": ".xml_results",
    "XmlSubject": ".xml_subject",
    "XmlWebResource": ".xml_web_resource",
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
    "AccessRight",
    "AccessRightOpenAccessRoute",
    "Affiliation",
    "AlternateIdentifier",
    "Apc",
    "ApiOrganization",
    "ApiPerson",
    "ApiProject",
    "ApiResult",
    "ApiResultOpenAccessColor",
    "Author",
    "AuthorPid",
    "AuthorPidSchemeValue",
    "BestAccessRight",
    "BipIndicators",
    "Category",
    "CfHbKeyValue",
    "CodeLabel",
    "CommunityInstance",
    "Concept",
    "Container",
    "Context",
    "Country",
    "DataSourceSearchResponse",
    "Datasource",
    "DatasourcePid",
    "DatasourceSchemeValue",
    "Entity",
    "ErrorResponse",
    "Funder",
    "Fundings",
    "GeoLocation",
    "Granted",
    "GraphResult",
    "GraphResultOpenAccessColor",
    "Identifier",
    "Indicator",
    "Instance",
    "Language",
    "Measure",
    "Node",
    "OrganizationPid",
    "OrganizationSearchResponse",
    "PersonTopic",
    "Programme",
    "Project",
    "ProjectPid",
    "ProjectSearchResponse",
    "Provenance",
    "RelType",
    "Relation",
    "ResearchProductsSearchResponse",
    "ResearchProductsSearchResponseV2",
    "ResultCountry",
    "ResultPid",
    "SearchHeader",
    "SearchHeaderDebug",
    "SearchResponse",
    "SearchResponseRelation",
    "SkgIfJsonLdResponse",
    "SkgIfNextPage",
    "SkgIfPartOf",
    "SkgIfPrevPage",
    "SkgIfResponseMeta",
    "SolrQueryParams",
    "SortClause",
    "SortClauseOrder",
    "Subject",
    "SubjectSchemeValue",
    "UsageCounts",
    "XmlChildResult",
    "XmlChildren",
    "XmlClassification",
    "XmlClassifiedValue",
    "XmlCollectedFrom",
    "XmlContext",
    "XmlContractType",
    "XmlCountry",
    "XmlCreator",
    "XmlDataInfo",
    "XmlEntity",
    "XmlFunder",
    "XmlFundingLevel",
    "XmlFundingLevelParent",
    "XmlFundingTree",
    "XmlHeader",
    "XmlInstance",
    "XmlJournalElement",
    "XmlMeasure",
    "XmlMetadata",
    "XmlPid",
    "XmlProject",
    "XmlProvenanceAction",
    "XmlPublicationResult",
    "XmlRel",
    "XmlRelTo",
    "XmlRels",
    "XmlResponse",
    "XmlResult",
    "XmlResultHeader",
    "XmlResults",
    "XmlSubject",
    "XmlWebResource",
]
