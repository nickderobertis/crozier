

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AdminStatusRequestModesItem(enum.StrEnum):
    INDEX = "index"
    BLOOMS = "blooms"
    BLOCKS = "blocks"
    TRANSACTIONS = "transactions"
    TRACES = "traces"
    LOGS = "logs"
    STATEMENTS = "statements"
    RESULTS = "results"
    STATE = "state"
    TOKENS = "tokens"
    MONITORS = "monitors"
    NAMES = "names"
    ABIS = "abis"
    SLURPS = "slurps"
    STAGING = "staging"
    UNRIPE = "unripe"
    MAPS = "maps"
    SOME = "some"
    ALL = "all"

    def visit(
        self,
        index: typing.Callable[[], T_Result],
        blooms: typing.Callable[[], T_Result],
        blocks: typing.Callable[[], T_Result],
        transactions: typing.Callable[[], T_Result],
        traces: typing.Callable[[], T_Result],
        logs: typing.Callable[[], T_Result],
        statements: typing.Callable[[], T_Result],
        results: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        tokens: typing.Callable[[], T_Result],
        monitors: typing.Callable[[], T_Result],
        names: typing.Callable[[], T_Result],
        abis: typing.Callable[[], T_Result],
        slurps: typing.Callable[[], T_Result],
        staging: typing.Callable[[], T_Result],
        unripe: typing.Callable[[], T_Result],
        maps: typing.Callable[[], T_Result],
        some: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdminStatusRequestModesItem.INDEX:
            return index()
        if self is AdminStatusRequestModesItem.BLOOMS:
            return blooms()
        if self is AdminStatusRequestModesItem.BLOCKS:
            return blocks()
        if self is AdminStatusRequestModesItem.TRANSACTIONS:
            return transactions()
        if self is AdminStatusRequestModesItem.TRACES:
            return traces()
        if self is AdminStatusRequestModesItem.LOGS:
            return logs()
        if self is AdminStatusRequestModesItem.STATEMENTS:
            return statements()
        if self is AdminStatusRequestModesItem.RESULTS:
            return results()
        if self is AdminStatusRequestModesItem.STATE:
            return state()
        if self is AdminStatusRequestModesItem.TOKENS:
            return tokens()
        if self is AdminStatusRequestModesItem.MONITORS:
            return monitors()
        if self is AdminStatusRequestModesItem.NAMES:
            return names()
        if self is AdminStatusRequestModesItem.ABIS:
            return abis()
        if self is AdminStatusRequestModesItem.SLURPS:
            return slurps()
        if self is AdminStatusRequestModesItem.STAGING:
            return staging()
        if self is AdminStatusRequestModesItem.UNRIPE:
            return unripe()
        if self is AdminStatusRequestModesItem.MAPS:
            return maps()
        if self is AdminStatusRequestModesItem.SOME:
            return some()
        if self is AdminStatusRequestModesItem.ALL:
            return all_()
