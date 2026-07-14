

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AnalysisArchiveSource(UniversalBaseModel):
    """
    An image reference in the analysis archive for the purposes of loading analysis from the archive into th working set
    """

    digest: str = pydantic.Field()
    """
    The image digest identify the analysis. Archived analyses are based on digest, tag records are restored as analysis is restored.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
