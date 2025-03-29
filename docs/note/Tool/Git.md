---
title: Git
---

# Git

**Git是一个分布式版本管理工具**

Github、Gitee是用于托管使用了Git进行管理的存储库的云存储服务

使用Git前需要下载Git的Windows版本

[Untitled Bookmark](https://git-scm.com/download/win)

## **Git初始化仓库与连接远程仓库**

### 开始一个储存库

#### **从本地开始**

```bash
git init
```

该命令将把命令行所处的文件夹变为Git可以管理的储存库

Ex：若命令行所在文件夹为 `~/repo` 则repo成为储存库

#### 从远程仓库开始

```bash
git clone
```

该命令将从远程仓库拉取储存库

Ex：若命令行所在文件为 `~/File` 则会在该目录下建立以远程仓库名称为名的文件夹存储库

### 连接远程仓库

连接远程仓库通常有两种方式：**SSH**和**HTTPS**

#### 配置SSH密钥对

<details>
<summary>**生成密钥对**</summary>

    使用SSH命令生成密钥对并将公钥上传到远端储存库以供验证

    **公钥永远在远端**

    > 生成文件的默认位置在  `%USERPROFILE%/.ssh` 
其中后缀名为 `.pub` 的为公钥

    ```powershell
    ssh-keygen -t ed25519 -C "your_email@example.com"
    #其中邮箱的部分不影响生成的密钥
    ```

</details>

<details>
<summary>**使用 **`**OpenSSH config**`** 文件管理多个远端**</summary>

    在  `%USERPROFILE%/.ssh` 目录下建立名为 `config` 的文件（无需后缀名）

    **多平台多账号：**使用config文件配置登录不同服务器的私钥

    **同平台多账号：**使用SSH的别名功能区分不同账号登录使用的私钥

    <details>
    <summary>`**config**`**文件内容**</summary>

        ```powershell
        # 配置文件参数
        # Host : 配置对应的的主机名和 ssh 文件（可以直接填写 ip 地址）
        # HostName : 要登录主机的主机名（建议与 Host 一致）
        # PreferredAuthentications ：配置登录的验证方式(含密码可自行查询配置方式)
        # IdentityFile : 指明上面 User 对应的配置路径
        # User : 登录名（如 github 的 username）
        # Port: 端口号（默认 22）
        #多平台多账号
        # github.com
        Host github.com
        HostName github.com
        PreferredAuthentications publickey
        IdentityFile C:/Users/nucle/.ssh/id_ed25519
        User nuclearrockstone@gmail.com
        
        # gitee.com
        Host gitee.com
        HostName gitee.com
        PreferredAuthentications publickey
        IdentityFile C:/Users/nucle/.ssh/id_rsa
        User nuclearrockstone@gmail.com
        
        # github.com
        Host github.com
            HostName github.com
            PreferredAuthentications publickey
            IdentityFile C:/Users/nucle/.ssh/id_ed25519
            User git
        
        Host github_atom
            HostName github.com
            PreferredAuthentications publickey
            IdentityFile C:/Users/nucle/.ssh/atomrockstone
            User git
        ```

    </details>

    > 可能需要的步骤：

    > 参考：

    在使用SSH连接远程仓库时，即可通过对应的HOST名使用对应的密钥

</details>

#### 配置HTPPS连接（不建议）

在使用Git对远程仓库进行需要权限的操作时，会自动弹出登陆界面并将账号密码自动保存至Windows凭据管理器

## Git分支

