# GitHub 使用笔记

GitHub 是一个基于 Git 的代码托管平台，允许用户存储、管理和分享代码。以下是一个详细的 GitHub 使用笔记。

## 1. 注册 GitHub 账号

1. **打开 GitHub 官网**：在浏览器中访问 [GitHub](https://github.com)。
2. **注册账号**：
   - 点击**Sign up** 按钮。
   - 输入邮箱地址
   - 设置一个密码。
   - 选择一个 GitHub 用户名。
   - 验证邮箱，完成注册。

3. **设置个人信息**：
   - 进入 **Settings**。
   - 在 **Profile** 中完善个人信息。

## 2. 创建一个新的代码库 (Repository)

1. **创建库**：
   - 点击的 **Repositories**，然后点击 **New** 按钮。
   - 输入仓库名称（例如：`Homework`）**不能有中文**
   - 添加一个简短的描述（**可以用中文描述代码功能**）。
   - 选择仓库的可见性：`Public` （公开）或 `Private` （私有）。
   - 勾选 **Initialize this repository with a README** 来自动生成一个 README 文件。
   - 点击 **Create repository** 创建库。

2. **克隆仓库到本地**：
   - 打开新建的仓库页面，点击 **Code** 按钮，选择 **HTTPS** 或 **SSH** 链接。
   - 在终端或命令提示符中输入：  
     ```
     git clone <仓库地址>
     ```
     
## 3. 提交代码到 GitHub

1. **添加文件到仓库**：
   - 将代码文件或文档添加到本地仓库目录中。
2. **Git 基本操作**：
   - 在终端或命令提示符中，进入本地仓库目录：
     ```
     cd my-first-repo
     ```
   - 添加更改：
     ```
     git add .
     ```
     或
     ```
     git add <文件名>
     ```
   - 提交更改：
     ```
     git commit -m "提交说明"
     ```
   - 推送更改到 GitHub：
     ```
     git push origin main
     ```

## 4. 学习其他作者的代码

1. **搜索和浏览项目**：
   - 使用 GitHub 的 **Explore** 功能浏览热门项目。
   - 或者使用搜索框输入关键词查找感兴趣的项目。

2. **学习和贡献**：
   - 浏览项目的代码和文档，学习作者的编程思路和技巧。
   - 如果发现问题或有改进建议，可以在项目的 **Issues** 区域提问或建议。
   - 如果有能力，可以通过 **Pull Request** 为项目贡献代码。


#### 5. 其他功能

1. **GitHub Issues**：
   - 用于跟踪项目中的 bug、任务和改进建议。
   - 在 Issues 页面可以创建新 issue，分配责任人，添加标签。

2. **GitHub Discussions**：
   - 用于社区讨论和问题解答。你可以在 Discussions 中提出问题或参与讨论。

3. **GitHub Projects**：
   - 用于项目管理的看板工具，可以创建任务板，管理项目进度。

4. **GitHub Gists**：
   - 用于分享代码片段，可以创建公开或私有的 Gist，方便快速分享代码。

## 6. git常用命令表

|命令|描述|
|:---:|:---:|
| `git clone <地址>`         | 克隆远程仓库到本地                   |
| `git add .`                | 添加所有更改到暂存区                 |
| `git commit -m "message"`  | 提交更改并添加提交信息               |
| `git push origin <branch>` | 将本地分支推送到远程                 |
| `git checkout -b <branch>` | 创建并切换到新分支                   |
| `git merge <branch>`       | 合并指定分支到当前分支               |
| `git pull`                 | 从远程仓库拉取最新代码               |
| `git status`               | 查看仓库当前状态                    |
| `git log`                  |查看提交历史                         |

