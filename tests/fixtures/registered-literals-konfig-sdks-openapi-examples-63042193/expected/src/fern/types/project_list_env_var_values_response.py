

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .project_list_env_var_values_response_items_item import ProjectListEnvVarValuesResponseItemsItem


class ProjectListEnvVarValuesResponse(UniversalBaseModel):
    items: typing.List[ProjectListEnvVarValuesResponseItemsItem]
    next_page_token: str = pydantic.Field()
    """
    A token to pass as a `page-token` query parameter to return the next page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
