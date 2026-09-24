

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TicData(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Taxability Information Code (TIC) identifier (numeric string).
    """

    label: str = pydantic.Field()
    """
    Longer, localized description of what the TIC category covers.
    """

    nl_label: str = pydantic.Field()
    """
    Non-localized (base English) description of the TIC category, independent of locale.
    """

    nl_title: str = pydantic.Field()
    """
    Non-localized (base English) title of the TIC category, independent of locale.
    """

    parent: str = pydantic.Field()
    """
    TIC code of this code's parent category in the TIC hierarchy; empty for top-level categories.
    """

    title: str = pydantic.Field()
    """
    Short, localized human-readable title of the TIC category.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
