

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiPagedResponseMetadata(UniversalBaseModel):
    """
    Metadata for the paged response
    """

    limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Limit"),
        pydantic.Field(alias="Limit", description="The number of entities this paged response is limited to."),
    ] = None
    """
    The number of entities this paged response is limited to.
    """

    offset: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Offset"),
        pydantic.Field(alias="Offset", description="The number of entities prior to this page of items."),
    ] = None
    """
    The number of entities prior to this page of items.
    """

    total_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TotalCount"),
        pydantic.Field(alias="TotalCount", description="The total number of entities matching the request."),
    ] = None
    """
    The total number of entities matching the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
