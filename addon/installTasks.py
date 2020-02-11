# -*- coding: UTF-8 -*-
import addonHandler
import os

addonHandler.initTranslation()

def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.manifest['name'] == "RightClickMenu":
			addon.requestRemove()
			break
