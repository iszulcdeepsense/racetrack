from abc import ABC
from typing import Dict, Optional, Tuple, Any
from pathlib import Path

from racetrack_client.manifest import Manifest
from racetrack_commons.entities.dto import FatmanDto


class PluginCore(ABC):
    """
    Abstract Racetrack Plugin with method interfaces to override
    
    Additional attributes can be used:
    - self.plugin_dir: pathlib.Path - path to a plugin directory
    - self.plugin_config: PluginConfig - Configuration of Racetrack plugin used to load this
    """

    def post_fatman_deploy(self, manifest: Manifest, fatman: FatmanDto, image_name: str, deployer_username: str = None):
        """
        Supplementary actions invoked after fatman is deployed
        :param image_name: full name of the fatman image
        :param deployer_username: username of the user who deployed the fatman
        """
        pass

    def fatman_runtime_env_vars(self) -> Optional[Dict[str, str]]:
        """Supplementary env vars dictionary added to runtime vars when deploying a Fatman"""
        return None

    def fatman_job_types(self, docker_registry_prefix: str) -> Dict[str, Tuple[str, Path]]:
        """
        Job types provided by this plugin
        :param docker_registry_prefix: prefix for the image names (docker registry + namespace)
        :return dict of job name -> (base image name, dockerfile template path)
        """
        return {}

    def fatman_deployers(self) -> Dict[str, Any]:
        """
        Fatman Deployers provided by this plugin
        :return dict of deployer name -> an instance of lifecycle.deployer.base.FatmanDeployer
        """
        return {}

    def fatman_monitors(self) -> Dict[str, Any]:
        """
        Fatman Monitors provided by this plugin
        :return dict of deployer name -> an instance of lifecycle.monitor.base.FatmanMonitor
        """
        return {}

    def fatman_logs_streamers(self) -> Dict[str, Any]:
        """
        Fatman Monitors provided by this plugin
        :return dict of deployer name -> an instance of lifecycle.monitor.base.LogsStreamer
        """
        return {}

    def markdown_docs(self) -> Optional[str]:
        """
        Return documentation for this plugin in markdown format
        """
        return None

    def post_fatman_delete(self, fatman: FatmanDto, username_executor: str = None):
        """
        Supplementary actions invoked after fatman is deleted
        :param username_executor: username of the user who deleted the fatman
        """
        pass
