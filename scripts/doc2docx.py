#!/usr/bin/env python

import glob
import subprocess
import os

out_dir = '../docx_files'
in_dir = 'doc_files'

os.chdir(in_dir)
for doc in glob.glob('*.doc'):
  subprocess.call(['soffice', '--headless', '--convert-to', 'docx', '--outdir', out_dir, doc])
