# -*- coding: UTF-8 -*-
# RightClickMenu
# A global plugin for NVDA
# Copyright 2013-2020 Alberto Buffolino, released under GPL
# code widely copied and adapted by NVDA source

import globalPluginHandler
import api
import winUser

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def script_rightClickMenu(self, gesture):
		obj = api.getFocusObject()
		api.moveMouseToNVDAObject(obj)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_RIGHTUP,0,0,None,None)

	__gestures = {
		"kb:control+applications": "rightClickMenu",
		"kb:control+shift+f10": "rightClickMenu",
	}
