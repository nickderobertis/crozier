

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CatalogCustomAttributeDefinitionSelectionConfigCustomAttributeSelection(UniversalBaseModel):
    """
    A named selection for this `SELECTION`-type custom attribute definition.
    """

    name: str = pydantic.Field()
    """
    Selection name, unique within `allowed_selections`.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID set by Square.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
