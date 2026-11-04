

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PaginationLinks(UniversalBaseModel):
    """
    Links to use for pagination
    """

    self_: typing_extensions.Annotated[
        str, FieldMetadata(alias="self"), pydantic.Field(alias="self", description="URL of this page")
    ]
    """
    URL of this page
    """

    prev: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the previous page, if any
    """

    next: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the next page, if any
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
