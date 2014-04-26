import sys
import os
import xbmc
import xbmcaddon

__addon__       = xbmcaddon.Addon()
__version__     = __addon__.getAddonInfo('version')
__id__          = __addon__.getAddonInfo('id')
__language__    = __addon__.getLocalizedString
__cwd__         = __addon__.getAddonInfo('path')

BASE_RESOURCE_PATH = xbmc.translatePath( os.path.join( __cwd__, 'resources', 'lib' ) )
sys.path.append (BASE_RESOURCE_PATH)

print "[SCRIPT] '%s: version %s' initialized!" % (__id__, __version__, )

if (__name__ == "__main__"):
    import qfpynm
    if not qfpynm.get_all_active_con():
        import addConnection
        addConnectionUI = addConnection.GUI("script_linux_nm-add.xml", __cwd__, "default")
        del addConnectionUI
    else:
        import gui
        ui = gui.GUI( "script_linux_nm-main.xml" , __cwd__ , "default",msg='', first=True)
        del ui

sys.modules.clear()
