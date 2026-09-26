

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V60ShippingExtended(UniversalBaseModel):
    description: str = pydantic.Field()
    """
    Human-readable description of the shipping taxability rule.
    """

    exempt_when_separately_stated: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="exemptWhenSeparatelyStated"),
        pydantic.Field(
            alias="exemptWhenSeparatelyStated",
            description="Whether shipping is exempt when separately stated on the invoice, as the string 'true' or 'false'.",
        ),
    ]
    """
    Whether shipping is exempt when separately stated on the invoice, as the string 'true' or 'false'.
    """

    rule: str = pydantic.Field()
    """
    General shipping-taxability rule for the state: one of EXEMPT, EXEMPT_WHEN_SEPARATELY_STATED, ITEM_SPECIFIC, CONDITIONAL, or TAXABLE.
    """

    state_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateCode"),
        pydantic.Field(alias="stateCode", description="Two-letter state code the shipping rule applies to."),
    ]
    """
    Two-letter state code the shipping rule applies to.
    """

    state_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateName"),
        pydantic.Field(alias="stateName", description="Full state name the shipping rule applies to."),
    ]
    """
    Full state name the shipping rule applies to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
