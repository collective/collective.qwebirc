IDENT_HEX = object()
IDENT_NICKNAME = object()
WEBIRC_REALNAME = object()

def get(name, default=None):
  from collective.qwebirc import config
  if hasattr(config, name):
    return getattr(config, name)
  return default
