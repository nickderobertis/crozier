

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxonomiesListResponseItemAttributes(UniversalBaseModel):
    """
    The properties of the taxonomy entity.
    """

    child_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of children this taxonomy contains.
    """

    parents: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of JSON objects containing keys for `text` (name) and `id` (unique identifier) of this taxonomy's parents
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text name of the taxonomy
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
