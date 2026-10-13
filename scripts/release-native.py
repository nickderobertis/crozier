#!/usr/bin/env python3
"""Build once through maturin; use its exact wheel binary in the release archive.

No publication. Staged installer transport uses file URLs; checksum and binary
validation still run through install.sh. Darwin x86 products run under Rosetta.
"""
import argparse
import hashlib
from email.parser import Parser
import struct
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import tarfile
import tomllib
import zipfile


def run(*args, env=None):
    subprocess.run(args, check=True, env=env)


def build(target, tag, output):
    version = tomllib.loads(Path('Cargo.toml').read_text())['package']['version']
    if tag != f'v{version}':
        raise ValueError(f'tag {tag} does not match Cargo.toml version {version}')
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    wheels = output / f'wheels-{target}'
    wheels.mkdir(exist_ok=True)
    run('rustup', 'target', 'add', target)
    run('maturin', 'build', '--release', '--locked', '--target', target, '--out', str(wheels))
    candidates = list(wheels.glob('*.whl'))
    if len(candidates) != 1:
        raise ValueError(f'expected one wheel for {target}, found {candidates}')
    wheel = candidates[0]
    stage = output / f'stage-{target}'
    stage.mkdir(exist_ok=True)
    with zipfile.ZipFile(wheel) as archive:
        names = [n for n in archive.namelist() if n.endswith('.data/scripts/crozier')]
        if len(names) != 1:
            raise ValueError('wheel must carry exactly one crozier executable')
        binary = archive.read(names[0])
        metadata_names = [n for n in archive.namelist() if n.endswith('.dist-info/METADATA')]
        if len(metadata_names) != 1:
            raise ValueError('wheel must carry exactly one METADATA')
        metadata = Parser().parsestr(archive.read(metadata_names[0]).decode())
        if metadata['Name'] != 'crozier' or metadata['Version'] != version:
            raise ValueError('wheel name/version does not match release')
        architecture = 'aarch64' if target.startswith('aarch64') else 'x86_64'
        wheel_arch = 'arm64' if target.endswith('apple-darwin') and architecture == 'aarch64' else architecture
        if wheel_arch not in wheel.name.rsplit('-', 1)[-1]:
            raise ValueError('wheel architecture does not match target')
        if target.endswith('apple-darwin'):
            if binary[:4] != b'\xcf\xfa\xed\xfe' or struct.unpack_from('<I', binary, 4)[0] != (0x0100000C if architecture == 'aarch64' else 0x01000007):
                raise ValueError('Mach-O executable architecture does not match target')
        elif binary[:4] != b'\x7fELF' or struct.unpack_from('<H', binary, 18)[0] != (183 if architecture == 'aarch64' else 62):
            raise ValueError('ELF executable architecture does not match target')
    exe = stage / 'crozier'
    exe.write_bytes(binary)
    exe.chmod(0o755)
    for name in ['README.md', 'LICENSE', 'NOTICE', 'CHANGELOG.md']:
        shutil.copyfile(name, stage / name)
    base = f'crozier-{tag}-{target}'
    release = output / tag
    release.mkdir(exist_ok=True)
    packed = release / f'{base}.tar.gz'
    with tarfile.open(packed, 'w:gz') as archive:
        for path in sorted(stage.iterdir()):
            archive.add(path, arcname=path.name)
    (release / f'{base}.sha256').write_text(f'{hashlib.sha256(packed.read_bytes()).hexdigest()}  {packed.name}\n')
    with tarfile.open(packed) as archive:
        archived = archive.extractfile('crozier').read()
    if archived != binary:
        raise ValueError('archive and wheel executable differ')
    digest = hashlib.sha256(binary).hexdigest()
    (output / f'contract-{target}.json').write_text(json.dumps({
        'schemaVersion': 1, 'target': target, 'tag': tag, 'version': version,
        'archive': str(packed), 'wheel': str(wheel), 'binarySha256': digest,
        'archiveBinarySha256': hashlib.sha256(archived).hexdigest(),
        'wheelBinarySha256': digest,
    }, indent=2) + '\n')
    return wheel, version


def smoke(target, tag, output, wheel, version):
    # Both Darwin targets are executable on the Apple Silicon job: Rosetta
    # selects x86 uname for install.sh and executes that architecture's binary.
    prefix = ['arch', '-x86_64'] if target == 'x86_64-apple-darwin' and platform.machine() == 'arm64' else []
    out = output.resolve()
    installed = out / f'installed-{target}'
    # Separate URL roots model forge archive and checksum transport. Both are
    # our just-built immutable bytes; the real installer verifies their digest.
    checksums = out / 'checksum-root'
    checksums.mkdir(exist_ok=True)
    shutil.copytree(out / tag, checksums / tag, dirs_exist_ok=True)
    env = {**os.environ, 'CROZIER_RELEASE_BASE_URL': out.as_uri(),
           'CROZIER_CHECKSUM_BASE_URL': checksums.as_uri()}
    run(*prefix, 'sh', 'scripts/install.sh', '--version', tag, '--to', str(installed), env=env)
    run(*prefix, 'bash', 'scripts/smoke.sh', version,
        env={**os.environ, 'CROZIER_BIN': str(installed / 'crozier')})
    venv = out / f'venv-{target}'
    run('python3', '-m', 'venv', str(venv))
    wheel_install = out / f'wheel-installed-{target}'
    # These are py3-none binary wheels. pip's explicit platform installs the
    # Intel product even when the runner's Python is ARM-only; Rosetta executes
    # the resulting CLI, without requiring an Intel Python distribution.
    wheel_platform = wheel.name[:-4].rsplit('-', 1)[-1]
    run(str(venv / 'bin/python'), '-m', 'pip', 'install', '--no-index', '--no-deps',
        '--only-binary=:all:', '--platform', wheel_platform, '--target', str(wheel_install), str(wheel))
    run(*prefix, 'bash', 'scripts/smoke.sh', version,
        env={**os.environ, 'CROZIER_BIN': str(wheel_install / 'bin/crozier')})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', required=True, choices=['x86_64-apple-darwin', 'aarch64-apple-darwin', 'x86_64-unknown-linux-gnu', 'aarch64-unknown-linux-gnu'])
    parser.add_argument('--tag', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    wheel, version = build(args.target, args.tag, args.out)
    smoke(args.target, args.tag, args.out, wheel, version)


if __name__ == '__main__':
    main()
