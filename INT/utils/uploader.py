#!/usr/bin/env python3
from fabrictestbed_extensions.fablib.fablib import FablibManager as fablib_manager
import subprocess

class Uploader():
    def __init__(self):
        self.slice_name = "INT"

    def upload(self,node_name, file):
        try:     
            fablib = fablib_manager()
            slice = fablib.get_slice(name=self.slice_name)
            node = slice.get_node(name=node_name)
            ssh = node.get_ssh_command()
            param = ssh.split("ssh ")[1]
            scp = "scp " + param
            scp_addr = '[' + scp.split('@')[1] + ']'
            scp_config = scp.split('@')[0]
            scp_base = scp_config + '@' + scp_addr
            scp_file = scp_base.split("ubuntu")[0] + file + " ubuntu" + scp_base.split("ubuntu")[1] + ":~"
            print(scp_file)
            subprocess.run(scp_file, shell=True, capture_output=True, text=True)

    
        except Exception as e:
            print(f"Exception: {e}")
    
