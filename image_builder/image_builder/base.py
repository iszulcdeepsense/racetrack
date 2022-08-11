from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Tuple, Optional

from image_builder.config import Config
from racetrack_client.manifest import Manifest
from racetrack_commons.plugin.engine import PluginEngine


class ImageBuilder(ABC):
    @abstractmethod
    def build(
            self,
            config: Config,
            manifest: Manifest,
            workspace: Path,
            tag: str,
            git_version: str,
            env_vars: Dict[str, str],
            deployment_id: str,
            plugin_engine: PluginEngine,
    ) -> Tuple[str, str, Optional[str]]:
        """
        Build image from manifest file in a workspace directory.
        :param config: Image builder configuration
        :param manifest: Fatman manifest
        :param workspace: Path to workspace directory
        :param tag: Image tag
        :param git_version: version name from Fatman git history
        :param env_vars: environment variables that should be set during building
        :param deployment_id: unique deployment id (UUID4)
        :return: Built image name, build logs, error message
        """
        raise NotImplementedError()
