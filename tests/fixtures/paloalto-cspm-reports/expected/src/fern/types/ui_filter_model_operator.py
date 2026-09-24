

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiFilterModelOperator(enum.StrEnum):
    """
    Operator
    """

    TAG_YAML_ORG2002VALUE = "tag:yaml.org,2002:value ="

    def visit(self, tag_yaml_org2002value: typing.Callable[[], T_Result]) -> T_Result:
        if self is UiFilterModelOperator.TAG_YAML_ORG2002VALUE:
            return tag_yaml_org2002value()
