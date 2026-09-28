

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VisualizeSessionIdGetResponseDataVisualizationsItemContentThreeItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique card identifier
    """

    title: str = pydantic.Field()
    """
    Card title
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Card description
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags/labels for the card
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
