import os

def can_build(env, platform):
	is_good_platform = platform=="x11" or platform=="windows" or platform=="osx"
	is_steam_build = os.getenv('STEAM_BUILD')
	return is_good_platform and is_steam_build

def configure(env):
	pass

def get_doc_classes():
	return [
		"Steam",
	]

def get_doc_path():
	return "doc_classes"
