

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_linkifiers_response_linkifiers_item import GetLinkifiersResponseLinkifiersItem


class GetLinkifiersResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    linkifiers: typing.Optional[typing.List[GetLinkifiersResponseLinkifiersItem]] = pydantic.Field(default=None)
    """
    An ordered array of objects, where each object
    describes a linkifier.
    
    Clients should always process linkifiers in the order given;
    this is important if the realm has linkifiers with overlapping
    patterns. The order can be modified using [`PATCH
    /realm/linkifiers`](/api/reorder-linkifiers).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
