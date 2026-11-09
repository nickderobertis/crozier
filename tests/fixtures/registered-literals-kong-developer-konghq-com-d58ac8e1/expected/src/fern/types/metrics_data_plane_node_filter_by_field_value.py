

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .metrics_data_plane_node_filter_by_field_value_field import MetricsDataPlaneNodeFilterByFieldValueField
from .requests_filter_type import RequestsFilterType
from .scoped_uuid import ScopedUuid


class MetricsDataPlaneNodeFilterByFieldValue(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.List[ScopedUuid] = pydantic.Field()
    """
    The IDs to include in the results. Because gateway IDs are only unique within a given control plane, the filter values must be of the form `control_plane_id:field_id` or `control_plane_group_id:field_id` for data plane nodes within a control plane group.
    """

    field: MetricsDataPlaneNodeFilterByFieldValueField = pydantic.Field()
    """
    The field to filter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
