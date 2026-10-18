

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActionRunResponseOutputRunStepsItemName(enum.StrEnum):
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
        if self is ActionRunResponseOutputRunStepsItemName.CLONE:
            return clone()
        if self is ActionRunResponseOutputRunStepsItemName.PULL:
            return pull()
        if self is ActionRunResponseOutputRunStepsItemName.HEALTH:
            return health()
        if self is ActionRunResponseOutputRunStepsItemName.CONFIGURE:
            return configure()
        if self is ActionRunResponseOutputRunStepsItemName.MIGRATE:
            return migrate()
        if self is ActionRunResponseOutputRunStepsItemName.SEED:
            return seed()
        if self is ActionRunResponseOutputRunStepsItemName.DEPLOY:
            return deploy()
