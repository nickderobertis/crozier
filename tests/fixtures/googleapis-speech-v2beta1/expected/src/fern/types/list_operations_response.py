

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operation import Operation


class ListOperationsResponse(UniversalBaseModel):
    """
    The response message for Operations.ListOperations.
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(alias="nextPageToken", description="The standard List next-page token."),
    ] = None
    """
    The standard List next-page token.
    """

    operations: typing.Optional[typing.List[Operation]] = pydantic.Field(default=None)
    """
    A list of operations that matches the specified filter in the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
