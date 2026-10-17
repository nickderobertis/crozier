

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListActionRunResponseOutputItemRunStepsItemName(enum.StrEnum):
    CLONE = "clone"
    PULL = "pull"
    HEALTH = "health"
    CONFIGURE = "configure"
    MIGRATE = "migrate"
    SEED = "seed"
    DEPLOY = "deploy"

    def visit(
        self,
        clone: typing.Callable[[], T_Result],
        pull: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
        configure: typing.Callable[[], T_Result],
        migrate: typing.Callable[[], T_Result],
        seed: typing.Callable[[], T_Result],
        deploy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActionRunResponseOutputItemRunStepsItemName.CLONE:
            return clone()
        if self is ListActionRunResponseOutputItemRunStepsItemName.PULL:
            return pull()
        if self is ListActionRunResponseOutputItemRunStepsItemName.HEALTH:
            return health()
        if self is ListActionRunResponseOutputItemRunStepsItemName.CONFIGURE:
            return configure()
        if self is ListActionRunResponseOutputItemRunStepsItemName.MIGRATE:
            return migrate()
        if self is ListActionRunResponseOutputItemRunStepsItemName.SEED:
            return seed()
        if self is ListActionRunResponseOutputItemRunStepsItemName.DEPLOY:
            return deploy()
