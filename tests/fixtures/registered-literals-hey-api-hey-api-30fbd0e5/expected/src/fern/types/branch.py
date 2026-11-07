

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .branch_links import BranchLinks


class Branch(UniversalBaseModel):
    """
    A Branch
    """

    name: str
    id: str = pydantic.Field()
    """
    The id of the branch
    """

    version: int
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    forked_branch_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="forkedBranchId"),
        pydantic.Field(alias="forkedBranchId", description="The id of the branch this branch was forked from"),
    ] = None
    """
    The id of the branch this branch was forked from
    """

    links: BranchLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
