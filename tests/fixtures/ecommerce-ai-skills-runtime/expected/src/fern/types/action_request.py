

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amazon_report_import_action_request_payload import AmazonReportImportActionRequestPayload
from .shopify_sync_action_request_payload import ShopifySyncActionRequestPayload


class ActionRequest_ShopifySyncProducts(UniversalBaseModel):
    operation: typing.Literal["shopify.sync_products"] = "shopify.sync_products"
    payload: ShopifySyncActionRequestPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionRequest_AmazonSpapiImportReport(UniversalBaseModel):
    operation: typing.Literal["amazon_spapi.import_report"] = "amazon_spapi.import_report"
    payload: AmazonReportImportActionRequestPayload

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActionRequest = typing_extensions.Annotated[
    typing.Union[ActionRequest_ShopifySyncProducts, ActionRequest_AmazonSpapiImportReport],
    pydantic.Field(discriminator="operation"),
]
