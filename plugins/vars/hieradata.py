# Copyright (c) 2020 Christian Meißner
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    name: hieradata
    version_added: "0.0.1"
    short_description: Loads configuration from a hierarchical configuration structure
    requirements:
        - whitelist in configuration
    description:
        - Loads YAML vars into corresponding groups/hosts in group_vars/ and host_vars/ directories.
        - Loads only files with extension to one of .yaml, .json, .yml or no extension.
        - Starting in 0.0.1, this plugin requires whitelisting and is whitelisted by default.
    options:
      hiera_basedir:
        default: "hieradata"
        description: The base directory where the hierarchy has to be placed in.
        type: str
        env:
          - name: HIERADATA_BASE_DIR
        ini:
          - section: hieradata
            key: basedir
      hiera_config:
        default: hieradata.yml
        description:
          - Name of hieradata configuration file.
        type: str
        env:
          - name: HIERADATA_CONFIG_FILE
        ini:
          - section: hieradata
            key: config
      stage:
        ini:
          - section: vars_host_group_vars
            key: stage
        env:
          - name: ANSIBLE_VARS_PLUGIN_STAGE
      _valid_extensions:
        default: [".yml", ".yaml", ".json"]
        description:
          - "Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these."
          - 'This affects vars_files, include_vars, inventory and vars plugins among others.'
        env:
          - name: ANSIBLE_YAML_FILENAME_EXT
        ini:
          - section: yaml_valid_extensions
            key: defaults
        type: list
    extends_documentation_fragment:
      - vars_plugin_staging
'''

import os
import yaml

from ansible import constants as C
from ansible.errors import AnsibleOptionsError, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars
from ansible.utils.display import Display as D

FOUND = {}


class VarsModule(BaseVarsPlugin):

    REQUIRES_WHITELIST = True

    def __init__(self, *args, **kwargs):

        super(VarsModule, self).__init__(*args, **kwargs)

        self.basedir = self.get_option('hiera_basedir')
        self.config = self.get_option('hiera_config')

    def get_vars(self, loader, path, entities, cache=True):
        ''' parses the inventory file '''
        pass

        if not isinstance(entities, list):
            entities = [entities]

        super(VarsModule, self).get_vars(loader, path, entities)

        hieradata = {}

        return hieradata
