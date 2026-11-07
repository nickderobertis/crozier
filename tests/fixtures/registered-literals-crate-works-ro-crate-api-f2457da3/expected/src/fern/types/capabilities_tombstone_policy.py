

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CapabilitiesTombstonePolicy(enum.StrEnum):
    """
    What deleted resource URIs return. `"410"` - deleted URIs respond 410 Gone with a `Tombstone` body; `"404"` - deleted resources are indistinguishable from those that never existed. One policy covers RO-Crate, entity and file URIs alike; implementations MUST NOT mix them.

    REQUIRED of every implementation, whether or not it provides the deposit surface: entities and files are mandatory core, so any catalog may hold a URI that no longer resolves.
    """

    FOUR_HUNDRED_TEN = "410"
    FOUR_HUNDRED_FOUR = "404"

    def visit(
        self, four_hundred_ten: typing.Callable[[], T_Result], four_hundred_four: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is CapabilitiesTombstonePolicy.FOUR_HUNDRED_TEN:
            return four_hundred_ten()
        if self is CapabilitiesTombstonePolicy.FOUR_HUNDRED_FOUR:
            return four_hundred_four()
