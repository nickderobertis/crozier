

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hal_link import HalLink


class QueryHalLinks(UniversalBaseModel):
    """
    HAL Links for a query entity.
    """

    self_: typing_extensions.Annotated[
        HalLink, FieldMetadata(alias="self"), pydantic.Field(alias="self", description="Link to the query definition.")
    ]
    """
    Link to the query definition.
    """

    execute: HalLink = pydantic.Field()
    """
    Link to the query execution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
