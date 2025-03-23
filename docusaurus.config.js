// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Nuclear Rock',
  tagline: 'Here is my space on Internet',
  favicon: 'img/favicon.ico',

  staticDirectories: ['docs/static', 'static'],
  // Set the production url of your site here
  url: process.env.PRODUCT_URL || 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl:process.env.BASE_URL || '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'nuclearrockstone', // Usually your GitHub org/user name.
  projectName: 'NuclearRock', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'zh',
    locales: ['en','zh'],
    localeConfigs: {
      en: {
        htmlLang: 'en-GB',
      },
      // 如果不需要重写默认值，可以忽略 locale (例如 fr)
      'zh': {
      },
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          /* editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/', */
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          // Please change this to your repo.
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/social_card.svg',
      navbar: {
        title: 'NUCLEAR ROCK',
        logo: {
          alt: 'My Site Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'noteSidebar',
            position: 'left',
            label: '笔记',
          },
          /* {
            type: 'dropdown',
            position: 'left',
            label: '文章',
            items:[
              {
                type: 'docSidebar',
                sidebarId: 'programSidebar',
                label: '编程',
              },
              {
                type: 'docSidebar',
                sidebarId: 'cloudSidebar',
                label: '云服务',
              },
            ]
          }, */
          {to: '/blog', label: '博客', position: 'left'},
          {label:'关于',href:'https://www.nuclearrockstone.xyz/'},
          {
            type: 'localeDropdown',
            position: 'left',
          },
          /* {
            href: 'https://github.com/facebook/docusaurus',
            label: 'GitHub',
            position: 'right',
          }, */
        ],
      },
      footer: {
        style: 'dark',
        copyright: `Copyright © ${new Date().getFullYear()} NuclearRockStone, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      metadata: [
        {name: 'description', content: 'nuclearrockstone personal site'},
        {property: 'og:description', content: 'nuclearrockstone personal site'},
      ],
    }),
  stylesheets: [
      {
        href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
        type: 'text/css',
        integrity:
          'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
        crossorigin: 'anonymous',
      },
    ],

  
  markdown: {
    mermaid: true,
  },
  themes: ['@docusaurus/theme-mermaid'],
  
};

export default config;
