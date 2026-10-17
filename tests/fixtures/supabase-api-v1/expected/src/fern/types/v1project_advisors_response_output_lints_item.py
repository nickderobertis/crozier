

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1project_advisors_response_output_lints_item_categories_item import (
    V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem,
)
from .v1project_advisors_response_output_lints_item_facing import V1ProjectAdvisorsResponseOutputLintsItemFacing
from .v1project_advisors_response_output_lints_item_level import V1ProjectAdvisorsResponseOutputLintsItemLevel
from .v1project_advisors_response_output_lints_item_metadata import V1ProjectAdvisorsResponseOutputLintsItemMetadata
from .v1project_advisors_response_output_lints_item_name import V1ProjectAdvisorsResponseOutputLintsItemName


class V1ProjectAdvisorsResponseOutputLintsItem(UniversalBaseModel):
    name: V1ProjectAdvisorsResponseOutputLintsItemName
    title: str
    level: V1ProjectAdvisorsResponseOutputLintsItemLevel
    facing: V1ProjectAdvisorsResponseOutputLintsItemFacing
    categories: typing.List[V1ProjectAdvisorsResponseOutputLintsItemCategoriesItem]
    description: str
    detail: str
    remediation: str
    metadata: typing.Optional[V1ProjectAdvisorsResponseOutputLintsItemMetadata] = None
    cache_key: str
    observed_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
