"""
lsmagic

Available line magics:
%alias  %alias_magic  %autoawait  %autocall  %autoindent  %automagic  %bookmark  %cd  %cls  %colors  %conda  %config  %copy  %cpaste  %ddir  %debug  %dhist  %dirs  %doctest_mode  %echo  %ed  %edit  %env  %gui  %hist  %history  %killbgscripts  %ldir  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %ls  %lsmagic  %macro  %magic  %matplotlib  %mkdir  %notebook  %page  %paste  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %pip  %popd  %pprint
  %precision  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %quickref  %recall  %rehashx  %reload_ext  %ren
%rep  %rerun  %reset  %reset_selective  %rmdir  %run  %save  %sc  %set_env  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%cmd  %%debug  %%file  %%html  %%javascript  %%js  %%latex  %%markdown  %%perl
%%prun  %%pypy  %%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile

Automagic is ON, % prefix IS NOT needed for line magics.
"""


"""
## 新版本执行不用加%
edit hello.py
run hello.py
hist 历史记录
save a.py 1-11 保存历史记录1-11行

debug 进入ipdb 
p a 查看变量a
p b 查看变量b
exit 退出

%rehashx 将Linux中的命令更新到ipython中

%store -r 恢复别名
load a.py 加载不执行

%logstart 开启日志记录
logoff
默认会生成ipython_log.py
ipython -i ipython_log.py 重新开始会话

ipython配置
C:\Users\admin\.ipython\profile_default
创建默认配置文件： ipython profile create

autoreload 自动保存 不用每次导入

""""