# Github

## Workflow与GithubAction

### GithubWorkflow简述

Workflow可以简单的理解为开设一个**“临时”**使用的服务器，并在此服务器上运行指定的命令或脚本

### Workflow配置

Workflow使用.yml进行配置，放在仓库根目录下的`.github/Workflow`文件夹中

具体配置文件可以在Github提供的模板文件的基础上进行修改

:::note 💡

若需要将要运行结果保存为文件，需要将代码提交到仓库

    并需要授予权限

    ```powershell
    permissions: write-all
    
    step:
    	- name: Commit and push changes to another branch
          env:
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          run: |
              git config --global user.name "github-actions"
              git config --global user.email "actions@github.com"
              git add -A
              git commit -m "Add generated files"
              git push origin main
    ```

    > secrets是Github提供的一项功能，可以保存个人TOKEN等需要保密的部分并在运行时加入程序

::: 

### Workflow触发器

Workflow可以设置为使用多种触发器，包括：

- **schedule**：定时触发（由于Github的机制问题，定时触发实际需要排队按照顺序运行，因此实际运行时间会比预定时间存在一定的延迟）

- **workflow_dispatch：**手动触发，在仓库的Actions选项卡下面选择相应的工作流文件手动触发

- **remote_triger：**使用HTTP的POST请求定时模拟手动触发工作流
    [Bookmark](https://console.cron-job.org/dashboard)


- URL:https://api.github.com/repos/AtomRockStone/reponame/actions/workflows/action.yml/dispatches

- Load:

![ca8d44369038](/img/ca8d44369038)



