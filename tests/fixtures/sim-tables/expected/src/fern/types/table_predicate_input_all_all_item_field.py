

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .table_predicate_input_all_all_item_field_op import TablePredicateInputAllAllItemFieldOp


class TablePredicateInputAllAllItemField(UniversalBaseModel):
    """
    One column comparison.
    """

    field: str = pydantic.Field()
    """
    Column name to compare, or one of the system fields `id`, `createdAt`, `updatedAt`.
    """

    op: TablePredicateInputAllAllItemFieldOp = pydantic.Field()
    """
    Operators: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`; `in`/`nin` take arrays; `isEmpty`, `isNotEmpty`, `isNull`, and `isNotNull` take no operand. Text operators are `contains`, `ncontains`, `startsWith`, `endsWith`, `like`, `nlike`, `ilike`, and `nilike`. Contains variants are case-insensitive and literal; `like`/`nlike` are case-sensitive, while `ilike`/`nilike` are case-insensitive. `*` is the only wildcard; `%`, `_`, and backslash are literal. For `select` columns, single-select accepts `eq`, `ne`, `in`, `nin`; multi-select accepts `contains`, `ncontains`. Option names resolve to IDs.
    """

    value: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    Operand. A scalar for the comparison operators, an array of at most 1000 entries for `in`/`nin`, a pattern for the matching operators, and omitted for `isEmpty`/`isNotEmpty`/`isNull`/`isNotNull`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
