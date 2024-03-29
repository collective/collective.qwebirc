# this is seperate to allow us to use python 2.5 syntax without
# the dependency checker breaking on earlier versions.

import sys
import subprocess

def fail(*message):
  print >>sys.stderr, "\n".join(message)
  sys.exit(1)
  
def warn(*message):
  print >>sys.stderr, "warning:", "\nwarning: ".join(message), "\n"

def check_dependencies():
  i = 0
  
  check_twisted()
  check_zope()
  check_win32()
  i+=check_json()
  i+=check_java()
  i+=check_hg()
  
  print "0 errors, %d warnings." % i
  
  if i == 0:
    print "looks like you've got everything you need to run qwebirc!"
  else:
    print "you can run qwebirc despite these."

  f = open(".checked", "w")
  f.close()
  
def check_win32():
  if not sys.platform.startswith("win"):
    return
  
  try:
    import win32con
  except ImportError:
    fail("qwebirc requires pywin32, see:", "https://sourceforge.net/project/showfiles.php?group_id=78018")
  
def check_java():
  def java_warn(specific):
    warn(specific, "java is not required, but allows qwebirc to compress output,", "making it faster to download.", "you can get java at https://www.java.com/")
    
  try:
    p = subprocess.Popen(["java", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate()
    if p.wait() != 0:
      java_warn("something went wrong looking for java.")
      return 1
  except: # ugh
    java_warn("couldn't find java.")
    return 1
    
  return 0
  
def check_hg():
  def hg_warn(specific):
    warn(specific, "mercurial (hg) is not required, but allows qwebirc to save bandwidth by versioning.", "you can get hg at https://www.selenic.com/mercurial/")
    
  try:
    p = subprocess.Popen(["hg", "id"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.communicate()
    if p.wait() != 0:
      hg_warn("something went wrong looking for mercurial.")
      return 1
  except: # ugh
    hg_warn("couldn't find mercurial.")
    return 1
    
  return 0
  
def check_zope():
  try:
    from zope.interface import Interface
  except ImportError:
    if sys.platform.startswith("win"):
      fail("qwebirc requires zope interface",
           "see pypi: https://pypi.python.org/pypi/zope.interface")
    else:
      fail("qwebirc requires zope interface.",
           "this should normally come with twisted, but can be downloaded",
           "from pypi: https://pypi.python.org/pypi/zope.interface")
           
def check_twisted():
  try:
    import twisted
  except ImportError:
    fail("qwebirc requires twisted (at least 8.2.0), see https://twistedmatrix.com/")

  def twisted_fail(x, y=None):
    fail("you don't seem to have twisted's %s module." % x,
         "your distro is most likely modular, look for a twisted %s package%s." % (x, " %s" % y if y else "",))

  try:
    import twisted.names
  except ImportError:
    twisted_fail("names")

  try:
    import twisted.mail
  except ImportError:
    twisted_fail("mail")

  try:
    import twisted.web
  except ImportError:
    twisted_fail("web", "(not web2)")

  try:
    import twisted.words
  except ImportError:
    twisted_fail("words")
    
def check_json():
  from collective.qwebirc.qwebirc.util.qjson import slow
  if slow:
    warn("simplejson module with C speedups not installed.",
         "using embedded module (slower); consider installing simplejson from:",
         "https://pypi.python.org/pypi/simplejson/")
    return 1
  return 0
  
if __name__ == "__main__":
  import dependencies
  dependencies.check_dependencies()
