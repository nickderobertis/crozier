

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogModifierOverride(UniversalBaseModel):
    """
    Options to control how to override the default behavior of the specified modifier.
    """

    modifier_id: str = pydantic.Field()
    """
    The ID of the `CatalogModifier` whose default behavior is being overridden.
    """

    on_by_default: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, this `CatalogModifier` should be selected by default for this `CatalogItem`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
