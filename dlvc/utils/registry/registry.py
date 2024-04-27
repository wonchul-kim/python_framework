# Copyright (c) OpenMMLab. All rights reserved.
import inspect
import logging
import sys
from collections.abc import Callable
from contextlib import contextmanager
from importlib import import_module
from typing import Any, Dict, Generator, List, Optional, Tuple, Type, Union

from rich.console import Console
from rich.table import Table


class Registry:
    def __init__(self, name: str):
        self._name = name 
        self._module_dict: Dict[str, Type] = dict()
        self._imported = False 
        
    @property 
    def name(self):
        return self._name 
    
    
    
    