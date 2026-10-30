

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_search_request_filter_value import PostSearchRequestFilterValue


class PostSearchRequestFilter(UniversalBaseModel):
    """
    A set of criteria, `value` and `property` keys, that limits the results to either only pages or only data sources. Possible `value` values are `"page"` or `"data_source"`. The only supported `property` value is `"object"`.
    """

    value: typing.Optional[PostSearchRequestFilterValue] = pydantic.Field(default=None)
    """
    The value of the property to filter the results by.  Possible values for object type include `page` or `data_source`.  **Limitation**: Currently the only filter allowed is `object` which will filter by type of object (either `page` or `data_source`)
    """

    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the property to filter by. Currently the only property you can filter by is the object type.  Possible values include `object`.   Limitation: Currently the only filter allowed is `object` which will filter by type of object (either `page` or `data_source`)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
