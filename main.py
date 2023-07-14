import importlib
import util
import os
import sys
sys.path.insert(0, './scripts')

def main():
    dir_pre = "./scripts/"
    dir_post = url_split.replace(".", "_")
    dir = dir_pre + dir_post
    if os.path.exists(dir):
        gs = util.grab_scripts(dir)
        script = input("enter a script to run: ")
        script_name = gs[int(script) - 1]
        script_import = str(dir_post + "." + script_name.replace(".py", ""))
        module = importlib.import_module(script_import)
        module.main(util.soup_grab_html(url))
    else:
        print("no scripts found")

url = input("enter a website's url: ")
url_split = util.grab_site_main(url)

if url_split != "ret": main()
else: print("url requires '://'")