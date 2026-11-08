export function event(branch = 'feature/change', fork = false) {
  const repo = 'nickderobertis/crozier';
  return { action: 'synchronize', repository: { full_name: repo }, pull_request: { title: 'chore: release', user: { login: 'nickderobertis' }, head: { ref: branch, repo: { full_name: fork ? 'contributor/crozier' : repo } }, base: { ref: 'main', repo: { full_name: repo } } } };
}

// Artifact names and paths compare platform-independently: a runner may hand
// back `C:\…\v1\crozier.tar.gz` where the contract says `v1/crozier.tar.gz`.
export function artifactPath(path) { return String(path).replace(/\\/g, '/').replace(/^(\.\/)+/, ''); }
export function artifactName(path) { return artifactPath(path).split('/').at(-1); }
// True when `actual` (absolute or relative, either separator) ends at the
// relative artifact path `expected` on a whole path-segment boundary.
export function isArtifact(actual, expected) {
  const a = artifactPath(actual), e = artifactPath(expected);
  return a === e || a.endsWith(`/${e}`);
}
