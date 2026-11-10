

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SubstitutionPolicy(enum.StrEnum):
    """
    The replacement logic for detected PII, can be `entity_name` or `hash`. See [PII redaction](https://www.assemblyai.com/docs/pii-redaction) for more details.
    """

    ENTITY_NAME = "entity_name"
    HASH = "hash"

    def visit(self, entity_name: typing.Callable[[], T_Result], hash: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubstitutionPolicy.ENTITY_NAME:
            return entity_name()
        if self is SubstitutionPolicy.HASH:
            return hash()
