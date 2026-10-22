"""Offline process doubles for the SDK driver's external compiler and package tools.

The driver, filesystem, virtual environments, installed metadata and runtime
inspector remain real. The promoted SDK-env journey uses the real toolchain.
"""

from __future__ import annotations

import os
import shlex
import sys
from pathlib import Path

VALIDATOR = r"""
import os, sys
from pathlib import Path
with open(os.environ['SDK_EVAL_CALLS'], 'a') as log:
    log.write('validation\n')
if os.environ.get('SDK_EVAL_MODE') == 'validation-fails':
    print('validation double rejected the source')
    sys.exit(9)
assert Path(sys.argv[1]).is_file()
"""

BUILDER = r"""
import argparse, csv, hashlib, io, os, sys, zipfile
from pathlib import Path
with open(os.environ['SDK_EVAL_CALLS'], 'a') as log:
    log.write('build\n')
mode = os.environ.get('SDK_EVAL_MODE')
if mode == 'build-fails':
    print('builder double failed')
    sys.exit(11)
p = argparse.ArgumentParser()
p.add_argument('--wheel', action='store_true')
p.add_argument('--no-isolation', action='store_true')
p.add_argument('source', type=Path)
p.add_argument('--outdir', type=Path)
a = p.parse_args()
a.outdir.mkdir()
if mode != 'missing-wheel':
    entries = {path.relative_to(a.source / 'src').as_posix(): path.read_bytes() for path in (a.source / 'src').rglob('*.py')}
    info = 'limitation_sdk-0.0.0.dist-info/'
    entries[info + 'METADATA'] = b'Metadata-Version: 2.1\nName: limitation-sdk\nVersion: 0.0.0\n'
    entries[info + 'WHEEL'] = b'Wheel-Version: 1.0\nRoot-Is-Purelib: true\nTag: py3-none-any\n'
    output = io.StringIO()
    writer = csv.writer(output)
    for name, value in sorted(entries.items()):
        writer.writerow((name, '', len(value)))
    writer.writerow((info + 'RECORD', '', ''))
    entries[info + 'RECORD'] = output.getvalue().encode()
    with zipfile.ZipFile(a.outdir / 'limitation_sdk-0.0.0-py3-none-any.whl', 'w') as wheel:
        for name, value in entries.items():
            wheel.writestr(name, value)
if mode == 'mutated-tree':
    (a.source / 'changed.txt').write_text('unexpected build mutation')
"""

UV = r"""
import importlib.metadata, json, os, shutil, subprocess, sys, zipfile
from pathlib import Path
args = sys.argv[1:]
mode = os.environ.get('SDK_EVAL_MODE')
real_python = os.environ['SDK_EVAL_PYTHON']
with open(os.environ['SDK_EVAL_CALLS'], 'a') as log:
    log.write('uv:' + args[0] + '\n')
match args:
    case ['venv', *_]:
        target = Path(args[-1])
        subprocess.run([real_python, '-m', 'venv', '--without-pip', str(target)], check=True)
        interpreter = target / 'bin/python'
        site = Path(subprocess.check_output([str(interpreter), '-c', 'import sysconfig; print(sysconfig.get_path("purelib"))'], text=True).strip())
        if os.environ.get('SDK_EVAL_COVERAGE'):
            # Instrument the actual child interpreter without downloading a package.
            # This copy is test infrastructure, not a change to the SDK driver.
            distribution = importlib.metadata.distribution('coverage')
            for entry in distribution.files or ():
                if entry.suffix == '.pyc':
                    continue
                source = Path(distribution.locate_file(entry))
                destination = site / str(entry)
                if not destination.resolve().is_relative_to(target.resolve()):
                    raise ValueError('coverage file record escapes the environment')
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, destination)
            (site / 'sdk-test-coverage.pth').write_text('import coverage; coverage.process_startup()\n')
    case ['pip', 'install', *_]:
        interpreter = args[args.index('--python') + 1]
        site = Path(subprocess.check_output([interpreter, '-c', 'import sysconfig; print(sysconfig.get_path("purelib"))'], text=True).strip())
        if any(arg.startswith('build==') for arg in args):
            (site / 'build.py').write_text(os.environ['SDK_EVAL_BUILDER'])
            (site / 'openapi_spec_validator.py').write_text(os.environ['SDK_EVAL_VALIDATOR'])
        else:
            if mode == 'installation-fails':
                print('installer double failed')
                sys.exit(13)
            with zipfile.ZipFile(args[-1]) as wheel:
                wheel.extractall(site)
    case _:
        raise ValueError('unexpected package-tool arguments: ' + repr(args))
"""

CROZIER = r"""
import os, sys
from pathlib import Path
args = sys.argv[1:]
strict = '--fern-strict' in args
label = 'strict_generation' if strict else 'default_generation'
with open(os.environ['SDK_EVAL_CALLS'], 'a') as log:
    log.write(label + '\n')
mode = os.environ.get('SDK_EVAL_MODE')
if mode == label + '-fails':
    print('compiler double failed')
    sys.exit(17)
if mode == 'missing-sdk':
    sys.exit(0)
output = Path(args[args.index('--output') + 1])
package = output / 'src/limitation_sdk'
package.mkdir(parents=True)
body = "import os\nfrom pathlib import Path\nwith open(os.environ['SDK_EVAL_CALLS'], 'a') as log: log.write('imports\\n')\nif os.environ.get('SDK_EVAL_MODE') == 'imports-fails': raise ImportError('module double failed')\n"
if mode == 'different-trees' and strict:
    body += 'STRICT_VARIANT = True\n'
(package / '__init__.py').write_text(body)
(package / 'reading.py').write_text('VALUE = 7\n')
(output / 'pyproject.toml').write_text('[project]\nname="limitation-sdk"\nversion="0.0.0"\n')
match mode:
    case 'symlink-sdk':
        (output / 'linked.py').symlink_to(package / '__init__.py')
    case 'outside-env':
        with (package / '__init__.py').open('a') as handle:
            handle.write("__file__ = '/outside-the-installation/sdk.py'\n")
    case 'discovery-fails':
        broken = package / 'broken'
        broken.mkdir()
        (broken / '__init__.py').write_text("raise ImportError('broken package')\n")
    case 'mutating-import':
        with (package / '__init__.py').open('a') as handle:
            handle.write("Path(__file__).with_name('reading.py').write_text('VALUE = 99\\n')\n")

"""


def install(directory: Path) -> tuple[Path, dict[str, str]]:
    directory.mkdir()
    for name, program in (("uv", UV), ("crozier", CROZIER)):
        source = directory / f"{name}.py"
        source.write_text(program, encoding="utf-8", newline="\n")
        launcher = directory / name
        launcher.write_text(
            f'#!/bin/sh\nexec {shlex.quote(sys.executable)} {shlex.quote(str(source))} "$@"\n',
            encoding="utf-8",
            newline="\n",
        )
        launcher.chmod(0o755)
    env = dict(os.environ)
    env.update(
        PATH=str(directory) + os.pathsep + env.get("PATH", ""),
        SDK_EVAL_PYTHON=sys.executable,
        SDK_EVAL_BUILDER=BUILDER,
        SDK_EVAL_VALIDATOR=VALIDATOR,
    )
    return directory / "crozier", env
