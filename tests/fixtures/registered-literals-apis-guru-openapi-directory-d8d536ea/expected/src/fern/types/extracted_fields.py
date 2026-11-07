

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExtractedFields(UniversalBaseModel):
    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    This can be an field that is extracted from rawOrderedDataArray on request of different users.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
