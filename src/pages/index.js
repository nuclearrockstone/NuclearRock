import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import React, { useEffect } from 'react';

import Heading from '@theme/Heading';
import styles from './index.module.css';
import Translate from '@docusaurus/Translate';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="background-circle"></div>
      <div className="background-circle"></div>
      <div className="background-circle-mobile"></div>
      <div className="container head_container">
        
        <Heading as="h1" className="hero__title">
          <Translate>哈喽!</Translate><span>&nbsp;</span><span className="responsive-break"><br/></span><Translate>我是</Translate><span className="i18n_space">&nbsp;</span><span className="i18n-break"><br/></span>
          <span className="hero__title_span"><Translate>核动力岩石</Translate></span>
        </Heading>
        {/* <Heading as="h1" className="hero__title">
          This is {siteConfig.title}
        </Heading> */}
        <p className="hero__subtitle"><Translate>这是我在互联网上的空间</Translate></p>
        {/* <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Go
          </Link>
        </div> */}
        <p align="center">
          <a href="https://skillicons.dev">
          <img className="techstack" src="https://skillicons.dev/icons?i=python,vscode,html,css,notion,markdown&theme=light" />
          </a>
        </p>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  useEffect(() => {
    // 定义处理逻辑的函数
    const updateNavbar = () => {
      // 获取页面中类名为 'navbar navbar--fixed-top' 的元素
      const navbarElement = document.querySelector('.navbar.navbar--fixed-top');
      if (navbarElement) {
        // 为该元素添加类名 'navbar_homepage'
        navbarElement.classList.add('navbar_homepage');
      }
    };

    // 在页面首次加载时运行
    updateNavbar();

    // 在每次点击时运行
    document.addEventListener('click', updateNavbar);

    // 清理事件监听器，防止内存泄漏
    return () => {
      document.removeEventListener('click', updateNavbar);
    };
  }, []); // 空数组确保只在组件挂载和卸载时执行一次
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}>
      <HomepageHeader />
      {/* <main>
        <HomepageFeatures />
      </main> */}
    </Layout>
  );
}
