

Timerange = str
"""
A timerange of timestamps. It is represented using one or two timestamps with inclusivity and exclusivity markers.

E.g.
* `[0:0_10:0)` represents 10 seconds of media starting at timestamp `0:0` and ending before `10:0`.
* `(5:0_` represents a timerange starting after `5:0` and to eternity.
* `_` without timestamps or inclusivity markers represents "eternity" (i.e. the entire timeline).
* `()` without timestamps represents "never" (i.e. a range of zero length in no particular position).
* `[1694429247:0_1694429248:0)` is a 1 second TAI timerange starting at 2023-09-11T10:46:50.0Z UTC.
* `[1694429247:0]` is an instantaneous TAI timerange at 2023-09-11T10:46:50.0Z UTC.
  This is equivalent to `[1694429247:0_1694429247:0]`.
  The short syntax is preferred due to ease of identification as instantaneous.
  Instantaneous TimeRanges cannot use exclusive markers (i.e. `(` or `)`).
* A `[` or `]` indicates that bound is inclusive, and a `(` or `)` indicates that bound is exclusive.

Details of the format can be found in the [Timestamps in TAMS](https://github.com/bbc/tams/blob/main/docs/appnotes/0008-timestamps-in-TAMS.md) application note.
"""
