

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PatchLinksBundleIdLinksRequestBodyItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Link template ID
    """

    sort_order: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="sortOrder"),
        pydantic.Field(alias="sortOrder", description="New sort order position"),
    ]
    """
    New sort order position
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
