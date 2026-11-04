

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TagStatus(UniversalBaseModel):
    """
    Observed tag state derived by content reconcilers.
    """

    observed_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="observedVersion"),
        pydantic.Field(
            alias="observedVersion", description="Metadata version observed by the last successful reconciliation."
        ),
    ] = None
    """
    Metadata version observed by the last successful reconciliation.
    """

    permalink: typing.Optional[str] = pydantic.Field(default=None)
    """
    Absolute permalink calculated from the tag permalink policy.
    """

    post_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="postCount"),
        pydantic.Field(alias="postCount", description="Total number of posts associated with the tag."),
    ] = None
    """
    Total number of posts associated with the tag.
    """

    visible_post_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="visiblePostCount"),
        pydantic.Field(
            alias="visiblePostCount", description="Total number of published and public posts associated with the tag."
        ),
    ] = None
    """
    Total number of published and public posts associated with the tag.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
