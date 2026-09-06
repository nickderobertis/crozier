

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class ItemIDsWithLocalesItemsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the CMS item
    """

    cms_locale_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="cmsLocaleIds"),
        pydantic.Field(
            alias="cmsLocaleIds", description="Array of identifiers for the locales where the item will be published"
        ),
    ] = None
    """
    Array of identifiers for the locales where the item will be published
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
