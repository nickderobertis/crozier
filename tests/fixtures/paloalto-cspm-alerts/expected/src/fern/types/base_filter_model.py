

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ui_filter_model import UiFilterModel


class BaseFilterModel(UniversalBaseModel):
    """
    Model for Filter
    """

    detailed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Detailed
    """

    fields: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Array of specific fields to return
    """

    filters: typing.Optional[typing.List[UiFilterModel]] = pydantic.Field(default=None)
    """
    Filtering parameters. 
    
    For filter names, refer to List Filters API. 
    
    For filter values, refer to List filter suggestions. 
    
    The only exception is **resource.tagv2** filter name, provide filter value for it in the following format: "{"key":"'CustomerTagKey'","value":"'CustomerTagValue'"}"
    """

    group_by: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="groupBy"),
        pydantic.Field(
            alias="groupBy",
            description="For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**",
        ),
    ] = None
    """
    For asset or data inventory only. Group returned items by **cloud.type**, **cloud.service**, **cloud.region**, **cloud.account**, and/or **resource.type**
    """

    limit: typing.Optional[float] = pydantic.Field(default=None)
    """
    Maximum number of items to return. When data is paginated, maximum number of items per page.The maximum cannot exceed 10,000. The default is 10,000.
    """

    offset: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of items to skip before selecting items to return. Default is zero
    """

    page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageToken"),
        pydantic.Field(
            alias="pageToken",
            description="Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data ",
        ),
    ] = None
    """
    Setting this pagination Token to the **nextPageToken** from a response object returns the next page of data 
    """

    sort_by: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="sortBy"),
        pydantic.Field(
            alias="sortBy",
            description="Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**",
        ),
    ] = None
    """
    Array of sort properties. Append **:asc** or  **:desc** to the key to sort by ascending or descending order respectively. Example sort properties are **id:asc** and **timestamp:desc**
    """

    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
