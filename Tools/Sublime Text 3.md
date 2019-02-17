## Sublime Text 3 
+ Environment
    + Ubuntu 16.04

+ Install
	+ The most convenient method: download compressed package from official website
		+ https://www.sublimetext.com/3
		+ I choose https://download.sublimetext.com/sublime_text_3_build_3143_x64.tar.bz2
	+ Extract this file
		+ run ./sublime_text in command line
	+ put the extracted file under /opt (recommend)

    + Reference website
        + https://www.jianshu.com/p/04e1b65dd2c0

+ Command line startup
	+ create a soft link
		+ $ sudo ln -s /opt/sublime_text/sublime_text /usr/bin/subl
	+ then you can start sublime by 
		+ $ subl

+ Chinese input method
	+ Tool Reference website
		+ https://github.com/lyfeyaj/sublime-text-imfix
	+ First of all to ensure
		+ Sublime is already installed and the directory is /opt/sublime_text/
			+ /opt/sublime_text/ is the default path to retrieve when the input method is installed
		+ you can start sublime by 
            + $ subl
    + Tool
        + sudo apt-get update && sudo apt-get upgrade
        + git clone https://github.com/lyfeyaj/sublime-text-imfix.git
        + cd sublime-text-imfix && ./sublime-imfix
        + restart sublime and you can input Chinese

## Settings
+  Install Package Control
    + Reference Website:
        + https://jingyan.baidu.com/article/925f8cb817fd49c0dce05653.html
+ Sublime Text 默认是没有显示或隐藏行号的快捷键
    + https://blog.csdn.net/luo200618/article/details/52014881
    + hot key : Alt + L

+ Show left dictionary tree
    + Ctrl + K + B
    + File - Open Folder

+ Package control

## Useful package 
+ Markdown preview
    + Ctrl + shift + P
        + input 'preview' to see preview of markdown 


## Browser Preview 
+ Ctrl + Alt + O (O of IOP)
+ Real time preview can be realized without other settings
+ Problem
```
Sorry, the requested URL 'http://127.0.0.1:51004/view/31' caused an error:

'buffer_id(31) is not valid (closed or unsupported file format)'

**NOTE:** If you run multiple instances of Sublime Text, you may want to adjust
the `server_port` option in order to get this plugin work again.
```
+ Reference Website
    + https://github.com/timonwong/OmniMarkupPreviewer/issues/85
    ```
    Quick Fix 1: Remove Strikethrough Extension

    Sublime Text > Preferences > Package Settings > OmniMarkupPreviewer > Settings - User
    paste the following to remove the strikeout package.

    {
        "renderer_options-MarkdownRenderer": {
            "extensions": ["tables", "fenced_code", "codehilite"]
        }
    }
    Quick Fix 2: Fix the Strikethrough Extension (if you need it)

    Find the python-markdown sublime package.

    On the Mac: subl "/Users/<username>/Library/Application Support/Sublime Text 3/Packages/OmniMarkupPreviewer/OmniMarkupLib/Renderers/libs/mdx_strikeout.py"

    Replace the makeExtension() method with the following:

    def makeExtension(*args, **kwargs):
        return StrikeoutExtension(*args, **kwargs)
    Save, quit and reload Sublime Text.
    ```

## Formula rendering
+ Reference websites
    + https://reginald1787.github.io/2014/06/29/sublime-markdown-mathjax/
+ Install OmniMarkupPreviewer 
+ Setting
    + Preferece - Settings - OmniMarkupPreviewer - Setting Default
        + change 'mathjax_enabled : false' to 'mathjax_enabled : true'
        + MathJax will be download automatically

## Draw Picture by PlantUML
+ Image 
    + 时序图
    + 流程图
    + 用例图
    + 状态图
    + 组件图
+ 软件安装
    + 这些软件全部是开源或共享软件，不存在版权问题，可以放心使用。
    + 安装 graphviz
        + apt-get install graphviz
        + graphviz 是个开源的图片渲染库
    + Install PlantUML for Sublime Plugin
        + Download and extract : https://github.com/jvantuyl/sublime_diagram_plugin/tarball/master
        + Use 'Preferences -> Browse Packages' open dictionary and put the extract file to it
        + restart Sublime
    + hot key 
        + Open Preferences -> Key Binding - User, add follow:
            + { "keys": ["alt+d"], "command": "display_diagrams"}

+ Effect test
    + open sublime and input
    ```
    Bob -> Alice : Hello, how are you
    Alice -> Bob : Fine, thank you, and you?
    ```
    + choose this test and  Press 'Alt +D'
    + image file will generate in this dictionary file, and a window displaying the picture will be popped up