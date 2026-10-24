

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_marketplace_catalog_entry import AmazonMarketplaceCatalogEntry
from .connector_provider_catalog_entry import ConnectorProviderCatalogEntry
from .evidence_report_type import EvidenceReportType
from .report_recipe_catalog_entry import ReportRecipeCatalogEntry
from .runtime_catalog_action_operations_item import RuntimeCatalogActionOperationsItem
from .runtime_catalog_platforms_item import RuntimeCatalogPlatformsItem
from .runtime_catalog_workflows_item import RuntimeCatalogWorkflowsItem


class RuntimeCatalog(UniversalBaseModel):
    platforms: typing.List[RuntimeCatalogPlatformsItem]
    report_types: typing.List[EvidenceReportType]
    workflows: typing.List[RuntimeCatalogWorkflowsItem]
    action_operations: typing.List[RuntimeCatalogActionOperationsItem]
    connector_providers: typing.List[ConnectorProviderCatalogEntry]
    amazon_marketplaces: typing.List[AmazonMarketplaceCatalogEntry]
    report_recipe_types: typing.List[ReportRecipeCatalogEntry]
    metric_materialization_report_types: typing.List[EvidenceReportType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
