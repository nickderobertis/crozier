

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetArtifactsResponseItemsItem(UniversalBaseModel):
    """
    An artifact
    """

    path: str = pydantic.Field()
    """
    The artifact path.
    """

    node_index: int = pydantic.Field()
    """
    The index of the node that stored the artifact.
    """

    url: str = pydantic.Field()
    """
    The URL to download the artifact contents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
