

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableRunDispatchScope(UniversalBaseModel):
    """
    What the dispatch was asked to run.
    """

    group_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="groupIds"),
        pydantic.Field(alias="groupIds", description="Workflow groups the dispatch runs."),
    ]
    """
    Workflow groups the dispatch runs.
    """

    row_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="rowIds"),
        pydantic.Field(
            alias="rowIds",
            description="Explicit rows the dispatch targets. Absent means it was given no row list and walks every eligible row, narrowed by `filtered` and `excludeRowIds` when either is present.",
        ),
    ] = None
    """
    Explicit rows the dispatch targets. Absent means it was given no row list and walks every eligible row, narrowed by `filtered` and `excludeRowIds` when either is present.
    """

    filtered: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Present and true when a stored filter narrows which rows run. The filter itself is not published: it is held compiled, in a different grammar from the predicate the request was written in. Absent means no filter narrows the dispatch — which, with no `rowIds` and no `excludeRowIds`, is what means every eligible row.
    """

    exclude_row_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="excludeRowIds"),
        pydantic.Field(
            alias="excludeRowIds",
            description="Rows the walk skips. Independent of `filtered`: a dispatch may exclude rows from a filtered set or from every eligible row. Never present alongside `rowIds`, which the run rejects and the walk would ignore.",
        ),
    ] = None
    """
    Rows the walk skips. Independent of `filtered`: a dispatch may exclude rows from a filtered set or from every eligible row. Never present alongside `rowIds`, which the run rejects and the walk would ignore.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
