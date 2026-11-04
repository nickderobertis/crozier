

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rule_kind import RuleKind
from .rule_mode import RuleMode


class Rule(UniversalBaseModel):
    """
    Rule
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rule name
    """

    doc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rule doc
    """

    kind: typing.Optional[RuleKind] = pydantic.Field(default=None)
    """
    Rule kind
    """

    mode: typing.Optional[RuleMode] = pydantic.Field(default=None)
    """
    Rule mode
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rule type
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags to which this rule applies
    """

    params: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Optional params for the rule
    """

    expr: typing.Optional[str] = pydantic.Field(default=None)
    """
    Rule expression
    """

    on_success: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="onSuccess"),
        pydantic.Field(alias="onSuccess", description="Rule action on success"),
    ] = None
    """
    Rule action on success
    """

    on_failure: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="onFailure"),
        pydantic.Field(alias="onFailure", description="Rule action on failure"),
    ] = None
    """
    Rule action on failure
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the rule is disabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
