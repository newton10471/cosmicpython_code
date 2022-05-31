from fnmatch import fnmatch
import hashlib
from importlib.util import source_hash
import os
import shutil
from pathlib import Path


BLOCKSIZE = 65536


def hash_file(path):
  hasher = hashlib.sha1()
  with path.open("rb") as file:
    buf = file.read(BLOCKSIZE)
    while buf:
      hasher.update(buf)
      buf = file.read(BLOCKSIZE)
  return hasher.hexdigest()


def reader(root):
  hashes = {}
  for folder, _, files in os.walk(root):
    for fn in files:
      hashes[hash_file(Path(folder) / fn)] = fn
  return hashes
  

def sync(reader, filesystem, source_root, dest_root):
  source_hashes = reader(source_root)
  dest_hashes = reader(dest_root)

  for sha, filename in source_hashes.items():
    if sha not in dest_hashes:
      sourcepath = source_root / filename
      destpath = dest_root / filename
      filesystem.copy(destpath, sourcepath)
    
    elif dest_hashes[sha] != filename:
      olddestpath = dest_root / dest_hashes[sha]
      newdestpath = dest_root / filename
      filesystem.move(olddestpath, newdestpath)

  for sha, filename in dest_hashes.items():
    if sha not in source_hashes:
      filesystem.delete(dest_root/filename)