

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .qa_meta_conformance import QaMetaConformance


class QaMeta(UniversalBaseModel):
    """
    Information concerning this response.
    """

    conformance: typing.Optional[QaMetaConformance] = pydantic.Field(default=None)
    """
    Conformance level of the record.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
