

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .identifier import Identifier


class DppIdPage(UniversalBaseModel):
    """
    A page of matching DPP identifiers. The EN 18222 payload is the identifier set; `nextCursor` carries the pagination token for the next page.
    """

    dpp_ids: typing_extensions.Annotated[
        typing.List[Identifier], FieldMetadata(alias="dppIds"), pydantic.Field(alias="dppIds")
    ]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextCursor"),
        pydantic.Field(
            alias="nextCursor", description="Token to pass as `cursor` for the next page; absent at the end."
        ),
    ] = None
    """
    Token to pass as `cursor` for the next page; absent at the end.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
