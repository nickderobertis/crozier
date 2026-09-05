

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetrulesforapricetableResponseRulesItemContextDateRange(UniversalBaseModel):
    """
    The rule will be active during this time range.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="Date when rule will be activated. Date format: `RFC3339`."),
    ] = None
    """
    Date when rule will be activated. Date format: `RFC3339`.
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date when the rule will be deactivated. Date format: `RFC3339`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
