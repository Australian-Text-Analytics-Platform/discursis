from subprocess import Popen

def _load_jupyter_server_extension(serverapp: 'jupyter_server.serverapp.ServerApp'):
    """
    This function is called when the extension is loaded.
    """
    Popen(["bokeh", "serve", "bokeh-app", "--allow-websocket-origin=*"])
    
