#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    unmanic.__init__.py
 
    Written by:               Josh.5 <jsunnex@gmail.com>
    Date:                     22 Jun 2019, (1:47 PM)
 
    Copyright:
           Copyright (C) Josh Sunnex - All Rights Reserved
 
           Permission is hereby granted, free of charge, to any person obtaining a copy
           of this software and associated documentation files (the "Software"), to deal
           in the Software without restriction, including without limitation the rights
           to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
           copies of the Software, and to permit persons to whom the Software is
           furnished to do so, subject to the following conditions:
  
           The above copyright notice and this permission notice shall be included in all
           copies or substantial portions of the Software.
  
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
           IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
           DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
           OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
           OR OTHER DEALINGS IN THE SOFTWARE.

"""

from __future__ import absolute_import

from .completedtaskscommandlogs import CompletedTasksCommandLogs
from .completedtasks import CompletedTasks
from .enabledplugins import EnabledPlugins
from .installation import Installation
from .pluginrepos import PluginRepos
from .plugins import Plugins
from .libraries import Libraries, LibraryTags
from .librarypluginflow import LibraryPluginFlow
from .tags import Tags
from .tasks import Tasks
from .workergroups import WorkerGroupTags, WorkerGroups
from .workerschedules import WorkerSchedules

__author__ = 'Josh.5 (jsunnex@gmail.com)'

__all__ = (
    'CompletedTasks',
    'CompletedTasksCommandLogs',
    'EnabledPlugins',
    'Installation',
    'Libraries',
    'LibraryTags',
    'LibraryPluginFlow',
    'PluginRepos',
    'Plugins',
    'Tags',
    'Tasks',
    'WorkerGroups',
    'WorkerGroupTags',
    'WorkerSchedules',
)


def list_all_models():
    return __all__
