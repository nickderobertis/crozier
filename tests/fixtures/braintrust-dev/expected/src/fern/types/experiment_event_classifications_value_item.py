

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .saved_function_id import SavedFunctionId


class ExperimentEventClassificationsValueItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Stable classification identifier
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Original label of the classification item, which is useful for search and indexing purposes
    """

    confidence: typing.Optional[float] = pydantic.Field(default=None)
    """
    Optional confidence score for the classification
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Optional metadata associated with the classification
    """

    source: typing.Optional[SavedFunctionId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
