# llmlint-resolution

- The suites that run the real `llmlint` binary, kept apart from
  `llmlint-tooling`'s offline ones so that project needs no host tool. They skip
  where llmlint is absent unless `CROZIER_REQUIRE_LLMLINT=1`, so both that
  variable and `llmlint --version` are cache inputs.
