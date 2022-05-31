import tempfile
from sync import sync
import pytest
import shutil
from pathlib import Path

class FakeFileSystem(list):

  def copy(self, src, dest):
    self.append(('COPY', src, dest))

  def move(self, src, dest):
    self.append(('MOVE', src, dest))

  def delete(self, src, dest):
    self.append(('DELETE', src, dest))


def test_when_a_file_exists_in_the_source_but_not_the_destination():
  source = {'hash1': 'fn1'}
  dest = {}
  filesystem = FakeFileSystem()

  reader = {"/source" : source, "/dest": dest}

  print(reader)
  
  sync(reader.pop, filesystem, "/source", "/dest")

  assert filesystem == [("MOVE", "/dest/original-file", "/dest/renamed-file")]


# def test_when_a_file_has_been_renamed_in_the_source():
#   src_hashes = {'hash1': 'fn1'}
#   dst_hashes = {'hash1': 'fn2'}
#   actions = determine_actions(src_hashes, dst_hashes, Path('/src'), Path('/dst'))
#   assert list(actions) == [('move', Path('/dst/fn2'), Path('/dst/fn1'))]