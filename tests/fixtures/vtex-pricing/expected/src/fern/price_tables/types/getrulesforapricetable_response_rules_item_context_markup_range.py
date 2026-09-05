

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetrulesforapricetableResponseRulesItemContextMarkupRange(UniversalBaseModel):
    """
    For an item to be eligible to the rule, it's markup should be in this Markup Range.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Item markup should be greater than or equal to this value."),
    ] = None
    """
    Item markup should be greater than or equal to this value.
    """

    to: typing.Optional[int] = pydantic.Field(default=None)
    """
    Item markup should be less than or equal to this value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
