

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_group_mapping_options import AdminGroupMappingOptions


class AdminGroupMapping(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    group name
    """

    options: typing.Optional[AdminGroupMappingOptions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
