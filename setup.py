#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import distutils.core
import sys

# Build the epoll extension for Linux systems with Python < 2.6
extensions = []
major, minor = sys.version_info[:2]
python_26 = (major > 2 or (major == 2 and minor >= 6))

distutils.core.setup(
    name="html_spec",
    version="0.1",
    packages = ["html_spec"],
    ext_modules = extensions,
    author="Rafael Martins",
    author_email="rafael.mws@gmail.com",
    url="http://github.com/rafaelmws/html_spec",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="",
)
