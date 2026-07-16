

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomerSort(UniversalBaseModel):
    """
    Specifies how searched customers profiles are sorted, including the sort key and sort order.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    Use one or more customer attributes as the sort key to sort searched customer profiles. 
    For example, use the creation date (`created_at`) of customers or default attributes as the sort key.
    
    
    Default: `DEFAULT`.
    """

    order: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates the order in which results should be sorted based on the
    sort field value. Strings use standard alphabetic comparison
    to determine order. Strings representing numbers are sorted as strings.
    
    Default: `ASC`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
