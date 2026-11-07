

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdvancedQueryDimensionsItem(enum.StrEnum):
    API = "api"
    API_PRODUCT = "api_product"
    API_PRODUCT_VERSION = "api_product_version"
    APPLICATION = "application"
    CONSUMER = "consumer"
    CONTROL_PLANE = "control_plane"
    CONTROL_PLANE_GROUP = "control_plane_group"
    DATA_PLANE_NODE = "data_plane_node"
    DATA_PLANE_NODE_VERSION = "data_plane_node_version"
    GATEWAY_SERVICE = "gateway_service"
    PORTAL = "portal"
    RESPONSE_SOURCE = "response_source"
    ROUTE = "route"
    STATUS_CODE = "status_code"
    STATUS_CODE_GROUPED = "status_code_grouped"
    TIME = "time"
    UPSTREAM_STATUS_CODE = "upstream_status_code"
    UPSTREAM_STATUS_CODE_GROUPED = "upstream_status_code_grouped"

    def visit(
        self,
        api: typing.Callable[[], T_Result],
        api_product: typing.Callable[[], T_Result],
        api_product_version: typing.Callable[[], T_Result],
        application: typing.Callable[[], T_Result],
        consumer: typing.Callable[[], T_Result],
        control_plane: typing.Callable[[], T_Result],
        control_plane_group: typing.Callable[[], T_Result],
        data_plane_node: typing.Callable[[], T_Result],
        data_plane_node_version: typing.Callable[[], T_Result],
        gateway_service: typing.Callable[[], T_Result],
        portal: typing.Callable[[], T_Result],
        response_source: typing.Callable[[], T_Result],
        route: typing.Callable[[], T_Result],
        status_code: typing.Callable[[], T_Result],
        status_code_grouped: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        upstream_status_code: typing.Callable[[], T_Result],
        upstream_status_code_grouped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdvancedQueryDimensionsItem.API:
            return api()
        if self is AdvancedQueryDimensionsItem.API_PRODUCT:
            return api_product()
        if self is AdvancedQueryDimensionsItem.API_PRODUCT_VERSION:
            return api_product_version()
        if self is AdvancedQueryDimensionsItem.APPLICATION:
            return application()
        if self is AdvancedQueryDimensionsItem.CONSUMER:
            return consumer()
        if self is AdvancedQueryDimensionsItem.CONTROL_PLANE:
            return control_plane()
        if self is AdvancedQueryDimensionsItem.CONTROL_PLANE_GROUP:
            return control_plane_group()
        if self is AdvancedQueryDimensionsItem.DATA_PLANE_NODE:
            return data_plane_node()
        if self is AdvancedQueryDimensionsItem.DATA_PLANE_NODE_VERSION:
            return data_plane_node_version()
        if self is AdvancedQueryDimensionsItem.GATEWAY_SERVICE:
            return gateway_service()
        if self is AdvancedQueryDimensionsItem.PORTAL:
            return portal()
        if self is AdvancedQueryDimensionsItem.RESPONSE_SOURCE:
            return response_source()
        if self is AdvancedQueryDimensionsItem.ROUTE:
            return route()
        if self is AdvancedQueryDimensionsItem.STATUS_CODE:
            return status_code()
        if self is AdvancedQueryDimensionsItem.STATUS_CODE_GROUPED:
            return status_code_grouped()
        if self is AdvancedQueryDimensionsItem.TIME:
            return time()
        if self is AdvancedQueryDimensionsItem.UPSTREAM_STATUS_CODE:
            return upstream_status_code()
        if self is AdvancedQueryDimensionsItem.UPSTREAM_STATUS_CODE_GROUPED:
            return upstream_status_code_grouped()
