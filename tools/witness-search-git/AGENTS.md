# witness-search-git

- witness-search's cases that run the real `git`, kept apart so the offline
  `witness-search` project needs no host tool. They share that project's test
  fixtures (`WideWitnessFixture`, `WitnessSearchGithubFixture`) by import, so a
  case that starts driving git moves here with its fixture left behind.
