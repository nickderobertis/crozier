

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hal_link import HalLink


class QueryListHalLinks(UniversalBaseModel):
    """
    HAL Links for a query entity.
    """

    self_: typing_extensions.Annotated[
        HalLink,
        FieldMetadata(alias="self"),
        pydantic.Field(alias="self", description="Link to the current page of results."),
    ]
    """
    Link to the current page of results.
    """

    first: typing.Optional[HalLink] = pydantic.Field(default=None)
    """
    Link to the first page of results.
    """

    prev: typing.Optional[HalLink] = pydantic.Field(default=None)
    """
    Link to the previous page of results.
    """

    next: typing.Optional[HalLink] = pydantic.Field(default=None)
    """
    Link to the next page of results.
    """

    last: typing.Optional[HalLink] = pydantic.Field(default=None)
    """
    Link to the last page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
