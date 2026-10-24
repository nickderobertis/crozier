

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .query_all_organizations_endpoint_output import QueryAllOrganizationsEndpointOutput


class QueryAllOrganizationsEndpointPagedResultOfOutput(UniversalBaseModel):
    total: int
    page: int
    page_size: typing_extensions.Annotated[int, FieldMetadata(alias="pageSize"), pydantic.Field(alias="pageSize")]
    items: typing.List[QueryAllOrganizationsEndpointOutput]
    total_pages: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalPages"), pydantic.Field(alias="totalPages")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
