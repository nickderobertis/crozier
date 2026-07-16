

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class QueriesPagedQuery(UniversalBaseModel):
    current_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="currentPage"), pydantic.Field(alias="currentPage")
    ] = None
    items_per_page: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="itemsPerPage"), pydantic.Field(alias="itemsPerPage")
    ] = None
    request_continuation_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="requestContinuationToken"),
        pydantic.Field(alias="requestContinuationToken"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
