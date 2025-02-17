---
title: Cloudflare Workers
description: How to deploy a Cloudflare Workers
toc_min_heading_level: 2
---

无服务器计算是一种按需提供后端服务的方法。无服务器提供者允许用户编写和部署代码，而不必担心底层基础设施。从无服务器提供商获得后端服务的公司将根据计算量来付费，由于这种服务是自动扩展的，不必预留和付费购买固定数量的带宽或服务器。请注意，虽然名为“无服务器”，实际上依然需要物理服务器，只不过开发人员不需要考虑服务器而已


**Cloudflare Workers**是由著名的网络服务厂商Cloudflare（小黄云）提供的Serverless服务，简单的说，以前如果要在云端部署一个Web服务都需要开发者先买一个云服务器，然后再把代码部署上去，往往开发者还需要自行折腾网络相关的配置，这样的方法既无法充分发挥云服务器的全部性能潜力，成本也较高，而Serverless模式相当于为开发者提供了一个配置好的运行容器，只要提交服务的核心代码，就可以在云端运行，即节省了成本，也降低了不必要的麻烦，还可以利用云服务厂商服务器分布较多的优势，在最近的服务器对用户进行相应，大大提升了应用性能。

使用Cloudflare Workers的先决条件：

- Node.js
- Cloudflare账号一个

Workers支持Javascript和Typescript进行开发，Python仍在测试中，且使用Pyodide作为解释器（重点是和你熟悉的那个Python**不完全一样**)

## 开发初步

一个Cloudflare Workers的开发流程如图所示：

```mermaid
flowchart LR
    A[Idea] --> B[初始化项目]
    B --> C[编写核心代码]
    C --> D[本地测试]
    D --> E[部署到Cloudflare]

```

Worker的本地开发通常使用Cloudflare开发的命令行工具**Wrangler**

使用下方的命令初始化项目并安装Wrangler

```bash
npm create cloudflare@latest -- my-first-worker
```

安装完成后，切换到项目根目录，执行：

```bash
npx wrangler dev
```

即可在本地测试项目，要注意项目中使用`console.log()`的输出位置在终端而不是在浏览器控制台

```bash
npx wrangler dev --ip '0.0.0.0'
```

可以在局域网中的设备上进行测试

开发完成后，通过命令：

```bash
npx wrangler deploy
```

即可部署到Cloudflare全球网络中