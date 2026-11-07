

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeleteDocumentsResponse(UniversalBaseModel):
    success: bool = pydantic.Field()
    """
    Whether any documents were deleted
    """

    documents_deleted: int = pydantic.Field()
    """
    The number of documents that were deleted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
