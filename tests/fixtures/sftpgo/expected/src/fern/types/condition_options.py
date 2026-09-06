

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition_options_protocols_item import ConditionOptionsProtocolsItem
from .condition_options_provider_objects_item import ConditionOptionsProviderObjectsItem
from .condition_pattern import ConditionPattern


class ConditionOptions(UniversalBaseModel):
    names: typing.Optional[typing.List[ConditionPattern]] = None
    group_names: typing.Optional[typing.List[ConditionPattern]] = None
    role_names: typing.Optional[typing.List[ConditionPattern]] = None
    fs_paths: typing.Optional[typing.List[ConditionPattern]] = None
    protocols: typing.Optional[typing.List[ConditionOptionsProtocolsItem]] = None
    provider_objects: typing.Optional[typing.List[ConditionOptionsProviderObjectsItem]] = None
    min_size: typing.Optional[int] = None
    max_size: typing.Optional[int] = None
    event_statuses: typing.Optional[typing.List[int]] = None
    concurrent_execution: typing.Optional[bool] = pydantic.Field(default=None)
    """
    allow concurrent execution from multiple nodes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
