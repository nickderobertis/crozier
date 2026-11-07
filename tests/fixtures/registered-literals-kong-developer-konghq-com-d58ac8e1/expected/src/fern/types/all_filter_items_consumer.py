

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .requests_filter_type import RequestsFilterType
from .scoped_uuid import ScopedUuid


class AllFilterItemsConsumer(UniversalBaseModel):
    operator: RequestsFilterType
    value: typing.Optional[typing.List[ScopedUuid]] = pydantic.Field(default=None)
    """
    The IDs to include in the results. Because gateway IDs are only unique within a given control plane, the filter values must be of the form `control_plane_id:field_id` or `control_plane_group_id:field_id` for data plane nodes within a control plane group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
