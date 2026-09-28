

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class KnowledgeAskPostResponseDataSourcesItem(UniversalBaseModel):
    uri: str = pydantic.Field()
    """
    Source document URI
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document title if available from metadata
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
