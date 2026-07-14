

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifact_reference import ArtifactReference


class ContentCreateRequest(UniversalBaseModel):
    """ """

    content: str = pydantic.Field()
    """
    Raw content of the artifact or a valid (and accessible) URL where the content can be found.
    """

    references: typing.List[ArtifactReference] = pydantic.Field()
    """
    Collection of references to other artifacts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
