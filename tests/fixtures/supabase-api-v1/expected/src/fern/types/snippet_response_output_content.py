

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SnippetResponseOutputContent(UniversalBaseModel):
    favorite: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Rely on root-level favorite property instead.
    """

    schema_version: str
    sql: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
