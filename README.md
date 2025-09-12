<div align = "center" >
    <h1>Create: Applied Machine</h1>
    <hr>
</div>

# 关于

**目前还处于早期开发阶段**

这是一个 `1.21.1` `NeoForge` 下的以科技为主的整合包

主要以各个模组之间的搭配为玩法

这个整合包是我第一次尝试去制作整合包

# 打包

## 前置工作

你需要 `Python`>=3.10 与 `VSCode`(可选)

### 下载源码

点击[这里](https://github.com/cueavyqwp/1.21.1-Create/archive/refs/heads/main.zip)下载

### 安装游戏

安装一个`1.21.1`版本的`NeoForge`客户端,命名为`1.21.1-Create`

### 覆盖文件

把下载的源码解压覆盖到安装的游戏文件夹

确保你开启了版本隔离

### VSCode

然后在当前游戏文件夹打开VSCode

## 更新模组列表

使用`PCL2`导出整合包

注意先读取配置`export_config.txt`然后再导出

运行`update.py`来更新`modrinth.index.json`

## 打包客户端

运行`pack.py`

打包后的压缩包在`dist`文件夹下

## 打包服务端

运行`pack-server.py`

打包后的压缩包在`dist`文件夹下

记得启用命令方块(`enable-command-block=true`)
